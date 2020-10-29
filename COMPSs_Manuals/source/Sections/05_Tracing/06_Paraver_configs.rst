Paraver: configurations
=======================

:numref:`paraver_configs_general`, :numref:`paraver_configs_python`
and :numref:`paraver_configs_comm` provide information about the different
pre-build configurations that are distributed with COMPSs and that can
be found under the ``/opt/COMPSs/Dependencies/`` ``paraver/cfgs/``
folder. The *cfgs* folder contains all the basic views, the *python*
folder contains the configurations for Python events, and finally the
*comm* folder contains the configurations related to communications.

.. table:: General paraver configurations for COMPSs Applications
    :name: paraver_configs_general

    +-----------------------------------+------------------------------------------------------------------------+
    | Configuration File Name           | Description                                                            |
    +===================================+========================================================================+
    | 2dp_runtime_state.cfg             | 2D plot of runtime state                                               |
    +-----------------------------------+------------------------------------------------------------------------+
    | 2dp_tasks.cfg                     | 2D plot of tasks duration                                              |
    +-----------------------------------+------------------------------------------------------------------------+
    | 3dh_duration_runtime.cfg          | 3D Histogram of runtime execution                                      |
    +-----------------------------------+------------------------------------------------------------------------+
    | 3dh_duration_tasks.cfg            | 3D Histogram of tasks duration                                         |
    +-----------------------------------+------------------------------------------------------------------------+
    | compss_cpu_constraints.cfg        | Shows tasks cpu constraints                                            |
    +-----------------------------------+------------------------------------------------------------------------+
    | compss_runtime.cfg                | Shows COMPSs Runtime events (master and workers)                       |
    +-----------------------------------+------------------------------------------------------------------------+
    | compss_runtime_master.cfg         | Shows COMPSs Runtime master events                                     |
    +-----------------------------------+------------------------------------------------------------------------+
    | compss_storage.cfg                | Shows COMPSs persistent storage events                                 |
    +-----------------------------------+------------------------------------------------------------------------+
    | compss_tasks_and_binding.cfg      | Shows COMPSs Binding events (master and workers) and tasks execution   |
    +-----------------------------------+------------------------------------------------------------------------+
    | compss_tasks_and_runtime.cfg      | Shows COMPSs Runtime events (master and workers) and tasks execution   |
    +-----------------------------------+------------------------------------------------------------------------+
    | compss_tasks.cfg                  | Shows tasks execution                                                  |
    +-----------------------------------+------------------------------------------------------------------------+
    | compss_tasks_cpu_affinity.cfg     | Shows tasks CPU affinity                                               |
    +-----------------------------------+------------------------------------------------------------------------+
    | compss_tasks_gpu_affinity.cfg     | Shows tasks GPU affinity                                               |
    +-----------------------------------+------------------------------------------------------------------------+
    | compss_tasks_id.cfg               | Shows tasks execution by task id                                       |
    +-----------------------------------+------------------------------------------------------------------------+
    | compss_waiting_tasks.cfg          | Shows waiting tasks                                                    |
    +-----------------------------------+------------------------------------------------------------------------+
    | histograms_HW_counters.cfg        | Shows hardware counters histograms                                     |
    +-----------------------------------+------------------------------------------------------------------------+
    | instantiation_time.cfg            | Shows the instantiation time                                           |
    +-----------------------------------+------------------------------------------------------------------------+
    | Interval_between_runtime.cfg      | Interval between runtime events                                        |
    +-----------------------------------+------------------------------------------------------------------------+
    | nb_executing_tasks.cfg            | Number of executing tasks                                              |
    +-----------------------------------+------------------------------------------------------------------------+
    | nb_requested_cpus.cfg             | Number of requested CPUs                                               |
    +-----------------------------------+------------------------------------------------------------------------+
    | nb_requested_disk_bw.cfg          | Number of requested disk bandwidth                                     |
    +-----------------------------------+------------------------------------------------------------------------+
    | nb_requested_gpus.cfg             | Number of requested GPUs                                               |
    +-----------------------------------+------------------------------------------------------------------------+
    | nb_executing_mem.cfg              | Number of executing memory                                             |
    +-----------------------------------+------------------------------------------------------------------------+
    | task_duration.cfg                 | Shows tasks duration                                                   |
    +-----------------------------------+------------------------------------------------------------------------+
    | thread_cpu.cfg                    | Shows the initial executing CPU                                        |
    +-----------------------------------+------------------------------------------------------------------------+
    | time_betw_tasks.cfg               | Shows the time between tasks                                           |
    +-----------------------------------+------------------------------------------------------------------------+
    | user_events.cfg                   | Shows the user events (type ``9000000``)                               |
    +-----------------------------------+------------------------------------------------------------------------+

.. table:: Available paraver configurations for Python events of COMPSs Applications
    :name: paraver_configs_python

    +--------------------------------------+---------------------------------------------------------------------------------------------------------------+
    | Configuration File Name              | Description                                                                                                   |
    +======================================+===============================================================================================================+
    | 3dh_events_inside_task.cfg           | 3D Histogram of python events                                                                                 |
    +--------------------------------------+---------------------------------------------------------------------------------------------------------------+
    | events_inside_tasks.cfg              | Events showing python information such as user function execution time, modules imports, or serializations    |
    +--------------------------------------+---------------------------------------------------------------------------------------------------------------+
    | events_in_workers.cfg                | Events showing python binding information in worker                                                           |
    +--------------------------------------+---------------------------------------------------------------------------------------------------------------+
    | nb_user_code_executing.cfg           | Number of user code executing                                                                                 |
    +--------------------------------------+---------------------------------------------------------------------------------------------------------------+
    | tasks_cpu_affinity.cfg               | Events showing the CPU affinity of the tasks (shows only the first core if multiple assigned)                 |
    +--------------------------------------+---------------------------------------------------------------------------------------------------------------+
    | tasks_gpu_affinity.cfg               | Events showing the GPU affinity of the tasks (shows only the first GPU if multiple assigned)                  |
    +--------------------------------------+---------------------------------------------------------------------------------------------------------------+
    | Time_between_events_inside_tasks.cfg | Shows the time between events inside tasks                                                                    |
    +--------------------------------------+---------------------------------------------------------------------------------------------------------------+


.. table:: Available paraver configurations for COMPSs Applications
    :name: paraver_configs_comm

    +--------------------------------------------+-----------------------------------------------------------------------------+
    | Configuration File Name                    | Description                                                                 |
    +============================================+=============================================================================+
    | communication_matrix.cfg                   | Table view of communications between each node                              |
    +--------------------------------------------+-----------------------------------------------------------------------------+
    | compss_data_transfers.cfg                  | Shows data transfers for each task’s parameter                              |
    +--------------------------------------------+-----------------------------------------------------------------------------+
    | compss_tasksID_transfers.cfg               | Task’s transfers request for each task (task with its IDs are also shown)   |
    +--------------------------------------------+-----------------------------------------------------------------------------+
    | process_bandwith.cfg                       | Send/Receive bandwith table for each node                                   |
    +--------------------------------------------+-----------------------------------------------------------------------------+
    | receive_bandwith.cfg                       | Receive bandwith view for each node                                         |
    +--------------------------------------------+-----------------------------------------------------------------------------+
    | send_bandwith.cfg                          | Send bandwith view for each node                                            |
    +--------------------------------------------+-----------------------------------------------------------------------------+
    | sr_bandwith.cfg                            | Send/Receive bandwith view for each node                                    |
    +--------------------------------------------+-----------------------------------------------------------------------------+
