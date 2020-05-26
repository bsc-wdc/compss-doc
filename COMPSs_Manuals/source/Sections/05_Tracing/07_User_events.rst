User Events in Python
=====================

Users can emit custom events inside their python **tasks**. Thanks to
the fact that python is not a compiled language, users can emit events
inside their own tasks using the available EXTRAE instrumentation object
because it is already loaded and available in the PYTHONPATH when
running with tracing enabled.  

To emit an event first import pyextrae using
``import pyextrae.multiprocessing as pyextrae``, and then just use the call
``pyextrae.event(type, id)`` (or ``pyextrae.eventandcounters (type, id)`` if
you also want to emit PAPI hardware counters).

.. TIP::

    It is recommended to use a type number higher than 8000050 in order to
    avoid type conflicts.

Usage example:

.. code-block:: python

    from pycompss.api.task import task

    @task()
    def compute():
        import pyextrae.multiprocessing as pyextrae
        pyextrae.eventandcounters(9000000, 2)
        ...
        # Code to wrap within event 2
        ...
        pyextrae.eventandcounters(9000000, 0)

.. IMPORTANT::

    Please, note that the ``import pyextrae.multiprocessing as pyextrae`` is
    performed within the task. If the user needs to add more events to tasks
    within the same module and wants to put this import in the top of the
    module making ``pyextrae`` available for all of them, it is necessary to
    enable the tracing hook on the tasks that emit events:

    .. code-block:: python

        from pycompss.api.task import task
        import pyextrae.multiprocessing as pyextrae

        @task(tracing_hook=True)
        def compute():
            pyextrae.eventandcounters(9000000, 2)
            ...
            # Code to wrap within event 2
            ...
            pyextrae.eventandcounters(9000000, 0)

    The ``tracing_hook`` is disabled by default in order to reduce the overhead
    introduced by tracing avoiding to intercept all function calls within the
    task code.


This events will appear automatically on the generated trace.
In order to visualize them, take, for example, ``compss_runtime.cfg`` and go
to ``Window Properties -> Filter -> Events`` ``-> Event Type`` and change
the value labeled *Types* for your custom events type.

.. TIP::

    If you want to name the events, you will need to manually add them to the
    ``.pcf`` file.

    Paraver uses by default the ``.pcf`` with the same name as the tracefile so
    if you add them to one, you can reuse it just by changing its name to
    the tracefile.

More information and examples of common python usage can be found under
the default directory ``/<INSTALLATION_PATH>/COMPSs/Dependencies/extrae/share/examples/PYTHON``.
