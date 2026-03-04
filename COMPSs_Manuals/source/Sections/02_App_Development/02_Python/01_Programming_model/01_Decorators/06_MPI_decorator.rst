@mpi
====

The *@mpi* (or @Mpi) decorator shall be used to define that a task is
going to invoke a MPI executable (:numref:`mpi_task_python`).

Definition
----------

.. code-block:: python
    :name: mpi_task_python
    :caption: MPI task example

    from pycompss.api.mpi import mpi

    @mpi(binary="mpiApp.bin", runner="mpirun", processes=2)
    @task()
    def mpi_func():
         pass

The MPI executable invocation can also be enriched with parameters,
files and prefixes as with the *@binary* decorator through the
function parameters and *@task* decorator information. Please,
check :ref:`Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/04_Binary_decorator:@binary` for more details.

The *@mpi* decorator can be also used to execute a MPI for python (mpi4py) code.
To indicate it, developers only need to remove the binary field and include
the Python MPI task implementation inside the function body as shown in the
following example (:numref:`mpi_for_python`).

.. code-block:: python
    :name: mpi_for_python
    :caption: Python MPI task example.

    from pycompss.api.mpi import mpi

    @mpi(processes=4)
    @task()
    def layout_test_with_all():
       from mpi4py import MPI
       rank = MPI.COMM_WORLD.rank
       return rank

In both cases, users can also define, MPI + OpenMP tasks by using ``processes``
property to indicate the number of MPI processes and ``computing_units`` in the
Task Constraints to indicate the number of OpenMP threads per MPI process.

Users can also limit the distribution of the MPI processes through the nodes by
using the ``processes_per_node`` property. In the following example
(:numref:`processes_per_node_example`) the four MPI processes defined in the task
will be divided in two groups of two processes. And all the processes of each
group will be allocated to the same node. It will ensure that
the defined MPI task will use up to two nodes.

.. code-block:: python
    :name: processes_per_node_example
    :caption: MPI task example grouping MPI processes

    from pycompss.api.mpi import mpi

    @mpi(processes=4, processes_per_node=2)
    @task()
    def layout_test_with_all():
       from mpi4py import MPI
       rank = MPI.COMM_WORLD.rank
       return rank


The *@mpi* decorator can be combined with collections to allow the process of
a list of parameters in the same MPI execution. By the default, all parameters
of the list will be deserialized to all the MPI processes. However, a common
pattern in MPI is that each MPI processes performs the computation in a subset
of data. So, all data serialization is not needed. To indicate the subset used
by each MPI process, developers can use the ``data_layout`` notation inside the
MPI task declaration.

.. code-block:: python
    :name: mpi_data_layout_python
    :caption: MPI task example with collections and data layout

    from pycompss.api.mpi import mpi

    @mpi(processes=4, col_layout={block_count: 4, block_length: 2, stride: 1})
    @task(col=COLLECTION_IN, returns=4)
    def layout_test_with_all(col):
       from mpi4py import MPI
       rank = MPI.COMM_WORLD.rank
       return data[0]+data[1]+rank

Figure (:numref:`mpi_data_layout_python`) shows an example about how to combine
MPI tasks with collections and data layouts. In this example, we have define a
MPI task with an input collection (``col``). We have also defined a data layout
with the property ``<arg_name>_layout`` and we specify the number of blocks
(``block_count``), the elements per block (``block_length``), and the number of
element between the starting block points (``stride``).

Users can specify the MPI runner command with the ``runner`` how ever the
arguments passed to the ``mpirun`` command differs depending on the implementation.
To ensure that the correct arguments are passed to the runner, users can define the
``COMPSS_MPIRUN_TYPE`` environment variable. The current supported values are
``impi`` for Intel MPI and `ompi` for OpenMPI. Other MPI implementation can be
supported by adding its corresponding properties file in the folder
``$COMPSS_HOME/Runtime/configuration/mpi``.


Summary
-------

Next table summarizes the parameters of this decorator. Please note that ``working_dir`` and ``args`` are the only decorator properties that can contain task parameters
defined in curly braces.

+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Parameter              | Description                                                                                                                             |
+========================+=========================================================================================================================================+
| **binary**             | String defining the full path of the binary that must be executed. Empty indicates python MPI code.                                     |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| **working_dir**        | Full path of the binary working directory inside the COMPSs Worker.                                                                     |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| **runner**             | (Mandatory) String defining the MPI runner command.                                                                                     |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| **processes**          | Integer defining the number of MPI processes spawned by the task. (Default 1)                                                           |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| **processes_per_node** | Integer defining the number of co-allocated MPI processes per node. The ``processes`` value should be multiple of this value            |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| **args**               | Args string to be added to end of the execution command of the binary. It can contain python task parameters defined in curly braces.   |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+

