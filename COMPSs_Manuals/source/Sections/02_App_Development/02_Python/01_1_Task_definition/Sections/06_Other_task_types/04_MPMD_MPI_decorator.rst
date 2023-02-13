MPMD MPI decorator
^^^^^^^^^^^^^^^^^^

The *@mpmd_mpi* decorator can be used to define Multiple Program Multiple Data (MPMD) MPI tasks as shown in the following example
(:numref:`mpmd_mpi_task`):

.. code-block:: python
    :name: mpmd_mpi_task
    :caption: MPMD MPI task example

    from pycompss.api.mpmd_mpi import mpmd_mpi
    from pycompss.api.parameter import *
    from pycompss.api.task import task


    @mpmd_mpi(runner="mpirun",
              programs=[
                   dict(binary="my_binary.bin", processes=2),
                   dict(binary="example.bin", processes=1)
              ])
    @task()
    def example():
        pass



The definition implies that MPMD MPI command will be run by 'mpirun', and will execute 2 processes for 'my_binary.bin', and a single process for the
'example.bin' . It's not mandatory to specify total number of programs as long as they are added inside ``programs`` list of dictionaries argument.

Each of the MPMD MPI programs must at least have ``binary``, but also can have ``processes`` and ``args`` string (:numref:`mpmd_mpi_task_args`). In the following
code snippet, parameters "first" and "second" are passed to "my_program" execution as input:

.. code-block:: python
    :name: mpmd_mpi_task_args
    :caption: MPMD MPI task example

    from pycompss.api.mpmd_mpi import mpmd_mpi
    from pycompss.api.parameter import *
    from pycompss.api.task import task

    @mpmd_mpi(runner="mpirun",
              programs=[
                   dict(binary="my_program", processes=2, args="-d {{first}}"),
                   dict(binary="my_program", processes=4, args="-d {{second}}")
              ])
    @task()
    def example(first, second):
        pass

    def main(self):
        task_args("next monday", "next friday")
        compss_barrier()


In general "args" string replaces every parameter that is 'called' between double curly braces with their real value.
This also allows using multiple ``FILE_IN`` parameters for multiple MPI programs. Moreover, output of the full MPMD MPI programs can be forwarded to
an ``FILE_OUT_STDOUT`` param:


.. code-block:: python
    :name: mpmd_mpi_task_file_args
    :caption: MPMD MPI task example

    from pycompss.api.mpmd_mpi import mpmd_mpi
    from pycompss.api.task import task
    from pycompss.api.parameter import *

    @mpmd_mpi(runner="mpirun",
              programs=[
                   dict(binary="grep", args="{{keyword}} -i {{in_file_1}}"),
                   dict(binary="grep", args="{{keyword}} -i {{in_file_2}}"),
              ])
    @task(in_file=FILE_IN, result={Type: FILE_OUT_STDOUT})
    def grep_multiple(keyword, in_file_1, in_file_2, result):
        pass

    def main():
        kw = "error"
        file_1 = "/logs/1.txt"
        file_2 = "/logs/2.txt"
        grep_multiple(kw, file_1, file_2, "errors.txt")

Other parameters of *@mpmd_mpi* decorator such as ``working_dir``, ``fail_by_exit_value``, ``processes_per_node``, have the same behaviors as in *@mpi*.
