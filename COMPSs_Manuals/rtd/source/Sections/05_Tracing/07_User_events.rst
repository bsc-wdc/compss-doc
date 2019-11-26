User Events in Python
=====================

Users can emit custom events inside their python **tasks**. Thanks to
the fact that python isn’t a compiled language, users can emit events
inside their own tasks using the available extrae instrumentation object
because it is already imported.  

To emit an event first ``import pyextrae`` just use the call
``pyextrae.event(type, id)`` or ``pyextrae.eventand``
``counters (type, id)`` if you also want to emit PAPI hardware counters.
It is recommended to use a type number higher than 8000050 in order to
avoid type’s conflicts. This events will appear automatically on the
generated trace. In order to visualize them, take, for example,
``compss_runtime.cfg`` and go to
``Window Properties -> Filter -> Events`` ``-> Event Type`` and change
the value labeled *Types* for your custom events type. If you want to
name the events, you will need to manually add them to the .pcf file.
Paraver uses by default the .pcf with the same name as the tracefile so
if you add them to one, you can reuse it just by changing its name to
the tracefile.q  

More information and examples of common python usage can be found under
the default directory
``/opt/COMPSs/Dependencies/extrae/share/examples/PYTHON``.


.. figure:: /Logos/bsc_logo.jpg
   :width: 40.0%
   :align: center
