MPMD MPI decorator
^^^^^^^^^^^^^^^^^^

The *@mpmd_mpi* decorator can be used to define Multiple Program Multiple Data (MPMD) MPI tasks as shown in the following example
(:numref:`mpmd_mpi_task`):

.. code-block:: python
    :name: mpmd_mpi_task
    :caption: MPMD MPI task example

    from pycompss.api.mpmd_mpi import mpmd_mpi

    @mpmd_mpi(runner="mpirun",
              programs=[
                   dict(binary="hostname", processes=2),
                   dict(binary="date", processes=2)
              ])
    @task()
    def basic():
        pass


The definition implies that MPMD MPI command will be run by 'mpirun', and will execute 2 processes for 'hostname', and 2 processes to show the '
date'. It's not mandatory to specify total number of programs as long as they are added inside ``programs`` list of dictionaries argument.

Each of the MPMD MPI programs must at least have ``binary``, but also can have ``processes`` and ``args`` string (:numref:`mpmd_mpi_task_args`):

.. code-block:: python
    :name: mpmd_mpi_task_args
    :caption: MPMD MPI task example

    from pycompss.api.mpmd_mpi import mpmd_mpi

    @mpmd_mpi(runner="mpirun",
              programs=[
                   dict(binary="date", processes=2, args="-d {{first}}"),
                   dict(binary="date", processes=4, args="-d {{second}}")
              ])
    @task()
    def task_args(first, second):
        pass

    def print_monday_friday(self):
        task_args("next monday", "next friday")
        compss_barrier()


When executed, this MPMD MPI program would invoke 2 MPI processes to print the date of next Monday, and 4 processes for next Friday. "args" string
replaces every parameter that is 'called' between double curly braces with their real value. This allows using multiple ``FILE_IN`` parameters for multiple MPI programs.
Moreover, output of the full MPMD MPI programs can be forwarded to an ``FILE_OUT_STDOUT`` param:


.. code-block:: python
    :name: mpmd_mpi_task_file_args
    :caption: MPMD MPI task example

    from pycompss.api.mpmd_mpi import mpmd_mpi

    @mpmd_mpi(runner="mpirun",
              programs=[
                   dict(binary="grep", args="{{keyword}} {{in_file_1}}"),
                   dict(binary="grep", args="{{keyword}} {{in_file_2}}"),
              ])
    @task(in_file=FILE_IN, result={Type: FILE_OUT_STDOUT})
    def std_out(keyword, in_file_1, in_file_2, result):
        pass

Other parameters of *@mpmd_mpi* decorator such as ``working_dir``, ``fail_by_exit_value``, ``processes_per_node``, have the same behaviors as in *@mpi*.
