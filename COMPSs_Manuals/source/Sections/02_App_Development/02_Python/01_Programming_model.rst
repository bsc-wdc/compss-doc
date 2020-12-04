Programming Model
-----------------

Task Selection
~~~~~~~~~~~~~~

As in the case of Java, a COMPSs Python application is a Python
sequential program that contains calls to tasks. In particular, the user
can select as a task:

-  Functions

-  Instance methods: methods invoked on objects.

-  Class methods: static methods belonging to a class.

The task definition in Python is done by means of Python decorators
instead of an annotated interface. In particular, the user needs to add
a ``@task`` decorator that describes the task before the
definition of the function/method.

As an example (:numref:`code_python`), let us assume that the application calls a function
*func*, which receives a file path (string parameter) and an integer
parameter. The code of *func* updates the file.

.. code-block:: python
    :name: code_python
    :caption: Python application example

    def func(file_path, value):
        # update the file 'file_path'

    def main():
        my_file = '/tmp/sample_file.txt'
        func(my_file, 1)

    if __name__ == '__main__':
        main()


In order to select *func* as a task, the corresponding *@task*
decorator needs to be placed right before the definition of the
function, providing some metadata about the parameters of that function.
The *@task* decorator has to be imported from the *pycompss*
library (:numref:`task_import_python`).

.. code-block:: python
    :name: task_import_python
    :caption: Python task import

    from pycompss.api.task import task

    @task()
    def func():
         ...

Function parameters
^^^^^^^^^^^^^^^^^^^

The *@task* decorator does not interfere with the function parameters,
Consequently, the user can define the function parameters as normal python
functions (:numref:`task_parameters_python`).

.. code-block:: python
    :name: task_parameters_python
    :caption: Task function parameters example

    @task()
    def func(param1, param2):
         ...

The use of *\*args* and *\*\*kwargs* as function parameters is
supported (:numref:`task_args_kwargs_python`).

.. code-block:: python
    :name: task_args_kwargs_python
    :caption: Python task *\*args* and *\*\*kwargs example*

    @task(returns=int)
    def argkwarg_func(*args, **kwargs):
        ...

And even with other parameters, such as usual parameters and *default
defined arguments*. :numref:`task_default_parameters_python` shows an example of a task with two
three parameters (whose one of them (*’s’*) has a default value), *\*args*
and *\*\*kwargs*.

.. code-block:: python
    :name: task_default_parameters_python
    :caption: Python task with default parameters example

    @task(returns=int)
    def multiarguments_func(v, w, s = 2, *args, **kwargs):
        ...


Tasks within classes
^^^^^^^^^^^^^^^^^^^^

Functions within classes can also be declared as tasks as normal functions.
The main difference is the existence of the ``self`` parameter which enables
to modify the callee object.

For tasks corresponding to instance methods, by default the task is
assumed to modify the callee object (the object on which the method is
invoked). The programmer can tell otherwise by setting the
*target_direction* argument of the *@task* decorator to *IN*
(:numref:`task_instance_method_python`).

.. code-block:: python
    :name: task_instance_method_python
    :caption: Python instance method example

    class MyClass(object):
        ...
        @task(target_direction=IN)
        def instance_method(self):
            ... # self is NOT modified here

Class methods and static methods can also be declared as tasks. The only
requirement is to place the ``@classmethod`` or ``@staticmethod`` over
the *@task* decorator (:numref:`task_classmethod_instancemethod_python`).
Note that there is no need to use the *target_direction* flag within the
*@task* decorator.

.. code-block:: python
    :name: task_classmethod_instancemethod_python
    :caption: Python ``@classmethod`` and ``@staticmethod`` tasks example

    class MyClass(object):
        ...
        @classmethod
        @task()
        def class_method(cls, a, b, c):
            ...

        @staticmethod
        @task(returns=int)
        def static_method(a, b, c):
            ...

.. TIP::

   Tasks inheritance and overriding supported!!!


.. CAUTION::

   The objects used as task parameters **MUST BE** serializable:

      * Implement the ``__getstate__`` and ``__setstate__`` functions in their
        classes for those objects that are not automatically serializable.
      * The classes must not be declared in the same file that contains the
        main method (``if __name__=='__main__'``) (known pickle issue).

.. IMPORTANT::

   For instances of user-defined classes, the classes of these objects
   should have an empty constructor, otherwise the programmer will not be
   able to invoke task instance methods on those objects (:numref:`user_class_return_python`).

   .. code-block:: python
       :name: user_class_return_python
       :caption: Using user-defined classes as task returns

       # In file utils.py
       from pycompss.api.task import task
       class MyClass(object):
           def __init__(self): # empty constructor
               ...

           @task()
           def yet_another_task(self):
               # do something with the self attributes
               ...

           ...

       # In file main.py
       from pycompss.api.task import task
       from utils import MyClass

       @task(returns=MyClass)
       def ret_func():
           ...
           myc = MyClass()
           ...
           return myc

       def main():
           o = ret_func()
           # invoking a task instance method on a future object can only
           # be done when an empty constructor is defined in the object's
           # class
           o.yet_another_task()

       if __name__=='__main__':
           main()


Task Parameters
~~~~~~~~~~~~~~~

The metadata corresponding to a parameter is specified as an argument of
the ``@task`` decorator, whose name is the formal parameter’s name and whose
value defines the type and direction of the parameter. The parameter types and
directions can be:

Types
   * *Primitive types* (integer, long, float, boolean)
   * *Strings*
   * *Objects* (instances of user-defined classes, dictionaries, lists, tuples, complex numbers)
   * *Files*
   * *Streams*
   * *IO streams* (for binaries)

Direction
   * Read-only (*IN* - default or *IN_DELETE*)
   * Read-write (*INOUT*)
   * Write-only (*OUT*)
   * Concurrent (*CONCURRENT*)
   * Conmutative (*CONMUTATIVE*)

COMPSs is able to automatically infer the parameter type for primitive
types, strings and objects, while the user needs to specify it for
files. On the other hand, the direction is only mandatory for *INOUT*
and *OUT* parameters. Thus, when defining the parameter metadata in the
*@task* decorator, the user has the following options:


.. LIST-TABLE::
    :header-rows: 1

    * - PARAMETER
      - DESCRIPTION
    * - *IN*
      - The parameter is read-only. The type will be inferred.
    * - *IN_DELETE*
      - The parameter is read-only. The type will be inferred. Will be automatically removed after its usage.
    * - *INOUT*
      - The parameter is read-write. The type will be inferred.
    * - *OUT*
      - The parameter is write-only. The type will be inferred.
    * - *CONCURRENT*
      - The parameter is read-write with concurrent access. The type will be inferred.
    * - *COMMUTATIVE*
      - The parameter is read-write with commutative access. The type will be inferred.
    * - *FILE/FILE_IN*
      - The parameter is a file. The direction is assumed to be *IN*.
    * - *FILE_INOUT*
      - The parameter is a read-write file.
    * - *FILE_OUT*
      - The parameter is a write-only file.
    * - *DIRECTORY_IN*
      - The parameter is a directory and the direction is *IN*. The directory will be compressed before any transfer amongst nodes.
    * - *DIRECTORY_INOUT*
      - The parameter is a read-write directory. The directory will be compressed before any transfer amongst nodes.
    * - *DIRECTORY_OUT*
      - The parameter is a write-only directory. The directory will be compressed before any transfer amongst nodes.
    * - *FILE_CONCURRENT*
      - The parameter is a concurrent read-write file.
    * - *FILE_COMMUTATIVE*
      - The parameter is a commutative read-write file.
    * - *COLLECTION_IN*
      - The parameter is read-only collection.
    * - *COLLECTION_INOUT*
      - The parameter is read-write collection.
    * - *COLLECTION_OUT*
      - The parameter is write-only collection.
    * - *COLLECTION_FILE/COLLECTION_FILE_IN*
      - The parameter is read-only collection of files.
    * - *COLLECTION_FILE_INOUT*
      - The parameter is read-write collection of files.
    * - *COLLECTION_FILE_OUT*
      - The parameter is write-only collection of files.
    * - *DICTIONARY_IN*
      - The parameter is read-only dictionary.
    * - *DICTIONARY_INOUT*
      - The parameter is read-write dictionary.
    * - *STREAM_IN*
      - The parameter is a read-only stream.
    * - *STREAM_OUT*
      - The parameter is a write-only stream*
    * - *STDIN*
      - The parameter is a IO stream for standard input redirection (only for binaries).
    * - *STDOUT*
      - The parameter is a IO stream for standard output redirection (only for binaries).
    * - *STDERR*
      - The parameter is a IO stream for standard error redirection (only for binaries).

Consequently, please note that in the following cases there is no need
to include an argument in the *@task* decorator for a given
task parameter:

-  Parameters of primitive types (integer, long, float, boolean) and
   strings: the type of these parameters can be automatically inferred
   by COMPSs, and their direction is always *IN*.

-  Read-only object parameters: the type of the parameter is
   automatically inferred, and the direction defaults to *IN*.

The parameter metadata is available from the *pycompss* library
(:numref:`parameter_import_python`)

.. code-block:: python
    :name: parameter_import_python
    :caption: Python task parameters import

    from pycompss.api.parameter import *

Continuing with the example, in :numref:`task_example_python` the decorator
specifies that *func* has a parameter called *f*, of type *FILE* and
*INOUT* direction. Note how the second parameter, *i*, does not need to
be specified, since its type (integer) and direction (*IN*) are
automatically inferred by COMPSs.

.. code-block:: python
    :name: task_example_python
    :caption: Python task example with input output file (*FILE_INOUT*)

    from pycompss.api.task import task     # Import @task decorator
    from pycompss.api.parameter import *   # Import parameter metadata for the @task decorator

    @task(f=FILE_INOUT)
    def func(f, i):
         fd = open(f, 'r+')
         ...

The user can also define that the access to a parameter is concurrent
with *CONCURRENT* or to a file *FILE_CONCURRENT* (:numref:`task_concurrent_python`).
Tasks that share a "CONCURRENT" parameter will be executed in parallel, if any
other dependency prevents this. The CONCURRENT direction allows users to have
access from multiple tasks to the same object/file during their executions.
However, note that COMPSs does not manage the interaction with the objects or
files used/modified concurrently. Taking care of the access/modification of
the concurrent objects is responsibility of the developer.

.. code-block:: python
    :name: task_concurrent_python
    :caption: Python task example with *FILE_CONCURRENT*

    from pycompss.api.task import task     # Import @task decorator
    from pycompss.api.parameter import *   # Import parameter metadata for the @task decorator

    @task(f=FILE_CONCURRENT)
    def func(f, i):
         ...

Or even, the user can also define that the access to a parameter is conmutative
with *CONMUTATIVE* or to a file *FILE_CONMUTATIVE* (:numref:`task_conmutative_python`).
The execution order of tasks that share a "CONMUTATIVE" parameter can be changed
by the runtime following the conmutative property.

.. code-block:: python
    :name: task_conmutative_python
    :caption: Python task example with *FILE_CONMUTATIVE*

    from pycompss.api.task import task     # Import @task decorator
    from pycompss.api.parameter import *   # Import parameter metadata for the @task decorator

    @task(f=FILE_CONMUTATIVE)
    def func(f, i):
         ...

Moreover, it is possible to specify that a parameter is a collection of
elements (e.g. list) and its direction (COLLECTION_IN or
COLLECTION_INOUT) (:numref:`task_collection_python`). In this case, the list
may contain sub-objects that will be handled automatically by the runtime.
It is important to annotate data structures as collections if in other tasks
there are accesses to individual elements of these collections as parameters.
Without this annotation, the runtime will not be able to identify data
dependences between the collections and the individual elements.

.. code-block:: python
    :name: task_collection_python
    :caption: Python task example with *COLLECTION* (*IN*)

    from pycompss.api.task import task             # Import @task decorator
    from pycompss.api.parameter import COLLECTION  # Import parameter metadata for the @task decorator

    @task(my_collection=COLLECTION)
    def func(my_collection):
         for element in my_collection:
             ...

The sub-objects of the collection can be collections of elements (and
recursively). In this case, the runtime also keeps track of all elements
contained in all sub-collections. In order to improve the performance,
the depth of the sub-objects can be limited through the use of the
*depth* parameter (:numref:`task_collection_depth_python`)

.. code-block:: python
    :name: task_collection_depth_python
    :caption: Python task example with *COLLECTION_IN* and *Depth*

    from pycompss.api.task import task                # Import @task decorator
    from pycompss.api.parameter import COLLECTION_IN  # Import parameter metadata for the @task decorator

    @task(my_collection={Type:COLLECTION_IN, Depth:2})
    def func(my_collection):
         for inner_collection in my_collection:
             for element in inner_collection:
                 # The contents of element will not be tracked
                 ...

As with the collections, it is possible to specify that a parameter is
a dictionary of elements (e.g. dict) and its direction (DICTIONARY_IN or
DICTIONARY_INOUT) (:numref:`task_dictionary_python`),
whose sub-objects will be handled automatically by the runtime.

.. code-block:: python
    :name: task_dictionary_python
    :caption: Python task example with *DICTIONARY* (*IN*)

    from pycompss.api.task import task             # Import @task decorator
    from pycompss.api.parameter import DICTIONARY  # Import parameter metadata for the @task decorator

    @task(my_dictionary=DICTIONARY)
    def func(my_dictionary):
         for k, v in my_dictionary.items():
             ...

The sub-objects of the dictionary can be collections or dictionary of elements
(and recursively). In this case, the runtime also keeps track of all elements
contained in all sub-collections/sub-dictionaries.
In order to improve the performance, the depth of the sub-objects can be
limited through the use of the *depth* parameter
(:numref:`task_dictionary_depth_python`)

.. code-block:: python
    :name: task_dictionary_depth_python
    :caption: Python task example with *DICTIONARY_IN* and *Depth*

    from pycompss.api.task import task                # Import @task decorator
    from pycompss.api.parameter import DICTIONARY_IN  # Import parameter metadata for the @task decorator

    @task(my_dictionary={Type:DICTIONARY_IN, Depth:2})
    def func(my_dictionary):
         for key, inner_dictionary in my_dictionary.items():
             for sub_key, sub_value in inner_dictionary.items():
                 # The contents of element will not be tracked
                 ...

.. TIP::

    A collection can contain dictionaries, and dictionaries can contain
    collections.


It is possible to use streams as input or output of the tasks by defining
that a parameter is *STREAM_IN* or *STREAM_OUT* accordingly
(:numref:`task_streams`).
This parameters enable to mix a task-driven workflow with a data-driven
workflow.


.. code-block:: python
    :name: task_streams
    :caption: Python task example with *STREAM_IN* and *STREAM_OUT*

    from pycompss.api.task import task             # Import @task decorator
    from pycompss.api.parameter import STREAM_IN   # Import parameter metadata for the @task decorator
    from pycompss.api.parameter import STREAM_OUT  # Import parameter metadata for the @task decorator

    @task(ods=STREAM_OUT)
    def write_objects(ods):
        ...
        for i in range(NUM_OBJECTS):
            # Build object
            obj = MyObject()
            # Publish object
            ods.publish(obj)
            ...
        ...
        # Mark the stream for closure
        ods.close()

    @task(ods=STREAM_IN, returns=int)
    def read_objects(ods):
        ...
        num_total = 0
        while not ods.is_closed():
            # Poll new objects
            new_objects = ods.poll()
            # Process files
            ...
            # Accumulate read files
            num_total += len(new_objects)
        ...
        # Return the number of processed files
        return num_total

The stream parameter also supports Files (:numref:`task_streams_files`).

.. code-block:: python
    :name: task_streams_files
    :caption: Python task example with *STREAM_IN* and *STREAM_OUT* for files

    from pycompss.api.task import task             # Import @task decorator
    from pycompss.api.parameter import STREAM_IN   # Import parameter metadata for the @task decorator
    from pycompss.api.parameter import STREAM_OUT  # Import parameter metadata for the @task decorator

    @task(fds=STREAM_OUT)
    def write_files(fds):
        ...
        for i in range(NUM_FILES):
            file_name = str(uuid.uuid4())
            # Write file
            with open(file_path, 'w') as f:
                f.write("Test " + str(i))
            ...
        ...
        # Mark the stream for closure
        fds.close()

    @task(fds=STREAM_IN, returns=int)
    def read_files(fds):
        ...
        num_total = 0
        while not fds.is_closed():
            # Poll new files
            new_files = fds.poll()
            # Process files
            for nf in new_files:
                with open(nf, 'r') as f:
                    ...
            # Accumulate read files
            num_total += len(new_files)
            ...
        ...
        # Return the number of processed files
        return num_total

In addition, the stream parameter can also be defined for binary tasks
(:numref:`task_streams_binary`).

.. code-block:: python
    :name: task_streams_binary
    :caption: Python task example with *STREAM_OUT* for binaries

    from pycompss.api.task import task             # Import @task decorator
    from pycompss.api.binary import binary         # Import @task decorator
    from pycompss.api.parameter import STREAM_OUT  # Import parameter metadata for the @task decorator

    @binary(binary="file_generator.sh")
    @task(fds=STREAM_OUT)
    def write_files(fds):
        pass


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

On failure task behaviour
^^^^^^^^^^^^^^^^^^^^^^^^^

In case a task fails, the whole application behaviour can be defined
using the *on_failure* argument (:numref:`task_on_failure_python`).
It has four possible values: **'RETRY'**,
**’CANCEL_SUCCESSORS’**, **’FAIL’** and **’IGNORE’**. *’RETRY’* is the default
behaviour, making the task to be executed again (on the same worker or
in another worker if the failure remains). *’CANCEL_SUCCESSORS’* ignores
the failed task and cancels the execution of the successor tasks, *’FAIL’*
stops the whole execution once a task fails and *’IGNORE’* ignores the
failure and continues with the normal execution.

.. code-block:: python
    :name: task_on_failure_python
    :caption: Python task *on_failure* example

    @task(on_failure='CANCEL_SUCCESSORS')
    def func():
        ...

Task Parameters Summary
~~~~~~~~~~~~~~~~~~~~~~~

:numref:`task_arguments` summarizes all arguments that can be found in the *@task* decorator.

.. table:: Arguments of the *@task* decorator
    :name: task_arguments

    +---------------------+--------------------------------------------------------------------------------------------------------------------+
    | Argument            | Value                                                                                                              |
    +=====================+=======================+============================================================================================+
    | Formal parameter    | **(default: empty)**  | The parameter is an object or a simple tipe that will be inferred.                         |
    | name                +-----------------------+--------------------------------------------------------------------------------------------+
    |                     | IN                    | Read-only parameter, all types.                                                            |
    |                     +-----------------------+--------------------------------------------------------------------------------------------+
    |                     | IN_DELETE             | Read-only parameter, all types. Automatic delete after usage.                              |
    |                     +-----------------------+--------------------------------------------------------------------------------------------+
    |                     | INOUT                 | Read-write parameter, all types except file (primitives, strings, objects).                |
    |                     +-----------------------+--------------------------------------------------------------------------------------------+
    |                     | OUT                   | Write-only parameter, all types except file (primitives, strings, objects).                |
    |                     +-----------------------+--------------------------------------------------------------------------------------------+
    |                     | CONCURRENT            | Concurrent read-write parameter, all types except file (primitives, strings, objects).     |
    |                     +-----------------------+--------------------------------------------------------------------------------------------+
    |                     | CONMUTATIVE           | Conmutative read-write parameter, all types except file (primitives, strings, objects).    |
    |                     +-----------------------+--------------------------------------------------------------------------------------------+
    |                     | FILE(_IN)             | Read-only file parameter.                                                                  |
    |                     +-----------------------+--------------------------------------------------------------------------------------------+
    |                     | FILE_INOUT            | Read-write file parameter.                                                                 |
    |                     +-----------------------+--------------------------------------------------------------------------------------------+
    |                     | FILE_OUT              | Write-only file parameter.                                                                 |
    |                     +-----------------------+--------------------------------------------------------------------------------------------+
    |                     | FILE_CONCURRENT       | Concurrent read-write file parameter.                                                      |
    |                     +-----------------------+--------------------------------------------------------------------------------------------+
    |                     | FILE_CONMUTATIVE      | Conmutative read-write file parameter.                                                     |
    |                     +-----------------------+--------------------------------------------------------------------------------------------+
    |                     | DIRECTORY(_IN)        | The parameter is a read-only directory.                                                    |
    |                     +-----------------------+--------------------------------------------------------------------------------------------+
    |                     | DIRECTORY_INOUT       | The parameter is a read-write directory.                                                   |
    |                     +-----------------------+--------------------------------------------------------------------------------------------+
    |                     | DIRECTORY_OUT         | the parameter is a write-only directory.                                                   |
    |                     +-----------------------+--------------------------------------------------------------------------------------------+
    |                     | COLLECTION(_IN)       | Read-only collection parameter (list).                                                     |
    |                     +-----------------------+--------------------------------------------------------------------------------------------+
    |                     | COLLECTION_INOUT      | Read-write collection parameter (list).                                                    |
    |                     +-----------------------+--------------------------------------------------------------------------------------------+
    |                     | COLLECTION_OUT        | Read-only collection parameter (list).                                                     |
    |                     +-----------------------+--------------------------------------------------------------------------------------------+
    |                     | COLLECTION_FILE(_IN)  | Read-only collection of files parameter (list of files).                                   |
    |                     +-----------------------+--------------------------------------------------------------------------------------------+
    |                     | COLLECTION_FILE_INOUT | Read-write collection of files parameter (list of files).                                  |
    |                     +-----------------------+--------------------------------------------------------------------------------------------+
    |                     | COLLECTION_FILE_OUT   | Read-only collection of files parameter (list of files).                                   |
    |                     +-----------------------+--------------------------------------------------------------------------------------------+
    |                     | DICTIONARY(_IN)       | Read-only dictionary parameter (dict).                                                     |
    |                     +-----------------------+--------------------------------------------------------------------------------------------+
    |                     | DICTIONARY_INOUT      | Read-write dictionary parameter (dict).                                                    |
    |                     +-----------------------+--------------------------------------------------------------------------------------------+
    |                     | STREAM_IN             | The parameter is a read-only stream.                                                       |
    |                     +-----------------------+--------------------------------------------------------------------------------------------+
    |                     | STREAM_OUT            | The parameter is a write-only stream.                                                      |
    |                     +-----------------------+--------------------------------------------------------------------------------------------+
    |                     | STDIN                 | The parameter is a file for standard input redirection (only for binaries).                |
    |                     +-----------------------+--------------------------------------------------------------------------------------------+
    |                     | STDOUT                | The parameter is a file for standard output redirection (only for binaries).               |
    |                     +-----------------------+--------------------------------------------------------------------------------------------+
    |                     | STDERR                | The parameter is a file for standard error redirection (only for binaries).                |
    |                     +-----------------------+--------------------------------------------------------------------------------------------+
    |                     | Explicit: {Type:(empty=object)/FILE/COLLECTION/DICTIONARY, Direction:(empty=IN)/IN/IN_DELETE/INOUT/OUT/CONCURRENT} |
    +---------------------+--------------------------------------------------------------------------------------------------------------------+
    | returns             | int (for integer and boolean), long, float, str, dict, list, tuple, user-defined classes                           |
    +---------------------+--------------------------------------------------------------------------------------------------------------------+
    | target_direction    | INOUT (default), IN or CONCURRENT                                                                                  |
    +---------------------+--------------------------------------------------------------------------------------------------------------------+
    | priority            | True or False (default)                                                                                            |
    +---------------------+--------------------------------------------------------------------------------------------------------------------+
    | is_distributed      | True or False (default)                                                                                            |
    +---------------------+--------------------------------------------------------------------------------------------------------------------+
    | is_replicated       | True or False (default)                                                                                            |
    +---------------------+--------------------------------------------------------------------------------------------------------------------+
    | on_failure          | ’RETRY’ (default), ’CANCEL_SUCCESSORS’, ’FAIL’ or ’IGNORE’                                                         |
    +---------------------+--------------------------------------------------------------------------------------------------------------------+
    | time_out            | int (time in seconds)                                                                                              |
    +---------------------+--------------------------------------------------------------------------------------------------------------------+

Task Return
~~~~~~~~~~~

If the function or method returns a value, the programmer can use the
*returns* argument within the *@task* decorator. In this
argument, the programmer can specify the type of that value
(:numref:`task_returns_python`).

.. code-block:: python
    :name: task_returns_python
    :caption: Python task returns example

    @task(returns=int)
    def ret_func():
         return 1

Moreover, if the function or method returns more than one value, the
programmer can specify how many and their type in the *returns*
argument. :numref:`task_multireturn_python` shows how to specify that two
values (an integer and a list) are returned.

.. code-block:: python
    :name: task_multireturn_python
    :caption: Python task with multireturn example

    @task(returns=(int, list))
    def ret_func():
         return 1, [2, 3]

Alternatively, the user can specify the number of return statements as
an integer value (:numref:`task_returns_integer_python`).
This way of specifying the amount of return eases the
*returns* definition since the user does not need to specify explicitly
the type of the return arguments. However, it must be considered that
the type of the object returned when the task is invoked will be a
future object. This consideration may lead to an error if the user
expects to invoke a task defined within an object returned by a previous
task. In this scenario, the solution is to specify explicitly the return
type.

.. code-block:: python
    :name: task_returns_integer_python
    :caption: Python task returns with integer example

    @task(returns=1)
    def ret_func():
         return "my_string"

    @task(returns=2)
    def ret_func():
         return 1, [2, 3]

.. IMPORTANT::

   If the programmer selects as a task a function or method that returns a
   value, that value is not generated until the task executes (:numref:`task_return_value_python`).

   .. code-block:: python
       :name: task_return_value_python
       :caption: Task return value generation

       @task(return=MyClass)
       def ret_func():
           return MyClass(...)

       ...

       if __name__=='__main__':
           o = ret_func()  # o is a future object

   The object returned can be involved in a subsequent task call, and the
   COMPSs runtime will automatically find the corresponding data
   dependency. In the following example, the object *o* is passed as a
   parameter and callee of two subsequent (asynchronous) tasks,
   respectively (:numref:`task_return_value_usage_python`).

   .. code-block:: python
       :name: task_return_value_usage_python
       :caption: Task return value subsequent usage

       if __name__=='__main__':
           # o is a future object
           o = ret_func()

           ...

           another_task(o)

           ...

           o.yet_another_task()

.. TIP::

    PyCOMPSs is able to infer if the task returns something and its amount in
    most cases. Consequently, the user can specify the task without *returns*
    argument. But this is discouraged since it requires code analysis,
    including an overhead that can be avoided by using the *returns* argument.

.. TIP::

    PyCOMPSs is compatible with Python 3 type hinting. So, if type hinting
    is present in the code, PyCOMPSs is able to detect the return type and
    use it (there is no need to use the *returns*):

    .. code-block:: python
        :name: task_returns_type_hinting_python
        :caption: Python task returns with type hinting

        @task()
        def ret_func() -> str:
             return "my_string"

        @task()
        def ret_func() -> (int, list):
             return 1, [2, 3]


Other task types
~~~~~~~~~~~~~~~~

In addition to this API functions, the programmer can use a set of
decorators for other purposes.

For instance, there is a set of decorators that can be placed over the
*@task* decorator in order to define the task methods as a
**binary invocation** (with the :ref:`Sections/02_App_Development/02_Python/01_Programming_model:Binary decorator`), as a **OmpSs
invocation** (with the :ref:`Sections/02_App_Development/02_Python/01_Programming_model:OmpSs decorator`), as a **MPI invocation**
(with the :ref:`Sections/02_App_Development/02_Python/01_Programming_model:MPI decorator`), as a **COMPSs application** (with the
:ref:`Sections/02_App_Development/02_Python/01_Programming_model:COMPSs decorator`), as a **task that requires multiple
nodes** (with the :ref:`Sections/02_App_Development/02_Python/01_Programming_model:Multinode decorator`), or as a **Reduction task** that
can be executed in parallel having a subset of the original input data as input (with the
:ref:`Sections/02_App_Development/02_Python/01_Programming_model:Reduction decorator`). These decorators must be placed over the
*@task* decorator, and under the *@constraint* decorator if defined.

Consequently, the task body will be empty and the function parameters
will be used as invocation parameters with some extra information that
can be provided within the *@task* decorator.

The following subparagraphs describe their usage.

Binary decorator
^^^^^^^^^^^^^^^^

The *@binary* decorator shall be used to define that a task is
going to invoke a binary executable.

In this context, the *@task* decorator parameters will be used
as the binary invocation parameters (following their order in the
function definition). Since the invocation parameters can be of
different nature, information on their type can be provided through the
*@task* decorator.

:numref:`binary_task_python` shows the most simple binary task definition
without/with constraints (without parameters); please note that @constraint decorator has to be provided on top of the others.

.. code-block:: python
    :name: binary_task_python
    :caption: Binary task example

    from pycompss.api.task import task
    from pycompss.api.binary import binary

    @binary(binary="mybinary.bin")
    @task()
    def binary_func():
         pass

    @constraint(computingUnits="2")
    @binary(binary="otherbinary.bin")
    @task()
    def binary_func2():
         pass

The invocation of these tasks would be equivalent to:

.. code-block:: console

    $ ./mybinary.bin
    $ ./otherbinary.bin   # in resources that respect the constraint.

The ``@binary`` decorator supports the ``working_dir`` parameter to define
the working directory for the execution of the defined binary.

:numref:`complex_binary_task_python` shows a more complex binary invocation, with files
as parameters:

.. code-block:: python
    :name: complex_binary_task_python
    :caption: Binary task example 2

    from pycompss.api.task import task
    from pycompss.api.binary import binary
    from pycompss.api.parameter import *

    @binary(binary="grep", working_dir=".")
    @task(infile={Type:FILE_IN_STDIN}, result={Type:FILE_OUT_STDOUT})
    def grepper():
         pass

    # This task definition is equivalent to the folloowing, which is more verbose:

    @binary(binary="grep", working_dir=".")
    @task(infile={Type:FILE_IN, StdIOStream:STDIN}, result={Type:FILE_OUT, StdIOStream:STDOUT})
    def grepper(keyword, infile, result):
         pass

    if __name__=='__main__':
        infile = "infile.txt"
        outfile = "outfile.txt"
        grepper("Hi", infile, outfile)

The invocation of the *grepper* task would be equivalent to:

.. code-block:: console

    $ # grep keyword < infile > result
    $ grep Hi < infile.txt > outfile.txt

Please note that the *keyword* parameter is a string, and it is
respected as is in the invocation call.

Thus, PyCOMPSs can also deal with prefixes for the given parameters. :numref:`complex2_binary_task_python`
performs a system call (ls) with specific prefixes:

.. code-block:: python
    :name: complex2_binary_task_python
    :caption: Binary task example 3

    from pycompss.api.task import task
    from pycompss.api.binary import binary
    from pycompss.api.parameter import *

    @binary(binary="ls")
    @task(hide={Type:FILE_IN, Prefix:"--hide="}, sort={Prefix:"--sort="})
    def myLs(flag, hide, sort):
        pass

    if __name__=='__main__':
        flag = '-l'
        hideFile = "fileToHide.txt"
        sort = "time"
        myLs(flag, hideFile, sort)

The invocation of the *myLs* task would be equivalent to:

.. code-block:: console

    $ # ls -l --hide=hide --sort=sort
    $ ls -l --hide=fileToHide.txt --sort=time

This particular case is intended to show all the power of the
*@binary* decorator in conjuntion with the *@task*
decorator. Please note that although the *hide* parameter is used as a
prefix for the binary invocation, the *fileToHide.txt* would also be
transfered to the worker (if necessary) since its type is defined as
FILE_IN. This feature enables to build more complex binary invocations.

In addition, the ``@binary`` decorator also supports the ``fail_by_exit_value``
parameter to define the failure of the task by the exit value of the binary
(:numref:`binary_task_python_exit`).
It accepts a boolean (``True`` to consider the task failed if the exit value is
not 0, or ``False`` to ignore the failure by the exit value (**default**)), or
a string to determine the environment variable that defines the fail by
exit value (as boolean).
The default behaviour (``fail_by_exit_value=False``) allows users to receive
the exit value of the binary as the task return value, and take the
necessary decissions based on this value.

.. code-block:: python
    :name: binary_task_python_exit
    :caption: Binary task example with ``fail_by_exit_value``

    @binary(binary="mybinary.bin", fail_by_exit_value=True)
    @task()
    def binary_func():
         pass

OmpSs decorator
^^^^^^^^^^^^^^^

The *@ompss* decorator shall be used to define that a task is
going to invoke a OmpSs executable (:numref:`ompss_task_python`).

.. code-block:: python
    :name: ompss_task_python
    :caption: OmpSs task example

    from pycompss.api.ompss import ompss

    @ompss(binary="ompssApp.bin")
    @task()
    def ompss_func():
         pass

The OmpSs executable invocation can also be enriched with parameters,
files and prefixes as with the *@binary* decorator through the
function parameters and *@task* decorator information. Please,
check :ref:`Sections/02_App_Development/02_Python/01_Programming_model:Binary decorator` for more details.

MPI decorator
^^^^^^^^^^^^^

The *@mpi* decorator shall be used to define that a task is
going to invoke a MPI executable (:numref:`mpi_task_python`).

.. code-block:: python
    :name: mpi_task_python
    :caption: MPI task example

    from pycompss.api.mpi import mpi

    @mpi(binary="mpiApp.bin", runner="mpirun", processes=2)
    @task()
    def mpi_func():
         pass

The MPI executable invocation can also be enriched with parameters,
files and prefixes as with the *@binary* decorator through the
function parameters and *@task* decorator information. Please,
check :ref:`Sections/02_App_Development/02_Python/01_Programming_model:Binary decorator` for more details.

The *@mpi* decorator can be also used to execute a MPI for python (mpi4py) code.
To indicate it, developers only need to remove the binary field and include
the Python MPI task implementation inside the function body as shown in the
following example (:numref:`mpi_for_python`).

.. code-block:: python
    :name: mpi_for_python
    :caption: MPI task example with collections and data layout

    from pycompss.api.mpi import mpi

    @mpi(processes=4)
    @task()
    def layout_test_with_all():
       from mpi4py import MPI
       rank = MPI.COMM_WORLD.rank
       return rank

In both cases, users can also define, MPI + OpenMP tasks by using ``processes``
property to indicate the number of MPI processes and ``computing_units`` in the
Task Constraints to indicate the number of OpenMP threads per MPI process.

The *@mpi* decorator can be combined with collections to allow the process of
a list of parameters in the same MPI execution. By the default, all parameters
of the list will be deserialized to all the MPI processes. However, a common
pattern in MPI is that each MPI processes performs the computation in a subset
of data. So, all data serialization is not needed. To indicate the subset used
by each MPI process, developers can use the ``data_layout`` notation inside the
MPI task declaration.

.. code-block:: python
    :name: mpi_data_layout_python
    :caption: MPI task example with collections and data layout

    from pycompss.api.mpi import mpi

    @mpi(processes=4, col_layout={block_count: 4, block_length: 2, stride: 1})
    @task(col=COLLECTION_IN, returns=4)
    def layout_test_with_all(col):
       from mpi4py import MPI
       rank = MPI.COMM_WORLD.rank
       return data[0]+data[1]+rank

Figure (:numref:`mpi_data_layout_python`) shows an example about how to combine
MPI tasks with collections and data layouts. In this example, we have define a
MPI task with an input collection (``col``). We have also defined a data layout
with the property ``<arg_name>_layout`` and we specify the number of blocks
(``block_count``), the elements per block (``block_length``), and the number of
element between the starting block points (``stride``).

COMPSs decorator
^^^^^^^^^^^^^^^^

The *@compss* decorator shall be used to define that a task is
going to be a COMPSs application (:numref:`compss_task_python`).
It enables to have nested PyCOMPSs/COMPSs applications.

.. code-block:: python
    :name: compss_task_python
    :caption: COMPSs task example

    from pycompss.api.compss import compss

    @compss(runcompss="${RUNCOMPSS}", flags="-d",
            app_name="/path/to/simple_compss_nested.py", computing_nodes="2")
    @task()
    def compss_func():
         pass

The COMPSs application invocation can also be enriched with the flags
accepted by the *runcompss* executable. Please, check execution manual
for more details about the supported flags.

Multinode decorator
^^^^^^^^^^^^^^^^^^^

The *@multinode* decorator shall be used to define that a task
is going to use multiple nodes (e.g. using internal parallelism) (:numref:`multinode_task_python`).

.. code-block:: python
    :name: multinode_task_python
    :caption: Multinode task example

    from pycompss.api.multinode import multinode

    @multinode(computing_nodes="2")
    @task()
    def multinode_func():
         pass

The only supported parameter is *computing_nodes*, used to define the
number of nodes required by the task (the default value is 1). The
mechanism to get the number of nodes, threads and their names to the
task is through the *COMPSS_NUM_NODES*, *COMPSS_NUM_THREADS* and
*COMPSS_HOSTNAMES* environment variables respectively, which are
exported within the task scope by the COMPSs runtime before the task
execution.

Reduction decorator
^^^^^^^^^^^^^^^^^^^

The *@reduction* decorator shall be used to define that a task
is going to be subdivided into smaller tasks that take as input
a subset of the input data. (:numref:`reduction_task_python`).

.. code-block:: python
    :name: reduction_task_python
    :caption: Reduction task example

    from pycompss.api.reduction import reduction

    @reduction(chunk_size="2")
    @task()
    def myreduction():
        pass

The only supported parameter is *chunk_size*, used to define the
size of the data that the generated tasks will get as input parameter.
The data given as input to the main reduction task is subdivided into chunks
of the set size.

Container decorator
^^^^^^^^^^^^^^^^^^^

The *@container* decorator shall be used to define that a task is
going to be executed within a container (:numref:`container_task_python`).

.. code-block:: python
    :name: container_task_python
    :caption: Container task example

    from pycompss.api.compss import container

    @container(engine="DOCKER",
               image="compss/compss")
    @task()
    def container_func():
         pass

The *container_fun* will be executed within the container defined in the
*@container* decorator. For example, using *docker* engine with the *image*
compss/compss.

This feature allows to use specific containers for tasks where the dependencies
are met.

In addition, the *@container* decorator can be placed on top of the
*@binary*, *@ompss* or *@mpi* decorators.

Other task types summary
^^^^^^^^^^^^^^^^^^^^^^^^

Next tables summarizes the parameters of these decorators.

* @binary
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | Parameter              | Description                                                                                                                       |
    +========================+===================================================================================================================================+
    | **binary**             | (Mandatory) String defining the full path of the binary that must be executed.                                                    |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | **working_dir**        | Full path of the binary working directory inside the COMPSs Worker.                                                               |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+

* @ompss
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | Parameter              | Description                                                                                                                       |
    +========================+===================================================================================================================================+
    | **binary**             | (Mandatory) String defining the full path of the binary that must be executed.                                                    |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | **working_dir**        | Full path of the binary working directory inside the COMPSs Worker.                                                               |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+

* @mpi
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | Parameter              | Description                                                                                                                       |
    +========================+===================================================================================================================================+
    | **binary**             | (Optional) String defining the full path of the binary that must be executed. Empty indicates python MPI code.                    |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | **working_dir**        | Full path of the binary working directory inside the COMPSs Worker.                                                               |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | **runner**             | (Mandatory) String defining the MPI runner command.                                                                               |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | **processes**          | Integer defining the number of computing nodes reserved for the MPI execution (only a single node is reserved by default).        |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+

* @compss
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | Parameter              | Description                                                                                                                       |
    +========================+===================================================================================================================================+
    | **runcompss**          | (Mandatory) String defining the full path of the runcompss binary that must be executed.                                          |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | **flags**              | String defining the flags needed for the runcompss execution.                                                                     |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | **app_name**           | (Mandatory) String defining the application that must be executed.                                                                |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | **computing_nodes**    | Integer defining the number of computing nodes reserved for the COMPSs execution (only a single node is reserved by default).     |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+

* @multinode
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | Parameter              | Description                                                                                                                       |
    +========================+===================================================================================================================================+
    | **computing_nodes**    | Integer defining the number of computing nodes reserved for the task execution (only a single node is reserved by default).       |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+

* @reduction
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | Parameter              | Description                                                                                                                       |
    +========================+===================================================================================================================================+
    | **chunk_size**         |  Size of data fragments to be given as input parameter to the reduction function.                                                 |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+

* @container
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | Parameter              | Description                                                                                                                       |
    +========================+===================================================================================================================================+
    | **engine**             |  Container engine to use (e.g. DOCKER).                                                                                           |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | **image**              |  Container image to be deployed and used for the task execution.                                                                  |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+

In addition to the parameters that can be used within the
*@task* decorator, :numref:`supported_streams`
summarizes the *StdIOStream* parameter that can be used within the
*@task* decorator for the function parameters when using the
@binary, @ompss and @mpi decorators. In
particular, the *StdIOStream* parameter is used to indicate that a parameter
is going to be considered as a *FILE* but as a stream (e.g. :math:`>`,
:math:`<` and :math:`2>` in bash) for the @binary,
@ompss and @mpi calls.

.. table:: Supported StdIOStreams for the @binary, @ompss and @mpi decorators
    :name: supported_streams

    +------------------------+-------------------+
    | Parameter              | Description       |
    +========================+===================+
    | **(default: empty)**   | Not a stream.     |
    +------------------------+-------------------+
    | **STDIN**              | Standard input.   |
    +------------------------+-------------------+
    | **STDOUT**             | Standard output.  |
    +------------------------+-------------------+
    | **STDERR**             | Standard error.   |
    +------------------------+-------------------+

Moreover, there are some shorcuts that can be used for files type
definition as parameters within the *@task* decorator (:numref:`file_parameter_definition`).
It is not necessary to indicate the *Direction* nor the *StdIOStream* since it may be already be indicated with
the shorcut.

.. table:: File parameters definition shortcuts
    :name: file_parameter_definition

    +-----------------------------+---------------------------------------------------------+
    | Alias                       | Description                                             |
    +=============================+=========================================================+
    | **COLLECTION(_IN)**         | Type: COLLECTION, Direction: IN                         |
    +-----------------------------+---------------------------------------------------------+
    | **COLLECTION_INOUT**        | Type: COLLECTION, Direction: INOUT                      |
    +-----------------------------+---------------------------------------------------------+
    | **COLLECTION_OUT**          | Type: COLLECTION, Direction: OUT                        |
    +-----------------------------+---------------------------------------------------------+
    | **COLLECTION_FILE(_IN)**    | Type: COLLECTION (File), Direction: IN                  |
    +-----------------------------+---------------------------------------------------------+
    | **COLLECTION_FILE_INOUT**   | Type: COLLECTION (File), Direction: INOUT               |
    +-----------------------------+---------------------------------------------------------+
    | **COLLECTION_FILE_OUT**     | Type: COLLECTION (File), Direction: OUT                 |
    +-----------------------------+---------------------------------------------------------+
    | **FILE(_IN)_STDIN**         | Type: File, Direction: IN, StdIOStream: STDIN           |
    +-----------------------------+---------------------------------------------------------+
    | **FILE(_IN)_STDOUT**        | Type: File, Direction: IN, StdIOStream: STDOUT          |
    +-----------------------------+---------------------------------------------------------+
    | **FILE(_IN)_STDERR**        | Type: File, Direction: IN, StdIOStream: STDERR          |
    +-----------------------------+---------------------------------------------------------+
    | **FILE_OUT_STDIN**          | Type: File, Direction: OUT, StdIOStream: STDIN          |
    +-----------------------------+---------------------------------------------------------+
    | **FILE_OUT_STDOUT**         | Type: File, Direction: OUT, StdIOStream: STDOUT         |
    +-----------------------------+---------------------------------------------------------+
    | **FILE_OUT_STDERR**         | Type: File, Direction: OUT, StdIOStream: STDERR         |
    +-----------------------------+---------------------------------------------------------+
    | **FILE_INOUT_STDIN**        | Type: File, Direction: INOUT, StdIOStream: STDIN        |
    +-----------------------------+---------------------------------------------------------+
    | **FILE_INOUT_STDOUT**       | Type: File, Direction: INOUT, StdIOStream: STDOUT       |
    +-----------------------------+---------------------------------------------------------+
    | **FILE_INOUT_STDERR**       | Type: File, Direction: INOUT, StdIOStream: STDERR       |
    +-----------------------------+---------------------------------------------------------+
    | **FILE_CONCURRENT**         | Type: File, Direction: CONCURRENT                       |
    +-----------------------------+---------------------------------------------------------+
    | **FILE_CONCURRENT_STDIN**   | Type: File, Direction: CONCURRENT, StdIOStream: STDIN   |
    +-----------------------------+---------------------------------------------------------+
    | **FILE_CONCURRENT_STDOUT**  | Type: File, Direction: CONCURRENT, StdIOStream: STDOUT  |
    +-----------------------------+---------------------------------------------------------+
    | **FILE_CONCURRENT_STDERR**  | Type: File, Direction: CONCURRENT, StdIOStream: STDERR  |
    +-----------------------------+---------------------------------------------------------+
    | **FILE_CONMUTATIVE**        | Type: File, Direction: CONMUTATIVE                      |
    +-----------------------------+---------------------------------------------------------+
    | **FILE_CONMUTATIVE_STDIN**  | Type: File, Direction: CONMUTATIVE, StdIOStream: STDIN  |
    +-----------------------------+---------------------------------------------------------+
    | **FILE_CONMUTATIVE_STDOUT** | Type: File, Direction: CONMUTATIVE, StdIOStream: STDOUT |
    +-----------------------------+---------------------------------------------------------+
    | **FILE_CONMUTATIVE_STDERR** | Type: File, Direction: CONMUTATIVE, StdIOStream: STDERR |
    +-----------------------------+---------------------------------------------------------+

These parameter keys, as well as the shortcuts, can be imported from the
PyCOMPSs library:

.. code-block:: python

    from pycompss.api.parameter import *


Task Constraints
~~~~~~~~~~~~~~~~

It is possible to define constraints for each task.
To this end, the decorator *@constraint* followed
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
A full description of the supported constraints can be found in :numref:`supported_constraints`.

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

Multiple Task Implementations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As in Java COMPSs applications, it is possible to define multiple
implementations for each task. In particular, a programmer can define a
task for a particular purpose, and multiple implementations for that
task with the same objective, but with different constraints (e.g.
specific libraries, hardware, etc). To this end, the *@implement*
decorator followed with the specific implementations constraints (with
the *@constraint* decorator, see Section [subsubsec:constraints]) needs
to be placed ON TOP of the @task decorator. Although the user only
calls the task that is not decorated with the *@implement* decorator,
when the application is executed in a heterogeneous distributed
environment, the runtime will take into account the constraints on each
implementation and will try to invoke the implementation that fulfills
the constraints within each resource, keeping this management invisible
to the user (:numref:`implements_python`).

.. code-block:: python
    :name: implements_python
    :caption: Multiple task implementations example

    from pycompss.api.implement import implement

    @implement(source_class="sourcemodule", method="main_func")
    @constraint(app_software="numpy")
    @task(returns=list)
    def myfunctionWithNumpy(list1, list2):
        # Operate with the lists using numpy
        return resultList

    @task(returns=list)
    def main_func(list1, list2):
        # Operate with the lists using built-int functions
        return resultList

Please, note that if the implementation is used to define a binary,
OmpSs, MPI, COMPSs, multinode or reduction task invocation (see
:ref:`Sections/02_App_Development/02_Python/01_Programming_model:Other task types`),
the @implement decorator must be always on top of the decorators stack,
followed by the @constraint decorator, then the
@binary/\ @ompss/\ @mpi/\ @compss/\ @multinode
decorator, and finally, the @task decorator in the lowest
level.


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

compss_wait_on_file(file_name)
   Synchronizes for the last version of the file *file_name*.
   Returns True if success (False otherwise).

compss_wait_on_directory(directory_name)
   Synchronizes for the last version of the directory *directory_name*.
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
   See :ref:`Sections/02_App_Development/02_Python/01_Programming_model:Task Groups`
   for more information about task groups.

compss_wait_on(obj, to_write=True)
   Synchronizes for the last version of object *obj* and returns the synchronized object.
   It can have an optional boolean parameter *to_write*, which defaults to
   *True*, that indicates whether the main program will modify the
   returned object. It is possible to wait on a list of objects. In this
   particular case, it will synchronize all future objects contained in
   the list.


To illustrate the use of the aforementioned API functions, the following
example (:numref:`api_usage_python`) first invokes a task *func* that writes a
file, which is later synchronized by calling *compss_open()*.
Later in the program, an object of class *MyClass* is created and a task method
*method* that modifies the object is invoked on it; the object is then
synchronized with *compss_wait_on()*, so that it can be used in the main
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

    @task(returns=list)
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

compss_delete_file(file_name)
 Notifies the runtime to delete a file.

compss_delete_object(object)
  Notifies the runtime to delete all the associated files to a given object.


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
*TaskGroup* context (:numref:`task_group`) which can be tuned with the group name, and a second parameter (boolean) to
perform an implicit barrier for the whole group. Users can also define
task groups within task groups.

TaskGroup(group_name, implicit_barrier=True)
   Python context to define a group of tasks. All tasks submitted within the
   context will belong to *group_name* context and are sensitive to wait for
   them while the rest are being executed. Tasks groups are depicted within
   a box into the generated task dependency graph.


.. code-block:: python
    :name: task_group
    :caption: PyCOMPSs Task group definiton

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
        with TaskGroup('Group1', False):
            for i in range(NUM_TASKS):
                func1()
                func2()
            ...
        ...
        compss_barrier_group('Group1')
        ...

    if __name__=='__main__':
        test_taskgroup()


Other
^^^^^

PyCOMPSs also provides other function within its API to check if a file exists.

compss_file_exists(file_name)
 Checks if a file exists. If it does not exist, the function checks
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
    |                 | compss_wait_on_file(file_name)               | Synchronizes for the last version of a file.                                            |
    |                 +----------------------------------------------+-----------------------------------------------------------------------------------------+
    |                 | compss_wait_on_directory(directory_name)     | Synchronizes for the last version of a directory.                                       |
    |                 +----------------------------------------------+-----------------------------------------------------------------------------------------+
    |                 | compss_barrier(no_more_tasks=False)          | Wait for all tasks submitted before the barrier.                                        |
    |                 +----------------------------------------------+-----------------------------------------------------------------------------------------+
    |                 | compss_barrier_group(group_name)             | Wait for all tasks that belong to *group_name* group submitted before the barrier.      |
    |                 +----------------------------------------------+-----------------------------------------------------------------------------------------+
    |                 | compss_wait_on(obj, to_write=True)           | Synchronizes for the last version of an object (or a list of objects) and returns it.   |
    +-----------------+----------------------------------------------+-----------------------------------------------------------------------------------------+
    | File/Object     | compss_file_exists(file_name)                | Check if a file exists.                                                                 |
    | deletion        +----------------------------------------------+-----------------------------------------------------------------------------------------+
    |                 | compss_delete_file(file_name)                | Notifies the runtime to remove a file.                                                  |
    |                 +----------------------------------------------+-----------------------------------------------------------------------------------------+
    |                 | compss_delete_object(object)                 | Notifies the runtime to delete the associated file to this object.                      |
    +-----------------+----------------------------------------------+-----------------------------------------------------------------------------------------+
    | Task Groups     | TaskGroup(group_name, implicit_barrier=True) | Context to define a group of tasks. *implicit_barrier* forces waiting on context exit.  |
    +-----------------+----------------------------------------------+-----------------------------------------------------------------------------------------+
    | Other           | compss_file_exists(file_name)                | Check if a file exists.                                                                 |
    +-----------------+----------------------------------------------+-----------------------------------------------------------------------------------------+



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
