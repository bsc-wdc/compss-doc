Task Parameters
---------------

The metadata corresponding to a parameter is specified as an argument of
the ``@task`` decorator, whose name is the formal parameter's name and whose
value defines the type and direction of the parameter. The parameter types and
directions can be:

Types
   * *Primitive types* (integer, long, float, boolean, strings)
   * *Objects* (instances of user-defined classes, dictionaries, lists, tuples, complex numbers)
   * *Files*
   * *Collections* (instances of lists)
   * *Dictionaries* (instances of dictionary)
   * *Streams*
   * *IO streams* (for binaries)

Direction
   * Read-only (``IN`` - default or ``IN_DELETE``)
   * Read-write (``INOUT``)
   * Write-only (``OUT``)
   * Concurrent (``CONCURRENT``)
   * Commutative (``COMMUTATIVE``)

COMPSs is able to automatically infer the parameter type for primitive
types, strings and objects, while the user needs to specify it for
files. On the other hand, the direction is only mandatory for ``INOUT``, ``OUT``,
``CONCURRENT`` and ``COMMUTATIVE`` parameters.

.. NOTE::

  Please note that in the following cases there is no need
  to include an argument in the *@task* decorator for a given
  task parameter:

  -  Parameters of primitive types (integer, long, float, boolean) and
     strings: the type of these parameters can be automatically inferred
     by COMPSs, and their direction is always ``IN``.

  -  Read-only object parameters: the type of the parameter is
     automatically inferred, and the direction defaults to ``IN``.

The parameter metadata is available from the *pycompss* library
(:numref:`parameter_import_python`)

.. code-block:: python
    :name: parameter_import_python
    :caption: Python task parameters import

    from pycompss.api.parameter import *


Objects
^^^^^^^

The default type for a parameter is object. Consequently, there is no need
to use a specific keyword. However, it is necessary to indicate its direction
(unless for input parameters):

.. LIST-TABLE::
    :header-rows: 1

    * - PARAMETER
      - DESCRIPTION
    * - ``IN``
      - The parameter is read-only. The type will be inferred.
    * - ``IN_DELETE``
      - The parameter is read-only. The type will be inferred. Will be automatically removed after its usage.
    * - ``INOUT``
      - The parameter is read-write. The type will be inferred.
    * - ``OUT``
      - The parameter is write-only. The type will be inferred.
    * - ``CONCURRENT``
      - The parameter is read-write with concurrent access. The type will be inferred.
    * - ``COMMUTATIVE``
      - The parameter is read-write with commutative access. The type will be inferred.


Continuing with the example, in :numref:`task_example_python_object` the
decorator specifies that ``foo`` has a parameter called ``obj``, of type object
and ``INOUT`` direction. Note how the second parameter, ``i``, does not need to
be specified, since its type (integer) and direction (``IN``) are
automatically inferred by COMPSs.

.. code-block:: python
    :name: task_example_python_object
    :caption: Python task example with input output object (``INOUT``) and input object (``IN``)

    from pycompss.api.task import task
    from pycompss.api.parameter import INOUT, IN

    @task(obj=INOUT, i=IN)
    def foo(obj, i):
         ...

The previous task definition can be simplified due to the default ``IN`` direction
for objects (:numref:`task_example_python_object_simplified`):

.. code-block:: python
    :name: task_example_python_object_simplified
    :caption: Python task example with input output object (``INOUT``) simplified

    from pycompss.api.task import task
    from pycompss.api.parameter import INOUT

    @task(obj=INOUT)
    def foo(obj, i):
         ...

.. TIP::

  In order to choose the appropriate direction, a good exercise is to think if
  the function only consumes the object (``IN``), modifies the object (``INOUT``),
  or produces an object (``OUT``).


.. TIP::

  The ``IN_DELETE`` definition is intended to one use objects. Consequently,
  the information related to the object will be released as soon as possible.


The user can also define that the access to a object is concurrent
with ``CONCURRENT`` (:numref:`task_concurrent_python_object`). Tasks that share
a ``CONCURRENT`` parameter will be executed in parallel, if any other dependency
prevents this.
The ``CONCURRENT`` direction allows users to have access from multiple tasks to
the same object/file during their executions.

.. code-block:: python
    :name: task_concurrent_python_object
    :caption: Python task example with ``CONCURRENT``

    from pycompss.api.task import task
    from pycompss.api.parameter import CONCURRENT

    @task(obj=CONCURRENT)
    def foo(obj, i):
         ...

.. CAUTION::

  COMPSs does not manage the interaction with the objects used/modified
  concurrently. Taking care of the access/modification of the concurrent
  objects is responsibility of the developer.

Or even, the user can also define that the access to a parameter is commutative
with ``COMMUTATIVE`` (:numref:`task_commutative_python_object`).
The execution order of tasks that share a ``COMMUTATIVE`` parameter can be changed
by the runtime following the commutative property.

.. code-block:: python
    :name: task_commutative_python_object
    :caption: Python task example with ``COMMUTATIVE``

    from pycompss.api.task import task
    from pycompss.api.parameter import COMMUTATIVE

    @task(obj=COMMUTATIVE)
    def foo(obj, i):
         ...


Files
^^^^^

It is possible to define that a parameter is a file (``FILE``), and its direction:

.. LIST-TABLE::
    :header-rows: 1

    * - PARAMETER
      - DESCRIPTION
    * - ``FILE/FILE_IN``
      - The parameter is a file. The direction is assumed to be ``IN``.
    * - ``FILE_INOUT``
      - The parameter is a read-write file.
    * - ``FILE_OUT``
      - The parameter is a write-only file.
    * - ``FILE_CONCURRENT``
      - The parameter is a concurrent read-write file.
    * - ``FILE_COMMUTATIVE``
      - The parameter is a commutative read-write file.


Continuing with the example, in :numref:`task_example_python` the decorator
specifies that ``foo`` has a parameter called ``f``, of type ``FILE`` and
``INOUT`` direction (``FILE_INOUT``).

.. code-block:: python
    :name: task_example_python
    :caption: Python task example with input output file (``FILE_INOUT``)

    from pycompss.api.task import task
    from pycompss.api.parameter import FILE_INOUT

    @task(f=FILE_INOUT)
    def foo(f):
        fd = open(f, 'a+')
        ...
        # append something to fd
        ...
        fd.close()

    def main():
        f = "/path/to/file.extension"
        # Populate f
        foo(f)

.. TIP::

    The value for a FILE (e.g. ``f``) is a string pointing to the file
    to be used at ``foo`` task. However, it can also be ``None`` if it is
    optional. Consequently, the user can define task that can receive a FILE
    or not, and act accordingly. For example (:numref:`task_example_python_optional`):

    .. code-block:: python
        :name: task_example_python_optional
        :caption: Python task example with optional input file (``FILE_IN``)

        from pycompss.api.task import task
        from pycompss.api.parameter import FILE_IN

        @task(f=FILE_IN)
        def foo(f):
            if f:
                # Do something with the file
                with open(f, 'r') as fd:
                    num_lines = len(rd.readlines())
                return num_lines
            else:
                # Do something when there is no input file
                return -1

        def main():
            f = "/path/to/file.extension"
            # Populate f
            num_lines_f = foo(f)  # num_lines_f == actual number of lines of file.extension
            g = None
            num_lines_g = foo(g)  # num_lines_g == -1

The user can also define that the access to file parameter is concurrent
with ``FILE_CONCURRENT`` (:numref:`task_concurrent_python`).
Tasks that share a ``FILE_CONCURRENT`` parameter will be executed in parallel,
if any other dependency prevents this.
The ``CONCURRENT`` direction allows users to have access from multiple tasks to
the same file during their executions.

.. code-block:: python
    :name: task_concurrent_python
    :caption: Python task example with ``FILE_CONCURRENT``

    from pycompss.api.task import task
    from pycompss.api.parameter import FILE_CONCURRENT

    @task(f=FILE_CONCURRENT)
    def foo(f, i):
         ...

.. CAUTION::

  COMPSs does not manage the interaction with the files used/modified
  concurrently. Taking care of the access/modification of
  the concurrent files is responsibility of the developer.


Or even, the user can also define that the access to a parameter is a file
``FILE_COMMUTATIVE`` (:numref:`task_commutative_python`).
The execution order of tasks that share a ``FILE_COMMUTATIVE`` parameter can be
changed by the runtime following the commutative property.

.. code-block:: python
    :name: task_commutative_python
    :caption: Python task example with ``FILE_COMMUTATIVE``

    from pycompss.api.task import task
    from pycompss.api.parameter import FILE_COMMUTATIVE

    @task(f=FILE_COMMUTATIVE)
    def foo(f, i):
         ...


Directories
^^^^^^^^^^^

In addition to files, it is possible to define that a parameter is a directory
(``DIRECTORY``), and its direction:

.. LIST-TABLE::
    :header-rows: 1

    * - PARAMETER
      - DESCRIPTION
    * - ``DIRECTORY_IN``
      - The parameter is a directory and the direction is ``IN``. The directory will be compressed before any transfer among nodes.
    * - ``DIRECTORY_INOUT``
      - The parameter is a read-write directory. The directory will be compressed before any transfer among nodes.
    * - ``DIRECTORY_OUT``
      - The parameter is a write-only directory. The directory will be compressed before any transfer among nodes.


The definition of a ``DIRECTORY`` parameter is shown in
:numref:`task_example_python_directory`. The decorator specifies that ``foo``
has a parameter called:

* ``d_in``, of type ``DIRECTORY`` and ``IN`` direction
* ``d_inout``, of type ``DIRECTORY`` and ``INOUT`` direction
* ``d_out``, of type ``DIRECTORY`` and ``OUT`` direction

And finally synchronizes the values of the ``d_inout`` and ``d_out`` directories.

.. code-block:: python
    :name: task_example_python_directory
    :caption: Python task example with directory (``DIRECTORY``)

    import os

    from pycompss.api.task import task
    from pycompss.api.parameter import DIRECTORY_IN
    from pycompss.api.parameter import DIRECTORY_INOUT
    from pycompss.api.parameter import DIRECTORY_OUT
    from pycompss.api.api import compss_wait_on_directory

    @task(d_in=DIRECTORY_IN, d_inout=DIRECTORY_INOUT, d_out=DIRECTORY_OUT)
    def foo(d_in, d_inout, d_out):
        # Read any file from d_in
        for file in os.listdir(d_in):
            with open(file, "r") as f:  # Open in read mode
                content = f.read()
            ...
        ...
        # Read and/or write files from/within d_inout
        for file in os.listdir(d_in):
            with open(file, "rw") as f:  # Open in read/write mode (could be "a" for append)
                content = f.read()
                # Update content
                f.write(content)
            ...
        ...
        # Write files to d_out
        for file in os.listdir(d_in):
            with open(file, "w") as f:  # Open in write mode
                f.write(new_content)
            ...
        ...

    def main():
        d_in="/path/to/in_directory/"
        d_inout="/path/to/inout_directory/"
        d_out="/path/to/out_directory/"

        foo(d_in, d_inout, d_out)

        compss_wait_on_directory(d_inout)
        # Now it is possible to access to 'd_inout' updated contents
        ...

        compss_wait_on_directory(d_out)
        # Now it is possible to access to 'd_out' new contents
        ...

    if __name__=="__main__":
        main()


Collections
^^^^^^^^^^^

It is possible to specify that a parameter is a collection of elements (e.g. list) and its direction.

.. LIST-TABLE::
    :header-rows: 1

    * - PARAMETER
      - DESCRIPTION
    * - ``COLLECTION_IN``
      - The parameter is read-only collection.
    * - ``COLLECTION_IN_DELETE``
      - The parameter is read-only collection for single usage (will be automatically removed after its usage).
    * - ``COLLECTION_INOUT``
      - The parameter is read-write collection.
    * - ``COLLECTION_OUT``
      - The parameter is write-only collection.

In this case (:numref:`task_collection_python`), the list may contain
sub-objects that will be handled automatically by the runtime.
It is important to annotate data structures as collections if in other tasks
there are accesses to individual elements of these collections as parameters.
Without this annotation, the runtime will not be able to identify data
dependencies between the collections and the individual elements.

.. code-block:: python
    :name: task_collection_python
    :caption: Python task example with ``COLLECTION`` (``IN``)

    from pycompss.api.task import task
    from pycompss.api.parameter import COLLECTION

    @task(my_collection=COLLECTION)
    def foo(my_collection):
         for element in my_collection:
             ...

.. CAUTION::

    The current support for collections is limited to **static number of
    elements** lists.

    Consequently, *the length of the collection must be kept* during the
    execution, and it is *NOT possible to append or delete elements* from
    the collection in the tasks (only to receive elements or to modify
    the existing if they are not primitives).

The sub-objects of the collection can be collections of elements (and
recursively). In this case, the runtime also keeps track of all elements
contained in all sub-collections. In order to improve the performance,
the depth of the sub-objects can be limited through the use of the
``depth`` parameter (:numref:`task_collection_depth_python`)

.. code-block:: python
    :name: task_collection_depth_python
    :caption: Python task example with ``COLLECTION_IN`` and ``Depth``

    from pycompss.api.task import task
    from pycompss.api.parameter import COLLECTION_IN

    @task(my_collection={Type:COLLECTION_IN, Depth:2})
    def foo(my_collection):
         for inner_collection in my_collection:
             for element in inner_collection:
                 # The contents of element will not be tracked
                 ...

.. TIP::

   A collection can contain dictionaries, and will be analyzed automatically.


.. TIP::

   If the collection is intended to be used only once with ``IN`` direction, the
   ``COLLECTION_IN_DELETE`` type is recommended, since it automatically removes
   the entire collection after the task. This enables to release as soon as
   possible memory and storage.


Collections of files
^^^^^^^^^^^^^^^^^^^^

It is also possible to specify that a parameter is a collection of
files (e.g. list) and its direction.

.. LIST-TABLE::
    :header-rows: 1

    * - PARAMETER
      - DESCRIPTION
    * - ``COLLECTION_FILE/COLLECTION_FILE_IN``
      - The parameter is read-only collection of files.
    * - ``COLLECTION_FILE_INOUT``
      - The parameter is read-write collection of files.
    * - ``COLLECTION_FILE_OUT``
      - The parameter is write-only collection of files.


In this case (:numref:`task_collection_file_python`), the list
may contain files that will be handled automatically by the runtime.
It is important to annotate data structures as collections if in other tasks
there are accesses to individual elements of these collections as parameters.
Without this annotation, the runtime will not be able to identify data
dependencies between the collections and the individual elements.

.. code-block:: python
    :name: task_collection_file_python
    :caption: Python task example with ``COLLECTION_FILE`` (``IN``)

    from pycompss.api.task import task
    from pycompss.api.parameter import COLLECTION_FILE

    @task(my_collection=COLLECTION_FILE)
    def foo(my_collection):
         for file in my_collection:
             ...

The file of the collection can be collections of elements (and
recursively). In this case, the runtime also keeps track of all files
contained in all sub-collections.
In order to improve the performance, the depth of the sub-files can be
limited through the use of the ``depth`` parameter as with objects
(:numref:`task_collection_depth_python`)

.. CAUTION::

    The current support for collections of files is also limited to a
    **static number of elements**, as with
    :ref:`Sections/02_app_development/02_python/01_Programming_model/01_Decorators/01_Task_decorator:Collections`.


Dictionaries
^^^^^^^^^^^^

It is possible to specify that a parameter is a dictionary of elements (e.g. dict) and its direction.

.. LIST-TABLE::
    :header-rows: 1

    * - PARAMETER
      - DESCRIPTION
    * - ``DICTIONARY_IN``
      - The parameter is read-only dictionary.
    * - ``DICTIONARY_IN_DELETE``
      - The parameter is read-only dictionary for single usage (will be automatically removed after its usage).
    * - ``DICTIONARY_INOUT``
      - The parameter is read-write dictionary.

As with the collections, it is possible to specify that a parameter is
a dictionary of elements (e.g. dict) and its direction (DICTIONARY_IN or
DICTIONARY_INOUT) (:numref:`task_dictionary_python`),
whose sub-objects will be handled automatically by the runtime.

.. code-block:: python
    :name: task_dictionary_python
    :caption: Python task example with ``DICTIONARY`` (``IN``)

    from pycompss.api.task import task
    from pycompss.api.parameter import DICTIONARY

    @task(my_dictionary=DICTIONARY)
    def foo(my_dictionary):
         for k, v in my_dictionary.items():
             ...

.. CAUTION::

   The current support for dictionaries is also limited to a
   **static number of elements**, as with
   :ref:`Sections/02_app_development/02_python/01_Programming_model/01_Decorators/01_Task_decorator:Collections`.


The sub-objects of the dictionary can be collections or dictionary of elements
(and recursively). In this case, the runtime also keeps track of all elements
contained in all sub-collections/sub-dictionaries.
In order to improve the performance, the depth of the sub-objects can be
limited through the use of the ``depth`` parameter
(:numref:`task_dictionary_depth_python`)

.. code-block:: python
    :name: task_dictionary_depth_python
    :caption: Python task example with ``DICTIONARY_IN`` and ``Depth``

    from pycompss.api.task import task
    from pycompss.api.parameter import DICTIONARY_IN

    @task(my_dictionary={Type:DICTIONARY_IN, Depth:2})
    def foo(my_dictionary):
         for key, inner_dictionary in my_dictionary.items():
             for sub_key, sub_value in inner_dictionary.items():
                 # The contents of element will not be tracked
                 ...

.. TIP::

    A dictionary can contain collections, and will be analyzed automatically.


.. TIP::

    If the dictionary is intended to be used only once with ``IN`` direction, the
    ``DICTIONARY_IN_DELETE`` type is recommended, since it automatically removes
    the entire dictionary after the task. This enables to release as soon as
    possible memory and storage.

Streams
^^^^^^^

It is possible to use streams as input or output of the tasks by defining
that a parameter is ``STREAM`` and its direction.

.. LIST-TABLE::
    :header-rows: 1

    * - PARAMETER
      - DESCRIPTION
    * - ``STREAM_IN``
      - The parameter is a read-only stream.
    * - ``STREAM_OUT``
      - The parameter is a write-only stream.

For example, :numref:`task_streams` shows an example using ``STREAM_IN`` or ``STREAM_OUT``
parameters
This parameters enable to mix a task-driven workflow with a data-driven workflow.


.. code-block:: python
    :name: task_streams
    :caption: Python task example with ``STREAM_IN`` and ``STREAM_OUT``

    from pycompss.api.task import task
    from pycompss.api.parameter import STREAM_IN
    from pycompss.api.parameter import STREAM_OUT

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
    :caption: Python task example with ``STREAM_IN`` and ``STREAM_OUT`` for files

    from pycompss.api.task import task
    from pycompss.api.parameter import STREAM_IN
    from pycompss.api.parameter import STREAM_OUT

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
    :caption: Python task example with ``STREAM_OUT`` for binaries

    from pycompss.api.task import task
    from pycompss.api.binary import binary
    from pycompss.api.parameter import STREAM_OUT

    @binary(binary="file_generator.sh")
    @task(fds=STREAM_OUT)
    def write_files(fds):
        # Equivalent to: ./file_generator.sh > fds
        pass

:numref:`task_streams_main` shows an example of how streams are used in the main code.
In this code snippet we can see how the object representing the data stream is
created how the a producer task is invoked and how the stream data generated
at tasks can be poll from the main code.

.. code-block:: python
    :name: task_streams_main
    :caption: Python task example using streams in the main code

    from pycompss.api.task import task
    from pycompss.api.parameter import STREAM_OUT
    from pycompss.streams.distro_stream import ObjectDistroStream

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

    @task()
    def process_object(obj):
        ...
        # Do something with obj
        ...

    if __name__=='__main__':

        ods = ObjectDistroStream()

        # Create producers
        for _ in range(num_producers):
            write_objects(ods, producer_sleep)

        # Process stream
        while not ods.is_closed():
            # Poll new objects
            new_objects = ods.poll()

            # Process received objects
            for obj in new_objects:
                res = process_object(obj)
        ...

Standard Streams
^^^^^^^^^^^^^^^^

Finally, a parameter can also be defined as the standard input, standard
output, and standard error.

.. LIST-TABLE::
    :header-rows: 1

    * - PARAMETER
      - DESCRIPTION
    * - ``STDIN``
      - The parameter is a IO stream for standard input redirection.
    * - ``STDOUT``
      - The parameter is a IO stream for standard output redirection.
    * - ``STDERR``
      - The parameter is a IO stream for standard error redirection.

.. CAUTION::

    ``STDIN``, ``STDOUT`` and ``STDERR`` are only supported in binary tasks

This is particularly useful with binary tasks that consume/produce from standard
IO streams, and the user wants to redirect the standard input/output/error to a
particular file. :numref:`task_streams_binary_std` shows an example of a
binary task that invokes `output_generator.sh` which produces the result
in the standard output, and the task takes that output and stores it into `fds`.

.. code-block:: python
    :name: task_streams_binary_std
    :caption: Python task example with ``STDOUT`` for binaries

    from pycompss.api.task import task
    from pycompss.api.binary import binary
    from pycompss.api.parameter import STDOUT

    @binary(binary="output_generator.sh")
    @task(fds=STDOUT)
    def write_files(fds):
        # Equivalent to: ./file_generator.sh > fds
        pass
