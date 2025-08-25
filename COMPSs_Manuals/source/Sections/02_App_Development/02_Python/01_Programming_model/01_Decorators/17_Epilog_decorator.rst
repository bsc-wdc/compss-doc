@epilog
=======

The *@prolog* and *@epilog* decorators are definitions of binaries to be executed before / after ```task``` execution on the worker. All kind of
PyCOMPSs tasks can have a *@prolog* or an *@epilog*, or both at the same time. A basic usage is shown in the example below:


.. IMPORTANT::

    Please note that *@prolog* and *@epilog* definitions should be on top of *@task* decorators.

Definition
----------

.. code-block:: python
    :name: prolog_epilog_basic
    :caption: Prolog and Epilog definitions.

    from pycompss.api.epilog import epilog
    from pycompss.api.prolog import prolog
    from pycompss.api.task import task


    @prolog(binary="/my_service/start.bin")
    @epilog(binary="/my_service/stop.bin")
    @task()
    def run_simulation():
        ...

    def main():
        run_simulation()


Both decorators have the same syntax and have 3 parameters: ```binary``` is the only mandatory parameter where ```args``` and ```fail_by_exit_value``` are
optional. ```args``` describe the command line arguments of the binary. Users can also pass the task parameters as arguments. In this case, the task parameter
should be surrounded by double curly braces (*"{{"* and *"}}"*) in the 'args' string. These parameters can be results of previous tasks and PyCOMPSs will handle data dependencies
between tasks:


.. IMPORTANT::

    Task parameters used in 'args' strings can be type of primitive types such as int, float, string, and boolean.


.. code-block:: python
    :name: prolog_task_with_param
    :caption: Task parameter in Prolog/Epilog definition.


    from pycompss.api.prolog import prolog
    from pycompss.api.epilog import epilog
    from pycompss.api.task import task

    @prolog(binary="mkdir", args="/tmp/{{working_dir}}")
    @epilog(binary="tar", args="zcvf {{out_tgz}} /tmp/{{working_dir}}")
    @task(returns=1)
    def run_simulation(working_dir, out_tgz):
        ...

    def main():
        # call to the task function
        run_simulation("my_logs", "my_logs_compressed")


```fail_by_exit_value``` is used to indicate the behavior when the prolog or epilog returns an exit value different than zero.
Users can set the ```fail_by_exit_value``` to *True*, if they want to consider the exit value as a task failure. If set to *False*, failure of the prolog
will be ignored and task execution will start as usual. The same rule applies for the ```epilog``` as well. Default value of 'fail_by_exit_value' is *True* for Prolog
and *False* for Epilog:


.. code-block:: python
    :name: prolog_epilog_fail
    :caption: Prolog & Epilog with 'fail_by_exit_value'.


    from pycompss.api.epilog import epilog
    from pycompss.api.prolog import prolog
    from pycompss.api.task import task

    @prolog(binary="mkdir", args="-p {{sandbox_path}}", fail_by_exit_value=True)
    @epilog(binary="rm", args="-r {{sandbox_path}}", fail_by_exit_value=False)
    @task()
    def run_simulation(sandbox_path):
        ...
        return 1

    # call to the task function
    run_simulation("/tmp/my_task_sandbox")


In the example above, if creation of the 'sandbox_path' fails, the task execution won't start at all and task will be considered as failed. However, if removing the sandbox is not
crucial and can be ignored, ```fail_by_exit_value``` in the Epilog can be set to *False*.
