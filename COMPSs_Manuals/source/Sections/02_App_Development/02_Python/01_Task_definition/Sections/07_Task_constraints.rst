Task Constraints
~~~~~~~~~~~~~~~~

It is possible to define constraints for each task.
To this end, the *@constraint* (or @Constraint) decorator followed
by the desired constraints needs to be placed ON TOP of the @task
decorator (:numref:`constraint_task_python`).

.. IMPORTANT::

    Please note the the order of *@constraint* and *@task* decorators is important.

.. code-block:: python
    :name: constraint_task_python
    :caption: Constrained task example

    from pycompss.api.task import task
    from pycompss.api.constraint import constraint
    from pycompss.api.parameter import INOUT

    @constraint(computing_units="4")
    @task(c=INOUT)
    def func(a, b, c):
         c += a * b
         ...

This decorator enables the user to set the particular constraints for
each task, such as the amount of Cores required explicitly.
Alternatively, it is also possible to indicate that the value of a
constraint is specified in a environment variable (:numref:`constraint_env_var_task_python`).
A full description of the supported constraints can be found in :numref:`supported_constraints`.

For example:

.. code-block:: python
    :name: constraint_env_var_task_python
    :caption: Constrained task with environment variable example

    from pycompss.api.task import task
    from pycompss.api.constraint import constraint
    from pycompss.api.parameter import INOUT

    @constraint(computing_units="4",
                app_software="numpy,scipy,gnuplot",
                memory_size="$MIN_MEM_REQ")
    @task(c=INOUT)
    def func(a, b, c):
         c += a * b
         ...

Or another example requesting a CPU core and a GPU (:numref:`CPU_GPU_constraint_task_python`).

.. code-block:: python
    :name: CPU_GPU_constraint_task_python
    :caption: CPU and GPU constrained task example

    from pycompss.api.task import task
    from pycompss.api.constraint import constraint

    @constraint(processors=[{'processorType':'CPU', 'computingUnits':'1'},
                            {'processorType':'GPU', 'computingUnits':'1'}])
    @task(returns=1)
    def func(a, b, c):
         ...
         return result

When the task requests a GPU, COMPSs provides the information about
the assigned GPU through the *COMPSS_BINDED_GPUS*,
*CUDA_VISIBLE_DEVICES* and *GPU_DEVICE_ORDINAL* environment
variables. This information can be gathered from the task code in
order to use the GPU.

Please, take into account that in order to respect the constraints,
the peculiarities of the infrastructure must be defined in the
*resources.xml* file.
