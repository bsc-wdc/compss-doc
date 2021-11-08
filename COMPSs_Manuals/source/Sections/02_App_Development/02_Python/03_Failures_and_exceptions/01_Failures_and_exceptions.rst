Failures and Exceptions
~~~~~~~~~~~~~~~~~~~~~~~

COMPSs is able to deal with failures and exceptions raised during the execution of the
applications. In this case, if a user/python defined exception happens, the
user can choose the task behaviour using the *on_failure* argument within the
*@task* decorator.

The possible values are:
  - **'RETRY'** (Default): The task is executed twice in the same worker and a different worker.
  - **’CANCEL_SUCCESSORS’**: All successors of this task are canceled.
  - **’FAIL’**: The task failure produces a failure of the whole application.
  - **’IGNORE’**: The task failure is ignored and the output parameters are set with empty values.

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
    def func(v):
        ...

COMPSs provides an special exception (``COMPSsException``) that the user can
raise when necessary and can be catched in the main code for user defined
behaviour management. :numref:`task_group_compss_exception`
shows an example of *COMPSsException* raising. In this case, the group
definition is blocking, and waits for all task groups to finish.
If a task of the group raises a *COMPSsException* it will be captured by the
runtime. It will react to it by canceling the running and pending tasks of the
group and raising the COMPSsException to enable the execution
except clause.
Consequenty, the *COMPSsException* must be combined with task groups.

In addition, the tasks which belong to the group will be affected by the
*on_failure* value defined in the *@task* decorator.

.. code-block:: python
    :name: task_group_compss_exception
    :caption: COMPSs Exception with task group example

    from pycompss.api.task import task
    from pycompss.api.exceptions import COMPSsException
    from pycompss.api.api import TaskGroup

    @task()
    def func(v):
        ...
        if v == 8:
            raise COMPSsException("8 found!")

    ...

    if __name__=='__main__':
        try:
            with TaskGroup('exceptionGroup1'):
                for i in range(10):
                    func(i)
        except COMPSsException:
            ...  # React to the exception (maybe calling other tasks or with other parameters)


It is possible to use a non-blocking task group for asynchronous behaviour
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
    def func1():
        ...

    @task()
    def func2():
        ...

    def test_taskgroup():
        # Creation of group
        for i in range(10):
            with TaskGroup('Group' + str(i), False):
                for i in range(NUM_TASKS):
                    func1()
                    func2()
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
     To ensure the COMPSs Exception is catched, they must be always combined with TaskGroups.
