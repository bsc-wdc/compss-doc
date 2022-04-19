Application graph
=================

At the end of the application execution a dependency graph can be
generated representing the order of execution of each type of task and
their dependencies. To allow the final graph generation the ``-g`` flag
has to be passed to the ``runcompss`` command; the graph file is written
in the ``base_log_folder/monitor/complete_graph.dot`` at the end of the
execution.

:numref:`complete_graph` shows a dependency graph example of a
*SparseLU* java application. The graph can be visualized by running the
following command:

.. code-block:: console

    compss@bsc:~$ compss_gengraph ~/.COMPSs/sparseLU.arrays.SparseLU_01/monitor/complete_graph.dot

.. figure:: ./Figures/dependency_graph.jpeg
   :name: complete_graph
   :alt: The dependency graph of the SparseLU application
   :align: center
   :width: 25.0%

   The dependency graph of the SparseLU application
