Application graph
=================

At the end of the application execution a dependency graph can be
generated representing the order of execution of each type of task and
their dependencies. To allow the final graph generation the ``-g`` flag
has to be passed to the ``runcompss`` command (alternative flags to the
``-g`` are the ``--graph`` or the ``--graph=true``); the graph file is
written in the ``<BASE_LOG_DIR>/monitor/complete_graph.dot`` at the end
of the execution (``<BASE_LOG_DIR>`` is usually ``$HOME/.COMPSs`` unless
the ``--base_log_dir=<BASE_LOG_DIR>`` flag is specified).

.. WARNING::

    Application graph generation is **not supported using agents**.


:numref:`complete_graph` shows a dependency graph example of a
*SparseLU* Java application. The graph can be converted from *dot* format to
*pdf* format by running the following command:

.. code-block:: console

    compss@bsc:~$ compss_gengraph ~/.COMPSs/sparseLU.arrays.SparseLU_01/monitor/complete_graph.dot

.. figure:: ./Figures/dependency_graph.jpeg
   :name: complete_graph
   :alt: The dependency graph of the SparseLU application
   :align: center
   :width: 25.0%

   The dependency graph of the SparseLU application
