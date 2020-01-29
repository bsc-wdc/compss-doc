Constraints
===========

This section provides a detailed information about all the supported
constraints by the COMPSs runtime for **Java**, **Python** and **C/C++**
languages. The constraints are defined as key-value pairs, where the key
is the name of the constraint. :numref:`supported_constraints` details the
available constraints names for *Java*, *Python* and *C/C++*, its value
type, its default value and a brief description.

.. table:: Arguments of the *@constraint* decorator
    :name: supported_constraints
    :widths: auto

    +-------------------------------+-------------------------------------+-------------------------------+------------------------------------------+---------------------+---------------------------------------------------------------------------------------+
    | **Java**                      | **Python**                          | **C / C++**                   | **Value type**                           | **Default value**   | **Description**                                                                       |
    +===============================+=====================================+===============================+==========================================+=====================+=======================================================================================+
    | computingUnits                | computing_units                     | ComputingUnits                | :math:`<`\ string\ :math:`>`             | "1"                 | Required number of computing units                                                    |
    +-------------------------------+-------------------------------------+-------------------------------+------------------------------------------+---------------------+---------------------------------------------------------------------------------------+
    | processorName                 | processor_name                      | ProcessorName                 | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Required processor name                                                               |
    +-------------------------------+-------------------------------------+-------------------------------+------------------------------------------+---------------------+---------------------------------------------------------------------------------------+
    | processorSpeed                | processor_speed                     | ProcessorSpeed                | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Required processor speed                                                              |
    +-------------------------------+-------------------------------------+-------------------------------+------------------------------------------+---------------------+---------------------------------------------------------------------------------------+
    | processorArchitecture         | processor_architecture              | ProcessorArchitecture         | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Required processor architecture                                                       |
    +-------------------------------+-------------------------------------+-------------------------------+------------------------------------------+---------------------+---------------------------------------------------------------------------------------+
    | processorType                 | processor_type                      | ProcessorType                 | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Required processor type                                                               |
    +-------------------------------+-------------------------------------+-------------------------------+------------------------------------------+---------------------+---------------------------------------------------------------------------------------+
    | processorPropertyName         | processor_property_name             | ProcessorPropertyName         | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Required processor property                                                           |
    +-------------------------------+-------------------------------------+-------------------------------+------------------------------------------+---------------------+---------------------------------------------------------------------------------------+
    | processorPropertyValue        | processor_property_value            | ProcessorPropertyValue        | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Required processor property value                                                     |
    +-------------------------------+-------------------------------------+-------------------------------+------------------------------------------+---------------------+---------------------------------------------------------------------------------------+
    | processorInternalMemorySize   | processor_internal_memory_size      | ProcessorInternalMemorySize   | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Required internal device memory                                                       |
    +-------------------------------+-------------------------------------+-------------------------------+------------------------------------------+---------------------+---------------------------------------------------------------------------------------+
    | processors                    | processors                          | -                             | List\ :math:`<`\ @Processor\ :math:`>`   | "{}"                | Required processors (check :numref:`processor_constraints` for Processor details)     |
    +-------------------------------+-------------------------------------+-------------------------------+------------------------------------------+---------------------+---------------------------------------------------------------------------------------+
    | memorySize                    | memory_size                         | MemorySize                    | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Required memory size in GBs                                                           |
    +-------------------------------+-------------------------------------+-------------------------------+------------------------------------------+---------------------+---------------------------------------------------------------------------------------+
    | memoryType                    | memory_type                         | MemoryType                    | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Required memory type (SRAM, DRAM, etc.)                                               |
    +-------------------------------+-------------------------------------+-------------------------------+------------------------------------------+---------------------+---------------------------------------------------------------------------------------+
    | storageSize                   | storage_size                        | StorageSize                   | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Required storage size in GBs                                                          |
    +-------------------------------+-------------------------------------+-------------------------------+------------------------------------------+---------------------+---------------------------------------------------------------------------------------+
    | storageType                   | storage_type                        | StorageType                   | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Required storage type (HDD, SSD, etc.)                                                |
    +-------------------------------+-------------------------------------+-------------------------------+------------------------------------------+---------------------+---------------------------------------------------------------------------------------+
    | operatingSystemType           | operating_system_type               | OperatingSystemType           | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Required operating system type (Windows, MacOS, Linux, etc.)                          |
    +-------------------------------+-------------------------------------+-------------------------------+------------------------------------------+---------------------+---------------------------------------------------------------------------------------+
    | operatingSystemDistribution   | operating_system_distribution       | OperatingSystemDistribution   | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Required operating system distribution (XP, Sierra, openSUSE, etc.)                   |
    +-------------------------------+-------------------------------------+-------------------------------+------------------------------------------+---------------------+---------------------------------------------------------------------------------------+
    | operatingSystemVersion        | operating_system_version            | OperatingSystemVersion        | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Required operating system version                                                     |
    +-------------------------------+-------------------------------------+-------------------------------+------------------------------------------+---------------------+---------------------------------------------------------------------------------------+
    | wallClockLimit                | wall_clock_limit                    | WallClockLimit                | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Maximum wall clock time                                                               |
    +-------------------------------+-------------------------------------+-------------------------------+------------------------------------------+---------------------+---------------------------------------------------------------------------------------+
    | hostQueues                    | host_queues                         | HostQueues                    | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Required queues                                                                       |
    +-------------------------------+-------------------------------------+-------------------------------+------------------------------------------+---------------------+---------------------------------------------------------------------------------------+
    | appSoftware                   | app_software                        | AppSoftware                   | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Required applications that must be available within the remote node for the task      |
    +-------------------------------+-------------------------------------+-------------------------------+------------------------------------------+---------------------+---------------------------------------------------------------------------------------+

All constraints are defined with a simple value except the *HostQueue*
and *AppSoftware* constraints, which allow multiple values.

The *processors* constraint allows the users to define multiple
processors for a task execution. This constraint is specified as a list
of @Processor annotations that must be defined as shown in :numref:`processor_constraints`

.. table:: Arguments of the *@Processor* decorator
    :name: processor_constraints
    :widths: auto

    +----------------------+--------------------------------+---------------------+---------------------------------------------+
    | **Annotation**       | **Value type**                 | **Default value**   | **Description**                             |
    +======================+================================+=====================+=============================================+
    | processorType        | :math:`<`\ string\ :math:`>`   | "CPU"               | Required processor type (e.g. CPU or GPU)   |
    +----------------------+--------------------------------+---------------------+---------------------------------------------+
    | computingUnits       | :math:`<`\ string\ :math:`>`   | "1"                 | Required number of computing units          |
    +----------------------+--------------------------------+---------------------+---------------------------------------------+
    | name                 | :math:`<`\ string\ :math:`>`   | "[unassigned]"      | Required processor name                     |
    +----------------------+--------------------------------+---------------------+---------------------------------------------+
    | speed                | :math:`<`\ string\ :math:`>`   | "[unassigned]"      | Required processor speed                    |
    +----------------------+--------------------------------+---------------------+---------------------------------------------+
    | architecture         | :math:`<`\ string\ :math:`>`   | "[unassigned]"      | Required processor architecture             |
    +----------------------+--------------------------------+---------------------+---------------------------------------------+
    | propertyName         | :math:`<`\ string\ :math:`>`   | "[unassigned]"      | Required processor property                 |
    +----------------------+--------------------------------+---------------------+---------------------------------------------+
    | propertyValue        | :math:`<`\ string\ :math:`>`   | "[unassigned]"      | Required processor property value           |
    +----------------------+--------------------------------+---------------------+---------------------------------------------+
    | internalMemorySize   | :math:`<`\ string\ :math:`>`   | "[unassigned]"      | Required internal device memory             |
    +----------------------+--------------------------------+---------------------+---------------------------------------------+
