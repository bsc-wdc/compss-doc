Schedulers
===========

This section provides detailed information about all the schedulers that
are implemented in COMPSs and can be used for the executions of the applications.
Depending on the scheduler selected for your executions the tasks will be
scheduled in a way or another and this will result in different execution
times depending on the scheduler used.


.. table:: Schedulers
    :name: schedulers description

    +-----------------------------------+------------------------------------------------------------------------------------+------------+-------------------------------------------------------------------------------------------+----------------------------+
    | **Scheduler name**                | **Class name**                                                                     | **Type**   | **Description**                                                                           | **Comments**               |
    +===================================+====================================================================================+============+===========================================================================================+============================+
    | LoadBalancingScheduler            | es.bsc.compss.scheduler.loadbalancing.LoadBalancingScheduler                       | Ready      | Prioratizes data location and then (FIFO) task generation.                                | Default no supercomputer   |
    +-----------------------------------+------------------------------------------------------------------------------------+------------+-------------------------------------------------------------------------------------------+----------------------------+
    | FIFODataLocationScheduler         | es.bsc.compss.scheduler.fifodatalocation.FIFODataLocationScheduler                 | Ready      | Prioratizes data dependencies then data location and finally the task generation order.   | Default when using local   |
    |                                   |                                                                                    |            |                                                                                           | disk in supercomputer      |
    +-----------------------------------+------------------------------------------------------------------------------------+------------+-------------------------------------------------------------------------------------------+----------------------------+
    | FIFODataScheduler                 | es.bsc.compss.scheduler.fifodatanew.FIFODataScheduler                              | Ready      | Prioritizes data dependencies and then the task generation order.                         | Default when using shared  |
    |                                   |                                                                                    |            |                                                                                           | disk in supercomputer      |
    +-----------------------------------+------------------------------------------------------------------------------------+------------+-------------------------------------------------------------------------------------------+----------------------------+
    | DependencyConstraintFIFOScheduler | es.bsc.compss.scheduler.dependencyconstraintfifo.DependencyConstraintFIFOScheduler | Ready      | Prioratizes data dependencies then task constraints (computing_units) and finally the     |                            |
    | (Experimental)                    |                                                                                    |            | task generation order.                                                                    |                            |
    +-----------------------------------+------------------------------------------------------------------------------------+------------+-------------------------------------------------------------------------------------------+----------------------------+
    | FIFOScheduler                     | es.bsc.compss.scheduler.fifonew.FIFOScheduler                                      | Ready      | Prioritzies the FIFO order of the tasks arriving to the ready queue. It is the generation |                            |
    |                                   |                                                                                    |            | order for task without dependencies, or the order of how dependencies are released.       |                            |
    +-----------------------------------+------------------------------------------------------------------------------------+------------+-------------------------------------------------------------------------------------------+----------------------------+
    | LIFOScheduler                     | es.bsc.compss.scheduler.lifonew.LIFOScheduler                                      | Ready      | Prioritzies the LIFO order of the tasks arriving to the ready queue.                      |                            |
    +-----------------------------------+------------------------------------------------------------------------------------+------------+-------------------------------------------------------------------------------------------+----------------------------+
    | MOScheduler (Experimental)        | es.bsc.compss.scheduler.multiobjective                                             | Full graph | Schedules all tasks based on a multiobjective function (time, energy and cost estimation) |                            |
    +-----------------------------------+------------------------------------------------------------------------------------+------------+-------------------------------------------------------------------------------------------+----------------------------+
