Failures and Exceptions
~~~~~~~~~~~~~~~~~~~~~~~

COMPSs is able to deal with failures and exceptions raised during the execution of the
applications. In this case, if a user/python defined exception happens, the
user can choose the task behavior using the *on_failure* argument within the
*@task* decorator.

The possible values are:
  - **'RETRY'** (Default): The task is executed twice in the same worker and a different worker.
  - **'CANCEL_SUCCESSORS'**: All successors of this task are canceled.
  - **'FAIL'**: The task failure produces a failure of the whole application.
  - **'IGNORE'**: The task failure is ignored and the output parameters are set with empty values.

A part from failures, COMPSs can also manage blocked tasks executions. Users can
use the *time_out* property in the task definition to indicate the maximum duration
of a task. If the task execution takes more seconds than the specified in the
property. The task will be considered failed. This property can be combined with
the *on_failure* mechanism.

.. code-block:: python
    :name: task_failures
    :caption: Task failures example

    from pycompss.api.task import task

    @task(time_out=60, on_failure='IGNORE')
    def foo(v):
        ...

.. TIP::

    The *on_failure* behavior can also be defined with the ``@on_failure``
    decorator placed over the ``@task`` decorator, which provides more options.
    For example:

    .. code-block:: python
        :name: task_failures_decorator
        :caption: Task failures example with @on_failure decorator

        from pycompss.api.task import task
        from pycompss.api.on_failure import on_failure
        from pycompss.api.parameter import INOUT

        from myclass import generate_empty  # private function that generates empty object

        @on_failure(management='IGNORE', returns=0, w=generate_empty())
        @task(time_out=60, w=INOUT, returns=int)
        def foo(v, w):
            ...

    This example depicts a task named ``foo`` that has two parameters (``v``
    (IN) and ``w`` (INOUT)) and has a timeout of 60 seconds. If the timeout is
    reached or an exception is thrown, the task will be considered as failed,
    and the management action defined in the ``@on_failure`` decorator applied,
    which in this example is to ignore the failure and continue. However, when
    continuing with the execution, the ``foo`` task should have produced a
    return element and modifies the ``w`` parameter. Consequently, the return
    and ``w`` values when the task fails are defined in the ``@on_failure``
    decorator. The return value will be 0 when the task fails, and ``w`` will
    contain the object produced by ``generate_empty`` function.


COMPSs provides an special exception (``COMPSsException``) that the user can
raise when necessary and can be caught in the main code for user defined
behavior management. :numref:`task_group_compss_exception`
shows an example of *COMPSsException* raising. In this case, the group
definition is blocking, and waits for all task groups to finish.
If a task of the group raises a *COMPSsException* it will be captured by the
runtime. It will react to it by canceling the running and pending tasks of the
group and raising the COMPSsException to enable the execution
except clause.
Consequently, the *COMPSsException* must be combined with task groups.

In addition, the tasks which belong to the group will be affected by the
*on_failure* value defined in the *@task* decorator.

.. code-block:: python
    :name: task_group_compss_exception
    :caption: COMPSs Exception with task group example

    from pycompss.api.task import task
    from pycompss.api.exceptions import COMPSsException
    from pycompss.api.api import TaskGroup

    @task()
    def foo(v):
        ...
        if v == 8:
            raise COMPSsException("8 found!")

    ...

    if __name__=='__main__':
        try:
            with TaskGroup('exceptionGroup1'):
                for i in range(10):
                    foo(i)
        except COMPSsException:
            ...  # React to the exception (maybe calling other tasks or with other parameters)


It is possible to use a non-blocking task group for asynchronous behavior
(see :numref:`task_group_compss_exception_async`).
In this case, the *try-except* can be defined later in the code surrounding
the *compss_barrier_group*, enabling to check exception from the defined
groups without retrieving data while other tasks are being executed.

.. code-block:: python
    :name: task_group_compss_exception_async
    :caption: Asynchronous COMPSs Exception with task group example

    from pycompss.api.task import task
    from pycompss.api.api import TaskGroup
    from pycompss.api.api import compss_barrier_group

    @task()
    def foo1():
        ...

    @task()
    def foo2():
        ...

    def test_taskgroup():
        # Creation of group
        for i in range(10):
            with TaskGroup('Group' + str(i), False):
                for i in range(NUM_TASKS):
                    foo1()
                    foo2()
                ...
        for i in range(10):
            try:
                compss_barrier_group('Group' + str(i))
            except COMPSsException:
                ...  # React to the exception (maybe calling other tasks or with other parameters)
        ...

    if __name__=='__main__':
        test_taskgroup()

.. IMPORTANT::
     To ensure the COMPSs Exception is caught, they must be always combined with TaskGroups.
