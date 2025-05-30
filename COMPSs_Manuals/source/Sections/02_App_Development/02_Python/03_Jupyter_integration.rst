.. |pyjbr| raw:: html

   <br />

Integration with Jupyter notebook
---------------------------------

PyCOMPSs can also be used within Jupyter notebooks. This feature allows
users to develop and run their PyCOMPSs applications in a Jupyter
notebook, where it is possible to modify the code during the execution
and experience an interactive behavior.

Environment Variables
~~~~~~~~~~~~~~~~~~~~~

The following libraries must be present in the appropriate environment
variables in order to enable PyCOMPSs within Jupyter notebook:

PYTHONPATH
    The path where PyCOMPSs is installed (e.g. ``/opt/COMPSs/Bindings/python/``).
    Please, note that the path contains the folder ``2`` and/or ``3``. This is
    due to the fact that PyCOMPSs is able to choose the appropriate one depending
    on the kernel used with jupyter.

LD_LIBRARY_PATH
    The path where the ``libbindings-commons.so`` library is located
    (e.g. ``<COMPSS_INSTALLATION_PATH>/Bindings/bindings-common/lib/``)
    and the path where the ``libjvm.so`` library is located (e.g.
    ``/usr/lib/jvm/java-11-openjdk/jre/lib/amd64/server/``).

API calls
~~~~~~~~~

In this case, the user is responsible of **starting** and **stopping** the
COMPSs runtime during the jupyter notebook execution. |pyjbr|
To this end, PyCOMPSs provides a module with two main API calls:
one for starting the COMPSs runtime, and another for stopping it.

This module can be imported from the *pycompss* library:

.. code-block:: python

    import pycompss.interactive as ipycompss

And contains two main functions: *start* and *stop*. These functions can
then be invoked as follows for the COMPSs runtime deployment with
default parameters:

.. code-block:: python

    # Previous user code/cells

    import pycompss.interactive as ipycompss
    ipycompss.start()

    # User code/cells that can benefit from PyCOMPSs

    ipycompss.stop()

    # Subsequent code/cells

Between the *start* and *stop* function calls, the user can write its
own python code including PyCOMPSs imports, decorators and
synchronization calls described in the
:ref:`Sections/02_App_Development/02_Python/01_Programming_model:Programming Model` Section.
The code can be split into multiple cells.

The *start* and *stop* functions accept parameters in order to customize
the COMPSs runtime (such as the flags that can be selected with the
``runcompss`` command). :numref:`start_jupyter` summarizes
the accepted parameters of the *start* function. :numref:`stop_jupyter`
summarizes the accepted parameters of
the *stop* function.


.. table:: PyCOMPSs **start** function for Jupyter notebook
    :name: start_jupyter

    +-----------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Parameter Name                    | Parameter Type | Description                                                                                                                                                                                                                                                                                                                                                                                                   |
    +===================================+================+===============================================================================================================================================================================================================================================================================================================================================================================================================+
    | ``log_level``                     | String         | Log level |pyjbr| Options: ``"off"``, ``"info"`` and ``"debug"``. |pyjbr| (Default: ``"off"``)                                                                                                                                                                                                                                                                                                                |
    +-----------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``debug``                         | Boolean        | COMPSs runtime debug |pyjbr| (Default: ``False``) (overrides log level)                                                                                                                                                                                                                                                                                                                                       |
    +-----------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``o_c``                           | Boolean        | Object conversion to string when possible |pyjbr| (Default: ``False``)                                                                                                                                                                                                                                                                                                                                        |
    +-----------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``graph``                         | Boolean        | Task dependency graph generation |pyjbr| (Default: ``False``)                                                                                                                                                                                                                                                                                                                                                 |
    +-----------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``trace``                         | Boolean        | Paraver trace generation |pyjbr| (Default: ``False``)                                                                                                                                                                                                                                                                                                                                                         |
    +-----------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``monitor``                       | Integer        | Monitor refresh rate |pyjbr| (Default: ``None`` - Monitoring disabled)                                                                                                                                                                                                                                                                                                                                        |
    +-----------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``project_xml``                   | String         | Path to the project XML file |pyjbr| (Default: ``"$COMPSS/Runtime/configuration/xml/projects/default project.xml"``)                                                                                                                                                                                                                                                                                          |
    +-----------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``resources_xml``                 | String         | Path to the resources XML file |pyjbr| (Default: ``"$COMPSs/Runtime/configuration/xml/resources/default resources.xml"``)                                                                                                                                                                                                                                                                                     |
    +-----------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``summary``                       | Boolean        | Show summary at the end of the execution |pyjbr| (Default: ``False``)                                                                                                                                                                                                                                                                                                                                         |
    +-----------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``storage_impl``                  | String         | Path to an storage implementation |pyjbr| (Default: ``None``)                                                                                                                                                                                                                                                                                                                                                 |
    +-----------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``storage_conf``                  | String         | Storage configuration file path |pyjbr| (Default: ``None``)                                                                                                                                                                                                                                                                                                                                                   |
    +-----------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``task_count``                    | Integer        | Number of task definitions |pyjbr| (Default: ``50``)                                                                                                                                                                                                                                                                                                                                                          |
    +-----------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``app_name``                      | String         | Application name |pyjbr| (Default: ``"Interactive"``)                                                                                                                                                                                                                                                                                                                                                         |
    +-----------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``uuid``                          | String         | Application uuid |pyjbr| (Default: ``None`` - Will be random)                                                                                                                                                                                                                                                                                                                                                 |
    +-----------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``base_log_dir``                  | String         | Base directory to store COMPSs log files (a .COMPSs/ folder will be created inside this location)|pyjbr| (Default: User ``$HOME`` path)                                                                                                                                                                                                                                                                       |
    +-----------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``specific_log_dir``              | String         | Use a specific directory to store COMPSs log files (the folder MUST exist and no sandbox is created) |pyjbr| (Default: ``Disabled``)                                                                                                                                                                                                                                                                          |
    +-----------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``extrae_cfg``                    | String         | Sets a custom Extrae config file. Must be in a shared disk between all COMPSs workers |pyjbr| (Default: ``None``)                                                                                                                                                                                                                                                                                             |
    +-----------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``comm``                          | String         | Class that implements the adaptor for communications. Supported adaptors: |pyjbr| - ``"es.bsc.compss.nio.master.NIOAdaptor"`` |pyjbr| - ``"es.bsc.compss.gat.master.GATAdaptor"`` |pyjbr| (Default: ``"es.bsc.compss.nio.master.NIOAdaptor"``)                                                                                                                                                                |
    +-----------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``conn``                          | String         | Class that implements the runtime connector for the cloud. Supported connectors: |pyjbr| - ``"es.bsc.compss.connectors.DefaultSSHConnector"`` |pyjbr| - ``"es.bsc.compss.connectors.DefaultNoSSHConnector"`` (Default: ``"es.bsc.compss.connectors.DefaultSSHConnector"``)                                                                                                                                    |
    +-----------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``master_name``                   | String         | Hostname of the node to run the COMPSs master |pyjbr| (Default: ``""``)                                                                                                                                                                                                                                                                                                                                       |
    +-----------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``master_port``                   | String         | Port to run the COMPSs master communications (Only for NIO adaptor) |pyjbr| (Default: ``"[43000,44000]"``)                                                                                                                                                                                                                                                                                                    |
    +-----------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``scheduler``                     | String         | Class that implements the Scheduler for COMPSs. Supported schedulers: |pyjbr| - ``"es.bsc.compss.scheduler.fullGraphScheduler.FullGraphScheduler"`` |pyjbr| - ``"es.bsc.compss.scheduler.fifoScheduler.FIFOScheduler"`` |pyjbr| - ``"es.bsc.compss.scheduler.resourceEmptyScheduler. ResourceEmptyScheduler"`` |pyjbr| (Default: ``"es.bsc.compss.scheduler.loadBalancingScheduler.LoadBalancingScheduler"``) |
    +-----------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``jvm_workers``                   | String         | Extra options for the COMPSs Workers JVMs. Each option separated by "," and without blank spaces |pyjbr| (Default: ``"-Xms1024m,-Xmx1024m,-Xmn400m"``)                                                                                                                                                                                                                                                        |
    +-----------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``cpu_affinity``                  | String         | Sets the CPU affinity for the workers. |pyjbr| Supported options: ``"disabled"``, ``"automatic"``, user defined map of the form ``"0-8/9,10,11/12-14,15,16"`` |pyjbr| (Default: ``"automatic"``)                                                                                                                                                                                                              |
    +-----------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``gpu_affinity``                  | String         | Sets the GPU affinity for the workers. |pyjbr| Supported options: ``"disabled"``, ``"automatic"``, user defined map of the form ``"0-8/9,10,11/12-14,15,16"`` |pyjbr| (Default: ``"automatic"``)                                                                                                                                                                                                              |
    +-----------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``profile_input``                 | String         | Path to the file which stores the input application profile |pyjbr| (Default: ``""``)                                                                                                                                                                                                                                                                                                                         |
    +-----------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``profile_output``                | String         | Path to the file to store the application profile at the end of the execution |pyjbr| (Default: ``""``)                                                                                                                                                                                                                                                                                                       |
    +-----------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``scheduler_config``              | String         | Path to the file which contains the scheduler configuration |pyjbr| (Default: ``""``)                                                                                                                                                                                                                                                                                                                         |
    +-----------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``external_adaptation``           | Boolean        | Enable external adaptation (this option will disable the Resource Optimizer) |pyjbr| (Default: ``False``)                                                                                                                                                                                                                                                                                                     |
    +-----------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``propagate_virtual_environment`` | Boolean        | Propagate the master virtual environment to the workers |pyjbr| (Default: ``False``)                                                                                                                                                                                                                                                                                                                          |
    +-----------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``verbose``                       | Boolean        | Verbose mode |pyjbr| (Default: ``False``)                                                                                                                                                                                                                                                                                                                                                                     |
    +-----------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. table:: PyCOMPSs **stop** function for Jupyter notebook
    :name: stop_jupyter

    +----------------+----------------+---------------------------------------------------------------------------------+
    | Parameter Name | Parameter Type | Description                                                                     |
    +================+================+=================================================================================+
    | ``sync``       | Boolean        |  Synchronize the objects left on the user scope. |pyjbr| (Default: ``False``)   |
    +----------------+----------------+---------------------------------------------------------------------------------+


The following code snippet shows how to start a COMPSs runtime with
tracing and graph generation enabled (with *trace* and *graph*
parameters), as well as enabling the monitor with a refresh rate of 2
seconds (with the *monitor* parameter). It also synchronizes all
remaining objects in the scope with the *sync* parameter when invoking
the *stop* function.

.. code-block:: python

    # Previous user code

    import pycompss.interactive as ipycompss
    ipycompss.start(graph=True, trace=True, monitor=2000)

    # User code that can benefit from PyCOMPSs

    ipycompss.stop(sync=True)

    # Subsequent code


.. ATTENTION::

   Once the COMPSs runtime has been stopped it, the value of the variables that
   have not been synchronized will be lost.


Notebook execution
~~~~~~~~~~~~~~~~~~

The application can be executed as a common Jupyter notebook by steps or
the whole application.

.. IMPORTANT::

   A message showing the failed task/s will pop up if an exception within them
   happens.

   This pop up message will also allow you to continue the execution without
   PyCOMPSs, or to restart the COMPSs runtime. Please, note that in the case
   of COMPSs restart, the tracking of some objects may be lost (will need to be
   recomputed).

More information on the Notebook execution can be found in the Execution
Environments :ref:`Sections/03_Execution_Environments/03_Deployments/01_Master_worker/05_Jupyter_notebook:Jupyter notebook` Section.

Notebook example
~~~~~~~~~~~~~~~~

Sample notebooks can be found in the :ref:`Sections/09_PyCOMPSs_Notebooks:PyCOMPSs Notebooks` Section.
