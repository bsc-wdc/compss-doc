Jupyter Notebook
================

Notebook execution
~~~~~~~~~~~~~~~~~~

The jupyter notebook can be executed as a common Jupyter notebook by steps or
the whole application.

.. IMPORTANT::

   A message showing the failed task/s will pop up if an exception within them
   happens.

   This pop up message will also allow you to continue the execution without
   PyCOMPSs, or to restart the COMPSs runtime. Please, note that in the case
   of COMPSs restart, the tracking of some objects may be lost (will need to be
   recomputed).


Notebook example
~~~~~~~~~~~~~~~~

Sample notebooks can be found in the :ref:`Sections/09_PyCOMPSs_Notebooks:PyCOMPSs Notebooks` Section.


Tips and Tricks
~~~~~~~~~~~~~~~

Tasks information
^^^^^^^^^^^^^^^^^

It is possible to show task related information with ``tasks_info`` function.

.. code-block:: python

    # Previous user code

    import pycompss.interactive as ipycompss
    ipycompss.start(graph=True)

    # User code that calls tasks

    # Check the current tasks info
    ipycompss.tasks_info()

    ipycompss.stop(sync=True)

    # Subsequent code

.. IMPORTANT::

    The tasks information will not be displayed if the ``monitor`` option at
    ``ipycompss.start`` is not set (to a refresh value).

The ``tasks_info`` function provides a widget that can be updated while running
other cells from the notebook, and will keep updating every second until stopped.
Alternatively, it will show a snapshot of the tasks information status if ipywidgets is
not available.

The information displayed is composed by two plots: the left plot shows the
average time per task, while the right plot shows the amount of tasks.
Then, a table with the specific number of number of executed tasks,
maximum execution time, mean execution time and minimum execution time, per task
is shown.

Tasks status
^^^^^^^^^^^^

It is possible to show task status (running or completed) tasks with the
``tasks_status`` function.

.. code-block:: python

    # Previous user code

    import pycompss.interactive as ipycompss
    ipycompss.start(graph=True)

    # User code that calls tasks

    # Check the current tasks info
    ipycompss.tasks_status()

    ipycompss.stop(sync=True)

    # Subsequent code

.. IMPORTANT::

    The tasks information will not be displayed if the ``monitor`` option at
    ``ipycompss.start`` is not set (to a refresh value).

The ``tasks_status`` function provides a widget that can be updated while running
other cells from the notebook, and will keep updating every second until stopped.
Alternatively, it will show a snapshot of the tasks status if ipywidgets is
not available.

The information displayed is composed by a pie chart and a table showing
the number of running tasks, and the number of completed tasks.

Resources status
^^^^^^^^^^^^^^^^

It is possible to show resources status with the ``resources_status`` function.

.. code-block:: python

    # Previous user code

    import pycompss.interactive as ipycompss
    ipycompss.start(graph=True)

    # User code that calls tasks

    # Check the current tasks info
    ipycompss.resources_status()

    ipycompss.stop(sync=True)

    # Subsequent code

.. IMPORTANT::

    The tasks information will not be displayed if the ``monitor`` option at
    ``ipycompss.start`` is not set (to a refresh value).

The ``resources_status`` function provides a widget that can be updated while running
other cells from the notebook, and will keep updating every second until stopped.
Alternatively, it will show a snapshot of the resources status if ipywidgets is
not available.

The information displayed is a table showing the number of computing units,
gpus, fpgas, other computing units, amount of memory, amount of disk, status
and actions.


Current task graph
^^^^^^^^^^^^^^^^^^

It is possible to show the current task graph with the ``current_task_graph``
function.

.. code-block:: python

    # Previous user code

    import pycompss.interactive as ipycompss
    ipycompss.start(graph=True)

    # User code that calls tasks

    # Check the current task graph
    ipycompss.current_task_graph()

    ipycompss.stop(sync=True)

    # Subsequent code


.. IMPORTANT::

    The graph will not be displayed if the ``graph`` option at
    ``ipycompss.start`` is not set to ``true``.

In addition, the ``current_task_graph`` has some options. Specifically, its
full signature is:

.. code-block:: python

     current_task_graph(fit=False, refresh_rate=1, timeout=0)

Parameters:

    ``fit``
        Adjust the size to the available space in jupyter if set to true.
        Display full size if set to false (default).

    ``refresh_rate``
        When *timeout* is set to a value different from 0, it defines the
        number of seconds between graph refresh.

    ``timeout``
        Check the current task graph during the *timeout* value (seconds).
        During the *timeout* value, it refresh the graph considering the
        *refresh_rate* value.
        It can be stopped with the stop button of Jupyter.
        Does not update the graph if set to 0 (default).


.. CAUTION::

    The graph can be empty if all pending tasks have been completed.


Complete task graph
^^^^^^^^^^^^^^^^^^^

It is possible to show the complete task graph with the ``complete_task_graph``
function.

.. code-block:: python

    # Previous user code

    import pycompss.interactive as ipycompss
    ipycompss.start(graph=True)

    # User code that calls tasks

    # Check the current task graph
    ipycompss.complete_task_graph()

    ipycompss.stop(sync=True)

    # Subsequent code


.. IMPORTANT::

    The graph will not be displayed if the ``graph`` option at
    ``ipycompss.start`` is not set to ``true``.


In addition, the ``complete_task_graph`` has some options. Specifically, its
full signature is:

.. code-block:: python

     complete_task_graph(fit=False, refresh_rate=1, timeout=0)

Parameters:

    ``fit``
        Adjust the size to the available space in jupyter if set to true.
        Display full size if set to false (default).

    ``refresh_rate``
        When *timeout* is set to a value different from 0, it defines the
        number of seconds between graph refresh.

    ``timeout``
        Check the current task graph during the *timeout* value (seconds).
        During the *timeout* value, it refresh the graph considering the
        *refresh_rate* value.
        It can be stopped with the stop button of Jupyter.
        Does not update the graph if set to 0 (default).


.. CAUTION::

    The graph may be empty or raise an exception if the graph has not been
    updated by the runtime (may happen if there are too few tasks).
    In this situation, stop the compss runtime (synchronizing the remaining
    objects if intended to start the runtime afterwards) and try again.
