Other Task Parameters
~~~~~~~~~~~~~~~~~~~~~

Task time out
^^^^^^^^^^^^^

The user is also able to define the time out of a task within the ``@task`` decorator
with the ``time_out=<TIME_IN_SECONDS>`` hint.
The runtime will cancel the task if the time to execute the task exceeds the time defined by the user.
For example, :numref:`task_time_out` shows how to specify that the ``unknown_duration_task``
maximum duration before canceling (if exceeded) is one hour.

.. code-block:: python
    :name: task_time_out
    :caption: Python task *time_out* example

    @task(time_out=3600)
    def unknown_duration_task(self):
        ...

Scheduler hints
^^^^^^^^^^^^^^^

The programmer can provide hints to the scheduler through specific
arguments within the *@task* decorator.

For instance, the programmer can mark a task as a high-priority task
with the ``priority`` argument of the ``@task`` decorator (:numref:`task_priority_python`).
In this way, when the task is free of dependencies, it will be scheduled before
any of the available low-priority (regular) tasks. This functionality is
useful for tasks that are in the critical path of the application’s task
dependency graph.

.. code-block:: python
    :name: task_priority_python
    :caption: Python task *priority* example

    @task(priority=True)
    def func():
        ...

Moreover, the user can also mark a task as distributed with the
*is_distributed* argument or as replicated with the *is_replicated*
argument (:numref:`task_isdistributed_isreplicated_python`). When a task is marked with *is_distributed=True*, the method
must be scheduled in a forced round robin among the available resources.
On the other hand, when a task is marked with *is_replicated=True*, the
method must be executed in all the worker nodes when invoked from the
main application. The default value for these parameters is False.

.. code-block:: python
    :name: task_isdistributed_isreplicated_python
    :caption: Python task *is_distributed* and *is_replicated* examples

    @task(is_distributed=True)
    def func():
        ...

    @task(is_replicated=True)
    def func2():
        ...

On failure task behavior
^^^^^^^^^^^^^^^^^^^^^^^^^

In case a task fails, the whole application behavior can be defined
using the *@on_failure* decorator on top of the *@task* decorator
(:numref:`task_on_failure_python`).
It has four possible values that can be defined with the **management**
parameter: **'RETRY'**, **’CANCEL_SUCCESSORS’**, **’FAIL’** and **’IGNORE’**.
*’RETRY’* is the default behavior, making the task to be executed again (on
the same worker or in another worker if the failure remains).
*’CANCEL_SUCCESSORS’* ignores the failed task and cancels the execution of the
successor tasks, *’FAIL’* stops the whole execution once a task fails and
*’IGNORE’* ignores the failure and continues with the normal execution.

.. code-block:: python
    :name: task_on_failure_python
    :caption: Python task *@on_failure* decorator example

    from pycompss.api.task import task
    from pycompss.api.on_failure import on_failure

    @on_failure(management ='CANCEL_SUCCESSORS')
    @task()
    def func():
        ...

Since the **’CANCEL_SUCCESSORS’** and **’IGNORE’** policies enable to continue
the execution accepting that tasks may have failed, it is possible to define
the value for the objects and/or files produced by the failed tasks (INOUT,
OUT, FILE_INOUT, FILE_OUT and return).
This is considered as the default output objects/files.
For example, :numref:`task_on_failure_python_default_return` shows a the ``func``
task which returns one integer. In the case of failure within ``func``, the
execution of the workflow will continue since the on failure management policy
is set to *'IGNORE'*, with 0 as return value.

.. code-block:: python
    :name: task_on_failure_python_default_return
    :caption: Python task *@on_failure* example with default return value

    from pycompss.api.task import task
    from pycompss.api.on_failure import on_failure

    @on_failure(management='IGNORE', returns=0)
    @task(returns=int)
    def func():
        ...

For the INOUT parameters, the default value can be set by using the parameter
name of ``func`` in the *@on_failure* decorator.
:numref:`task_on_failure_python_default_inout` shows how to define the default
value for a FILE_INOUT parameter (named ``f_inout``).
The example is also valid for FILE_OUT values.

.. code-block:: python
    :name: task_on_failure_python_default_inout
    :caption: Python task *@on_failure* example with default FILE_INOUT value

    from pycompss.api.task import task
    from pycompss.api.on_failure import on_failure
    from pycompss.api.parameter import FILE_INOUT

    @on_failure(management='IGNORE', f_inout="/path/to/default.file")
    @task(f_inout=FILE_INOUT)
    def func(f_inout):
        ...

.. TIP::

    The default FILE_INOUT/FILE_OUT can be generated at task generation time
    by calling a function instead of providing a static file path.
    :numref:`task_on_failure_python_default_inout_func` shows an example of this
    case, where the default value for the output file produced by ``func`` is
    defined by the ``generate_empty`` function.

    .. code-block:: python
        :name: task_on_failure_python_default_inout_func
        :caption: Python task *@on_failure* example with default FILE_OUT value from function

        from pycompss.api.task import task
        from pycompss.api.on_failure import on_failure
        from pycompss.api.parameter import FILE_OUT

        def generate_empty(msg, name):
            empty_file = "/tmp/empty_file_" + name
            with open(empty_file, 'w') as f:
                f.write("EMPTY FILE " + msg)
            return empty_file

        @on_failure(management='IGNORE', f_out=generate_empty("OUT", "out.tmp"))
        @task(f_out=FILE_OUT)
        def func(f_inout):
            ...
