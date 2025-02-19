Paraver: configurations
=======================

:numref:`paraver_configs_general`, :numref:`paraver_configs_python`
and :numref:`paraver_configs_comm` provide information about the different
pre-build configurations that are distributed with COMPSs and that can
be found under the ``/opt/COMPSs/Dependencies/`` ``paraver/cfgs/``
folder. The *cfgs* folder contains all the basic views, the *python*
folder contains the configurations for Python events, and finally the
*comm* folder contains the configurations related to communications.

Additionally, it can be shown the data transfers and the task dependencies.
To see them it is needed to show communication lines in the paraver windows,
to only see the task dependencies are needed to put in Filter > Communications
> Comm size, the size equal to 0. Some of the dependencies between tasks may be lost.

.. table:: General paraver configurations for COMPSs Applications
    :name: paraver_configs_general

    +-----------------------------------+------------------------------------------------------------------------+-------------+
    | Configuration File Name           | Description                                                            | Target      |
    +===================================+========================================================================+=============+
    | 2dp_runtime_state.cfg             | 2D plot of runtime state                                               | Runtime     |
    +-----------------------------------+------------------------------------------------------------------------+-------------+
    | 2dp_tasks.cfg                     | 2D plot of tasks duration                                              | Application |
    +-----------------------------------+------------------------------------------------------------------------+-------------+
    | 3dh_duration_runtime.cfg          | 3D Histogram of runtime execution                                      | Runtime     |
    +-----------------------------------+------------------------------------------------------------------------+-------------+
    | 3dh_duration_tasks.cfg            | 3D Histogram of tasks duration                                         | Application |
    +-----------------------------------+------------------------------------------------------------------------+-------------+
    | compss_cpu_constraints.cfg        | Shows tasks cpu constraints                                            | Runtime     |
    +-----------------------------------+------------------------------------------------------------------------+-------------+
    | compss_executors.cfg              | Shows the number of executor threads in each node                      | Runtime     |
    +-----------------------------------+------------------------------------------------------------------------+-------------+
    | compss_runtime.cfg                | Shows COMPSs Runtime events (master and workers)                       | Runtime     |
    +-----------------------------------+------------------------------------------------------------------------+-------------+
    | compss_runtime_master.cfg         | Shows COMPSs Runtime master events                                     | Runtime     |
    +-----------------------------------+------------------------------------------------------------------------+-------------+
    | compss_storage.cfg                | Shows COMPSs persistent storage events                                 | Runtime     |
    +-----------------------------------+------------------------------------------------------------------------+-------------+
    | compss_tasks_and_runtime.cfg      | Shows COMPSs Runtime events (master and workers) and tasks execution   | Application |
    +-----------------------------------+------------------------------------------------------------------------+-------------+
    | compss_tasks.cfg                  | Shows tasks execution and tasks instantiation in master nodes          | Application |
    +-----------------------------------+------------------------------------------------------------------------+-------------+
    | compss_tasks_communications.cfg   | Shows tasks and communications                                         | Application |
    +-----------------------------------+------------------------------------------------------------------------+-------------+
    | compss_tasks_cpu_affinity.cfg     | Shows tasks CPU affinity                                               | Application |
    +-----------------------------------+------------------------------------------------------------------------+-------------+
    | compss_tasks_dependencies.cfg     | Shows tasks and dependencies (only for the master node)                | Application |
    +-----------------------------------+------------------------------------------------------------------------+-------------+
    | compss_tasks_gpu_affinity.cfg     | Shows tasks GPU affinity                                               | Application |
    +-----------------------------------+------------------------------------------------------------------------+-------------+
    | compss_tasks_id.cfg               | Shows tasks execution by task id                                       | Application |
    +-----------------------------------+------------------------------------------------------------------------+-------------+
    | compss_tasks_runtime_&_agents.cfg | Shows COMPSs Agent and Runtime events and tasks execution              | Application |
    +-----------------------------------+------------------------------------------------------------------------+-------------+
    | compss_waiting_tasks.cfg          | Shows waiting tasks                                                    | Runtime     |
    +-----------------------------------+------------------------------------------------------------------------+-------------+
    | histograms_HW_counters.cfg        | Shows hardware counters histograms                                     | Both        |
    +-----------------------------------+------------------------------------------------------------------------+-------------+
    | instantiation_time.cfg            | Shows the instantiation time                                           | Runtime     |
    +-----------------------------------+------------------------------------------------------------------------+-------------+
    | Interval_between_runtime.cfg      | Interval between runtime events                                        | Runtime     |
    +-----------------------------------+------------------------------------------------------------------------+-------------+
    | nb_executing_tasks.cfg            | Number of executing tasks                                              | Application |
    +-----------------------------------+------------------------------------------------------------------------+-------------+
    | nb_requested_cpus.cfg             | Number of requested CPUs                                               | Runtime     |
    +-----------------------------------+------------------------------------------------------------------------+-------------+
    | nb_requested_disk_bw.cfg          | Number of requested disk bandwidth                                     | Runtime     |
    +-----------------------------------+------------------------------------------------------------------------+-------------+
    | nb_requested_gpus.cfg             | Number of requested GPUs                                               | Runtime     |
    +-----------------------------------+------------------------------------------------------------------------+-------------+
    | nb_executing_mem.cfg              | Number of executing memory                                             | Runtime     |
    +-----------------------------------+------------------------------------------------------------------------+-------------+
    | number_executors.cfg              | Number of executors                                                    | Runtime     |
    +-----------------------------------+------------------------------------------------------------------------+-------------+
    | task_duration.cfg                 | Shows tasks duration                                                   | Application |
    +-----------------------------------+------------------------------------------------------------------------+-------------+
    | thread_cpu.cfg                    | Shows the initial executing CPU                                        | Runtime     |
    +-----------------------------------+------------------------------------------------------------------------+-------------+
    | thread_identifiers.cfg            | Shows the type of each thread                                          | Runtime     |
    +-----------------------------------+------------------------------------------------------------------------+-------------+
    | time_btw_tasks.cfg                | Shows the time between tasks                                           | Runtime     |
    +-----------------------------------+------------------------------------------------------------------------+-------------+
    | user_events.cfg                   | Shows the user events (type ``9100000``)                               | Application |
    +-----------------------------------+------------------------------------------------------------------------+-------------+

.. table:: Available paraver configurations for Python events of COMPSs Applications
    :name: paraver_configs_python

    +-----------------------------------------+---------------------------------------------------------------------------------------------------------------+----------------+
    | Configuration File Name                 | Description                                                                                                   | Target         |
    +=========================================+===============================================================================================================+================+
    | 3dh_duration_runtime_master_binding.cfg | 3D Histogram of runtime events of python in master node                                                       | Python Binding |
    +-----------------------------------------+---------------------------------------------------------------------------------------------------------------+----------------+
    | 3dh_events_inside_task.cfg              | 3D Histogram of python events                                                                                 | Python Binding |
    +-----------------------------------------+---------------------------------------------------------------------------------------------------------------+----------------+
    | 3dh_tasks_phase.cfg                     | 3D Histogram of execution functions                                                                           | Python Binding |
    +-----------------------------------------+---------------------------------------------------------------------------------------------------------------+----------------+
    | compss_runtime_master_binding.cfg       | Shows runtime events of python in master node                                                                 | Python Binding |
    +-----------------------------------------+---------------------------------------------------------------------------------------------------------------+----------------+
    | deserialization_object_number.cfg       | Shows the numbers of the objects that are being deserialized                                                  | Python Binding |
    +-----------------------------------------+---------------------------------------------------------------------------------------------------------------+----------------+
    | deserialization_size.cfg                | Shows the size of the objects that are being deserialized (Bytes)                                             | Python Binding |
    +-----------------------------------------+---------------------------------------------------------------------------------------------------------------+----------------+
    | events_inside_tasks.cfg                 | Events showing python information such as user function execution time, modules imports, or serializations    | Python Binding |
    +-----------------------------------------+---------------------------------------------------------------------------------------------------------------+----------------+
    | events_in_workers.cfg                   | Events showing python binding information in worker                                                           | Python Binding |
    +-----------------------------------------+---------------------------------------------------------------------------------------------------------------+----------------+
    | nb_user_code_executing.cfg              | Number of user code executing                                                                                 | Python Binding |
    +-----------------------------------------+---------------------------------------------------------------------------------------------------------------+----------------+
    | serdes_bw.cfg                           | Serialization and deserialization bandwidth (MB/s)                                                            | Python Binding |
    +-----------------------------------------+---------------------------------------------------------------------------------------------------------------+----------------+
    | serdes_cache_bw.cfg                     | Serialization and deserialization to cache bandwidth (MB/s)                                                   | Python Binding |
    +-----------------------------------------+---------------------------------------------------------------------------------------------------------------+----------------+
    | serialization_object_number.cfg         | Shows the numbers of the objects that are being serialized                                                    | Python Binding |
    +-----------------------------------------+---------------------------------------------------------------------------------------------------------------+----------------+
    | serialization_size.cfg                  | Shows the size of the objects that are being serialized (Bytes)                                               | Python Binding |
    +-----------------------------------------+---------------------------------------------------------------------------------------------------------------+----------------+
    | tasks_cpu_affinity.cfg                  | Events showing the CPU affinity of the tasks (shows only the first core if multiple assigned)                 | Python Binding |
    +-----------------------------------------+---------------------------------------------------------------------------------------------------------------+----------------+
    | tasks_gpu_affinity.cfg                  | Events showing the GPU affinity of the tasks (shows only the first GPU if multiple assigned)                  | Python Binding |
    +-----------------------------------------+---------------------------------------------------------------------------------------------------------------+----------------+
    | Time_between_events_inside_tasks.cfg    | Shows the time between events inside tasks                                                                    | Python Binding |
    +-----------------------------------------+---------------------------------------------------------------------------------------------------------------+----------------+


.. table:: Available paraver configurations for COMPSs Applications
    :name: paraver_configs_comm

    +--------------------------------------------+-----------------------------------------------------------------------------+------------------------+
    | Configuration File Name                    | Description                                                                 | Target                 |
    +============================================+=============================================================================+========================+
    | communication_matrix.cfg                   | Table view of communications between each node                              | Runtime Communications |
    +--------------------------------------------+-----------------------------------------------------------------------------+------------------------+
    | compss_data_transfers.cfg                  | Shows data transfers for each task’s parameter                              | Runtime Communications |
    +--------------------------------------------+-----------------------------------------------------------------------------+------------------------+
    | compss_tasksID_transfers.cfg               | Task’s transfers request for each task (task with its IDs are also shown)   | Runtime Communications |
    +--------------------------------------------+-----------------------------------------------------------------------------+------------------------+
    | process_bandwidth.cfg                      | Send/Receive bandwidth table for each node                                  | Runtime Communications |
    +--------------------------------------------+-----------------------------------------------------------------------------+------------------------+
    | receive_bandwidth.cfg                      | Receive bandwidth view for each node                                        | Runtime Communications |
    +--------------------------------------------+-----------------------------------------------------------------------------+------------------------+
    | send_bandwidth.cfg                         | Send bandwidth view for each node                                           | Runtime Communications |
    +--------------------------------------------+-----------------------------------------------------------------------------+------------------------+
    | sr_bandwidth.cfg                           | Send/Receive bandwidth view for each node                                   | Runtime Communications |
    +--------------------------------------------+-----------------------------------------------------------------------------+------------------------+
