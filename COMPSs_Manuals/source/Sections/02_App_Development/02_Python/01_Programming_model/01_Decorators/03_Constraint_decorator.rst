@constraint
===========

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
---------------------

The constraints are defined as key-value pairs, where the key
is the name of the constraint. :numref:`python_supported_constraints`
details the available constraints names for **Python** its value
type, its default value and a brief description.

.. table:: Arguments of the *@constraint* decorator
    :name: python_supported_constraints

    +-------------------------------------+------------------------------------------+---------------------+------------------------------------------------------------------------------------------+
    | **Python**                          | **Value type**                           | **Default value**   | **Description**                                                                          |
    +=====================================+==========================================+=====================+==========================================================================================+
    | computing_units                     | :math:`<`\ string\ :math:`>`             | "1"                 | Required number of computing units                                                       |
    +-------------------------------------+------------------------------------------+---------------------+------------------------------------------------------------------------------------------+
    | is_local                            | :math:`<`\ "true"\|"false"\ :math:`>`    | "false"             | The task must be executed in the node it's detected                                      |
    +-------------------------------------+------------------------------------------+---------------------+------------------------------------------------------------------------------------------+
    | processor_name                      | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Required processor name                                                                  |
    +-------------------------------------+------------------------------------------+---------------------+------------------------------------------------------------------------------------------+
    | processor_speed                     | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Required processor speed                                                                 |
    +-------------------------------------+------------------------------------------+---------------------+------------------------------------------------------------------------------------------+
    | processor_architecture              | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Required processor architecture                                                          |
    +-------------------------------------+------------------------------------------+---------------------+------------------------------------------------------------------------------------------+
    | processor_type                      | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Required processor type                                                                  |
    +-------------------------------------+------------------------------------------+---------------------+------------------------------------------------------------------------------------------+
    | processor_property_name             | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Required processor property                                                              |
    +-------------------------------------+------------------------------------------+---------------------+------------------------------------------------------------------------------------------+
    | processor_property_value            | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Required processor property value                                                        |
    +-------------------------------------+------------------------------------------+---------------------+------------------------------------------------------------------------------------------+
    | processor_internal_memory_size      | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Required internal device memory                                                          |
    +-------------------------------------+------------------------------------------+---------------------+------------------------------------------------------------------------------------------+
    | processors                          | Dict\ :math:`<`\ Processor\ :math:`>`    | "{}"                | Required processors (check :numref:`python_processor_constraints` for Processor details) |
    +-------------------------------------+------------------------------------------+---------------------+------------------------------------------------------------------------------------------+
    | memory_size                         | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Required memory size in GBs                                                              |
    +-------------------------------------+------------------------------------------+---------------------+------------------------------------------------------------------------------------------+
    | memory_type                         | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Required memory type (SRAM, DRAM, etc.)                                                  |
    +-------------------------------------+------------------------------------------+---------------------+------------------------------------------------------------------------------------------+
    | storage_size                        | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Required storage size in GBs                                                             |
    +-------------------------------------+------------------------------------------+---------------------+------------------------------------------------------------------------------------------+
    | storage_type                        | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Required storage type (HDD, SSD, etc.)                                                   |
    +-------------------------------------+------------------------------------------+---------------------+------------------------------------------------------------------------------------------+
    | operating_system_type               | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Required operating system type (Windows, MacOS, Linux, etc.)                             |
    +-------------------------------------+------------------------------------------+---------------------+------------------------------------------------------------------------------------------+
    | operating_system_distribution       | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Required operating system distribution (XP, Sierra, OpenSUSE, etc.)                      |
    +-------------------------------------+------------------------------------------+---------------------+------------------------------------------------------------------------------------------+
    | operating_system_version            | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Required operating system version                                                        |
    +-------------------------------------+------------------------------------------+---------------------+------------------------------------------------------------------------------------------+
    | wall_clock_limit                    | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Maximum wall clock time                                                                  |
    +-------------------------------------+------------------------------------------+---------------------+------------------------------------------------------------------------------------------+
    | host_queues                         | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Required queues                                                                          |
    +-------------------------------------+------------------------------------------+---------------------+------------------------------------------------------------------------------------------+
    | app_software                        | :math:`<`\ string\ :math:`>`             | "[unassigned]"      | Required applications that must be available within the remote node for the task         |
    +-------------------------------------+------------------------------------------+---------------------+------------------------------------------------------------------------------------------+

All constraints are defined with a simple value except the *host_queues*
and *app_software* constraints, which allow multiple values.

The *processors* constraint allows the users to define multiple
processors for a task execution. This constraint is specified as a list
that must be defined as shown in :numref:`python_processor_constraints`

.. table:: Arguments of the *processor* type
    :name: python_processor_constraints

    +----------------------+--------------------------------+---------------------+---------------------------------------------+
    | **Key**              | **Value type**                 | **Default value**   | **Description**                             |
    +======================+================================+=====================+=============================================+
    | processorType        | :math:`<`\ string\ :math:`>`   | "CPU"               | Required processor type (e.g. CPU or GPU)   |
    +----------------------+--------------------------------+---------------------+---------------------------------------------+
    | computingUnits       | :math:`<`\ string\ :math:`>`   | "1"                 | Required number of computing units          |
    +----------------------+--------------------------------+---------------------+---------------------------------------------+
    | name                 | :math:`<`\ string\ :math:`>`   | "[unassigned]"      | Required processor name                     |
    +----------------------+--------------------------------+---------------------+---------------------------------------------+
    | speed                | :math:`<`\ string\ :math:`>`   | "[unassigned]"      | Required processor speed                    |
    +----------------------+--------------------------------+---------------------+---------------------------------------------+
    | architecture         | :math:`<`\ string\ :math:`>`   | "[unassigned]"      | Required processor architecture             |
    +----------------------+--------------------------------+---------------------+---------------------------------------------+
    | propertyName         | :math:`<`\ string\ :math:`>`   | "[unassigned]"      | Required processor property                 |
    +----------------------+--------------------------------+---------------------+---------------------------------------------+
    | propertyValue        | :math:`<`\ string\ :math:`>`   | "[unassigned]"      | Required processor property value           |
    +----------------------+--------------------------------+---------------------+---------------------------------------------+
    | internalMemorySize   | :math:`<`\ string\ :math:`>`   | "[unassigned]"      | Required internal device memory             |
    +----------------------+--------------------------------+---------------------+---------------------------------------------+


Dynamic constraints
-------------------

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
(:ref:`Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/03_Constraint_decorator/Alternative_dynamic_constraints:Alternative ways to define dynamic constraints`).


Special constraints
-------------------

There is a special constraint when **considering the COMPSs agents deployment**
(:ref:`Sections/03_Execution/03_Agents:Agents Deployments`)
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
     (:ref:`Sections/03_Execution/99_Deployment_models:Deployment Models`).


.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Table of Contents

   03_Constraint_decorator/Alternative_dynamic_constraints
