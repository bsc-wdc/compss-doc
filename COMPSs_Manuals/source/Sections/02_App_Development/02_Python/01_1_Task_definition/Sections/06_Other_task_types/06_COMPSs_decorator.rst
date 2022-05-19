COMPSs decorator
^^^^^^^^^^^^^^^^

The *@compss* (or @COMPSs) decorator shall be used to define that a task is
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
