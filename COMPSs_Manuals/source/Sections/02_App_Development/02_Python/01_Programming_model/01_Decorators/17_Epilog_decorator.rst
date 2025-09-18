@epilog
=======

The ``@epilog`` decorator enables the definition of binaries to be executed **after** the ``task`` execution on the worker.
All kind of PyCOMPSs tasks can have a ``@epilog``.
A basic usage is shown in the example below.

.. TIP::
    There is a similar decorator to the define binaries to be executed **before** the ``task`` execution on the worker.
    It is the :ref:`Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/16_Prolog_decorator:@prolog` decorator.

    You can check the documentation of both decorators combined: :ref:`Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/16_17_Prolog_Epilog_decorator/01_Prolog_Epilog_decorator:@prolog and @epilog`


Definition
----------

.. code-block:: python
    :name: epilog_basic
    :caption: Epilog definition.

    from pycompss.api.epilog import epilog
    from pycompss.api.task import task

    @epilog(binary="/my_service/stop.bin")
    @task()
    def run_simulation():
        ...

    def main():
        run_simulation()


The ``@epilog`` decorator has 3 parameters:

``binary``
    Defines the binary to be executed after the task.
    **Mandatory**

``args``
    Describe the command line arguments of the binary.
    Users can also pass the task parameters as arguments.
    In this case, the task parameter should be surrounded by double curly braces (*"{{"* and *"}}"*) in the 'args' string.
    **Optional**

    .. IMPORTANT::

        Task parameters used in 'args' strings can be type of primitive types such as int, float, string, and boolean.

``fail_by_exit_value``
    Is used to indicate the behavior when the epilog returns an exit value different than zero.
    Users can set the ``fail_by_exit_value`` to *True*, if they want to consider the exit value as a task failure.
    If set to *False*, failure of the epilog will be ignored and task execution will start as usual.
    Default value of 'fail_by_exit_value' is *False* for Epilog.
    **Optional**


These parameters can be results of previous tasks and PyCOMPSs will handle data dependencies between tasks:

.. code-block:: python
    :name: epilog_task_with_param
    :caption: Task parameter in Epilog definition.

    from pycompss.api.epilog import epilog
    from pycompss.api.task import task

    @epilog(binary="tar", args="zcvf {{out_tgz}} /tmp/{{working_dir}}")
    @task(returns=1)
    def run_simulation(working_dir, out_tgz):
        ...

    def main():
        # call to the task function
        run_simulation("my_logs", "my_logs_compressed")


In the next example, removing the sandbox is not crucial and can be ignored, so ``fail_by_exit_value`` in the Epilog can be set to *False*.

.. code-block:: python
    :name: epilog_fail
    :caption: Epilog with 'fail_by_exit_value'.


    from pycompss.api.epilog import epilog
    from pycompss.api.task import task

    @epilog(binary="rm", args="-r {{sandbox_path}}", fail_by_exit_value=False)
    @task()
    def run_simulation(sandbox_path):
        ...
        return 1

    # call to the task function
    run_simulation("/tmp/my_task_sandbox")
