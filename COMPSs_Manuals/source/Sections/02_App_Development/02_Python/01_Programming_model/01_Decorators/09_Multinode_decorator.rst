@multinode
==========

The *@multinode* (or @Multinode) decorator shall be used to define that a task
is going to use multiple nodes (e.g. using internal parallelism) (:numref:`multinode_task_python`).

Definition
----------

.. code-block:: python
    :name: multinode_task_python
    :caption: Multinode task example

    from pycompss.api.multinode import multinode

    @multinode(computing_nodes="2")
    @task()
    def multinode_func():
         pass

The multinode annotation is prepared to receive different parameters.
The most important one is *computing_nodes*, used to define the number of
nodes required by the task, 1 is the default value. Then, one can specify
the number of processes per node by using the parameter *processes_per_node*,
by default. By default, this number is equal to the number of cores of the nodes
where the multinode task is running. In the following block of code it can be seen
how to specify a number for the *processes_per_node* parameter.

.. code-block:: python
    :name: multinode_task_python_2
    :caption: Multinode task example

    from pycompss.api.multinode import multinode
    from pycompss.api.constraint import constraint

    @multinode(computing_nodes="2", processes_per_node="8")
    @task()
    def multinode_func():
         pass

When the number of *processes_per_node* specified is smaller than the number
of cores in the node the processes can use more than one core. This can be
specified by using the constraint annotation with the *computing_units*
parameter. The number of *computing_units* will be the number of cores that each
process can use. In the next block of code we can see an example of using both
decorators with the parameters. With the values specified in the example, the task
will be executed in two nodes, in each node it can run up to 8 processes, and each
process will get assigned two cores. This example, (:numref:`multinode_task_python_3`),
can exploit internal parallelism at process and even at thread level.

.. code-block:: python
    :name: multinode_task_python_3
    :caption: Multinode task example

    from pycompss.api.multinode import multinode
    from pycompss.api.constraint import constraint

    @constraint(computing_units="2")
    @multinode(computing_nodes="2", processes_per_node="8")
    @task()
    def multinode_func():
         pass

The *@multinode* (or @Multinode) decorator is compatible with all the parameters of
the task decorator. This means that it can receive all the regular parameters that
a regular COMPSs task can receive. In the following block of code,  (:numref:`multinode_task_python_4`),
we show a more practical example of usage of multinode tasks running a MPI binary:

.. code-block:: python
    :name: multinode_task_python_4
    :caption: Multinode task example

    from pycompss.api.multinode import multinode
    from pycompss.api.constraint import constraint

    @constraint(computing_units="${ComputingUnitsMN}")
    @multinode(computing_nodes="${Num_Nodes}", processes_per_node="${PPN}")
    @task(binary_mpi=FILE_IN, returns=1)
    def multinode_func(binary_mpi):
         command = ["srun " + str(binary_mpi)]
         process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
         stdout, stderr = process.communicate()
         return stdout.decode()
