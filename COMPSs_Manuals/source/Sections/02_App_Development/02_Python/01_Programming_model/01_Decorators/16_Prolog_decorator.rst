@prolog
=======

The ``@prolog`` decorator enables the definition of binaries to be executed **before** the ``task`` execution on the worker.
All kind of PyCOMPSs tasks can have a ``@prolog``.
A basic usage is shown in the example below.

.. TIP::
    There is a similar decorator to the define binaries to be executed **after** the ``task`` execution on the worker.
    It is the :ref:`Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/17_Epilog_decorator:@epilog` decorator.

    You can check the documentation of both decorators combined: :ref:`Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/16_17_Prolog_Epilog_decorator/01_Prolog_Epilog_decorator:@prolog and @epilog`

Definition
----------

.. code-block:: python
    :name: prolog_basic
    :caption: Prolog definition.

    from pycompss.api.prolog import prolog
    from pycompss.api.task import task

    @prolog(binary="/my_service/start.bin")
    @task()
    def run_simulation():
        ...

    def main():
        run_simulation()


.. IMPORTANT::

    Please note that ``@prolog`` definition should be on top of ``@task`` decorator.


The ``@prolog`` decorator has 3 parameters:

``binary``
    Defines the binary to be executed before the task.
    **Mandatory**

``args``
    Describe the command line arguments of the binary.
    Users can also pass the task parameters as arguments.
    In this case, the task parameter should be surrounded by double curly braces (*"{{"* and *"}}"*) in the 'args' string.
    **Optional**

    .. IMPORTANT::

        Task parameters used in 'args' strings can be type of primitive types such as int, float, string, and boolean.

``fail_by_exit_value``
    Is used to indicate the behavior when the prolog returns an exit value different than zero.
    Users can set the ``fail_by_exit_value`` to *True*, if they want to consider the exit value as a task failure.
    If set to *False*, failure of the prolog will be ignored and task execution will start as usual.
    Default value of 'fail_by_exit_value' is *True* for Prolog.
    **Optional**


These parameters can be results of previous tasks and PyCOMPSs will handle data dependencies between tasks:

.. code-block:: python
    :name: prolog_task_with_param
    :caption: Task parameter in Prolog definition.

    from pycompss.api.prolog import prolog
    from pycompss.api.task import task

    @prolog(binary="mkdir", args="/tmp/{{working_dir}}")
    @task(returns=1)
    def run_simulation(working_dir):
        ...

    def main():
        # call to the task function
        run_simulation("my_logs")


In the next example, the task execution won't start at all if the creation of the 'sandbox_path' fails, and task will be considered as failed.

.. code-block:: python
    :name: prolog_fail
    :caption: Prolog with 'fail_by_exit_value'.

    from pycompss.api.prolog import prolog
    from pycompss.api.task import task

    @prolog(binary="mkdir", args="-p {{sandbox_path}}", fail_by_exit_value=True)
    @task()
    def run_simulation(sandbox_path):
        ...
        return 1

    # call to the task function
    run_simulation("/tmp/my_task_sandbox")

