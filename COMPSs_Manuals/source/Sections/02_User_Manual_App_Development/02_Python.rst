Python Binding
==============

COMPSs features a binding for Python 2 and 3 applications. The next
subsections explain how to program a Python application for COMPSs and a
brief overview on how to execute it.

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
a *@task* decorator that describes the task before the
definition of the function/method.

As an example (:numref:`code_python`), let us assume that the application calls a function
*func*, which receives a file path (string parameter) and an integer
parameter. The code of *func* updates the file.

.. code-block:: python
    :name: code_python
    :caption: Python application example

    def func(file_path, value):
        # update the file 'file_path'

    if __name__=='__main__':
        my_file = '/tmp/sample_file.txt'
        func(my_file, 1)

.. hint::

   The main code is defined within *if __name__==__main__'*.
   A better performance alternative would be to define the main code within a function
   and invoke it from the *if __name__=='__main__'*:

   .. code-block:: python

       def func(file_path, value):
           # update the file 'file_path'

       def main():
           my_file = '/tmp/sample_file.txt'
           func(my_file, 1)

       if __name__=='__main__':
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

The metadata corresponding to a parameter is specified as an argument of
the decorator, whose name is the formal parameter’s name and whose value
defines the type and direction of the parameter. The parameter types and
directions can be:

-  Types: *primitive types* (integer, long, float, boolean), *strings*,
   *objects* (instances of user-defined classes, dictionaries, lists,
   tuples, complex numbers) and *files* are supported.

-  Direction: it can be read-only (*IN* - default), read-write
   (*INOUT*), write-only (*OUT*) or in some cases concurrent
   (*CONCURRENT*).

COMPSs is able to automatically infer the parameter type for primitive
types, strings and objects, while the user needs to specify it for
files. On the other hand, the direction is only mandatory for *INOUT*
and *OUT* parameters. Thus, when defining the parameter metadata in the
*@task* decorator, the user has the following options:

-  *IN*: the parameter is read-only. The type will be inferred.

-  *INOUT*: the parameter is read-write. The type will be inferred.

-  *OUT*: the parameter is write-only. The type will be inferred.

-  *CONCURRENT*: the parameter is read-write with concurrent access. The
   type will be inferred.

-  *CONMUTATIVE*: the parameter is read-write with conmutative access. The
   type will be inferred.

-  *FILE/FILE_IN*: the parameter is a file. The direction is assumed to
   be *IN*.

-  *FILE_INOUT*: the parameter is a read-write file.

-  *FILE_OUT*: the parameter is a write-only file.

-  *DIRECTORY_IN*: the parameter is a directory and the direction is *IN*. In this
   case the directory will be compressed before any transfer amongst nodes.

-  *DIRECTORY_INOUT*: the parameter is a read-write directory.

-  *DIRECTORY_OUT*: the parameter is a write-only directory.

-  *FILE_CONCURRENT*: the parameter is a concurrent read-write file.

-  *FILE_CONMUTATIVE*: the parameter is a conmutative read-write file.

-  *COLLECTION_IN*: the parameter is read-only collection.

-  *COLLECTION_INOUT*: the parameter is read-write collection.

-  *COLLECTION_OUT*: the parameter is write-only collection.

-  *COLLECTION_FILE/COLLECTION_FILE_IN*: the parameter is read-only collection of files.

-  *COLLECTION_FILE_INOUT*: the parameter is read-write collection of files.

-  *COLLECTION_FILE_OUT*: the parameter is write-only collection of files.


Consequently, please note that in the following cases there is no need
to include an argument in the *@task* decorator for a given
task parameter:

-  Parameters of primitive types (integer, long, float, boolean) and
   strings: the type of these parameters can be automatically inferred
   by COMPSs, and their direction is always *IN*.

-  Read-only object parameters: the type of the parameter is
   automatically inferred, and the direction defaults to *IN*.

The parameter metadata is available from the *pycompss* library (:numref:`parameter_import_python`)

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
    :caption: Python task example

    from pycompss.api.task import task     # Import @task decorator
    from pycompss.api.parameter import *   # Import parameter metadata for the @task decorator

    @task(f=FILE_INOUT)
    def func(f, i):
         fd = open(f, 'r+')
         ...

The user can also define that the access to a parameter is concurrent
with *CONCURRENT* or to a file *FILE_CONCURRENT* (:numref:`task_concurrent_python`). Tasks that share a
"CONCURRENT" parameter will be executed in parallel, if any other
dependency prevents this. The CONCURRENT direction allows users to have
access from multiple tasks to the same object/file during their
executions. However, note that COMPSs does not manage the interaction
with the objects or files used/modified concurrently. Taking care of the
access/modification of the concurrent objects is responsibility of the
developer.

.. code-block:: python
    :name: task_concurrent_python
    :caption: Python task example with CONCURRENT

    from pycompss.api.task import task     # Import @task decorator
    from pycompss.api.parameter import *   # Import parameter metadata for the @task decorator

    @task(f=FILE_CONCURRENT)
    def func(f, i):
         ...

In addition, the user can also define that the access to a parameter is conmutative
with *CONMUTATIVE* or to a file *FILE_CONMUTATIVE* (:numref:`task_conmutative_python`).
The execution order of tasks that share a "CONMUTATIVE" parameter can be changed
by the runtime following the conmutative property.

.. code-block:: python
    :name: task_conmutative_python
    :caption: Python task example with CONMUTATIVE

    from pycompss.api.task import task     # Import @task decorator
    from pycompss.api.parameter import *   # Import parameter metadata for the @task decorator

    @task(f=FILE_CONMUTATIVE)
    def func(f, i):
         ...

Moreover, it is possible to specify that a parameter is a collection of
elements (e.g. list) and its direction (COLLECTION_IN or
COLLECTION_INOUT) (:numref:`task_collection_python`). In this case, the list may contain sub-objects that
will be handled automatically by the runtime. It is important to
annotate data structures as collections if in other tasks there are
accesses to individual elements of these collections as parameters.
Without this annotation, the runtime will not be able to identify data
dependences between the collections and the individual elements.

.. code-block:: python
    :name: task_collection_python
    :caption: Python task example with COLLECTION

    from pycompss.api.task import task    # Import @task decorator
    from pycompss.api.parameter import *  # Import parameter metadata for the @task decorator

    @task(my_collection=COLLECTION_IN)
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
    :caption: Python task example with COLLECTION and depth

    @task(my_collection={Type:COLLECTION_IN, Depth:2})
    def func(my_collection):
         for inner_collection in my_collection:
             for element in inner_collection:
                 # The contents of element will not be tracked
                 ...

If the function or method returns a value, the programmer must use the
*returns* argument within the *@task* decorator. In this
argument, the programmer can specify the type of that value (:numref:`task_returns_python`).

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
an integer value (:numref:`task_returns_integer_python`). This way of specifying the amount of return eases the
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

The use of *\*args* and *\*\*kwargs* as function parameters is also
supported (:numref:`task_args_kwargs_python`).

.. code-block:: python
    :name: task_args_kwargs_python
    :caption: Python task *\*args* and *\*\*kwargs example*

    @task(returns=int)
    def argkwarg_func(*args, **kwargs):
        return sum(args) + len(kwargs)

And even with other parameters, such as usual parameters and *default
defined arguments*. :numref:`task_default_parameters_python` shows an example of a task with two
three parameters (whose one of them (*’s’*) has a default value), *\*args*
and *\*\*kwargs*.

.. code-block:: python
    :name: task_default_parameters_python
    :caption: Python task with default parameters example

    @task(returns=int)
    def multiarguments_func(v, w, s = 2, *args, **kwargs):
        return (v * w) + sum(args) + len(kwargs) + s

For tasks corresponding to instance methods, by default the task is
assumed to modify the callee object (the object on which the method is
invoked). The programmer can tell otherwise by setting the
*target_direction* argument of the *@task* decorator to *IN* (:numref:`task_instance_method_python`).

.. code-block:: python
    :name: task_instance_method_python
    :caption: Python instance method example

    class MyClass(object):
        ...
        @task(target_direction=IN)
        def instance_method(self):
            ... # self is NOT modified here

.. caution::
   In order to avoid serialization issues, the classes must not
   be declared in the same file that contains the main method (``if __name__=='__main__'``).


The user is also able to define the time out of a task within the ``@task`` decorator
with the ``time_out=<TIME_IN_SECONDS>`` hint.
The runtime will cancel the task if the time to execute the task exceeds the time defined by the user.
For example, :numref:`task_time_out` shows how to specify that the ``unknown_duration_task``
maximum duration before canceling (if exceeded) is one hour.

.. code-block:: python
    :name: task_time_out
    :caption: Python tasl time out example

    @task(time_out=3600)
    def unknown_duration_task(self):
        ...

Scheduler hints
^^^^^^^^^^^^^^^

The programmer can provide hints to the scheduler through specific
arguments within the *@task* decorator.

For instance, the programmer can mark a task as a high-priority task
with the *priority* argument of the *@task* decorator (:numref:`task_priority_python`). In this
way, when the task is free of dependencies, it will be scheduled before
any of the available low-priority (regular) tasks. This functionality is
useful for tasks that are in the critical path of the application’s task
dependency graph.

.. code-block:: python
    :name: task_priority_python
    :caption: Python task priority example

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
    :caption: Python task is_distributed and is_replicated examples

    @task(is_distributed=True)
    def func():
        ...

    @task(is_replicated=True)
    def func2():
        ...

In case a task fails, the whole application behaviour can be defined
using the *on_failure* argument (:numref:`task_on_failure_python`).
It has four possible values: **'RETRY'**,
**’CANCEL_SUCCESSORS’**, **’FAIL’** and **’IGNORE’**. *’RETRY’* is the default
behaviour, making the task to be executed again, on the same worker or
in another worker if the failure remains. *’CANCEL_SUCCESSORS’* ignores
the failed task and cancels the execution of the successor tasks, *’FAIL’*
stops the whole execution once a task fails and *’IGNORE’* ignores the
failure and continues with the normal execution.

.. code-block:: python
    :name: task_on_failure_python
    :caption: Python task on_failure example

    @task(on_failure='CANCEL_SUCCESSORS')
    def func():
        ...

:numref:`task_arguments` summarizes the arguments that can be found in the *@task* decorator.

.. table:: Arguments of the *@task* decorator
    :name: task_arguments
    :widths: auto

    +---------------------+---------------------------------------------------------------------------------------------------------+
    | Argument            | Value                                                                                                   |
    +=====================+=========================================================================================================+
    | Formal parameter    | - **(default: empty)** The parameter is an object or a simple tipe that will be inferred.               |
    | name                | - IN: Read-only parameter, all types.                                                                   |
    |                     | - INOUT: Read-write parameter, all types except file (primitives, strings, objects).                    |
    |                     | - OUT: Write-only parameter, all types except file (primitives, strings, objects).                      |
    |                     | - CONCURRENT: Concurrent read-write parameter, all types except file (primitives, strings, objects).    |
    |                     | - CONMUTATIVE: Conmutative read-write parameter, all types except file (primitives, strings, objects).  |
    |                     | - FILE/FILE_IN: Read-only file parameter.                                                               |
    |                     | - FILE_INOUT: Read-write file parameter.                                                                |
    |                     | - FILE_OUT: Write-only file parameter.                                                                  |
    |                     | - FILE_CONCURRENT: Concurrent read-write file parameter.                                                |
    |                     | - FILE_CONMUTATIVE: Conmutative read-write file parameter.                                                |
    |                     | - DIRECTORY_IN: the parameter is a read-only directory.                                                 |
    |                     | - DIRECTORY_INOUT: the parameter is a read-write directory.                                             |
    |                     | - DIRECTORY_OUT: the parameter is a write-only directory.                                               |
    |                     | - COLLECTION_IN: Read-only collection parameter (list).                                                 |
    |                     | - COLLECTION_INOUT: Read-write collection parameter (list).                                             |
    |                     | - COLLECTION_OUT: Read-only collection parameter (list).                                                |
    |                     | - COLLECTION_FILE/COLLECTION_FILE_IN: Read-only collection of files parameter (list of files).          |
    |                     | - COLLECTION_FILE_INOUT: Read-write collection of files parameter (list of files).                      |
    |                     | - COLLECTION_FILE_OUT: Read-only collection of files parameter (list opf files).                        |
    |                     | - Dictionary: {Type:(empty=object)/FILE/COLLECTION, Direction:(empty=IN)/IN/INOUT/OUT/CONCURRENT}       |
    +---------------------+---------------------------------------------------------------------------------------------------------+
    | returns             | int (for integer and boolean), long, float, str, dict, list, tuple, user-defined classes                |
    +---------------------+---------------------------------------------------------------------------------------------------------+
    | target_direction    | INOUT (default), IN or CONCURRENT                                                                       |
    +---------------------+---------------------------------------------------------------------------------------------------------+
    | priority            | True or False (default)                                                                                 |
    +---------------------+---------------------------------------------------------------------------------------------------------+
    | is_distributed      | True or False (default)                                                                                 |
    +---------------------+---------------------------------------------------------------------------------------------------------+
    | is_replicated       | True or False (default)                                                                                 |
    +---------------------+---------------------------------------------------------------------------------------------------------+
    | on_failure          | ’RETRY’ (default), ’CANCEL_SUCCESSORS’, ’FAIL’ or ’IGNORE’                                              |
    +---------------------+---------------------------------------------------------------------------------------------------------+
    | time_out            | int (time in seconds)                                                                                   |
    +---------------------+---------------------------------------------------------------------------------------------------------+


Other task types
^^^^^^^^^^^^^^^^

In addition to this API functions, the programmer can use a set of
decorators for other purposes.

For instance, there is a set of decorators that can be placed over the
*@task* decorator in order to define the task methods as a
**binary invocation** (with the :ref:`Binary decorator`), as a **OmpSs
invocation** (with the :ref:`OmpSs decorator`), as a **MPI invocation**
(with the :ref:`MPI decorator`), as a **COMPSs application** (with the
:ref:`COMPSs decorator`), or as a **task that requires multiple
nodes** (with the :ref:`Multinode decorator`). These decorators must
be placed over the *@task* decorator, and under the
*@constraint* decorator if defined.

Consequently, the task body will be empty and the function parameters
will be used as invocation parameters with some extra information that
can be provided within the *@task* decorator.

The following subparagraphs describe their usage.

Binary decorator
''''''''''''''''

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

OmpSs decorator
'''''''''''''''

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
check :ref:`Binary decorator` for more details.

MPI decorator
'''''''''''''

The *@mpi* decorator shall be used to define that a task is
going to invoke a MPI executable (:numref:`mpi_task_python`).

.. code-block:: python
    :name: mpi_task_python
    :caption: MPI task example

    from pycompss.api.mpi import mpi

    @mpi(binary="mpiApp.bin", runner="mpirun", computing_nodes=2)
    @task()
    def mpi_func():
         pass

The MPI executable invocation can also be enriched with parameters,
files and prefixes as with the *@binary* decorator through the
function parameters and *@task* decorator information. Please,
check :ref:`Binary decorator` for more details.

COMPSs decorator
''''''''''''''''

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
'''''''''''''''''''

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

Parameters summary
''''''''''''''''''

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
    | **binary**             | (Mandatory) String defining the full path of the binary that must be executed.                                                    |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | **working_dir**        | Full path of the binary working directory inside the COMPSs Worker.                                                               |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | **runner**             | (Mandatory) String defining the MPI runner command.                                                                               |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | **computing_nodes**    | Integer defining the number of computing nodes reserved for the MPI execution (only a single node is reserved by default).        |
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
    :widths: auto

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
    :widths: auto

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

Constraints
~~~~~~~~~~~

As in Java COMPSs applications, it is possible to define constraints for
each task. To this end, the decorator *@constraint* followed
by the desired constraints needs to be placed ON TOP of the @task
decorator (:numref:`constraint_task_python`). Please note the the order of @constraint and @task decorators is important.

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

Implements
~~~~~~~~~~

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
OmpSs, MPI, COMPSs or multinode task invocation (see :ref:`Other task types`), the @implement decorator must be
always on top of the decorators stack, followed by the
@constraint decorator, then the
@binary/\ @ompss/\ @mpi/\ @compss/\ @multinode
decorator, and finally, the @task decorator in the lowest
level.


Main Program
~~~~~~~~~~~~

The main program of the application is a sequential code that contains
calls to the selected tasks. In addition, when synchronizing for task
data from the main program, there exist seven API functions that can to
be invoked:

compss_file_exists(file_name)
   Check if a file exists. If it does not exist, it check
   if file has been accessed before by calling the runtime.

compss_open(file_name, mode=’r’)
   Similar to the Python *open()* call.
   It synchronizes for the last version of file *file_name* and
   returns the file descriptor for that synchronized file. It can have
   an optional parameter *mode*, which defaults to ’\ *r*\ ’, containing
   the mode in which the file will be opened (the open modes are
   analogous to those of Python *open()*).

compss_delete_file(file_name)
   Notifies the runtime to delete a file.

compss_wait_on_file(file_name)
   Synchronizes for the last version of the file *file_name*.
   Returns True if success (False otherwise).

compss_delete_object(object)
   Notifies the runtime to delete all the associated files to a given object.

compss_barrier(no_more_tasks=False)
   Performs a explicit synchronization, but does not return any object.
   The use of *compss_barrier()* forces to wait for all tasks that have been
   submitted before the *compss_barrier()* is called. When all tasks
   submitted before the *compss_barrier()* have finished, the execution
   continues. The *no_more_tasks* is used to specify if no more tasks
   are going to be submitted after the *compss_barrier()*.

compss_wait_on(obj, to_write=True)
   Synchronizes for the last version of object *obj* and returns the synchronized object.
   It can have an optional boolean parameter *to_write*, which defaults to
   *True*, that indicates whether the main program will modify the
   returned object. It is possible to wait on a list of objects. In this
   particular case, it will synchronize all future objects contained in
   the list.

To illustrate the use of the aforementioned API functions, the following
example (:numref:`api_usage_python`) first invokes a task *func* that writes a file, which is later
synchronized by calling *compss_open()*. Later in the program, an
object of class *MyClass* is created and a task method *method* that
modifies the object is invoked on it; the object is then synchronized
with *compss_wait_on()*, so that it can be used in the main program
from that point on.

Then, a loop calls again ten times to *func* task. Afterwards, the
barrier performs a synchronization, and the execution of the main user
code will not continue until the ten *func* tasks have finished.

.. code-block:: python
    :name: api_usage_python
    :caption: PyCOMPSs API usage

    from pycompss.api.api import compss_file_exists
    from pycompss.api.api import compss_open
    from pycompss.api.api import compss_delete_file
    from pycompss.api.api import compss_delete_object
    from pycompss.api.api import compss_wait_on
    from pycompss.api.api import compss_wait_on_file
    from pycompss.api.api import compss_barrier

    if __name__=='__main__':
        my_file = 'file.txt'
        func(my_file)
        if compss_file_exists(my_file):
            print("Exists")
        else:
            print("Not exists")
        ...
        fd = compss_open(my_file)
        ...

        my_file2 = 'file2.txt'
        func(my_file2)
        compss_delete_file(my_file2)
        ...

        my_file3 = 'file3.txt'
        func(my_file3)
        compss_wait_on_file(my_file3)
        ...

        my_obj1 = MyClass()
        my_obj1.method()
        compss_delete_object(my_obj1)
        ...

        my_obj2 = MyClass()
        my_obj2.method()
        my_obj2 = compss_wait_on(my_obj2)
        ...

        for i in range(10):
            func(str(i) + my_file)
        compss_barrier()
        ...

The corresponding task selection for the example above would be (:numref:`api_usage_tasks_python`):

.. code-block:: python
    :name: api_usage_tasks_python
    :caption: PyCOMPSs API usage tasks

    @task(f=FILE_OUT)
    def func(f):
        ...

    class MyClass(object):
        ...

        @task()
        def method(self):
            ... # self is modified here


COMPSs also enables to specify task groups. To this end, COMPSs provides the
*TaskGroup* context (:numref:`task_group`) which can be tuned with the group name, and a second parameter (boolean) to
perform an implicit barrier for the whole group. Users can also define
task groups within task groups.

.. code-block:: python
    :name: task_group
    :caption: PyCOMPSs Task group definiton

    @task()
    def func1():
        ...

    @task()
    def func2():
        ...

    def test_taskgroup():
        # Creation of group
        with TaskGroup('Group1', True):
            for i in range(NUM_TASKS):
                func1()
                func2()
            ...
        ...

    if __name__=='__main__':
        test_taskgroup()


:numref:`python_api_functions` summarizes the API functions to be
used in the main program of a COMPSs Python application.

.. table:: COMPSs Python API functions
    :name: python_api_functions
    :widths: auto

    +------------------------------------------+-----------------------------------------------------------------------------------------+
    | API Function                             | Description                                                                             |
    +==========================================+=========================================================================================+
    | compss_file_exists(file_name)            | Check if a file exists.                                                                 |
    +------------------------------------------+-----------------------------------------------------------------------------------------+
    | compss_open(file_name, mode=’r’)         | Synchronizes for the last version of a file and returns its file descriptor.            |
    +------------------------------------------+-----------------------------------------------------------------------------------------+
    | compss_delete_file(file_name)            | Notifies the runtime to remove a file.                                                  |
    +------------------------------------------+-----------------------------------------------------------------------------------------+
    | compss_wait_on_file(file_name)           | Synchronizes for the last version of a file.                                            |
    +------------------------------------------+-----------------------------------------------------------------------------------------+
    | compss_delete_object(object)             | Notifies the runtime to delete the associated file to this object.                      |
    +------------------------------------------+-----------------------------------------------------------------------------------------+
    | compss_barrier(no_more_tasks=False)      | Wait for all tasks submitted before the barrier.                                        |
    +------------------------------------------+-----------------------------------------------------------------------------------------+
    | compss_wait_on(obj, to_write=True)       | Synchronizes for the last version of an object (or a list of objects) and returns it.   |
    +------------------------------------------+-----------------------------------------------------------------------------------------+

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

Exceptions
~~~~~~~~~~

COMPSs is able to deal with exceptions raised during the execution of the
applications. In this case, if a user/python defined exception happens, the
user can choose the task behaviour using the *on_failure* argument within the
*@task* decorator (with four possible values: **'RETRY'**,
**’CANCEL_SUCCESSORS’**, **’FAIL’** and **’IGNORE’**. *’RETRY’* is the default
behaviour).

However, COMPSs provides an exception (``COMPSsException``) that the user can
raise when necessary and can be catched in the main code for user defined
behaviour management (:numref:`task_compss_exception`). This mechanism avoids
any synchronization, and enables applications to react under particular
circunstances.

.. code-block:: python
    :name: task_compss_exception
    :caption: COMPSs Exception example

    from pycompss.api.exceptions import COMPSsException

    @task()
    def func():
        ...
        raise COMPSsException("Something happened!")

    ...

    if __name__=='__main__':
        try:
            func()
        except COMPSsException:
            ...  # React to the exception (maybe calling other tasks or with other parameters)

In addition, the *COMPSsException* can be combined with task groups, so that
the tasks which belong to the group will also be cancelled as soon as the
*COMPSsException* is raised (:numref:`task_group_compss_exception`)

.. code-block:: python
    :name: task_group_compss_exception
    :caption: COMPSs Exception with task group example

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

Important Notes
~~~~~~~~~~~~~~~

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
        # o is a future object
        o = ret_func()

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

In order to synchronize the object from the main program, the programmer
has to synchronize (using the *compss_wait_on* function) in the same
way as with any object updated by a task (:numref:`task_return_value_synchronization_python`).

.. code-block:: python
    :name: task_return_value_synchronization_python
    :caption: Task return value synchronization

    if __name__=='__main__':
        # o is a future object
        o = ret_func()

        ...

        o = compss_wait_on(o)

Moreover, it is possible to synchronize a list of objects. This is
particularly useful when the programmer expect to synchronize more than
one elements (using the *compss_wait_on* function) (:numref:`list_synchronization_python`.
This feature also works with dictionaries, where the value of each entry
is synchronized.
In addition, if the structure synchronized is a combination of lists and
dictionaries, the *compss_wait_on* will look for all objects to be synchronized
in the whole structure.

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

    if __name__=='__main__':
        o = ret_func()

        # invoking a task instance method on a future object can only
        # be done when an empty constructor is defined in the object's
        # class
        o.yet_another_task()

In order to make the COMPSs Python binding function correctly, the
programmer should not use relative imports in the code. Relative imports
can lead to ambiguous code and they are discouraged in Python, as
explained in:
http://docs.python.org/2/faq/programming.html#what-are-the-best-practices-for-using-import-in-a-module

Application Execution
---------------------

The next subsections describe how to execute applications with the
COMPSs Python binding.

Environment
~~~~~~~~~~~

The following environment variables must be defined before executing a
COMPSs Python application:

JAVA_HOME
    Java JDK installation directory (e.g. */usr/lib/jvm/java-8-openjdk/*)

Command
~~~~~~~

In order to run a Python application with COMPSs, the runcompss script
can be used, like for Java and C/C++ applications. An example of an
invocation of the script is:

.. code-block:: console

    compss@bsc:~$ runcompss \
                    --lang=python \
                    --pythonpath=$TEST_DIR \
                    --library_path=/home/user/libdir \
                    $TEST_DIR/test.py arg1 arg2

Or alternatively, use the ``pycompss`` module:

.. code-block:: console

    compss@bsc:~$ python -m pycompss \
                    --pythonpath=$TEST_DIR \
                    --library_path=/home/user/libdir \
                    $TEST_DIR/test.py arg1 arg2

For full description about the options available for the runcompss
command please check the :ref:`Application execution` Section.

Development with Jupyter notebook
---------------------------------

PyCOMPSs can also be used within Jupyter notebooks. This feature allows
users to develop and run their PyCOMPSs applications in a Jupyter
notebook, where it is possible to modify the code during the execution
and experience an interactive behaviour.

Environment
~~~~~~~~~~~

The following libraries must be present in the appropiate environment
variables in order to enable PyCOMPSs within Jupyter notebook:

PYTHONPATH
    The path where PyCOMPSs is installed (e.g. */opt/COMPSs/Bindings/python/*)

LD_LIBRARY_PATH
    The path where the *libbindings-commons.so* library is located
    (e.g. */opt/COMPSs/Bindings/bindings-common/lib/*) and the path
    where the *libjvm.so* library is located (e.g.
    */usr/lib/jvm/java-8-openjdk/jre/lib/amd64/server/*).

API calls
~~~~~~~~~

In this case, the user is responsible of starting and stopping the
COMPSs runtime. To this end, PyCOMPSs provides a module that provides
two API calls: one for starting the COMPSs runtime, and another for
stopping it.

This module can be imported from the *pycompss* library:

.. code-block:: python

    import pycompss.interactive as ipycompss

And contains two main functions: *start* and *stop*. These functions can
then be invoked as follows for the COMPSs runtime deployment with
default parameters:

.. code-block:: python

    # Previous user code

    ipycompss.start()

    # User code that can benefit from PyCOMPSs

    ipycompss.stop()

    # Subsequent code

Between the *start* and *stop* function calls, the user can write its
own python code including PyCOMPSs imports, decorators and
synchronization calls described in Section
[subsec:Python_programming_model]. The code can be splitted into
multiple cells.

The *start* and *stop* functions accept parameters in order to customize
the COMPSs runtime (such as the flags that can be selected with the
"runcompss" command). Table :numref:`start_jupyter` summarizes
the accepted parameters of the *start* function. :numref:`stop_jupyter`
summarizes the accepted parameters of
the *stop* function.


.. table:: PyCOMPSs **start** function for Jupyter notebook
    :name: start_jupyter
    :widths: auto

    +-----------------------------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Parameter Name                    | Parameter Type | Description                                                                                                                                                                                                                                                                                                                                                    |
    +===================================+================+================================================================================================================================================================================================================================================================================================================================================================+
    | log_level                         | String         | Log level. Options: "off", "info" and "debug". (Default: "off")                                                                                                                                                                                                                                                                                                |
    +-----------------------------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | debug                             | Boolean        | COMPSs runtime debug (Default: False) (overrides log level)                                                                                                                                                                                                                                                                                                    |
    +-----------------------------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | o_c                               | Boolean        | Object conversion to string when possible (Default: False)                                                                                                                                                                                                                                                                                                     |
    +-----------------------------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | graph                             | Boolean        | Task dependency graph generation (Default: False)                                                                                                                                                                                                                                                                                                              |
    +-----------------------------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | trace                             | Boolean        | Paraver trace generation (Default: False)                                                                                                                                                                                                                                                                                                                      |
    +-----------------------------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | monitor                           | Integer        | Monitor refresh rate (Default: None - Monitoring disabled)                                                                                                                                                                                                                                                                                                     |
    +-----------------------------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | project_xml                       | String         | Path to the project XML file (Default: $COMPSS/Runtime/configuration/xml/projects/default project.xml)                                                                                                                                                                                                                                                         |
    +-----------------------------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | resources_xml                     | String         | Path to the resources XML file (Default: $COMPSs/Runtime/configuration/xml/resources/default resources.xml)                                                                                                                                                                                                                                                    |
    +-----------------------------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | summary                           | Boolean        | Show summary at the end of the execution (Default: False)                                                                                                                                                                                                                                                                                                      |
    +-----------------------------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | storage_impl                      | String         | Path to an storage implementation (Default: None)                                                                                                                                                                                                                                                                                                              |
    +-----------------------------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | storage_conf                      | String         | Storage configuration file path (Default: None)                                                                                                                                                                                                                                                                                                                |
    +-----------------------------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | task_count                        | Integer        | Number of task definitions (Default: 50)                                                                                                                                                                                                                                                                                                                       |
    +-----------------------------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | app_name                          | String         | Application name (Default: "Interactive")                                                                                                                                                                                                                                                                                                                      |
    +-----------------------------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | uuid                              | String         | Application uuid (Default: None - Will be random)                                                                                                                                                                                                                                                                                                              |
    +-----------------------------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | base_log_dir                      | String         | Base directory to store COMPSs log files (a .COMPSs/ folder will be created inside this location) (Default: User homeBase log path)                                                                                                                                                                                                                            |
    +-----------------------------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | specific_log_dir                  | String         | Use a specific directory to store COMPSs log files (the folder MUST exist and no sandbox is created) (Default: Disabled)                                                                                                                                                                                                                                       |
    +-----------------------------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | extrae_cfg                        | String         | Sets a custom extrae config file. Must be in a shared disk between all COMPSs workers (Default: None)                                                                                                                                                                                                                                                          |
    +-----------------------------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | comm                              | String         | Class that implements the adaptor for communications. Supported adaptors: "es.bsc.compss.nio.master.NIOAdaptor" and "es.bsc.compss.gat.master.GATAdaptor" (Default: "es.bsc.compss.nio.master.NIOAdaptor")                                                                                                                                                     |
    +-----------------------------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | conn                              | String         | Class that implements the runtime connector for the cloud. Supported connectors: "es.bsc.compss.connectors.DefaultSSHConnector" and "es.bsc.compss.connectors.DefaultNoSSHConnector" (Default: es.bsc.compss.connectors.DefaultSSHConnector)                                                                                                                   |
    +-----------------------------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | master_name                       | String         | Hostname of the node to run the COMPSs master (Default: "")                                                                                                                                                                                                                                                                                                    |
    +-----------------------------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | master_port                       | String         | Port to run the COMPSs master communications. Only for NIO adaptor (Default: "[43000,44000]")                                                                                                                                                                                                                                                                  |
    +-----------------------------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | scheduler                         | String         | Class that implements the Scheduler for COMPSs. Supported schedulers: "es.bsc.compss.scheduler.fullGraphScheduler.FullGraphScheduler", "es.bsc.compss.scheduler.fifoScheduler.FIFOScheduler" and "es.bsc.compss.scheduler.resourceEmptyScheduler. ResourceEmptyScheduler" (Default: "es.bsc.compss.scheduler.loadBalancingScheduler.LoadBalancingScheduler")   |
    +-----------------------------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | jvm_workers                       | String         | Extra options for the COMPSs Workers JVMs. Each option separed by "," and without blank spaces (Default: "-Xms1024m,-Xmx1024m,-Xmn400m")                                                                                                                                                                                                                       |
    +-----------------------------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | cpu_affinity                      | String         | Sets the CPU affinity for the workers. Supported options: "disabled", "automatic", user defined map of the form "0-8/9,10,11/12-14,15,16" (Default: "automatic")                                                                                                                                                                                               |
    +-----------------------------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | gpu_affinity                      | String         | Sets the GPU affinity for the workers. Supported options: "disabled", "automatic", user defined map of the form "0-8/9,10,11/12-14,15,16" (Default: "automatic")                                                                                                                                                                                               |
    +-----------------------------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | profile_input                     | String         | Path to the file which stores the input application profile (Default: "")                                                                                                                                                                                                                                                                                      |
    +-----------------------------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | profile_output                    | String         | Path to the file to store the application profile at the end of the execution (Default: "")                                                                                                                                                                                                                                                                    |
    +-----------------------------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | scheduler_config                  | String         | Path to the file which contains the scheduler configuration (Default: "")                                                                                                                                                                                                                                                                                      |
    +-----------------------------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | external_adaptation               | Boolean        | Enable external adaptation. This option will disable the Resource Optimizer (Default: False)                                                                                                                                                                                                                                                                   |
    +-----------------------------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | propatage_virtual_environment     | Boolean        | Propagate the master virtual environment to the workers (DefaultFalse)                                                                                                                                                                                                                                                                                         |
    +-----------------------------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | verbose                           | Boolean        | Verbose mode (Default: False)                                                                                                                                                                                                                                                                                                                                  |
    +-----------------------------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. table:: PyCOMPSs **stop** function for Jupyter notebook
    :name: stop_jupyter
    :widths: auto

    +----------------+----------------+---------------------------------------------------------------------+
    | Parameter Name | Parameter Type | Description                                                         |
    +================+================+=====================================================================+
    | sync           | Boolean        |  Synchronize the objects left on the user scope. (Default: False)   |
    +----------------+----------------+---------------------------------------------------------------------+


The following code snippet shows how to start a COMPSs runtime with
tracing and graph generation enabled (with *trace* and *graph*
parameters), as well as enabling the monitor with a refresh rate of 2
seconds (with the *monitor* parameter). It also synchronizes all
remaining objects in the scope with the *sync* parameter when invoking
the *stop* function.

.. code-block:: python

    # Previous user code

    ipycompss.start(graph=True, trace=True, monitor=2000)

    # User code that can benefit from PyCOMPSs

    ipycompss.stop(sync=True)

    # Subsequent code

Application execution
~~~~~~~~~~~~~~~~~~~~~

The application can be executed as a common Jupyter notebook by steps or
the whole application.

.. attention::
   Once the COMPSs runtime has been stopped it is necessary to restart the
   python kernel in Jupyter before starting another COMPSs runtime.
   To this end, click on "Kernel" and "Restart" (or "Restart & Clear Output"
   or "Restart & Run All", depending on the need).

Integration with Numba
----------------------

PyCOMPSs can also be used with Numba. Numba (http://numba.pydata.org/)
is an Open Source JIT compiler for Python which provides a set of
decorators and functionalities to translate Python functios to optimized
machine code.

Basic usage
~~~~~~~~~~~

PyCOMPSs’ tasks can be decorated with Numba’s
@jit/\ @njit decorator (with the appropiate
parameters) just below the @task decorator in order to apply
Numba to that task.

.. code-block:: python

    from pycompss.api.task import task     # Import @task decorator
    from numba import jit

    @task(returns=1)
    @jit()
    def numba_func(a, b):
         ...

Advanced usage
~~~~~~~~~~~~~~

PyCOMPSs can be also used in conjuntion with the Numba’s
*@vectorize*, *@guvectorize*, *@stencil*
and *@cfunc*. But since these decorators do not preserve the
original argument specification of the original function, their usage is
done through the *numba* parameter withih the *@task*
decorator. This parameter accepts:

-  **Boolean**: True: Applies *jit* to the function.

-  **Dictionary{k, v}**: Applies *jit* with the dictionary parameters to the
   function (allows to specify specific jit parameters (e.g.
   *nopython=True*)).

-  **String**: "jit": Applies *jit* to the function. "njit": Applies *jit*
   with *nopython=True* to the function. "generated_jit": Applies
   *generated_jit* to the function. "vectorize": Applies *vectorize* to
   the function. Needs some extra flags in the *@task*
   decorator: - *numba_signature*: String with the *vectorize*
   signature. "guvectorize": Applies *guvectorize* to the function.
   Needs some extra flags in the *@task* decorator: -
   *numba_signature*: String with the *guvectorize* signature. -
   *numba_declaration*: String with the *guvectorize* declaration.
   "stencil": Applies *stencil* to the function. "cfunc": Applies
   *cfunc* to the function. Needs some extra flags in the
   *@task* decorator: - *numba_signature*: String with the
   *cfunc* signature.

Moreover, the *@task* decorator also allows to define specific
flags for the *jit*, *njit*, *generated_jit*, *vectorize*,
*guvectorize* and *cfunc* functionalities with the *numba_flags* hint.
This hint is used to declare a dictionary with the flags expected to use
with these numba functionalities. The default flag included by PyCOMPSs
is the *cache=True* in order to exploit the function caching of Numba
across tasks.

For example, to apply *jit* to a function:

.. code-block:: python

    from pycompss.api.task import task

    @task(numba='jit')  # Aternatively: @task(numba=True)
    def jit_func(a, b):
         ...

And if the developer wants to use specific flags with jit (e.g.
*parallel=True*):

.. code-block:: python

    from pycompss.api.task import task

    @task(numba='jit', numba_flags={'parallel':True})
    def jit_func(a, b):
         ...

Other Numba’s functionalities require the specification of the function
signature and declaration. In the next example a task that will use the
*vectorize* with three parameters and a specific flag to target the cpu
is shown:

.. code-block:: python

    from pycompss.api.task import task

    @task(returns=1,
          numba='vectorize',
          numba_signature=['float32(float32, float32, float32)'],
          numba_flags={'target':'cpu'})
    def vectorize_task(a, b, c):
        return a * b * c

Details about numba and the specification of the signature, declaration
and flags can be found in the Numba’s webpage
(http://numba.pydata.org/).
