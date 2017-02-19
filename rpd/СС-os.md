# IT 2008

## Platform Technologies (PT) – 14 core hours
PT. Operating Systems
PT. Architecture and Organization
PT. Computing Infrastructures
PT. Enterprise Deployment Software
PT. Firmware
PT. Hardware

IT professionals will encounter a variety of platforms in their careers. The role of the IT professional is to select, deploy, integrate and administer platforms or components to support the organization’s IT infrastructure. This knowledge area includes the fundamentals of hardware and software and how they integrate to form essential components of IT systems.

### PT. Operating Systems
Minimum core coverage time: 10 hours
Topics:
Overview
Operating system principles
Concurrency
Scheduling and dispatch
Memory management
Device management
Security and protection
File systems
Real-time and embedded systems
Fault tolerance
Scripting
Virtualization

*Core learning outcomes:*
1. Describe the necessary components and functions of an operating system.
2. Compare at least two operating systems and evaluate their suitability to a given task or goal.
3. Install a current operating system and validate that the installation was successful.
4. Explain the benefits of using scripts to automate operating systems tasks.
5. Explain concurrency as it relates to scheduling and dispatching.
6. Describe the advantages and issues associated with virtualization.
*Advanced learning outcomes:*
1. Analyze operating system requirements and recommend an appropriate operating system to meet the
requirements.
2. Install several current operating systems and validate that the installations were successful.
3. Write at least one script to perform an operating system task.
4. Install a system with at least two virtual machines.
5. Compare and contrast the memory management strategies of various popular operating systems.
6. Compare and contrast the security models of various popular operating systems.
7. Compare and contrast the file systems of various popular operating systems.
8. Explain the value of fault tolerance for disaster recovery.
9. Explain the implications of virtualization for disaster recovery.

### PT. Architecture and Organization
Minimum core coverage time: 3 hours
Topics:
Machine-level representation of data
Assembly-level machine organization
Memory system organization & architecture
Interfacing and communication
Functional organization
Multiprocessing and alternative architectures
Performance enhancements
*Core learning outcomes:*
1. Describe how numbers and characters are represented in a computer.
2. Draw a block diagram, including interconnections, of the main parts of a computer.
3. Describe how a computer stores and retrieves information to/from memory and hard drives.
4. Define the terms: bus, handshaking, serial, parallel, data rate.
*Advanced learning outcomes:*
1. Plan and write a simple assembly-language program.

## System Administration and Maintenance (SA) – 11 core hours

SA. Operating Systems
SA. Applications
SA. Administrative Activities
SA. Administrative Domains

Virtually all organizations have IT needs. It is the role of the IT professional to design, select, apply, deploy
and manage computing systems to support the organization. This knowledge area consists of those skills and
concepts that are essential to the administration of operating systems, networks, software, file systems, file
servers, web systems, database systems, and system documentation, policies, and procedures. This also
includes education and support of the users of these systems.

### SA. Operating Systems
Minimum core coverage time: 4 hours
Topics:
Installation
Configuration
Maintenance (service packs, patches, etc.)
Server services (print, file, DHCP, DNS, FTP, HTTP, mail, SNMP, telnet)
Client services
Support

*Core learning outcomes:*
1. Install at least one current operating system.
2. Discuss the importance of system configuration for an organization.
3. Describe the importance of system maintenance for an organization.
4. Identify situations in which a system needs to be reconfigured.
5. Describe when a system requires maintenance.
6. Distinguish between server and client services.
7. Identify situations in which a support organization needs to be consulted in resolving operating
system issues.

*Advanced learning outcomes:*
1. Evaluate various operating systems and recommend a particular operating system to satisfy given needs.
2. Modify the configuration of an operating system.
3. Analyze the pros and cons of installing service packs and updates.
4. Recommend when service packs and operating system updates should be installed.
5. Install service packs and operating system updates.
6. Install various server and client services

# CS2013
## OS
An operating system defines an abstraction of hardware and manages resource sharing among the computer’s users. The topics in this area explain the most basic knowledge of operating systems in the sense of interfacing an operating system to networks, teaching the difference between the kernel and user modes, and developing key approaches to operating system design and implementation. This knowledge area is structured to be complementary to the Systems Fundamentals (SF), Networking and Communication (NC), Information Assurance and Security (IAS), and the Parallel and Distributed Computing (PD) knowledge areas. The Systems Fundamentals and Information Assurance and Security knowledge areas are the new ones to include contemporary issues. For example, Systems Fundamentals includes topics such as performance, virtualization and isolation, and resource allocation and scheduling; Parallel and Distributed Systems includes parallelism fundamentals; and and Information Assurance and Security includes forensics and security issues in depth. Many courses in Operating Systems will draw material from across these knowledge areas.

### OS/Overview
1. Explain the objectives and functions of modern operating systems. [Familiarity]
2. Analyze the tradeoffs inherent in operating system design. [Usage]
3. Describe the functions of a contemporary operating system with respect to convenience, efficiency, and the ability to evolve. [Familiarity]
4. Discuss networked, client-server, distributed operating systems and how they differ from single user operating systems. [Familiarity]
5. Identify potential threats to operating systems and the security features design to guard against them. [Familiarity]

### Principles
1. Explain the concept of a logical layer. [Familiarity]
2. Explain the benefits of building abstract layers in hierarchical fashion. [Familiarity]
3. Describe the value of APIs and middleware. [Assessment]
4. Describe how computing resources are used by application software and managed by system software. [Familiarity]
5. Contrast kernel and user mode in an operating system. [Usage]
6. Discuss the advantages and disadvantages of using interrupt processing. [Familiarity]
7. Explain the use of a device list and driver I/O queue. [Familiarity]

### Concurrency
1. Describe the need for concurrency within the framework of an operating system. [Familiarity]
2. Demonstrate the potential run-time problems arising from the concurrent operation of many separate tasks. [Usage]
3. Summarize the range of mechanisms that can be employed at the operating system level to realize concurrent systems and describe the benefits of each. [Familiarity]
4. Explain the different states that a task may pass through and the data structures needed to support the management of many tasks. [Familiarity]
5. Summarize techniques for achieving synchronization in an operating system (e.g., describe how to implement a semaphore using OS primitives). [Familiarity]
6. Describe reasons for using interrupts, dispatching, and context switching to support concurrency in an operating system. [Familiarity]
7. Create state and transition diagrams for simple problem domains. [Usage]

### OS/Scheduling and Dispatch
1. Compare and contrast the common algorithms used for both preemptive and non-preemptive scheduling of tasks in operating systems, such as priority, performance comparison, and fair-share schemes. [Usage]
2. Describe relationships between scheduling algorithms and application domains. [Familiarity]
3. Discuss the types of processor scheduling such as short-term, medium-term, long-term, and I/O. [Familiarity]
4. Describe the difference between processes and threads. [Usage]
5. Compare and contrast static and dynamic approaches to real-time scheduling. [Usage]
6. Discuss the need for preemption and deadline scheduling. [Familiarity]
7. Identify ways that the logic embodied in scheduling algorithms are applicable to other domains, such as disk I/O, network scheduling, project scheduling, and problems beyond computing. [Usage]

### OS/Memory Management
1. Explain memory hierarchy and cost-performance trade-offs. [Familiarity]
2. Summarize the principles of virtual memory as applied to caching and paging. [Familiarity]
3. Evaluate the trade-offs in terms of memory size (main memory, cache memory, auxiliary memory) and processor speed. [Assessment]
4. Defend the different ways of allocating memory to tasks, citing the relative merits of each. [Assessment]
5. Describe the reason for and use of cache memory (performance and proximity, different dimension of how caches complicate isolation and VM abstraction). [Familiarity]
6. Discuss the concept of thrashing, both in terms of the reasons it occurs and the techniques used to recognize and manage the problem. [Familiarity]

### OS/File Systems
1. Describe the choices to be made in designing file systems. [Familiarity]
2. Compare and contrast different approaches to file organization, recognizing the strengths and weaknesses of each. [Usage]
3. Summarize how hardware developments have led to changes in the priorities for the design and the management of file systems. [Familiarity]
4. Summarize the use of journaling and how log-structured file systems enhance fault tolerance. [Familiarity]

### OS/Security
Learning Outcomes:

1. Articulate the need for protection and security in an OS (cross-reference IAS/Security Architecture and Systems Administration/Investigating Operating Systems Security for various systems). [Assessment]
2. Summarize the features and limitations of an operating system used to provide protection and security (cross-reference IAS/Security Architecture and Systems Administration). [Familiarity]
3. Explain the mechanisms available in an OS to control access to resources (cross-reference IAS/Security Architecture and Systems Administration/Access Control/Configuring systems to operate securely as an IT system). [Familiarity]
4. Carry out simple system administration tasks according to a security policy, for example creating accounts, setting permissions, applying patches, and arranging for regular backups (cross-reference IAS/Security Architecture and Systems Administration). [Usage]

### OS/Virtual Machines
Learning Outcomes:

1. Explain the concept of virtual memory and how it is realized in hardware and software. [Familiarity]
5. Differentiate emulation and isolation. [Familiarity]
6. Evaluate virtualization trade-offs. [Assessment]
2. Discuss hypervisors and the need for them in conjunction with different types of hypervisors. [Usage]