Local
=======================
This section is intended to show how to execute COMPSs applications deploying the runtime as an agent in local machines.

Deploying a COMPSs Agent
------------------------
COMPSs Agents are deployed using the **compss_agent_start** command:

.. code-block:: console

    compss@bsc:~$ compss_agent_start [OPTION]
    
There is one mandatory parameter ``--hostname`` that indicates the name that other agents and itself use to refer to the agent. Bear in mind that agents are not able to dynamically modify its classpath; therefore, the ``--classpath`` parameter becomes important to indicate the application available on the agent. Any public method available on the classpath is an execution request candidate. 

The following command raises an agent with name 192.168.1.100 and any of the public methods of the classes encapsulated in the jarfile ``/app/path.jar`` can be executed.

.. code-block:: console

    compss@bsc:~$ compss_agent_start  --hostname=192.168.1.100 --classpath=/app/path.jar

The ``compss_agent_start`` command allows users to set up the COMPSs runtime by specifying different options in the same way as done for the ``runcompss`` command. To indicate the available resources, the device administrator can use the ``--project`` and ``--resources`` option exactly in the same way as for the ``runcompss`` command. For further details on how to dynamically modify the available resources, please, refer to section :ref:`Sections/03_Execution_Environments/03_Deployments/02_Agents/01_Local:Modifying the available resources`. 

Currently, COMPSs agents allow interaction through two interfaces: the Comm interface and the REST interface. The Comm interface leverages on a propietary protocol to submit operations and request updates on the current resource configuration of the agent. Although users and applications can use this interface, its design purpose is to enable high-performance interactions among agents rather than supporting user interaction. The REST interface takes the completely opposed approach; Users should interact with COMPSs agents through it rather than submitting tasks with the Comm interface. The COMPSs agent allows to enact both interfaces at a time; thus, users can manually submit operations using the REST interface, while other agents can use the Comm interface. However, the device owner can decide at deploy time which of the interfaces will be available on the agent and through which port the API will be exposed using the ``rest_port`` and ``comm_port`` options of the ``compss_agent_start`` command. Other agents can be configured to interact with the agent through any of the interfaces. For further details on how to configure the interaction with another agent, please, refer to section :ref:`Sections/03_Execution_Environments/03_Deployments/02_Agents/01_Local:Modifying the available resources`. 

.. code-block:: console

    compss@bsc:~$ compss_agent_start -h

    Usage: /opt/COMPSs/Runtime/scripts/user/compss_agent_start [OPTION]...

    COMPSs options:

        --appdir=<path>                         Path for the application class folder.
                                                Default: /home/flordan/git/compss/framework/builders

        --classpath=<path>                      Path for the application classes / modules
                                                Default: Working Directory

        --comm=<className>                      Class that implements the adaptor for communications with other nodes
                                                Supported adaptors:
                                                    ├── es.bsc.compss.nio.master.NIOAdaptor
                                                    ├── es.bsc.compss.gat.master.GATAdaptor
                                                    ├── es.bsc.compss.agent.rest.Adaptor
                                                    └── es.bsc.compss.agent.comm.CommAgentAdaptor
                                                Default: es.bsc.compss.agent.comm.CommAgentAdaptor

        --comm_port=<int>                       Port on which the agent sets up a Comm interface. (<=0: Disabled)

        -d, --debug                             Enable debug. (Default: disabled)

        --hostname                              Name with which itself and other agents will identify the agent.

        --jvm_opts="string"                     Extra options for the COMPSs Runtime JVM. Each option separed by "," and without blank spaces (Notice the quotes)

        --library_path=<path>                   Non-standard directories to search for libraries (e.g. Java JVM library, Python library, C binding library)
                                                Default: Working Directory

        --log_dir=<path>                        Log directory. (Default: /tmp/)

        --log_level=<level>                     Set the debug level: off | info | api | debug | trace
                                                Default: off

        --master_port=<int>                     Port to run the COMPSs master communications.
                                                (Only when es.bsc.compss.nio.master.NIOAdaptor is used. The value is overriden by the comm_port value.)
                                                Default: [43000,44000]

        --pythonpath=<path>                     Additional folders or paths to add to the PYTHONPATH
                                                Default: /home/flordan/git/compss/framework/builders

        --python_interpreter=<string>           Python interpreter to use (python/python2/python3).
                                                Default: python Version: 

        --python_propagate_virtual_environment=<true>   Propagate the master virtual environment to the workers (true/false).
                                                        Default: true

        --python_mpi_worker=<false>             Use MPI to run the python worker instead of multiprocessing. (true/false).
                                                Default: false

        --python_memory_profile                 Generate a memory profile of the master.
                                                Default: false
        --python_worker_cache=<string>          Python worker cache (true/size/false).
                                                Only for NIO without mpi worker and python >= 3.8.
                                                Default: false

        --project=<path>                        Path of the project file
                                                (Default: /opt/COMPSs/Runtime/configuration/xml/projects/examples/local/project.xml)

        --resources=<path>                      Path of the resources file
                                                (Default: /opt/COMPSs/Runtime/configuration/xml/resources/examples/local/resources.xml)

        --rest_port=<int>                       Port on which the agent sets up a REST interface. (<=0: Disabled)

        --reuse_resources_on_block=<boolean>    Enables/Disables reusing the resources assigned to a task when its execution stalls.
                                                (Default:true)

        --scheduler=<className>                 Class that implements the Scheduler for COMPSs
                                                Supported schedulers:
                                                    ├── es.bsc.compss.scheduler.fifodatalocation.FIFODataLocationScheduler
                                                    ├── es.bsc.compss.scheduler.fifonew.FIFOScheduler
                                                    ├── es.bsc.compss.scheduler.fifodatanew.FIFODataScheduler
                                                    ├── es.bsc.compss.scheduler.lifonew.LIFOScheduler
                                                    ├── es.bsc.compss.components.impl.TaskScheduler
                                                    └── es.bsc.compss.scheduler.loadbalancing.LoadBalancingScheduler
                                                Default: es.bsc.compss.scheduler.loadbalancing.LoadBalancingScheduler

        --scheduler_config_file=<path>          Path to the file which contains the scheduler configuration.
                                                Default: Empty

        --input_profile=<path>                  Path to the file which stores the input application profile
                                                Default: Empty

        --output_profile=<path>                 Path to the file to store the application profile at the end of the execution
                                                Default: Empty

        --summary                               Displays a task execution summary at the end of the application execution
                                                Default: false

        --tracing=<level>, --tracing, -t        Set generation of traces and/or tracing level ( [ true | basic ] | advanced | scorep | arm-map | arm-ddt | false)
                                                True and basic levels will produce the same traces.
                                                When no value is provided it is set to 1
                                                Default: 0

        --trace_label=<string>                  Add a label in the generated trace file. Only used in the case of tracing is activated.
                                                Default: None

        Other options:
        --help                                  prints this message



Executing an operation
------------------------
The **compss_agent_call_operation** commands interacts with the REST interface of the COMPSs agent to submit an operation.

.. code-block:: console

    compss@bsc:~$ compss_agent_call_operation [options] application_name application_arguments

The command has two mandatory flags ``--master_node`` and ``--master_port`` to indicate the endpoint of the COMPSs Agent. By default, the command submits an execution of the ``main`` method of the Java class with the name passed in as the ``application_name`` and gathering all the application arguments in a single String[] instance. To execute Python methods, the user can use the ``--lang=PYTHON`` option and the Agent will execute the python script with the name passed in as ``application_name``. Operation invocations can be customized by using other options of the command. The ``--method_name`` option allow to execute a specific method; in the case of specifying a method, each of the parameters will be passed in as a different parameter to the function and it is necessary to indicate the ``--array`` flag to encapsulate all the parameters as an array.

Additionally, the command offers two options to shutdown a whole agents deployment upon the operation completion. The flag ``--stop`` indicates that, at the end of the operation, the agent receiving the operation request will stop. For shutting down the rest of the deployment, the command offers the option ``--forward_to`` to indicate a list of IP:port pairs. Upon the completion of the operation, the agent receiving the request will forward the stop command to all the nodes specified in such option.

.. code-block:: console

    compss@bsc.es:~$ compss_agent_call_operation -h

    Usage: compss_agent_call_operation [options] application_name application_arguments

    * Options:
    General:
        --help, -h                              Print this help message

        --opts                                  Show available options

        --version, -v                           Print COMPSs version

        --master_node=<string>                  Node where to run the COMPSs Master
                                                Mandatory

        --master_port=<string>                  Node where to run the COMPSs Master
                                                Mandatory    

        --stop                                  Stops the agent after the execution
                                                of the task.   

        --forward_to=<list>                     Forwards the stop action to other
                                                agents, the list shoud follow the
                                                format:
                                                <ip1>:<port1>;<ip2>:<port2>...
    Launch configuration:
        --cei=<string>                          Canonical name of the interface declaring the methods
                                                Default: No interface declared

        --lang=<string>                         Language implementing the operation
                                                Default: JAVA

        --method_name=<string>                  Name of the method to invoke
                                                Default: main and enables array parameter

        --parameters_array, --array             Parameters are encapsulated as an array
                                                Default: disabled




For example, to submit the execution of the ``demoFunction`` method from the ``es.bsc.compss.tests.DemoClass`` class passing in a single parameter with value 1 on the agent 127.0.0.1 with a REST interface listening on port 46101, the user should execute the following example command:

.. code-block:: console

    compss@bsc.es:~$ compss_agent_call_operation --master_node="127.0.0.1" --master_port="46101" --method_name="demoFunction" es.bsc.compss.test.DemoClass 1 

For the agent to detect inner tasks within the operation execution, the COMPSs Programming model requires an interface selecting the methods to be replaced by asynchronous task creations. An invoker should use the ``--cei`` option to specify the name of the interface selecting the tasks. 

Modifying the available resources
---------------------------------
Finally, the COMPSs framework offers tree commands to control dynamically the pool of resources available for the runtime un one agent. These commands are ``compss_agent_add_resources``, ``compss_agent_reduce_resources`` and ``compss_agent_lost_resources``.

The **compss_agent_add_resources** commands interacts with the REST interface of the COMPSs agent to attach new resources to the Agent.

.. code-block:: console

    compss@bsc.es:~$ compss_agent_add_resources [options] resource_name [<adaptor_property_name=adaptor_property_value>]

By default, the command modifies the resource pool of the agent deployed on the node running the command listenning on port 46101; however, this can be modified by using the options ``--agent_node`` and ``--agent_port`` to indicate the endpoint of the COMPSs Agent. The other options passed in to the command modify the characteristics of the resources to attach; by default, it adds one single CPU core. However, it also allows to modify the amount of GPU cores, FPGAs, memory type and size and OS details. 

.. code-block:: console

    compss@bsc.es:~$ compss_agent_add_resources -h 

    Usage: compss_agent_add_resources [options] resource_name [<adaptor_property_name=adaptor_property_value>]

    * Options:
    General:
        --help, -h                              Print this help message

        --opts                                  Show available options

        --version, -v                           Print COMPSs version

        --agent_node=<string>                   Name of the node where to add the resource
                                                Default: 

        --agent_port=<string>                   Port of the node where to add the resource
                                                Default:                                             
    Resource description:
        --comm=<string>                         Canonical class name of the adaptor to interact with the resource 
                                                Default: es.bsc.compss.agent.comm.CommAgentAdaptor

        --cpu=<integer>                         Number of cpu cores available on the resource 
                                                Default: 1

        --gpu=<integer>                         Number of gpus devices available on the resource 
                                                Default: 0

        --fpga=<integer>                        Number of fpga devices available on the resource 
                                                Default: 0

        --mem_type=<string>                     Type of memory used by the resource
                                                Default: [unassigned]

        --mem_size=<string>                     Size of the memory available on the resource
                                                Default: -1

        --os_type=<string>                      Type of operating system managing the resource  
                                                Default: [unassigned]

        --os_distr=<string>                     Distribution of the operating system managing the resource  
                                                Default: [unassigned]
                                                
        --os_version=<string>                   Version of the operating system managing the resource  
                                                Default: [unassigned]

If ``resource_name`` matches the name of the Agent, the capabilities of the device are increased according to the description; otherwise, the runtime adds a remote worker to the  resource pool with the specified characteristics. Notice that, if there is another resource within the pool with the same name, the agent will increase the resources of such node instead of adding it as a new one. The ``--comm`` option is used for selecting which adaptor is used for interacting with the remote node; the default adaptor (CommAgent) interacts with the remote node through the Comm interface of the COMPSs agent.


The following command adds a new Agent onto the pool of resources of the Agent deployed at IP 192.168.1.70 with a REST Interface on port 46101. The new agent, which has 4 CPU cores, is deployed on IP 192.168.1.72 and has a Comm interface endpoint on port 46102.

.. code-block:: console

    compss@bsc.es:~$ compss_agent_add_resources --agent_node=192.168.1.70 --agent_port=46101 --cpu=4 192.168.1.72 Port=46102

Conversely, the ``compss_agent_reduce_resources`` command allows to reduce the number of resources configured in an agent. Executing the command causes the target agent to reduce the specified amount of resources from one of its configured neighbors. At the moment of the reception of the resource removal request, the agent might be actively using those remote resources by executing some tasks. If that is the case, the agent will register the resource reduction request, stop submitting more workload to the corresponding node, and, when the idle resources of the node match the request, the agent removes them from the pool. If upon the completion of the ``compss_agent_reduce_resources`` command no resources are associated to the reduced node, the node is completely removed from the resource pool of the agent. The options and default values are the same than for the ``compss_agent_add_resources`` command. Notice that ``--comm`` option is not available because only one resource can be associated to that name regardless the selected adaptor.

.. code-block:: console

    compss@bsc.es:~$ compss_agent_reduce_resources -h
    
    Usage: compss_agent_reduce_resources [options] resource_name

    * Options:
    General:
        --help, -h                              Print this help message

        --opts                                  Show available options

        --version, -v                           Print COMPSs version

        --agent_node=<string>                   Name of the node where to add the resource
                                                Default: 

        --agent_port=<string>                   Port of the node where to add the resource
                                                Default:                                             
    Resource description:
        --cpu=<integer>                         Number of cpu cores available on the resource 
                                                Default: 1

        --gpu=<integer>                         Number of gpus devices available on the resource 
                                                Default: 0

        --fpga=<integer>                        Number of fpga devices available on the resource 
                                                Default: 0

        --mem_type=<string>                     Type of memory used by the resource
                                                Default: [unassigned]

        --mem_size=<string>                     Size of the memory available on the resource
                                                Default: -1

        --os_type=<string>                      Type of operating system managing the resource  
                                                Default: [unassigned]

        --os_distr=<string>                     Distribution of the operating system managing the resource  
                                                Default: [unassigned]
                                                
        --os_version=<string>                   Version of the operating system managing the resource  
                                                Default: [unassigned]
 

Finally, the last command to control the pool of resources configured, ``compss_agent_lost_resources``, immediately removes from an agent's pool all the resources corresponding to the remote node associated to that name.

.. code-block:: console

    compss@bsc.es:~$ compss_agent_lost_resources [options] resource_name 

In this case, the only available options are those used for identifying the endpoint of the agent:``--agent_node`` and ``--agent_port``. As with the previous commands, by default, the request is submitted to the agent deployed on the IP address 127.0.0.1 and listenning on port 46101.
