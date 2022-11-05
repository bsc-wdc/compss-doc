Schedulers
===========

This section provides detailed information about all the schedulers that
are implemented in COMPSs and can be used for the executions of the applications.
Depending on the scheduler selected for your executions the tasks will be
scheduled in a way or another and this will result in different execution
times depending on the scheduler used.

COMPSs schedulers are organized in three families:

* Order strict: Policies give a priority to those tasks that become dependency free tasks. Only the dependency-free task with a higher priority can be submitted to  execution. Tasks with lower priority can not overtake the execution of  higher-priority tasks even if there are free resources that could host the execution of the former ones.

* Lookahead: As with o the order-strict family, policies give tasks a priority when they become dependency free. However, in this case, if there are not enough resources to host the execution of the highest-priority dependency-free task, another task with a lower priority can be submitted for execution overtaking the execution of the most prioritary one.

    * Successors: Within this family, an important group of schedulers give a higher priority to the tasks that become dependency-free when trying to submit an action to fill the resources released by their data predecessor.

* Full graph: Unlike the other two families that only consider dependency-free tasks, full-graph policies schedule the whole graph of the application on the currently available resources. Besides task dependencies, full-graph policies declare resources dependencies among tasks to guarantee resource constraints, and redefines them  dynamically to optimize the execution.

Schedulers provided within the COMPSs release:

.. table:: Schedulers
    :name: schedulers description


    +------------------------------------------------------------------------------------+-----------------+------------------------------------------------------------------+-------------------------------------------+
    | **Class name**                                                                     | **Family**      | **Description**                                                  | **Comments**                              |
    +====================================================================================+=================+==================================================================+===========================================+
    | es.bsc.compss.scheduler.orderstrict.fifo.FifoTS                                    | order-strict    | Prioratizes task generation order (FIFO).                        |                                           |
    +------------------------------------------------------------------------------------+-----------------+------------------------------------------------------------------+-------------------------------------------+
    | es.bsc.compss.scheduler.lookahead.fifo.FifoTS                                      | lookahead       | Prioratizes task generation order (FIFO).                        |                                           |
    +------------------------------------------------------------------------------------+-----------------+------------------------------------------------------------------+-------------------------------------------+
    | es.bsc.compss.scheduler.lookahead.lifo.LifoTS                                      | lookahead       | Prioratizes task generation order (LIFO).                        |                                           |
    +------------------------------------------------------------------------------------+-----------------+------------------------------------------------------------------+-------------------------------------------+
    | es.bsc.compss.scheduler.lookahead.locality.LocalityTS                              | lookahead       | Prioratizes data location and then (FIFO) task generation.       | Default on runcompss executions           |
    +------------------------------------------------------------------------------------+-----------------+------------------------------------------------------------------+-------------------------------------------+
    | es.bsc.compss.scheduler.lookahead.successors.locality.LocalityTS                   | lookahead       | Prioratizes the successors of the ended task, then the data      | Default for local disk executions on SCs  |
    |                                                                                    | - successors    | locality on the worker and then the generation order.            |                                           |
    +------------------------------------------------------------------------------------+-----------------+------------------------------------------------------------------+-------------------------------------------+
    | es.bsc.compss.scheduler.lookahead.mt.successors.locality.LocalityTS                | lookahead       | Prioratizes the successors of the ended task, then the data      | Multi-threaded implementation.            |
    |                                                                                    | - successors    | locality on the worker and then the generation order.            |                                           |
    +------------------------------------------------------------------------------------+-----------------+------------------------------------------------------------------+-------------------------------------------+
    | es.bsc.compss.scheduler.lookahead.successors.fifo.FifoTS                           | lookahead       | Prioratizes the successors of the ended task, and then the       |                                           |
    |                                                                                    | - successors    | generation order.                                                |                                           |
    +------------------------------------------------------------------------------------+-----------------+------------------------------------------------------------------+-------------------------------------------+
    | es.bsc.compss.scheduler.lookahead.mt.successors.fifo.FifoTS                        | lookahead       | Prioratizes the successors of the ended task, and then the       | Multi-threaded implementation.            |
    |                                                                                    | - successors    | generation order.                                                | Default for shared disk executions on SCs |
    +------------------------------------------------------------------------------------+-----------------+------------------------------------------------------------------+-------------------------------------------+
    | es.bsc.compss.scheduler.lookahead.successors.lifo.LifoTS                           | lookahead       | Prioratizes the successors of the ended task, and then the       |                                           |
    |                                                                                    | - successors    | inverse generation order.                                        |                                           |
    +------------------------------------------------------------------------------------+-----------------+------------------------------------------------------------------+-------------------------------------------+
    | es.bsc.compss.scheduler.lookahead.mt.successors.lifo.LifoTS                        | lookahead       | Prioratizes the successors of the ended task, and then the       | Multi-threaded implementation.            |
    |                                                                                    | - successors    | inverse generation order.                                        |                                           |
    +------------------------------------------------------------------------------------+-----------------+------------------------------------------------------------------+-------------------------------------------+
    | es.bsc.compss.scheduler.lookahead.successors.constraintsfifo.ConstraintsFifoTS     | lookahead       | Prioratizes the successors of the ended task, then the task      |                                           |
    |                                                                                    | - successors    | constraints (computing_units) and then generation order (FIFO).  |                                           |
    +------------------------------------------------------------------------------------+-----------------+------------------------------------------------------------------+-------------------------------------------+
    | es.bsc.compss.scheduler.lookahead.mt.successors.constraintsfifo.ConstraintsFifoTS  | lookahead       | Prioratizes the successors of the ended task, then the task      | Multi-threaded implementation             |
    |                                                                                    | - successors    | constraints (computing_units) and then generation order (FIFO).  |                                           |
    +------------------------------------------------------------------------------------+-----------------+------------------------------------------------------------------+-------------------------------------------+
    | es.bsc.compss.scheduler.fullgraph.multiobjective.MOScheduler                       | full graph      | Based on a multi-objective function (time, energy, cost).        |                                           |
    +------------------------------------------------------------------------------------+-----------------+------------------------------------------------------------------+-------------------------------------------+


Specifying the ``--scheduler=<class>`` option when launching a COMPSs execution with
``enqueue_compss`` or ``runcompss`` selects the scheduler that will drive the execution.
In the case of having an agents deployment, the option indicates the scheduler used by
that agent; agents deployment allows combining different scheduling strategies by
setting up a different policy on each agent.

With the ``--input_profile=<path>`` option, application users can pass in to COMPSs the
task profiles obtained from previous executions. Thus, the scheduler makes better
decisions from an early time of the execution. To indicate the runtime a file where to
save these profiles at the end of the execution, it is necessary that the user specifies
the ``--output_profile=<path>`` option. If both paths match, the runtime will update its
content.
