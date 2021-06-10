Schedulers
===========

This section provides detailed information about all the schedulers that 
are implemented in COMPSs and can be used for the executions of the applications.
Depending on the scheduler selected for your executions the tasks will be
scheduled in a way or another and this will result in different execution 
times depending on the scheduler used.


.. table:: Schedulers
    :name: schedulers description

    +----------------------------------+---------------------------------------------------------------------+------------+-------------------------------------------------------------------------------------------+----------------------------+
    | **Scheduler name**               | **Class name**                                                      | **Type**   | **Description**                                                                           | **Recommendations**        |  
    +==================================+=====================================================================+============+===========================================================================================+============================+
    | LoadBalancingScheduler (default) | es.bsc.compss.scheduler.loadbalancing.LoadBalancingScheduler        | Ready      | Prioratizes data location and then (FIFO) task generation                                 |                            |
    +----------------------------------+---------------------------------------------------------------------+------------+-------------------------------------------------------------------------------------------+----------------------------+
    | FIFODataLocationScheduler        | es.bsc.compss.scheduler.fifodatalocation.FIFODataLocationScheduler  | Ready      | Prioratizes data dependencies then data location and then the (FIFO) task generation      | SCS when using local disk  |
    +----------------------------------+---------------------------------------------------------------------+------------+-------------------------------------------------------------------------------------------+----------------------------+
    | FIFOScheduler                    | es.bsc.compss.scheduler.fifonew.FIFOScheduler                       | Ready      | Prioritzies the (FIFO) generation order of the tasks                                      |                            |
    +----------------------------------+---------------------------------------------------------------------+------------+-------------------------------------------------------------------------------------------+----------------------------+
    | FIFODataScheduler                | es.bsc.compss.scheduler.fifodatanew.FIFODataScheduler               | Ready      | Prioritizes data dependencies and then the (FIFO) task generation                         | SCS when using shared disk |
    +----------------------------------+---------------------------------------------------------------------+------------+-------------------------------------------------------------------------------------------+----------------------------+
    | LIFOScheduler                    | es.bsc.compss.scheduler.lifonew.LIFOScheduler                       | Ready      | Prioritzies the (LIFO) generation order of the tasks                                      |                            |
    +----------------------------------+---------------------------------------------------------------------+------------+-------------------------------------------------------------------------------------------+----------------------------+
    | MOScheduler (Experimental)       | es.bsc.compss.scheduler.multiobjective                              | Full graph | Schedules all tasks based on a multiobjective function (time, energy and cost estimation) |                            |                            
    +----------------------------------+---------------------------------------------------------------------+------------+-------------------------------------------------------------------------------------------+----------------------------+
