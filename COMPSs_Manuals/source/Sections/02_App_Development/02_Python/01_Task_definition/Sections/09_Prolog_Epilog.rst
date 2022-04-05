Prolog & Epilog
~~~~~~~~~~~~~~~

The *@prolog* and *@epilog* decorators are definitions of binaries to be executed before / after ```task``` execution on the worker. All kind of
PyCOMPSs tasks can have a *@prolog* or an *@epilog*, or both at the same time. A basic usage is shown in the example below:


.. IMPORTANT::

    Please note that *@prolog* and *@epilog* definitions should be on top of *@task* decorators.

.. code-block:: python
    :name: prolog_epilog_basic
    :caption: Prolog and Epilog definitions.

    from pycompss.api.epilog import epilog
    from pycompss.api.prolog import prolog
    from pycompss.api.task import task


    @prolog(binary="start_some_service.bin")
    @task()
    def basic():
        ...
        return 1

    @epilog(binary="shut_down.bin")
    @task()
    def basic():
        ...
        return 1

Both decorators have the same syntax and have 3 parameters: ```binary``` is the only mandatory parameter where ```params``` and ```fail_by_exit_value``` are
arbitrary. ```params``` helps the user to pass task parameters to the ```binary``` as command line arguments. In this case, the task parameter should be surrounded
by double curly braces (*"{{"* and *"}}"*) in the 'params' string. These parameters can be products of previous tasks and PyCOMPSs will handle data dependencies
between tasks:

.. code-block:: python
    :name: prolog_task_with_param
    :caption: Task parameter in Prolog definition.


    from pycompss.api.prolog import prolog
    from pycompss.api.task import task

    @prolog(binary="mkdir", params="{{param_1}}")
    @task()
    def task_1(param_1):
        ...
        return 1

    # call to the task function
    task_1("/home/dir_to_be_created_before_task_exec")


If the user doesn't want the 'task' to be executed in case of ```prolog``` failure, they can set the ```fail_by_exit_value``` to *True*. If set to *False*, failure of the prolog
will be ignored and task execution will start as usual. The same rule applies for the ```epilog``` as well:


.. code-block:: python
    :name: prolog_epilog_fail
    :caption: Prolog & Epilog with 'fail_by_exit_value'.


    from pycompss.api.epilog import epilog
    from pycompss.api.prolog import prolog
    from pycompss.api.task import task

    @prolog(binary="mkdir", params="-p {{sandbox_path}}", fail_by_exit_value=True)
    @epilog(binary="rm", params="-r {{sandbox_path}}", fail_by_exit_value=False)
    @task()
    def task_2(sandbox_path):
        ...
        return 1

    # call to the task function
    task_2("/tmp/my_task_sandbox")


In the example above, if creation of the 'sandbox_path' fails, the task execution won't start at all and task will be considered as failed. However, if removing the sandbox is not
crucial and can be ignored, ```fail_by_exit_value``` in the Epilog can be set to *False*.