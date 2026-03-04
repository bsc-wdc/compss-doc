|:desktop:| Monitor
###################

COMPSs includes a Web graphical interface (COMPSs Monitor) that can be used
to monitor the execution of COMPSs applications.

The COMPSs Monitor supported features available through the graphical interface are:

-  **Resources information**: Provides information about the resources
   used by the application.

-  **Tasks information**: Provides information about the tasks definition
   used by the application.

-  **Current tasks graph**: Shows the tasks dependency graph currently
   stored into the COMPSs Runtime.

-  **Complete tasks graph**: Shows the complete tasks dependency graph of
   the application.

-  **Load chart**: Shows different dynamic charts representing the
   evolution over time of the resources load and the tasks load.

-  **Runtime log**: Shows the runtime log.

-  **Execution Information**: Shows specific job information allowing
   users to easily select failed or uncompleted jobs.

-  **Statistics**: Shows application statistics such as the accumulated
   cloud cost.


.. IMPORTANT::
   To enable the COMPSs Monitor, add the ``-m`` flag in your ``runcompss``
   or ``enqueue_compss`` command.

The webpage also allows users to configure some performance parameters
of the monitoring service by accessing the *Configuration* button at the
top-right corner of the web page.

Check the specific instructions depending on your infrastructure:

.. grid:: 1 1 2 2
    :gutter: 2

    .. grid-item-card:: Local
        :link: 02_Monitor/01_Local
        :link-type: doc
        :text-align: center

        :material-twotone:`lan;3em`

    .. grid-item-card:: Supercomputer
        :link: 02_Monitor/02_Supercomputer
        :link-type: doc
        :text-align: center

        :material-twotone:`storage;3em`

For specific COMPSs Monitor feature configuration please check our *FAQ*
section at the top-right corner of the web page.

.. toctree::
    :hidden:
    :maxdepth: 3
    :caption: Table of Contents

    02_Monitor/01_Local
    02_Monitor/02_Supercomputer
