Distributed Data Set (DDS)
--------------------------

Distributed Data Set (DDS) is a lightweight library to ease development of PyCOMPSs applications.
It provides an interface where programmers can load data from basic Python data structures, generators,
or files, distribute the data on available nodes, and run some most common big data operations on it.
By using DDS, number of code lines can be reduced, where performance improvement is not expected
comparing with regular PyCOMPSs applications.


How it works?
~~~~~~~~~~~~~

To take advantage of DDS, first of all, the user should load the data to a new instance of it.
Once one of the ``load`` functions is called, the data will be partitioned and sent to the
available nodes, and after that the user can perform any of DDS operations to manipulate the
data simply by calling methods of the instance.

In DDS environment, the initial data is always distributed on arbitrary number of partitions,
and passed from one task to another as *Future Objects*, until the programmer synchronizes or
``collects`` it.

Moreover, it is also possible to create a new DDS with a ``list`` of *Future Objects* from
user-defined functions, or send data from a DDS instance to other user defined functions as
*Future Objects* without retrieving it on the master node.
This flexibility gives the user an opportunity to use DDS methods anywhere in the code, mixing
the data from those methods with his/her own functions without sticking to pre-defined data
operations, as well as replace some methods with DDS ones on an existing project.

How to use?
~~~~~~~~~~~

As a library, DDS comes along with PyCOMPSs, thus it is not required to install a new package.
If PyCOMPSs is already installed on the system, the following single line of Python code is
enough to import DDS:

.. code-block:: python

    from pycompss.dds import DDS

After that, we would have to create an instance of the DDS class and provide it with some data.
In the following code snippet, we are filling our DDS instance with the numbers from 0 to 10,
which basically means elements of the DDS will be those digits:

.. code-block:: python

    data = range(10)
    dds = DDS().load(data)

Since the data set is ready to be used, we can simply call some methods of the DDS class.
For example, let's assume we want to filter our numbers and keep only even numbers.
Same as Python's built-in ``filter``, all we need is a ``lambda`` function which will
eliminate odd numbers, and send it as a parameter to the DDS's ``filter`` method:

.. code-block:: python

    even_numbers = dds.filter ( lambda x : x % 2 == 0 ).collect()

As we have already mentioned, without calling the ``collect`` method, the data is never
transferred to the master node. Since in our example, we do not want to perform any other
operation than filtering, we call it to retrieve the even numbers between 0 and 10 as a list:

.. code-block:: python

    print(even_numbers)

    [0, 2, 4, 6 , 8]

This is a very simple example of the use of DDS and before listing all available methods,
let us have a look at a more real-world case where we can take advantage of PyCOMPSs DDS.
One of the most-known Big Data examples is Word Count.
The required code to implement it with DDS would contain the following steps:

  1. Reading data from a file
  2. Splitting the lines into words (so that elements of DDS are not lines from the file, but words from each line)
  3. Counting the amount of each element (word)

And all these three steps can be performed within a single line of code:

.. code-block:: python

    from pycompss.dds import DDS
    results = DDS().load_text_file("book.txt").map_and_flatten(lambda x: x.split()).count_by_value( True )
    print ( results )

    {'a' : 10, 'the' : 15, ...}

For an explicit explanation, we can add that ``load_text_file`` reads ``book.txt`` file line-by-line
and loads it onto the DDS instance. At this point, elements of the DDS are ``string`` lines, and
each partition contains the same amount of them. Then, the ``map_and_flatten`` method does the
transformation from lines to words by parsing and spreading them inside the partitions.
In other words, if a partition contained lines before ``map_and_flatten`` method, afterwards it
contains all the words from its lines as elements (see different mapping functions from
:ref:`Sections/02_App_Development/02_Python/05_DDS_interface:Available Methods` Section
in order to have more clear idea).
The last method called is ``count_by_value`` which retrieves a dictionary where ``keys`` are elements
(words) of the DDS, and ``values`` are times of occurrence. The argument for this function ``True``,
represents whether we want to collect the results, or we prefer to have the final dictionary to be
partitioned and distributed on nodes again. It would be useful to set it to ``False``, if we
wanted to perform more operations on our data set.


Available Methods
~~~~~~~~~~~~~~~~~

All the methods provided by DDS are listed below with their arguments list, and descriptions:

- `dds_load`_
- `dds_load_file`_
- `dds_load_text_file`_
- `dds_load_files_from_dir`_
- `dds_load_pickle_files`_
- `dds_union`_
- `dds_num_of_partitions`_
- `dds_map`_
- `dds_map_partitions`_
- `dds_flat_map`_
- `dds_filter`_
- `dds_reduce`_
- `dds_distinct`_
- `dds_count_by_value`_
- `dds_key_by`_
- `dds_sum_count`_
- `dds_foreach`_
- `dds_collect`_
- `dds_save_as_text_file`_
- `dds_save_as_pickle`_
- `dds_collect_as_dict`_
- `dds_keys`_
- `dds_values`_
- `dds_partition_by`_
- `dds_map_values`_
- `dds_flatten_by_key`_
- `dds_join`_
- `dds_combine_by_key`_
- `dds_reduce_by_key`_
- `dds_count_by_key`_
- `dds_sort_by_key`_
- `dds_group_by_key`_


.. _dds_load:

**load**
  Definition:

  .. code-block:: python

    def load(self, iterator, num_of_parts=10, paac=False)

  Loads the data from a given iterator.

  Has one obligatory parameter (``iterator``). Iterator is any kind of ``iterable`` object from Python,
  such as generators, lists, etc. Iterator represents the data that will be distributed, and result of
  each iteration will be an element on DDS.

  And two arbitrary parameters (``num_of_parts`` and ``paac``). The number of partitions ``num_of_parts``
  can be defined by user, and will be set to **10 by default**. Partitions can be defined as collections
  by setting ``paac`` to ``True`` (**``False`` by default**).

  The return value of this method is a DDS with a partitioned data.
  When the number of partitions is set to ``-1``,
  DDS assumes that the ``iterator`` is already a list of *Future Objects* and skips data partitioning
  (distributing) step.

.. _dds_load_file:

**load_file**
  Definition:

  .. code-block:: python

    def load_file(self, file_path, chunk_size=1024, worker_read=False)

  Loads data from a file (``file_path``) in chunks and creates one partition for each chunk.

  Since COMPSs gives us the opportunity to read the files either on the master or worker nodes,
  this option is enabled for this method as well (by default it will be read on the Master node
  and each partition will be sent to worker nodes one-by-one (can be set to be read by the
  workers by setting ``worker_read`` to ``True``)).

  The ``chunk_size`` (partition) size is arbitrary and will be set to 1024 Bytes if not defined by the user.

  The return value of this method is a DDS containing Python Strings as elements.

  .. HINT::

      Usage sample:

      .. code-block:: python

          >>> with open("test.file", "w") as testFile:
          ...     _ = testFile.write("Hello world!")
          >>> DDS().load_file("test.file", 6).collect()
          ['Hello ', 'world!']

.. _dds_load_text_file:

**load_text_file**
  Definition:

  .. code-block:: python

    def load_text_file(self, file_name, chunk_size=1024, in_bytes=True, strip=True)

  Basically, same as ``load_file`` method. The only difference is the fact that reading a text
  file in bytes can cause incomplete words as elements in DDS. To avoid this situation, text
  files are read line-by-line, and the chunk size can define the size of partitions
  (``chunk_size``) in amount of lines or in bytes.
  In addition, the ``strip`` parameter determines if separators should be stripped from the
  lines.

  .. HINT::

      Usage sample:

      .. code-block:: python

          >>> with open("test.txt", "w") as testFile:
          ...     _ = testFile.write("First Line! \n")
          ...     _ = testFile.write("Second Line! \n")
          >>> DDS().load_text_file("test.txt").collect()
          ['First Line! ', 'Second Line! ']

.. _dds_load_files_from_dir:

**load_files_from_dir**
  Definition:

  .. code-block:: python

    def load_files_from_dir(self, dir_path, num_of_parts=-1)

  Reads multiple files from a given directory (``dir_path``) and saves them onto DDS by creating
  (key, value) tuples where keys are file names, and values are the file contents stored as Strings.
  By default, partitions can contain more than one file, when it is not possible to distribute one file
  in more than one partition. ``num_of_parts`` can be set to -1 to create one partition per file.

.. _dds_load_pickle_files:

**load_pickle_files**
  Definition:

  .. code-block:: python

    def load_pickle_files(self, dir_path)

  Equivalent to ``load_files_from_dir`` where the files within ``dir_path`` contain pickled objects.

.. _dds_union:

**union**
  Definition:

  .. code-block:: python

    def union(self, *args)

  Combine this data set with some other DDS data defined on ``*args``.

  .. HINT::

      Usage sample:

      .. code-block:: python

          >>> first = DDS().load([0, 1, 2, 3, 4], 2)
          >>> second = DDS().load([5, 6, 7, 8, 9], 3)
          >>> first.union(second).count()
          10

.. _dds_num_of_partitions:

**num_of_partitions**
  Definition:

  .. code-block:: python

    def num_of_partitions(self)

  Get the total amount of partitions.

.. _dds_map:

**map**
  Definition:

  .. code-block:: python

      def map(self, func, *args, **kwargs)

  Same as the Python's built-in ``map`` method, applies a given function to each element of the DDS,
  and replaces the old value with the result.

  .. HINT::

      Usage sample:

      .. code-block:: python

          >>> DDS().load( range (10) ).map( lambda x: x * 2).collect()
          [0, 2, 4, 6, 8 ,10 ,12, 14, 16, 18]

.. _dds_map_partitions:

**map_partitions**
  Definition:

  .. code-block:: python

      def map_partitions(self, func)

  Applies a given function to the partitions of a DDS.
  It can be thought as a map function where the input is a partition of DDS instead of an element of a partition.

  .. HINT::

      Usage sample:

      .. code-block:: python

          >>> DDS().load(range(10), 5).map_partitions(lambda x: [sum(x)]).collect(True)
          [[1], [5], [9], [13], [17]]

.. _dds_flat_map:

**flat_map**
  Definition:

  .. code-block:: python

      def flat_map(self, func, *args, **kwargs)

  Apply a function to each element of the dataset. Extends the derived elements if possible.

  .. HINT::

      Usage sample:

      .. code-block:: python

          >>> dds = DDS().load([2, 3, 4])
          >>> sorted(dds.flat_map(lambda x: range(1, x)).collect())
          [1, 1, 1, 2, 2, 3]

.. _dds_filter:

**filter**
  Definition:

  .. code-block:: python

      def filter(self, func)

  Same as Python's built-in ``filter`` method, applies a given function to each element of the DDS;
  if the result of the function applied to the element is ``False``, then the element is removed
  from the DDS.

  .. HINT::

      Usage sample:

      .. code-block:: python

          >>> DDS().load(range(10), 5).filter(lambda x: x % 2).count()
          5

.. _dds_reduce:

**reduce**
  Definition:

  .. code-block:: python

      def reduce(self, func, initial=MARKER, arity=-1)

  Same as the Python's built-in ``reduce`` method, applies a given function to each pair of the DDS elements and
  returns a single value.
  Since reductions are done inside partitions locally and then merged in a tree structure, it is possible
  to define depth (``arity``) of the reduction tree. The ``initial`` value for the reduce can be set as well.

  .. HINT::

      Usage sample:

      .. code-block:: python

          >>> DDS().load(range(10), 5).reduce((lambda b, a: b + a) , 100)
          145

.. _dds_distinct:

**distinct**
  Definition:

  .. code-block:: python

      def distinct(self)

  Keeps only one of the repeating elements inside the  DDS.
  The number of partitions is kept as initial and final elements are distributed proportionally.

  .. HINT::

      Usage sample:

      .. code-block:: python

          >>> test = list(range(10))
          >>> test.extend(list(range(5)))
          >>> len(test)
          15
          >>> DDS().load(test, 5).distinct().count()
          10

.. _dds_count_by_value:

**count_by_value**
  Definition:

  .. code-block:: python

      def count_by_value(self, arity=2, as_dict=True, as_fo=False)

  Returns the amount of each element inside the DDS.
  Allows to define the tree depth (``arity``) which by default is 2.
  And to define the returned object type (``as_dict`` or ``as_fo`` (as *future object*)).

  .. HINT::

      Usage sample:

      .. code-block:: python

          >>> first = DDS().load([0, 1, 2], 2)
          >>> second = DDS().load([2, 3, 4], 3)
          >>> dict(sorted(
          ...     first.union(second).count_by_value(as_dict=True).items()
          ... ))
          {0: 1, 1: 1, 2: 2, 3: 1, 4: 1}

.. _dds_key_by:

**key_by**
  Definition:

  .. code-block:: python

      def key_by(self, func)

  Creates ``(key, value)`` pairs from DDS data, where keys are generated by applying a given
  ``func`` function to the elements (``key = func(value)``).

  .. HINT::

      Usage sample:

      .. code-block:: python

          >>> dds = DDS().load(range(3), 2)
          >>> dds.key_by(lambda x: str(x)).collect()
          [('0', 0), ('1', 1), ('2', 2)]

.. _dds_sum_count:

**sum / count**
  Definitions:

  .. code-block:: python

      def sum(self)
      def count(self)

  Some self-explanatory functions that walk through all elements of the DDS and return a single value.

  .. HINT::

      Usage sample:

      .. code-block:: python

          >>> DDS().load( range (100) ).count()

.. _dds_foreach:

**foreach**
  Definition:

  .. code-block:: python

      def foreach(self, func)

  Applies a given function to each element of the DDS without returning any value.
  It a Barrier Point in order to make sure that all the tasks finish the execution.

.. _dds_collect:

**collect**
  Definition:

  .. code-block:: python

      def collect(self, keep_partitions=False, future_objects=False)

  Returns the data of a DDS.
  It is possible to synchronize the data and retrieve it inside a list. However, when the
  value of ``future_objects`` parameter is ``True``, the synchronization point will not take place,
  and each partition will be retrieved as a Future Object.
  The programmer can apply more operations on those Future Objects without transferring them to the Master node.

  .. HINT::

      Usage sample:

      .. code-block:: python

          >>> DDS().load( range (10) ).collect()
          [0, 1, 2, 3, 4, 5, 6, 7, 8 , 9]

.. _dds_save_as_text_file:

**save_as_text_file**
  Definition:

  .. code-block:: python

      def save_as_text_file(self, path)

  Save string representations of DDS elements as text files defined by ``path``.
  This saving creates one file per partition.

.. _dds_save_as_pickle:

**save_as_pickle**
  Definition:

  .. code-block:: python

      def save_as_pickle(self, path)

  Save string representations of DDS elements as pickle files defined by ``path``.
  This saving creates one file per partition.

.. _dds_collect_as_dict:

**collect_as_dict**
  Definition:

  .. code-block:: python

      def collect_as_dict(self)

  Get (key, value) DDS elements as { key: value } dictionary.

  .. HINT::

      Usage sample:

      .. code-block:: python

          >>> DDS().load([("a", 1), ("b", 1)]).collect_as_dict()
          {'a': 1, 'b': 1}

.. _dds_keys:

**keys**
  Definition:

  .. code-block:: python

      def keys(self)

  Get the DDS keys.

  .. HINT::

      Usage sample:

      .. code-block:: python

          >>> DDS().load([("a", 1), ("b", 1)]).keys().collect()
          ['a', 'b']

.. _dds_values:

**values**
  Definition:

  .. code-block:: python

      def values(self)

  Get the DDS values.

  .. HINT::

      Usage sample:

      .. code-block:: python

          >>> DDS().load([("a", 1), ("b", 2)]).values().collect()
          [1, 2]

.. _dds_partition_by:

**partition_by**
  Definition:

  .. code-block:: python

      def partition_by(self, partitioner_func=default_hash, num_of_partitions=-1)

  Create partitions by a partitioning function (``partitioner_func``). By default, uses the objects hash.
  It enables to define the number of partitions to be created (``num_partitions``).

  .. HINT::

      Usage sample:

      .. code-block:: python

          >>> dds = DDS().load(range(6)).map(lambda x: (x, x))
          >>> dds.partition_by(num_of_partitions=3).collect(True)
          [[(0, 0), (3, 3)], [(1, 1), (4, 4)], [(2, 2), (5, 5)]]

.. _dds_map_values:

**map_values**
  Definition:

  .. code-block:: python

      def map_values(self, func)

  Apply a function (``func``) to each value of the DDS.
  This function must take values as parameter.

  .. HINT::

      Usage sample:

      .. code-block:: python

          >>> DDS().load([("a", 1), ("b", 1)]).map_values(lambda x: x+1).collect()
          [('a', 2), ('b', 2)]

.. _dds_flatten_by_key:

**flatten_by_key**
  Definition:

  .. code-block:: python

      def flatten_by_key(self, func)

  Reverse of combine by key.Flat (k, v) as (k, v1), (k, v2).
  In detail: (key, values) as (key, value1), (key, value2) etc.

  .. HINT::

      Usage sample:

      .. code-block:: python

          >>> DDS().load([('a',[1, 2]), ('b',[1])]).flatten_by_key(lambda x: x).collect()
          [('a', 1), ('a', 2), ('b', 1)]

.. _dds_join:

**join**
  Definition:

  .. code-block:: python

      def join(self, other, num_of_partitions=-1)

  Join DDS objects (current with ``other``).

  .. HINT::

      Usage sample:

      .. code-block:: python

          >>> x = DDS().load([("a", 1), ("b", 3)])
          >>> y = DDS().load([("a", 2), ("b", 4)])
          >>> sorted(x.join(y).collect())
          [('a', (1, 2)), ('b', (3, 4))]

.. _dds_combine_by_key:

**combine_by_key**
  Definition:

  .. code-block:: python

      def combine_by_key(self, creator_func, combiner_func, merger_function, total_parts=-1)

  Combine elements of each key.
  Accepts the following parameters:

  - ``creator_func``: To apply to the first element of the key.
                      Takes only one argument which is the value from (k, v) pair (e.g: ``v = list(v)``).
  - ``combiner_func``: To apply when a new element with the same key is found.
                       It is used to combine partitions locally.
                       Takes 2 arguments; first one is the result of ``creator_func`` and the second one
                       is a ``value`` of the same ``key`` from the same partition. (e.g: ``v1.append(v2)``).
  - ``merger_function``: To merge local results. Basically takes two arguments (both are results of ``combiner_func``)
                         (e.g: ``list_1.extend(list_2)``).
  - ``total_parts``: Number of partitions after combinations.

  Returns the DDS object combined by key.

.. _dds_reduce_by_key:

**reduce_by_key**
  Definition:

  .. code-block:: python

      def reduce_by_key(self, func)

  Similar to the regular reduce, with the only difference that the elements of the DDS considered to be
  (key, value) tuples at the beginning of the reduction.

  The results can be retrieved as a dictionary in the master node, or as *Future Objects* of ``(key, value)``
  pairs where keys are unique, and values are reduced results for each key.

  .. HINT::

      Usage sample:

      .. code-block:: python

          >>> DDS().load([("a",1), ("a",2)]).reduce_by_key((lambda a, b: a+b)).collect()
          [('a', 3)]

.. _dds_count_by_key:

**count_by_key**
  Definition:

  .. code-block:: python

      def count_by_key(self, as_dict=False)

  Count by key.
  It is able to return the result as dictionary by setting ``as_dict`` to ``True``.

  .. HINT::

      Usage sample:

      .. code-block:: python

          >>> DDS().load([("a", 100), ("a", 200)]).count_by_key(True)
          {'a': 2}

.. _dds_sort_by_key:

**sort_by_key**
  Definition:

  .. code-block:: python

      def sort_by_key(self, ascending=True, num_of_parts=None, key_func=lambda x: x)

  Sort by key.
  It is able to perform the sorting ascending (default) or descending (if ``ascending=False``)
  using the given ``key_func`` function.

.. _dds_group_by_key:

**group_by_key**
  Definition:

  .. code-block:: python

      def group_by_key(self, num_of_parts=-1)

  Group values of each key in a single list.
  It is a special and most used case of ``combine_by_key``.

  .. HINT::

      Usage sample:

      .. code-block:: python

          >>> x = DDS().load([("a", 1), ("b", 2), ("a", 2), ("b", 4)])
          >>> sorted(x.group_by_key().collect())
          [('a', [1, 2]), ('b', [2, 4])]

Examples
~~~~~~~~

.. toctree::
    :maxdepth: 2
    :caption: Table of Contents

    05_DDS_examples/01_Wordcount
    05_DDS_examples/02_Pi_estimation
    05_DDS_examples/03_Terasort
    05_DDS_examples/04_Inverted_indexing
    05_DDS_examples/05_Transitive_closure
