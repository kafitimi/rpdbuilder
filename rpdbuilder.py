
import configparser, argparse
from xml.etree import ElementTree as XMLTree
from os.path import abspath, splitext, split as splitpath
from jinja2 import Environment as Jinja2Renderer, FileSystemLoader
from collections import OrderedDict
from subprocess import check_call as execute
from time import sleep

def main():
    args = parse_args()
    template = get_jinja_tex_template(args.template)

    for filename in args.filenames:
        print('FILE ' + filename + ':')
        ini = load_ini(filename) 
        planfile = ini['planfile'] if 'planfile' in ini else args.plan
        context = load_discipline_data_from_xml(planfile, ini.get('disciplinecode'), ini.get('discipline'))
        context.update({k: v for k,v in ini.items() if v})
        produce_tex(template, filename, context, compile=args.compile)


def parse_args():
    """настройка и получение аргументов командной строки
    """
    argp = argparse.ArgumentParser(description='скомпилировать РПД из данных в указанном ini файле и шаблоне')
    argp.add_argument('filenames', metavar='filename', default=['oop.ini'], type=str, nargs='*', help='ini-файл с данными РПД')
    argp.add_argument('-t', '--template', default='template.tex', help='файл шаблона (по умолчанию: template.tex)')
    argp.add_argument('-p', '--plan', metavar='PLANFILE', help='XML-файл РУП (по умолчанию: G09030101_16-1ИВТ.plm.xml)')
    argp.add_argument('-c', '--compile', action='store_true', default=False, help='компилировать latex-файлы в PDF (по умолчанию: нет)')
    return argp.parse_args()


def get_jinja_tex_template(template_filename : str):
    """Шаблонный движок jinja2 с переопределениями обозначений,
    чтобы не конфликтовать с макросами TeX
    """
    renderer = Jinja2Renderer(
        block_start_string='%{', block_end_string='%}',
        variable_start_string='<=', variable_end_string='=>',
        comment_start_string='<<<###', comment_end_string='###>>>',
        loader=FileSystemLoader(abspath('.'))
    )
    return renderer.get_template(template_filename)


def load_ini(filename)-> dict:
    """читает .INI-файл с данными
    """
    parser = configparser.ConfigParser(empty_lines_in_values=False)
    f = open(filename, encoding='utf-8')
    parser.read_file(f)
    f.close()
    res = {k: parser['Заголовки'][k] for k in parser['Заголовки']}
    for section in parser:
        if section in ('DEFAULT', 'Заголовки'): continue
        secname = ''.join(map(str.capitalize, section.split()))
        sec = parser[section]
        res.update({secname+key.capitalize(): [row.split('|') for row in sec[key].split('\n')] 
                                               for key in sec})
    return res 
        

def load_discipline_data_from_xml(planfile: str, disc_code : str, disc_name : str) -> dict:
    """Находит в XML-файле учебного плана информациою о данной дисциплине
    """ 
    d = {}
    tree = XMLTree.parse(planfile)
    p = tree.getroot()[0]

    if not any((disc_code, disc_name)):
        raise Exception('Must give at least a Discipline name or code')

    if not disc_code and disc_name:
        try:
            disc_code = p.findall('./СтрокиПлана/Строка[@Дис="{}"]'.format(disc_name))[0].attrib['НовИдДисциплины']
            d['disciplinecode'] = disc_code
        except:
            raise KeyError('Discipline {} not found in plan file {}'.format(disc_name, planfile))


    # где что искать в XML-фалйе плана
    plan_finder = [
        ('plancode',   './Титул',                                       None,      'ПоследнийШифр'),
        ('planname',   './Титул/Специальности/Специальность[@Ном="1"]', None,      'Название'),
        ('level',       './Титул/Квалификации/Квалификация[@Ном="1"]',   None,      'Название'),
        ('discipline',  './СтрокиПлана/Строка[@НовИдДисциплины="{}"]',   disc_code, 'Дис'),
        ('disc',        './СтрокиПлана/Строка[@НовИдДисциплины="{}"]',   disc_code, None),
        ('competences', './СтрокиПлана/Строка[@НовИдДисциплины="{}"]',   disc_code, 'КомпетенцииКоды'),
    ]

    for key, path_string, value, attribute in plan_finder:
        path = path_string.format(value)
        try:
            element = p.findall(path)[0]
            d[key] = element if not attribute else element.attrib[attribute] 
        except:
            raise KeyError('Path {} not found in plan file {}'.format(path, planfile))
        if type(d[key]) == str:
            d[key] = d[key].strip().replace('  ', ' ')

    print(' Found discipline {}-{} ({})'.format(disc_code, d['discipline'], d['competences']) )

    semesters = d['disc'].findall('./Сем')
    d.update(parse_semester_data(semesters))
    
    competences = p.findall('./Компетенции')[0]
    d['Компетенцииs'] = expand_competence_list(d['competences'], competences)

    d['zet'] = sum(map(int, d['ЗЕТ']))
    d['planname'] = d['planname'].replace('Направление:', '').strip()
    d['level'] = 'бакалавриата' if d['level']=='бакалавр' else 'магистратуры'
    del d['disc']
    
    print(' {}: Семестры {}:     {}'.format(d['level'].upper(), d['Семs'], d['формаконтроляs']))
    
    return d
    

def parse_semester_data(semesters : list) -> dict:
    """создает словарь, в котором типам занятий и формам контроля 
    соответатвуют списки по семестрам часов такого типа (ЗЕТов,...).
    Для списочных значений создаются простые строчные атрибуты 
    добавлением s к имени ключа, например, если
       d['Лаб'] = ['34', '38'], то
       d['Лабs'] = '34 / 38'.
    """
    d = {}
    hours = ('Лек', 'Пр', 'Лаб', 'КСР',  'СРС', 'ЧасЭкз',)
    controls = ('Зач', 'Экз')
    sems = ('Ном',  'ЗЕТ')

    for atts in (hours, controls, sems):
        for att in atts:
            d[att] = [sem.attrib.get(att, '') for sem in semesters]

    calc_hour_totals(d)

    d['Курс'] = list({str((int(sem_no) - 1)//2 + 1): 1 for sem_no in d['Ном']}.keys())
    d['Курс'].sort()

    for key in hours + ('ЗЕТ',):
        d[key+'s'] = ' / '.join([x if x else '–' for x in d[key]])

    d['Семs'] = ', '.join(d['Ном'])
    d['Курсs'] = ', '.join(d['Курс'])

    name = {'Зач': 'зачет', 'Экз': 'экзамен'}
    for form in controls:
        d[form] = [name[form] if x else '' for x in d[form]]    
    d['формаконтроля'] = [d['Зач'][i] + d['Экз'][i] for i,s in enumerate(semesters)]
    d['формаконтроляs'] = ' / '.join(d['формаконтроля']).replace('зачетэкзамен', 'зачет+экзамен')
    
    return d


def calc_hour_totals(d : dict):
    """ подсчитывает суммарные часы ВсегоЧас и ВсегоАудЧас в каждом семестре из
        словаря, в котором они по видам занятий уже есть""" 
    for aud in (True, False):
        h_types = ('Лек', 'Пр', 'Лаб') if aud else ('Лек', 'Пр', 'Лаб', 'КСР',  'СРС')
        totals_name = 'ВсегоАудЧас' if aud else 'ВсегоЧас'
        semester_count = len(d['Лек'])
        d[totals_name] = [0] * semester_count
        for sem in range(semester_count):
            for h_type in h_types:
                if d[h_type][sem]:
                    d[totals_name][sem] += int(d[h_type][sem])
        d[totals_name + 's'] = ' / '.join(map(str, d[totals_name]))


def expand_competence_list(comp_string : str, plan_competences : list):
    """по строке с кодами компетенций вида '6&11' дает словарь вида
    {'ОК-7': 'способность...', 'ПК-1': 'способность'}"""
    d = OrderedDict()
    for comp_code in comp_string.split('&'):
        x = plan_competences.findall('./Строка[@Код="{}"]'.format(comp_code))[0]
        d[x.attrib['Индекс']] = x.attrib['Содержание']
    return d


def produce_tex(template, filename, context, compile=True):
    """Генерирует новый .tex-файл РПД, подставляя данные контекста в шаблон.
    Если compile==True, вызывает xelatex на полученном файле"""
    fn = splitpath(filename)[1]
    tex_file = splitext(fn)[0] + '.tex'
    output = open(tex_file, 'w', encoding='utf-8')
    output.write(template.render(**context))
    output.close()
    
    if compile:
        sleep(0.5)
        execute(['xelatex', '--synctex=1', tex_file ])


if __name__ == '__main__':
    main()