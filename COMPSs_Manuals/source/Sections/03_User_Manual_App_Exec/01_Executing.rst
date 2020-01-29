Executing COMPSs applications
=============================

Prerequisites
-------------

Prerequisites vary depending on the application’s code language: for
Java applications the users need to have a **jar archive** containing
all the application classes, for Python applications there are no
requirements and for C/C++ applications the code must have been
previously compiled by using the *buildapp* command.

For further information about how to develop COMPSs applications please
refer to :ref:`Application development`.

Runcompss command
-----------------

COMPSs applications are executed using the **runcompss** command:

.. code-block:: console

    compss@bsc:~$ runcompss [options] application_name [application_arguments]

The application name must be the fully qualified name of the application
in Java, the path to the *.py* file containing the main program in
Python and the path to the master binary in C/C++.

The application arguments are the ones passed as command line to main
application. This parameter can be empty.

The ``runcompss`` command allows the users to customize a COMPSs
execution by specifying different options. For clarity purposes,
parameters are grouped in *Runtime configuration*, *Tools enablers* and
*Advanced options*.

.. code-block:: console

    compss@bsc:~$ runcompss -h

    Usage: runcompss [options] application_name application_arguments

    * Options:
    General:
      --help, -h                              Print this help message

      --opts                                  Show available options

      --version, -v 			    Print COMPSs version

    Tools enablers:
      --graph=<bool>, --graph, -g             Generation of the complete graph (true/false)
                                              When no value is provided it is set to true
                                              Default: false
      --tracing=<level>, --tracing, -t        Set generation of traces and/or tracing level ( [ true | basic ] | advanced | scorep | arm-map | arm-ddt | false)
                                              True and basic levels will produce the same traces.
                                              When no value is provided it is set to true
                                              Default: false
      --monitoring=<int>, --monitoring, -m    Period between monitoring samples (milliseconds)
                                              When no value is provided it is set to 2000
                                              Default: 0
      --external_debugger=<int>,
      --external_debugger                     Enables external debugger connection on the specified port (or 9999 if empty)
                                              Default: false

    Runtime configuration options:
      --task_execution=<compss|storage>       Task execution under COMPSs or Storage.
                                              Default: compss
      --storage_impl=<string>                 Path to an storage implementation. Shortcut to setting pypath and classpath. See Runtime/storage in your installation folder.
      --storage_conf=<path>                   Path to the storage configuration file
                                              Default: null
      --project=<path>                        Path to the project XML file
                                              Default: /apps/COMPSs/2.6.pr/Runtime/configuration/xml/projects/default_project.xml
      --resources=<path>                      Path to the resources XML file
                                              Default: /apps/COMPSs/2.6.pr/Runtime/configuration/xml/resources/default_resources.xml
      --lang=<name>                           Language of the application (java/c/python)
                                              Default: Inferred is possible. Otherwise: java
      --summary                               Displays a task execution summary at the end of the application execution
                                              Default: false
      --log_level=<level>, --debug, -d        Set the debug level: off | info | debug
                                              Warning: Off level compiles with -O2 option disabling asserts and __debug__
                                              Default: off

    Advanced options:
      --extrae_config_file=<path>             Sets a custom extrae config file. Must be in a shared disk between all COMPSs workers.
                                              Default: null
      --comm=<ClassName>                      Class that implements the adaptor for communications
                                              Supported adaptors: es.bsc.compss.nio.master.NIOAdaptor | es.bsc.compss.gat.master.GATAdaptor
                                              Default: es.bsc.compss.nio.master.NIOAdaptor
      --conn=<className>                      Class that implements the runtime connector for the cloud
                                              Supported connectors: es.bsc.compss.connectors.DefaultSSHConnector
                                                                  | es.bsc.compss.connectors.DefaultNoSSHConnector
                                              Default: es.bsc.compss.connectors.DefaultSSHConnector
      --streaming=<type>                      Enable the streaming mode for the given type.
                                              Supported types: FILES, OBJECTS, PSCOS, ALL, NONE
                                              Default: null
      --streaming_master_name=<str>           Use an specific streaming master node name.
                                              Default: null
      --streaming_master_port=<int>           Use an specific port for the streaming master.
                                              Default: null
      --scheduler=<className>                 Class that implements the Scheduler for COMPSs
                                              Supported schedulers: es.bsc.compss.scheduler.fullGraphScheduler.FullGraphScheduler
                                                                  | es.bsc.compss.scheduler.fifoScheduler.FIFOScheduler
                                                                  | es.bsc.compss.scheduler.resourceEmptyScheduler.ResourceEmptyScheduler
                                              Default: es.bsc.compss.scheduler.loadbalancing.LoadBalancingScheduler
      --scheduler_config_file=<path>          Path to the file which contains the scheduler configuration.
                                              Default: Empty
      --library_path=<path>                   Non-standard directories to search for libraries (e.g. Java JVM library, Python library, C binding library)
                                              Default: Working Directory
      --classpath=<path>                      Path for the application classes / modules
                                              Default: Working Directory
      --appdir=<path>                         Path for the application class folder.
                                              Default: /home/bsc19/bsc19234
      --pythonpath=<path>                     Additional folders or paths to add to the PYTHONPATH
                                              Default: /home/bsc19/bsc19234
      --base_log_dir=<path>                   Base directory to store COMPSs log files (a .COMPSs/ folder will be created inside this location)
                                              Default: User home
      --specific_log_dir=<path>               Use a specific directory to store COMPSs log files (no sandbox is created)
                                              Warning: Overwrites --base_log_dir option
                                              Default: Disabled
      --uuid=<int>                            Preset an application UUID
                                              Default: Automatic random generation
      --master_name=<string>                  Hostname of the node to run the COMPSs master
                                              Default:
      --master_port=<int>                     Port to run the COMPSs master communications.
                                              Only for NIO adaptor
                                              Default: [43000,44000]
      --jvm_master_opts="<string>"            Extra options for the COMPSs Master JVM. Each option separed by "," and without blank spaces (Notice the quotes)
                                              Default:
      --jvm_workers_opts="<string>"           Extra options for the COMPSs Workers JVMs. Each option separed by "," and without blank spaces (Notice the quotes)
                                              Default: -Xms1024m,-Xmx1024m,-Xmn400m
      --cpu_affinity="<string>"               Sets the CPU affinity for the workers
                                              Supported options: disabled, automatic, user defined map of the form "0-8/9,10,11/12-14,15,16"
                                              Default: automatic
      --gpu_affinity="<string>"               Sets the GPU affinity for the workers
                                              Supported options: disabled, automatic, user defined map of the form "0-8/9,10,11/12-14,15,16"
                                              Default: automatic
      --fpga_affinity="<string>"              Sets the FPGA affinity for the workers
                                              Supported options: disabled, automatic, user defined map of the form "0-8/9,10,11/12-14,15,16"
                                              Default: automatic
      --fpga_reprogram="<string>"             Specify the full command that needs to be executed to reprogram the FPGA with the desired bitstream. The location must be an absolute path.
                                              Default:
      --task_count=<int>                      Only for C/Python Bindings. Maximum number of different functions/methods, invoked from the application, that have been selected as tasks
                                              Default: 50
      --input_profile=<path>                  Path to the file which stores the input application profile
                                              Default: Empty
      --output_profile=<path>                 Path to the file to store the application profile at the end of the execution
                                              Default: Empty
      --PyObject_serialize=<bool>             Only for Python Binding. Enable the object serialization to string when possible (true/false).
                                              Default: false
      --persistent_worker_c=<bool>            Only for C Binding. Enable the persistent worker in c (true/false).
                                              Default: false
      --enable_external_adaptation=<bool>     Enable external adaptation. This option will disable the Resource Optimizer.
                                              Default: false
      --python_interpreter=<string>           Python interpreter to use (python/python2/python3).
                                              Default: python Version: 2
      --python_propagate_virtual_environment=<true>  Propagate the master virtual environment to the workers (true/false).
                                                     Default: true
      --python_mpi_worker=<false>             Use MPI to run the python worker instead of multiprocessing. (true/false).
                                              Default: false

    * Application name:
        For Java applications:   Fully qualified name of the application
        For C applications:      Path to the master binary
        For Python applications: Path to the .py file containing the main program

    * Application arguments:
        Command line arguments to pass to the application. Can be empty.

Running a COMPSs application
----------------------------

Before running COMPSs applications the application files **must** be in
the **CLASSPATH**. Thus, when launching a COMPSs application, users can
manually pre-set the **CLASSPATH** environment variable or can add the
``--classpath`` option to the ``runcompss`` command.

The next three sections provide specific information for launching
COMPSs applications developed in different code languages (Java, Python
and C/C++). For clarity purposes, we will use the *Simple*
application (developed in Java, Python and C++) available in the
COMPSs Virtual Machine or at https://compss.bsc.es/projects/bar webpage.
This application takes an integer as input parameter and increases it by
one unit using a task. For further details about the codes please refer
to :ref:`Sample Applications`.

Running Java applications
~~~~~~~~~~~~~~~~~~~~~~~~~

A Java COMPSs application can be launched through the following command:

.. code-block:: console

    compss@bsc:~$ cd tutorial_apps/java/simple/jar/
    compss@bsc:~/tutorial_apps/java/simple/jar$ runcompss simple.Simple <initial_number>

.. code-block:: console

    compss@bsc:~/tutorial_apps/java/simple/jar$ runcompss simple.Simple 1
    [  INFO] Using default execution type: compss
    [  INFO] Using default location for project file: /opt/COMPSs/Runtime/configuration/xml/projects/default_project.xml
    [  INFO] Using default location for resources file: /opt/COMPSs/Runtime/configuration/xml/resources/default_resources.xml
    [  INFO] Using default language: java

    ----------------- Executing simple.Simple --------------------------

    WARNING: COMPSs Properties file is null. Setting default values
    [(1066)    API]  -  Starting COMPSs Runtime v<version>
    Initial counter value is 1
    Final counter value is 2
    [(4740)    API]  -  Execution Finished

    ------------------------------------------------------------

In this first execution we use the default value of the ``--classpath``
option to automatically add the jar file to the classpath (by executing
runcompss in the directory which contains the jar file). However, we can
explicitly do this by exporting the **CLASSPATH** variable or by
providing the ``--classpath`` value. Next, we provide two more ways to
perform the same execution:

.. code-block:: console

    compss@bsc:~$ export CLASSPATH=$CLASSPATH:/home/compss/tutorial_apps/java/simple/jar/simple.jar
    compss@bsc:~$ runcompss simple.Simple <initial_number>

.. code-block:: console

    compss@bsc:~$ runcompss --classpath=/home/compss/tutorial_apps/java/simple/jar/simple.jar \
                            simple.Simple <initial_number>

Running Python applications
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To launch a COMPSs Python application users have to provide the
``--lang=python`` option to the runcompss command. If the extension of
the main file is a regular Python extension (``.py`` or ``.pyc``) the
*runcompss* command can also infer the application language without
specifying the *lang* flag.

.. code-block:: console

    compss@bsc:~$ cd tutorial_apps/python/simple/
    compss@bsc:~/tutorial_apps/python/simple$ runcompss --lang=python ./simple.py <initial_number>

.. code-block:: console

    compss@bsc:~/tutorial_apps/python/simple$ runcompss simple.py 1
    [  INFO] Using default execution type: compss
    [  INFO] Using default location for project file: /opt/COMPSs/Runtime/configuration/xml/projects/default_project.xml
    [  INFO] Using default location for resources file: /opt/COMPSs/Runtime/configuration/xml/resources/default_resources.xml
    [  INFO] Inferred PYTHON language

    ----------------- Executing simple.py --------------------------

    WARNING: COMPSs Properties file is null. Setting default values
    [(616)    API]  -  Starting COMPSs Runtime v<version>
    Initial counter value is 1
    Final counter value is 2
    [(4297)    API]  -  Execution Finished

    ------------------------------------------------------------

**Attention**: Executing without debug (e.g. default log level or
``--log_level=off``) uses -O2 compiled sources, disabling ``asserts``
and ``__debug__``.

Alternatively, it is possible to execute the a COMPSs Python application
using ``pycompss`` as module:

.. code-block:: console

    compss@bsc:~$ python -m pycompss <runcompss_flags> <application> <application_parameters>

Consequently, the previous example could also be run as follows:

.. code-block:: console

    compss@bsc:~$ cd tutorial_apps/python/simple/
    compss@bsc:~/tutorial_apps/python/simple$ python -m pycompss simple.py <initial_number>

If the ``-m pycompss`` is not set, the application will be run ignoring
all PyCOMPSs imports, decorators and API calls, that is, sequentially.

In order to run a COMPSs Python application with a different
interpreter, the *runcompss* command provides a specific flag:

.. code-block:: console

    compss@bsc:~$ cd tutorial_apps/python/simple/
    compss@bsc:~/tutorial_apps/python/simple$ runcompss --python_interpreter=python3 ./simple.py <initial_number>

However, when using the *pycompss* module, it is inferred from the
python used in the call:

.. code-block:: console

    compss@bsc:~$ cd tutorial_apps/python/simple/
    compss@bsc:~/tutorial_apps/python/simple$ python3 -m pycompss simple.py <initial_number>

Finally, both *runcompss* and *pycompss* module provide a particular
flag for virtual environment propagation
(``--python_propagate_virtual_environment=<bool>``). This, flag is
intended to activate the current virtual environment in the worker nodes
when set to true.

Running C/C++ applications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To launch a COMPSs C/C++ application users have to compile the
C/C++ application by means of the ``buildapp`` command. For
further information please refer to :ref:`Application development`. Once
complied, the ``--lang=c`` option must be provided to the runcompss
command. If the main file is a C/C++ binary the *runcompss* command
can also infer the application language without specifying the *lang*
flag.

.. code-block:: console

    compss@bsc:~$ cd tutorial_apps/c/simple/
    compss@bsc:~/tutorial_apps/c/simple$ runcompss --lang=c simple <initial_number>

.. code-block:: console

    compss@bsc:~/tutorial_apps/c/simple$ runcompss ~/tutorial_apps/c/simple/master/simple 1
    [  INFO] Using default execution type: compss
    [  INFO] Using default location for project file: /opt/COMPSs/Runtime/configuration/xml/projects/default_project.xml
    [  INFO] Using default location for resources file: /opt/COMPSs/Runtime/configuration/xml/resources/default_resources.xml
    [  INFO] Inferred C/C++ language

    ----------------- Executing simple --------------------------

    JVM_OPTIONS_FILE: /tmp/tmp.ItT1tQfKgP
    COMPSS_HOME: /opt/COMPSs
    Args: 1

    WARNING: COMPSs Properties file is null. Setting default values
    [(650)    API]  -  Starting COMPSs Runtime v<version>
    Initial counter value is 1
    [   BINDING]  -  @compss_wait_on  -  Entry.filename: counter
    [   BINDING]  -  @compss_wait_on  -  Runtime filename: d1v2_1497432831496.IT
    Final counter value is 2
    [(4222)    API]  -  Execution Finished

    ------------------------------------------------------------

Additional configurations
-------------------------

The COMPSs runtime has two configuration files: ``resources.xml`` and
``project.xml`` . These files contain information about the execution
environment and are completely independent from the application.

For each execution users can load the default configuration files or
specify their custom configurations by using, respectively, the
``--resources=<absolute_path_to_resources.xml>`` and the
``--project=<absolute_path_to_project.xml>`` in the ``runcompss``
command. The default files are located in the
``/opt/COMPSs/Runtime/configuration/xml/`` path. Users can manually edit
these files or can use the *Eclipse IDE* tool developed for COMPSs. For
further information about the *Eclipse IDE* please refer to :ref:`COMPSs IDE` Section.

For further details please check the :ref:`Configuration Files` Subsection
inside the :ref:`Installation and Administration` Section.
