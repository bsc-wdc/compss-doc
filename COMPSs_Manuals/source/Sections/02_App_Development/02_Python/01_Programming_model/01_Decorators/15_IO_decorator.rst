@IO
===

The ``@IO`` decorator is used to declare a task as an I/O task.
I/O tasks exclusively perform I/O (i.e., reading or writing) and should not perform any computations.

Definition
----------

.. code-block:: python
    :name: io_task_python
    :caption: I/O task example

    from pycompss.api.IO import IO

    @IO()
    @task()
    def io_func(text):
        fh = open("dump_file", "w")
        fh.write(text)
        fh.close()

The execution of I/O tasks can overlap with the execution of non-IO tasks (i.e., tasks that do not use the ``@IO`` decorator) if
there are no dependencies between them.
In addition to that, the scheduling of I/O tasks does not depend on the availability of computing units.
For instance, an I/O task can be still scheduled and executed on a certain node even if all the CPUs on
that node are busy executing non-I/O tasks. Hence, increasing parallelism level.

The ``@IO`` decorator can be also used on top of the ``@mpi`` decorator
(:ref:`Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/06_MPI_decorator:@mpi`)
to declare a task that performs parallel I/O.
Example :numref:`mpi_io_for_python` shows a MPI-IO task that does collective I/O with a NumPy array.

.. code-block:: python
    :name: mpi_io_for_python
    :caption: Python MPI-IO task example.

    from pycompss.api.IO import IO
    from pycompss.api.mpi import mpi

    @IO()
    @mpi(processes=4)
    @task()
    def mpi_io_func(text_chunks):
       from mpi4py import MPI
       import numpy as np

       fmode = MPI.MODE_WRONLY|MPI.MODE_CREATE
       fh = MPI.File.Open(MPI.COMM_WORLD, "dump_file", fmode)

       buffer = np.empty(20, dtype=np.int)
       buffer[:] = MPI.COMM_WORLD.Get_rank()

       offset = MPI.COMM_WORLD.Get_rank() * buffer.nbytes
       fh.Write_at_all(offset, buffer)

       fh.Close()
