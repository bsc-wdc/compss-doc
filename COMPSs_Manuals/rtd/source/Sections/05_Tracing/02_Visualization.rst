Visualization
=============

Paraver is the BSC tool for trace visualization. Trace events are
encoded in Paraver format (.prv) by the Extrae tool. Paraver is a
powerful tool and allows users to show many views of the trace data
using different configuration files. Users can manually load, edit or
create configuration files to obtain different tracing views.

The following subsections explain how to load a trace file into Paraver,
open the task events view using an already predefined configuration
file, and how to adjust the view to display the data properly.

For further information about Paraver, please visit the following site:

http://www.bsc.es/computer-sciences/performance-tools/paraver

Trace Loading
-------------

The final trace file in Paraver format (.prv) is at the base log folder
of the application execution inside the trace folder. The fastest way to
open it is calling the Paraver binary directly using the tracefile name
as the argument.

.. code-block:: console

    $ wxparaver /path/to/trace/trace.prv

Configurations
--------------

To see the different events, counters and communications that the
runtime generates, diverse configurations are available with the COMPSs
installation. To open one of them, go to the “Load Configuration” option
in the main window and select “File”. The configuration files are under
the following path for the default installation
``/opt/COMPSs/Dependencies/`` ``paraver/cfgs/``. A detailed list of all
the available configurations can be found in :ref:`Paraver: configurations`.

The following guide uses the *compss_tasks.cfg* as an example to
illustrate the basic usage of Paraver. After accepting the load of the
configuration file, another window appears showing the view.
:numref:`tracing_1` and :numref:`tracing_2` show an example of this process.

.. figure:: ./Figures/1.jpeg
   :name: tracing_1
   :alt: Paraver menu
   :align: center
   :width: 25.0%

   Paraver menu

.. figure:: ./Figures/2.jpeg
   :name: tracing_2
   :alt: Trace file
   :align: center
   :width: 60.0%

   Trace file

View Adjustment
---------------

In a Paraver view, a red exclamation sign may appear in the bottom-left
corner (see :numref:`tracing_2` in the previous section). This means
that some event values are not being shown (because they are out of the
current view scope), so little adjustments must be made to view the
trace correctly:

-  Fit window: modifies the view scope to fit and display all the events
   in the current window.

   -  Right click on the trace window

   -  Choose the option Fit Semantic Scale / Fit Both

.. figure:: ./Figures/3.jpeg
   :name: tracing_3
   :alt: Paraver view adjustment: Fit window
   :align: center
   :width: 60.0%

   Paraver view adjustment: Fit window

-  View Event Flags: marks with a green flag all the emitted the events.

   -  Right click on the trace window

   -  Chose the option View / Event Flags

.. figure:: ./Figures/4.jpeg
   :name: tracing_4
   :alt: Paraver view adjustment: View Event Flags
   :align: center
   :width: 60.0%

   Paraver view adjustment: View Event Flags

-  Show Info Panel: display the information panel. In the tab “Colors”
   we can see the legend of the colors shown in the view.

   -  Right click on the trace window

   -  Check the Info Panel option

   -  Select the Colors tab in the panel

.. figure:: ./Figures/5.jpeg
   :name: tracing_5
   :alt: Paraver view adjustment: Show info panel
   :align: center
   :width: 60.0%

   Paraver view adjustment: Show info panel

-  Zoom: explore the tracefile more in-depth by zooming into the most
   relevant sections.

   -  Select a region in the trace window to see that region in detail

   -  Repeat the previous step as many times as needed

   -  The undo-zoom option is in the right click panel

.. figure:: ./Figures/6.jpeg
   :name: tracing_6
   :alt: Paraver view adjustment: Zoom configuration
   :align: center
   :width: 60.0%

   Paraver view adjustment: Zoom configuration

.. figure:: ./Figures/6_2.jpeg
   :name: tracing_6_2
   :alt: Paraver view adjustment: Zoom configuration
   :align: center
   :width: 60.0%

   Paraver view adjustment: Zoom configuration


.. figure:: /Logos/bsc_logo.jpg
   :width: 40.0%
   :align: center
