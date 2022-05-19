Multinode decorator
^^^^^^^^^^^^^^^^^^^

The *@multinode* (or @Multinode) decorator shall be used to define that a task
is going to use multiple nodes (e.g. using internal parallelism) (:numref:`multinode_task_python`).

.. code-block:: python
    :name: multinode_task_python
    :caption: Multinode task example

    from pycompss.api.multinode import multinode

    @multinode(computing_nodes="2")
    @task()
    def multinode_func():
         pass

The only supported parameter is *computing_nodes*, used to define the
number of nodes required by the task (the default value is 1). The
mechanism to get the number of nodes, threads and their names to the
task is through the *COMPSS_NUM_NODES*, *COMPSS_NUM_THREADS* and
*COMPSS_HOSTNAMES* environment variables respectively, which are
exported within the task scope by the COMPSs runtime before the task
execution.
