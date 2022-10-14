Julia decorator
^^^^^^^^^^^^^^^

The `@julia` (or `@Julia`) decorator shall be used to define that a task is
going to invoke a `Julia <https://julialang.org/>`_ executable, which can be
parallelized with `Julia Parallel ClusterManagers <https://github.com/JuliaParallel/ClusterManagers.jl>`_
described in the `Julia documentation <https://docs.julialang.org/en/v1/manual/distributed-computing/>`_.

In this context, the `@task` decorator parameters will be used
as the julia invocation parameters (following their order in the
function definition). Since the invocation parameters can be of
different nature, information on their type can be provided through the
*@task* decorator.

:numref:`julia_task_python` shows the most simple julia task definition
without constraints and without parameters.

.. code-block:: python
    :name: julia_task_python
    :caption: Julia task example

    from pycompss.api.task import task
    from pycompss.api.julia import julia

    @julia(script="my_julia_app.jl")
    @task()
    def julia_func():
         pass


.. code-block:: julia
    :name: julia_app_hello_world
    :caption: my_julia_app.jl code

    println("Hello world")


The invocation of the `julia_func` task would be equivalent to:

.. code-block:: console

    $ julia my_julia_app.jl
    Hello world


The ``@julia`` decorator supports the ``working_dir`` parameter to define
the working directory for the execution of the defined julia script.

:numref:`complex_julia_task_python` shows a more complex julia invocation,
with parameters (`x` and `y`) and a file (that captures the standard output
stream during the `mandelbrot.jl` execution) as parameters:

.. code-block:: python
    :name: complex_julia_task_python
    :caption: Julia task example using `mandelbrot.jl` application (`julia_decorator_test.py`)

    from pycompss.api.task import task
    from pycompss.api.julia import julia
    from pycompss.api.parameter import *

    @julia(script="mandelbrot.jl", working_dir=".")
    @task(result={Type:FILE_OUT_STDOUT})
    def julia_mandelbrot(x, y, result):
         pass

    # This task definition is equivalent to the following, which is more verbose:
    #
    # @julia(script="mandelbrot.jl", working_dir=".")
    # @task(result={Type:FILE_OUT, StdIOStream:STDOUT})
    # def julia_mandelbrot(x, y, result):
    #     pass

    if __name__=='__main__':
        outfile = "fractal.txt"
        julia_mandelbrot(-0.05, 0.0315, outfile)


.. code-block:: julia
    :name: julia_mandelbrot_code
    :caption: Julia Mandelbrot implementation (mandelbrot.jl)

    function mandelbrot(a)
        z = 0
        for i=1:50
            z = z^2 + a
        end
        return z
    end

    Y = parse(Float32, ARGS[1])
    X = parse(Float32, ARGS[2])

    for y=1.0:Y:-1.0
        for x=-2.0:X:0.5
            abs(mandelbrot(complex(x, y))) < 2 ? print("*") : print(" ")
        end
        println()
    end

    # Taken from: https://rosettacode.org/wiki/Mandelbrot_set#Julia
    # Added X and Y command line parse.


The invocation of the *julia_mandelbrot* task would be equivalent to:

.. code-block:: console

    $ # julia mandelbrot.jl x y > result
    $ julia mandelbrot.jl -0.05, 0.0315 > fractal.txt

And the final result of `fractal.txt` after executing the is:

.. code-block:: console

    $ runcompss julia_decorator_test.py
    [ INFO ] Inferred PYTHON language
    [ INFO ] Using default location for project file: /opt/COMPSs//Runtime/configuration/xml/projects/default_project.xml
    [ INFO ] Using default location for resources file: /opt/COMPSs//Runtime/configuration/xml/resources/default_resources.xml
    [ INFO ] Using default execution type: compss

    ----------------- Executing julia_decorator_test.py --------------------------

    WARNING: COMPSs Properties file is null. Setting default values
    [(930)    API]  -  Starting COMPSs Runtime v3.0.rc2210 (build 20221014-1030.reba7fbb482a79b596e249b2c3b6b17509a05652a)
    [(5300)    API]  -  Execution Finished

    ------------------------------------------------------------
    $ cat fractal.txt



                                                           **
                                                         ******
                                                       ********
                                                         ******
                                                      ******** **   *
                                              ***   *****************
                                              ************************  ***
                                              ****************************
                                           ******************************
                                            *******************************
                                         ************************************
                                *         **********************************
                           ** ***** *     **********************************
                           ***********   ************************************
                         ************** ************************************
                         ***************************************************
                     *****************************************************
       **   *  *********************************************************
                     *****************************************************
                         ***************************************************
                         ************** ************************************
                           ***********   ************************************
                           ** ***** *     **********************************
                                *         **********************************
                                         ************************************
                                            *******************************
                                           ******************************
                                              ****************************
                                              ************************  ***
                                              ***   *****************
                                                      ******** **   *
                                                         ******
                                                       ********
                                                         ******
                                                           **


Please note that the *keyword* parameter is a string, and it is respected as is
in the invocation call.
Another way of passing task parameters to julia execution command is to use
```args``` parameter in the julia definition.
In this case, task parameters should be defined between curly braces and the
full string with parameter replacements will be added to the command.
In the following example, value of 'param_1' is added to the execution command
after '-d' arg:

.. code-block:: python
    :name: julia_task_python_print_date
    :caption: Julia task example with args

    from pycompss.api.task import task
    from pycompss.api.julia import julia
    from pycompss.api.parameter import *


    @julia(script="my_julia_app.jl", args= "-d {{param_1}}")
    @task()
    def julia_task(param_1):
         pass

    if __name__=='__main__':
        julia_task("hello")



The invocation of the *julia_task* task would be equivalent to:

.. code-block:: console

    $ # julia my_julia_app.jl -d param_1
    $ julia -d hello


Thus, PyCOMPSs can also deal with prefixes for the given parameters:

.. code-block:: python
    :name: complex2_julia_task_python
    :caption: Julia task example 4

    from pycompss.api.task import task
    from pycompss.api.julia import julia
    from pycompss.api.parameter import *

    @julia(script="my_julia_app.jl")
    @task(hide={Type:FILE_IN, Prefix:"--hide="}, sort={Prefix:"--sort="})
    def julia_task(flag, hide, sort):
        pass

    if __name__=='__main__':
        flag = '-l'
        hideFile = "fileToHide.txt"
        sort = "time"
        julia_task(flag, hideFile, sort)

The invocation of the *julia_task* task would be equivalent to:

.. code-block:: console

    $ # julia my_julia_app.jl -l --hide=hide --sort=sort
    $ julia my_julia_app.jl -l --hide=fileToHide.txt --sort=time

This particular case is intended to show all the power of the
*@julia* decorator in conjuntion with the *@task*
decorator. Please note that although the *hide* parameter is used as a
prefix for the julia invocation, the *fileToHide.txt* would also be
transfered to the worker (if necessary) since its type is defined as
`FILE_IN`. This feature enables to build more complex julia invocations.

In addition, the ``@julia`` decorator also supports the ``fail_by_exit_value``
parameter to define the failure of the task by the exit value of the julia
(:numref:`julia_task_python_exit`).
It accepts a boolean (``True`` to consider the task failed if the exit value is
not 0, or ``False`` to ignore the failure by the exit value (**default**)), or
a string to determine the environment variable that defines the fail by
exit value (as boolean).
The default behaviour (``fail_by_exit_value=False``) allows users to receive
the exit value of the julia as the task return value, and take the
necessary decissions based on this value.

.. code-block:: python
    :name: julia_task_python_exit
    :caption: Julia task example with ``fail_by_exit_value``

    @julia(script="my_julia_app.jl", fail_by_exit_value=True)
    @task()
    def julia_task():
         pass

In addition, to all previous possibilities, a `@julia` task can also be defined
with constraints. To this end, the `@constraint` decorator has to be provided
on top of the `@julia` decorator:

.. code-block:: python
   :name: complex_julia_task_python_with_constraint
   :caption: Julia task example using `mandelbrot.jl` application (`julia_decorator_test.py`) with constraint

   from pycompss.api.task import task
   from pycompss.api.julia import julia
   from pycompss.api.parameter import *
   from pycompss.api.constraint import constraint

   @constraint(computing_units="2")
   @julia(script="mandelbrot.jl", working_dir=".")
   @task(result={Type:FILE_OUT_STDOUT})
   def julia_mandelbrot(x, y, result):
        pass

   # This task definition is equivalent to the following, which is more verbose:
   #
   # @constraint(computing_units="2")
   # @julia(script="mandelbrot.jl", working_dir=".")
   # @task(result={Type:FILE_OUT, StdIOStream:STDOUT})
   # def julia_mandelbrot(x, y, result):
   #     pass

   if __name__=='__main__':
       outfile = "fractal.txt"
       julia_mandelbrot(-0.05, 0.0315, outfile)

:numref:`complex_julia_task_python_with_constraint` extends the
:numref:`complex_julia_task_python` with the `@constraint` decorator in order
to define that the `julia_mandelbrot` task requires 2 computing nodes (cores).
In this scenario, the julia script (`mandelbrot.jl`) needs to implement a mechanism
to exploit multiple cores.

Finally, the PyCOMPSs integration with Julia also enables to use multiple computing
nodes, enabling to have two levels of parallelism (PyCOMPSs and
`Julia Parallel ClusterManagers <https://github.com/JuliaParallel/ClusterManagers.jl>`_)
However, this feature is limited to SLURM enabled clusters (i.e. supercomputers
with SLURM queuing system).

The following code snippet (:numref:`complex_julia_task_python_multinode`)
shows the definition of a Julia task that requires to be executed using 2
nodes and with 2 processes on each node (4 total processes).
The julia script executed as task (:numref:`julia_distributed_code`)
used the `Julia Parallel ClusterManagers <https://github.com/JuliaParallel/ClusterManagers.jl>`_
library to spawn the processes in the nodes where COMPSs runtime has enabled,
and on each node and process prints its identifier and node name.

.. code-block:: python
   :name: complex_julia_task_python_multinode
   :caption: Julia task example using multiple nodes

   from pycompss.api.task import task
   from pycompss.api.julia import julia
   from pycompss.api.parameter import *
   from pycompss.api.constraint import constraint
   from pycompss.api.multinode import multinode

   @multinode(computing_nodes="2")
   @constraint(computing_units="2")
   @julia(script="distributed_app.jl")
   @task(result={Type:FILE_OUT_STDOUT})
   def julia_distributed_app(result):
        pass

   # This task definition can also be defined as follows:
   #
   # @constraint(computing_units="2")
   # @julia(script="distributed_app.jl", computing_nodes="2")
   # @task(result={Type:FILE_OUT_STDOUT})
   # def julia_distributed_app(result):
   #     pass

   if __name__=='__main__':
       outfile = "fractal.txt"
       julia_mandelbrot(-0.05, 0.0315, outfile)


.. code-block:: julia
    :name: julia_distributed_code
    :caption: Julia application using distributed parallelism (`distributed_app.jl`)

    using Distributed, ClusterManagers
    addprocs_slurm(parse(Int, ENV["SLURM_NTASKS"]))

    @everywhere using Distributed
    @everywhere println(myid())
    @everywhere println(gethostname())

    println("Hello world")

.. TIP::

    If the julia script sets the number or processes based on the `SLURM_NTASKS`
    environment variable allows to change the number of total processes and
    nodes without modifying the julia script. This enables to adapt the
    julia script parallelism in terms of the `computing_units` and `computing_nodes`
    defined in the `@constraint` and `@multinode` decorators accordingly.
