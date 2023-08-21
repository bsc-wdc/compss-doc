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

Supported constraints
^^^^^^^^^^^^^^^^^^^^^

A full description of the supported constraints can be found in :numref:`supported_constraints`.

Dynamic constraints
^^^^^^^^^^^^^^^^^^^

The dynamic constraints are supported for **computing units**, **memory size** and **disk size**. 
In order to define a constraint as dynamic, instead of setting a static value or environment variable, 
the user needs to set the name of the **global variable** desired for the constraint.

.. code-block:: python
    :name: dynamic_constraint_task_python
    :caption: dynamic_constraint task example

    from pycompss.api.task import task
    from pycompss.api.constraint import constraint
    MS = 1

    @constraint(memory_size="MS")
    @task()
    def func(a, b, c):
         c += a * b
         ...

Having the dynamic constraint defined with a global variable, the user now has the ability to change
the global variable value between task calls, in order to have different constraint values for each call.

.. code-block:: python
    :name: dynamic_constraint_task_call_python
    :caption: dynamic_constraint task call example

    def main():
        global MS
        {...}
        func(a, b, c)
        MS = 2
        func(a, b, c)
        MS = a + b * c
        func(a, b, c)

It is possible to define dynamic constraints using alternative syntax
(:ref:`sections/02_App_Development/02_Python/01_1_Task_definition/Sections/07_Task_constraints/01_Alternative_dynamic_constraints:Alternative ways to define dynamic constraints`).

.. toctree::
    :hidden:
    :maxdepth: 2
    :caption: Table of Contents

    07_Task_constraints/01_Alternative_dynamic_constraints


Special constraints
^^^^^^^^^^^^^^^^^^^

There is a special constraint when **considering the COMPSs agents deployment**
(:ref:`sections/03_Execution_Environments/03_Deployments/02_Agents:Agents Deployments`)
to specify that the task MUST be executed in the node that received the task.
This constraint is indicated in the *@constraint* decorator with the
``is_local`` argument equal a boolean (``True`` or ``False``) (:numref:`is_local_task_python`)
in addition to other constraints.

.. code-block:: python
    :name: is_local_task_python
    :caption: is_local task example

    from pycompss.api.task import task
    from pycompss.api.constraint import constraint

    @constraint(is_local=True)
    @task(c=INOUT)
    def func(a, b, c):
         c += a * b

.. IMPORTANT::

     The ``is_local`` constraint has NO effect with the default COMPSs deployment
     (master-workers)
     (:ref:`sections/03_Execution_Environments/03_Deployments/01_Master_worker:Master-Worker Deployments`).
