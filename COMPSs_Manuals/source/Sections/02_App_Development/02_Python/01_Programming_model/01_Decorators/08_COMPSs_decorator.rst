@compss
=======

The ``@compss`` (or ``@COMPSs``) decorator shall be used to define that a task is
going to be a COMPSs application (:numref:`compss_task_python`).
It enables to have nested COMPSs applications.

Definition
----------

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


Summary
-------

Next table summarizes the parameters of this decorator. Please note that ``working_dir`` and ``args`` are the only decorator properties that can contain task parameters
defined in curly braces.

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
