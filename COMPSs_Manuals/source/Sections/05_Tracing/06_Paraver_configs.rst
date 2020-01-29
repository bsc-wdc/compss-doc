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
    :widths: auto

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
    | compss_runtime.cfg                | Shows COMPSs Runtime events (master and workers)                       |
    +-----------------------------------+------------------------------------------------------------------------+
    | compss_tasks_and_runtime.cfg      | Shows COMPSs Runtime events (master and workers) and tasks execution   |
    +-----------------------------------+------------------------------------------------------------------------+
    | compss_tasks.cfg                  | Shows tasks execution                                                  |
    +-----------------------------------+------------------------------------------------------------------------+
    | compss_tasks_numbers.cfg          | Shows tasks execution by task id                                       |
    +-----------------------------------+------------------------------------------------------------------------+
    | Interval_between_runtime.cfg      | Interval between runtime events                                        |
    +-----------------------------------+------------------------------------------------------------------------+
    | thread_cpu.cfg                    | Shows the initial executing CPU.                                       |
    +-----------------------------------+------------------------------------------------------------------------+

.. table:: Available paraver configurations for Python events of COMPSs Applications
    :name: paraver_configs_python
    :widths: auto

    +-----------------------------------+---------------------------------------------------------------------------------------------------------------+
    | Configuration File Name           | Description                                                                                                   |
    +===================================+===============================================================================================================+
    | 3dh_events_inside_task.cfg        | 3D Histogram of python events                                                                                 |
    +-----------------------------------+---------------------------------------------------------------------------------------------------------------+
    | 3dh_events_inside_tasks.cfg       | Events showing python information such as user function execution time, modules imports, or serializations.   |
    +-----------------------------------+---------------------------------------------------------------------------------------------------------------+

.. table:: Available paraver configurations for COMPSs Applications
    :name: paraver_configs_comm
    :widths: auto

    +--------------------------------------------+-----------------------------------------------------------------------------+
    | Configuration File Name                    | Description                                                                 |
    +============================================+=============================================================================+
    | sr_bandwith.cfg                            | Send/Receive bandwith view for each node                                    |
    +--------------------------------------------+-----------------------------------------------------------------------------+
    | send_bandwith.cfg                          | Send bandwith view for each node                                            |
    +--------------------------------------------+-----------------------------------------------------------------------------+
    | receive_bandwith.cfg                       | Receive bandwith view for each node                                         |
    +--------------------------------------------+-----------------------------------------------------------------------------+
    | process_bandwith.cfg                       | Send/Receive bandwith table for each node                                   |
    +--------------------------------------------+-----------------------------------------------------------------------------+
    | compss_tasks_scheduling_transfers.cfg      | Task’s transfers requests for scheduling (gradient of tasks ID)             |
    +--------------------------------------------+-----------------------------------------------------------------------------+
    | compss_tasksID_transfers.cfg               | Task’s transfers request for each task (task with its IDs are also shown)   |
    +--------------------------------------------+-----------------------------------------------------------------------------+
    | compss_data_transfers.cfg                  | Shows data transfers for each task’s parameter                              |
    +--------------------------------------------+-----------------------------------------------------------------------------+
    | communication_matrix.cfg                   | Table view of communications between each node                              |
    +--------------------------------------------+-----------------------------------------------------------------------------+
