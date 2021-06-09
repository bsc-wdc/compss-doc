Schedulers
===========

This section provides a detailed information about all the schedulers that 
are implemented in COMPSs and can be used for the executions of the applications.
Depending on the scheduler selected for your executions the tasks will be
scheduled in a way or another and this will result in different execution 
times depending on the schduler used


.. table:: Schedulers
    :name: schedulers description

    +----------------------------------+---------------------------------------------------------------------+------------------+----------------------------+
    | **Scheduler name**               | **Class name**                                                      | **Description**  | **Recommendations**        |
    +==================================+=====================================================================+==================+============================+
    | LoadBalancingScheduler (default) | es.bsc.compss.scheduler.loadbalancing.LoadBalancingScheduler        |                  | SCS when using shared disk |
    +----------------------------------+---------------------------------------------------------------------+------------------+----------------------------+
    | FIFODataLoctionScheduler         | es.bsc.compss.scheduler.fifodatalocation.FIFODataLocationScheduler  |                  | SCS when using local disk  |
    +----------------------------------+---------------------------------------------------------------------+------------------+----------------------------+
    | FIFOScheduler                    | es.bsc.compss.scheduler.fifonew.FIFOScheduler                       |                  |                            |
    +----------------------------------+---------------------------------------------------------------------+------------------+----------------------------+
    | FIFODataScheduler                | es.bsc.compss.scheduler.fifodatanew.FIFODataScheduler               |                  |                            |
    +----------------------------------+---------------------------------------------------------------------+------------------+----------------------------+
    | LIFOScheduler                    | es.bsc.compss.scheduler.lifonew.LIFOScheduler                       |                  |                            |
    +----------------------------------+---------------------------------------------------------------------+------------------+----------------------------+
    | TaskScheduler                    | es.bsc.compss.components.impl.TaskScheduler                         |                  |                            |
    +----------------------------------+---------------------------------------------------------------------+------------------+----------------------------+
