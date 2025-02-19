API
~~~

PyCOMPSs provides an API for data synchronization and other functionalities,
such as task group definition and automatic function parameter synchronization
(local decorator).

Synchronization
^^^^^^^^^^^^^^^

The main program of the application is a sequential code that contains
calls to the selected tasks. In addition, when synchronizing for task
data from the main program, there exist six API functions that can be invoked:

compss_open(file_name, mode=’r’)
   Similar to the Python *open()* call.
   It synchronizes for the last version of file *file_name* and
   returns the file descriptor for that synchronized file. It can have
   an optional parameter *mode*, which defaults to ’\ *r*\ ’, containing
   the mode in which the file will be opened (the open modes are
   analogous to those of Python *open()*).

compss_wait_on_file(\*file_name)
   Synchronizes for the last version of the file/s specified by *file_name*.
   Returns True if success (False otherwise).

compss_wait_on_directory(\*directory_name)
   Synchronizes for the last version of the directory/ies specified by *directory_name*.
   Returns True if success (False otherwise).

compss_barrier(no_more_tasks=False)
   Performs a explicit synchronization, but does not return any object.
   The use of *compss_barrier()* forces to wait for all tasks that have been
   submitted before the *compss_barrier()* is called. When all tasks
   submitted before the *compss_barrier()* have finished, the execution
   continues. The *no_more_tasks* is used to specify if no more tasks
   are going to be submitted after the *compss_barrier()*.

compss_barrier_group(group_name)
   Performs a explicit synchronization over the tasks that belong to the group
   *group_name*, but does not return any object.
   The use of *compss_barrier_group()* forces to wait for all tasks that belong
   to the given group submitted before the *compss_barrier_group()* is called.
   When all group tasks submitted before the *compss_barrier_group()* have
   finished, the execution continues.
   See :ref:`Sections/02_App_Development/02_Python/01_2_Synchronization/01_API:Task Groups`
   for more information about task groups.

compss_wait_on(\*obj, mode="r" | "rw")
   Synchronizes for the last version of object/s specified by *obj* and returns
   the synchronized object.
   It can have an optional string parameter *mode*, which defaults to
   *rw*, that indicates whether the main program will modify the
   returned object. It is possible to wait on a list of objects. In this
   particular case, it will synchronize all future objects contained in
   the list recursively.


To illustrate the use of the aforementioned API functions, the following
example (:numref:`api_usage_python`) first invokes a task *func* that writes a
file, which is later synchronized by calling *compss_open()*.
Later in the program, an object of class *MyClass* is created and a task method
*method* that modifies the object is invoked on it; the object is then
synchronized with *compss_wait_on*, so that it can be used in the main
program from that point on.

Then, a loop calls again ten times to *func* task. Afterwards, the
*compss_barrier()* call performs a synchronization, and the execution of
the main user code will not continue until the ten *func* tasks have finished.
This call does not retrieve any information.

.. code-block:: python
    :name: api_usage_python
    :caption: PyCOMPSs Synchronization API functions usage

    from pycompss.api.api import compss_open
    from pycompss.api.api import compss_wait_on
    from pycompss.api.api import compss_wait_on_file
    from pycompss.api.api import compss_wait_on_directory
    from pycompss.api.api import compss_barrier

    if __name__=='__main__':
        my_file = 'file.txt'
        func(my_file)
        fd = compss_open(my_file)
        ...

        my_file2 = 'file2.txt'
        func(my_file2)
        compss_wait_on_file(my_file2)
        ...

        my_directory = '/tmp/data'
        func_dir(my_directory)
        compss_wait_on_directory(my_directory)
        ...

        my_obj2 = MyClass()
        my_obj2.method()
        my_obj2 = compss_wait_on(my_obj2)
        ...

        for i in range(10):
            func(str(i) + my_file)
        compss_barrier()
        ...

The corresponding task definition for the example above would be
(:numref:`api_usage_tasks_python`):

.. code-block:: python
    :name: api_usage_tasks_python
    :caption: PyCOMPSs Synchronization API usage tasks

    @task(f=FILE_OUT)
    def func(f):
        ...

    class MyClass(object):
        ...

        @task()
        def method(self):
            ... # self is modified here

.. TIP::

    It is possible to synchronize a list of objects. This is
    particularly useful when the programmer expect to synchronize more than
    one elements (using the *compss_wait_on* function)
    (:numref:`list_synchronization_python`).
    This feature also works with dictionaries, where the value of each entry
    is synchronized.
    In addition, if the structure synchronized is a combination of lists and
    dictionaries, the *compss_wait_on* will look for all objects to be
    synchronized in the whole structure.

    .. code-block:: python
        :name: list_synchronization_python
        :caption: Synchronization of a list of objects

        if __name__=='__main__':
            # l is a list of objects where some/all of them may be future objects
            l = []
            for i in range(10):
                l.append(ret_func())

            ...

            l = compss_wait_on(l)

.. IMPORTANT::

    In order to make the COMPSs Python binding function correctly, the
    programmer **should not use relative imports** in the code. Relative imports
    can lead to ambiguous code and they are discouraged in Python, as
    explained in:
    http://docs.python.org/2/faq/programming.html#what-are-the-best-practices-for-using-import-in-a-module


Local Decorator
"""""""""""""""

Besides the synchronization API functions, the programmer has also a
decorator for automatic function parameters synchronization at his
disposal. The *@local* decorator can be placed over functions
that are not decorated as tasks, but that may receive results from
tasks (:numref:`local_python`). In this case, the *@local* decorator synchronizes the
necessary parameters in order to continue with the function execution
without the need of using explicitly the *compss_wait_on* call for
each parameter.

.. code-block:: python
    :name: local_python
    :caption: @local decorator example

    from pycompss.api.task import task
    from pycompss.api.api import compss_wait_on
    from pycompss.api.parameter import INOUT
    from pycompss.api.local import local

    @task(v=INOUT)
    def append_three_ones(v):
        v += [1, 1, 1]

    @local
    def scale_vector(v, k):
        return [k*x for x in v]

    if __name__=='__main__':
        v = [1,2,3]
        append_three_ones(v)
        # v is automatically synchronized when calling the scale_vector function.
        w = scale_vector(v, 2)




File/Object deletion
^^^^^^^^^^^^^^^^^^^^

PyCOMPSs also provides two functions within its API for object/file deletion.
These calls allow the runtime to clean the infrastructure explicitly, but
the deletion of the objects/files will be performed as soon as the
objects/files dependencies are released.

compss_delete_file(\*file_name)
 Notifies the runtime to delete a file/s.

compss_delete_object(\*object)
  Notifies the runtime to delete all the associated files to a given object/s.

  .. WARNING::

      It does not support collections.


The following example (:numref:`api_delete_usage_python`) illustrates the use
of the aforementioned API functions.


.. code-block:: python
    :name: api_delete_usage_python
    :caption: PyCOMPSs delete API functions usage

    from pycompss.api.api import compss_delete_file
    from pycompss.api.api import compss_delete_object

    if __name__=='__main__':
        my_file = 'file.txt'
        func(my_file)
        compss_delete_file(my_file)
        ...

        my_obj = MyClass()
        my_obj.method()
        compss_delete_object(my_obj)
        ...


The corresponding task definition for the example above would be
(:numref:`api_delete_usage_tasks_python`):

.. code-block:: python
    :name: api_delete_usage_tasks_python
    :caption: PyCOMPSs delete API usage tasks

    @task(f=FILE_OUT)
    def func(f):
        ...

    class MyClass(object):
        ...

        @task()
        def method(self):
            ... # self is modified here


Task Groups
^^^^^^^^^^^

COMPSs also enables to specify task groups. To this end, COMPSs provides the
*TaskGroup* context (:numref:`task_group`) which can be tuned with the group name,
and a second parameter (boolean) to perform an implicit barrier for the whole group.
Users can also define task groups within task groups.

TaskGroup(group_name, implicit_barrier=True)
   Python context to define a group of tasks. All tasks submitted within the
   context will belong to *group_name* context and are sensitive to wait for
   them while the rest are being executed. Tasks groups are depicted within
   a box into the generated task dependency graph.


.. code-block:: python
    :name: task_group
    :caption: PyCOMPSs Task group definition

    from pycompss.api.task import task
    from pycompss.api.api import TaskGroup
    from pycompss.api.api import compss_barrier_group

    @task()
    def func1():
        ...

    @task()
    def func2():
        ...

    if __name__=='__main__':
        # Creation of group
        with TaskGroup('Group1', False):
            for i in range(NUM_TASKS):
                func1()
                func2()
            ...
        ...
        compss_barrier_group('Group1')
        ...

compss_barrier_group(group_name)
    Task Groups are commonly used to implement the exception mechanism in PyCOMPSs
    applications (see :ref:`Sections/02_App_Development/02_Python/01_3_Failures_and_exceptions/01_Failures_and_exceptions:Failures and Exceptions`
    section for more information about this feature.). Moreover, developers can also cancel
    task groups using the *compss_cancel_group* API call, indicating the name of the
    group to cancel as depicted in (:numref:`cancel_task_group`).

.. code-block:: python
    :name: cancel_task_group
    :caption: PyCOMPSs Task group cancellation

    from pycompss.api.task import task
    from pycompss.api.api import TaskGroup
    from pycompss.api.api import compss_cancel_group

    @task()
    def func1():
        ...

    @task()
    def func2():
        ...

    if __name__=='__main__':
        # Creation of group
        with TaskGroup('Group1', False):
            for i in range(NUM_TASKS):
                func1()
                func2()
            ...
        ...
        compss_cancel_group('Group1')
        ...


Other
^^^^^

PyCOMPSs also provides other function within its API to check if a file exists.

compss_file_exists(\*file_name)
 Checks if a file or files exist. If it does not exist, the function checks
 if the file has been accessed before by calling the runtime.

:numref:`api_file_exists` illustrates its usage.

.. code-block:: python
    :name: api_file_exists
    :caption: PyCOMPSs API file exists usage

    from pycompss.api.api import compss_file_exists

    if __name__=='__main__':
        my_file = 'file.txt'
        func(my_file)
        if compss_file_exists(my_file):
            print("Exists")
        else:
            print("Not exists")
        ...

The corresponding task definition for the example above would be
(:numref:`api_file_exists_usage_tasks_python`):

.. code-block:: python
    :name: api_file_exists_usage_tasks_python
    :caption: PyCOMPSs delete API usage tasks

    @task(f=FILE_OUT)
    def func(f):
        ...


API Summary
^^^^^^^^^^^

Finally, :numref:`python_api_functions` summarizes the API functions to be
used in the main program of a COMPSs Python application.

.. table:: COMPSs Python API functions
    :name: python_api_functions

    +-----------------+----------------------------------------------+-----------------------------------------------------------------------------------------+
    | Type            | API Function                                 | Description                                                                             |
    +=================+==============================================+=========================================================================================+
    | Synchronization | compss_open(file_name, mode=’r’)             | Synchronizes for the last version of a file and returns its file descriptor.            |
    |                 +----------------------------------------------+-----------------------------------------------------------------------------------------+
    |                 | compss_wait_on_file(\*file_name)             | Synchronizes for the last version of the specified file/s.                              |
    |                 +----------------------------------------------+-----------------------------------------------------------------------------------------+
    |                 | compss_wait_on_directory(\*directory_name)   | Synchronizes for the last version of the specified directory/ies.                       |
    |                 +----------------------------------------------+-----------------------------------------------------------------------------------------+
    |                 | compss_barrier(no_more_tasks=False)          | Wait for all tasks submitted before the barrier.                                        |
    |                 +----------------------------------------------+-----------------------------------------------------------------------------------------+
    |                 | compss_barrier_group(group_name)             | Wait for all tasks that belong to *group_name* group submitted before the barrier.      |
    |                 +----------------------------------------------+-----------------------------------------------------------------------------------------+
    |                 | compss_wait_on(\*obj, mode="r" | "rw")       | Synchronizes for the last version of an object (or a list of objects) and returns it.   |
    +-----------------+----------------------------------------------+-----------------------------------------------------------------------------------------+
    | File/Object     | compss_delete_file(\*file_name)              | Notifies the runtime to remove the given file/s.                                        |
    | deletion        +----------------------------------------------+-----------------------------------------------------------------------------------------+
    |                 | compss_delete_object(\*object)               | Notifies the runtime to delete the associated file to the object/s.                     |
    +-----------------+----------------------------------------------+-----------------------------------------------------------------------------------------+
    | Task Groups     | TaskGroup(group_name, implicit_barrier=True) | Context to define a group of tasks. *implicit_barrier* forces waiting on context exit.  |
    |                 +----------------------------------------------+-----------------------------------------------------------------------------------------+
    |                 | compss_cancel_group(group_name)              | Cancel all the task defined in a TaskGroup                                              |
    +-----------------+----------------------------------------------+-----------------------------------------------------------------------------------------+
    | Other           | compss_file_exists(\*file_name)              | Check if a file or files exist.                                                         |
    +-----------------+----------------------------------------------+-----------------------------------------------------------------------------------------+
