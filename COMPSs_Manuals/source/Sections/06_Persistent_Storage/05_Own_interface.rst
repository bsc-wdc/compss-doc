Implement your own Storage interface for COMPSs
===============================================

In order to implement an interface for a Storage framework, it is necessary to
implement the Java SRI (mandatory), and depending on the desired language,
implement the Python SRI and the specific SOI inheriting from the generic SOI
provided by COMPSs.


Generic Storage Object Interface
--------------------------------

:numref:`sco_object_definition` shows the functions that must exist in the storage
object interface, that enables the object that inherits it to interact with the
storage framework.

.. table:: SCO object definition
    :name: sco_object_definition

    +---------------------------+---------+-----------------------------------------------------------------------------------------+
    | Name                      | Returns | Comments                                                                                |
    +===========================+=========+=========================================================================================+
    | Constructor               | Nothing | | Instantiates the object.                                                              |
    +---------------------------+---------+-----------------------------------------------------------------------------------------+
    | get_by_alias(String id)   | Object  | | Retrieve the object with alias "name".                                                |
    +---------------------------+---------+-----------------------------------------------------------------------------------------+
    | makePersistent(String id) | Nothing | | Inserts the object in the storage framework with the id.                              |
    |                           |         | | If id is null, a random UUID will be computed instead.                                |
    +---------------------------+---------+-----------------------------------------------------------------------------------------+
    | deletePersistent()        | Nothing | | Removes the object from the storage.                                                  |
    |                           |         | | It does nothing if it was not already there.                                          |
    +---------------------------+---------+-----------------------------------------------------------------------------------------+
    | getID()                   | String  | | Returns the current object identifier if the object is not persistent (null instead). |
    +---------------------------+---------+-----------------------------------------------------------------------------------------+

For example, the **makePersistent** function is intended to store the object
content into the persistent storage, **deletePersistent** to remove it, and
**getID** to provide the object identifier.

.. important::
   An object will be considered persisted if the ``getID`` function retrieves
   something different from ``None``.

This interface must be implemented in the target language desired (e.g. Java or Python).


Generic Storage Runtime Interfaces
----------------------------------

:numref:`java_api` shows the functions that must exist in the storage
runtime interface, that enables the COMPSs runtime to interact with the
storage framework.

.. table:: Java API
    :name: java_api

    +----------------------------------------+--------------+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Name                                   | Returns      | Comments                                    | Signature                                                                                                                                            |
    +========================================+==============+=============================================+======================================================================================================================================================+
    | | init(String storage_conf)            | Nothing      | | Do any initialization action before       | public static void init(String storageConf) throws StorageException {}                                                                               |
    |                                        |              | | starting to execute the application.      |                                                                                                                                                      |
    |                                        |              | | Receives the storage configuration        |                                                                                                                                                      |
    |                                        |              | | file path defined in the ``runcompss``    |                                                                                                                                                      |
    |                                        |              | | or ``enqueue_composs`` command.           |                                                                                                                                                      |
    +----------------------------------------+--------------+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
    | | finish()                             | Nothing      | | Do any finalization action after          | public static void finish() throws StorageException                                                                                                  |
    |                                        |              | | executing the application.                |                                                                                                                                                      |
    +----------------------------------------+--------------+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
    | | getLocations(String id)              | List<String> | | Retrieve the locations where a particular | public static List<String> getLocations(String id) throws StorageException                                                                           |
    |                                        |              | | object is from its identifier.            |                                                                                                                                                      |
    +----------------------------------------+--------------+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
    | | getByID(String id)                   | Object       | | Retrieve an object from its identifier.   | public static Object getByID(String id) throws StorageException                                                                                      |
    |                                        |              |                                             |                                                                                                                                                      |
    +----------------------------------------+--------------+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
    | | newReplica(String id,                | String       | | Create a new replica of an object in the  | public static void newReplica(String id, String hostName) throws StorageException                                                                    |
    | |            String hostName)          |              | | storage framework.                        |                                                                                                                                                      |
    +----------------------------------------+--------------+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
    | | newVersion(String id,                | String       | | Create a new version of an object in the  | public static String newVersion(String id, String hostName) throws StorageException                                                                  |
    | |            String hostname)          |              | | storage framework.                        |                                                                                                                                                      |
    +----------------------------------------+--------------+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
    | | consolidateVersion(String id)        | Nothing      | | Consolidate a version of an object in the | public static void consolidateVersion(String idFinal) throws StorageException                                                                        |
    |                                        |              | | storage framework.                        |                                                                                                                                                      |
    +----------------------------------------+--------------+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
    | | executeTask(String id, ...)          | String       | | Execute the task into the datastore.      | public static String executeTask(String id, String descriptor, Object[] values, String hostName, CallbackHandler callback) throws StorageException   |
    |                                        |              |                                             |                                                                                                                                                      |
    +----------------------------------------+--------------+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
    | | getResult(CallbackEvent event())     | Object       | | Retrieve the result of the execution into | public static Object getResult(CallbackEvent event) throws StorageException                                                                          |
    |                                        |              | | the storage framework.                    |                                                                                                                                                      |
    +----------------------------------------+--------------+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+

This functions enable the COMPSs runtime to keep the data consistency through
the distributed execution.

In addition, :numref:`python_api` shows the functions that must exist in the storage
runtime interface, that enables the COMPSs Python binding to interact with the
storage framework. It is only necessary if the target language is Python.

.. table:: Python API
    :name: python_api

    +---------------------------+---------+-----------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
    | Name                      | Returns | Comments                                                                          | Signature                                                                     |
    +===========================+=========+===================================================================================+===============================================================================+
    | init(String storage_conf) | Nothing | | Do any initialization action before starting to execute the application.        | | def initWorker(config_file_path=None, \*\*kwargs)                           |
    |                           |         | | Receives the storage configuration file path defined in the ``runcompss`` or    | |     # Does not return                                                       |
    |                           |         | | ``enqueue_composs`` command.                                                    |                                                                               |
    +---------------------------+---------+-----------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
    | finish()                  | Nothing | | Do any finalization action after executing the application.                     | | def finishWorker(\*\*kwargs)                                                |
    |                           |         |                                                                                   | |     # Does not return                                                       |
    +---------------------------+---------+-----------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
    | getByID(String id)        | Object  | | Retrieve an object from its identifier.                                         | | def getByID(id)                                                             |
    |                           |         |                                                                                   | |     # Returns the object with Id ‘id’                                       |
    +---------------------------+---------+-----------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
    | TaskContext               | Context | | Define a task context (task enter/exit actions).                                | | class TaskContext(object):                                                  |
    |                           |         |                                                                                   | |                                                                             |
    |                           |         |                                                                                   | |     def __init__(self, logger, values, config_file_path=None, \*\*kwargs):  |
    |                           |         |                                                                                   | |         self.logger = logger                                                |
    |                           |         |                                                                                   | |         self.values = values                                                |
    |                           |         |                                                                                   | |         self.config_file_path = config_file_path                            |
    |                           |         |                                                                                   | |                                                                             |
    |                           |         |                                                                                   | |     def __enter__(self):                                                    |
    |                           |         |                                                                                   | |         # Do something for task prolog                                      |
    |                           |         |                                                                                   | |                                                                             |
    |                           |         |                                                                                   | |     def __exit__(self, type, value, traceback):                             |
    |                           |         |                                                                                   | |         # Do something for task epilog                                      |
    +---------------------------+---------+-----------------------------------------------------------------------------------+-------------------------------------------------------------------------------+


Storage Interface usage
-----------------------

Using ``runcompss``
```````````````````
The first consideration is to deploy the storage framework, and then follow the next
steps:

#. Create a ``storage_conf.cfg`` file with the configuation required by
   the ``init`` SRIs functions.

#. Add the flag ``--classpath=${path_to_SRI.jar}`` to the ``runcompss`` command.

#. Add the flag ``--storage_conf="path to storage_conf.cfg file`` to the ``runcompss`` command.

#. If you are running a Python app, also add the
   ``--pythonpath=${app_path}:${path_to_the_bundle_folder}/python``
   flag to the ``runcompss`` command.

As usual, the ``project.xml`` and ``resources.xml`` files must be
correctly set. It must be noted that there can be nodes that are
not COMPSs nodes (although **this is a highly unrecommended** practice since
they will **always** need data that must be transferred from another node).
Also, any locality policy will likely cause this node to have a very low workload.

Using ``enqueue_compss``
````````````````````````
In order to run a COMPSs + your storage on a queue system the user
must add the following flags to the ``enqueue_compss`` command:

#. ``--storage-home=${path_to_the_user_storage_folder}`` This must point to
   the root of the user storage folder, where the scripts for starting (``storage_init.sh``) and
   stopping (``storage_stop.sh``) the storage framework must exist.

   * ``storage_init.sh`` is called before the application execution and it
      is intended to deploy the storage framework within the nodes provided
      by the queuing system. The parameters that receives are (in order):

      JOBID
         The job identifier provided by the queuing system.

      MASTER_NODE
         The name of the master node considered by COMPSs.

      STORAGE_MASTER_NODE
         The name of the node to be considere the master for the Storage framework.

      WORKER_NODES
         The set of nodes provided by the queuing system that will be considered
         as worker nodes by COMPSs.

      NETWORK
         Network interface (e.g. ib0)

      STORAGE_PROPS
         Storage properties file path (defined as ``enqueue_compss`` flag).

      VARIABLES_TO_BE_SOURCED
         If environment variables for the Storage framework need to be defined
         COMPSs provides an empty file to be filled by the ``storage_init.sh``
         script, that will be sourced afterwards. This file is cleaned inmediately
         after sourcing it.

      STORAGE_CONTAINER_IMAGE
         Storage container image identifier. Used if the storage backend is
         deployed within a container. Default value is ``false`` to identify
         that the storage backend is not within a container.

      STORAGE_CPU_AFFINITY
         CPU affinity for the storage backend.

   * ``storage_stop.sh`` is called after the application execution and it
      is intended to stop the storage framework within the nodes provided
      by the queuing system. The parameters that receives are (in order):

      JOBID
         The job identifier provided by the queuing system.

      MASTER_NODE
         The name of the master node considered by COMPSs.

      STORAGE_MASTER_NODE
         The name of the node to be considere the master for the Storage framework.

      WORKER_NODES
         The set of nodes provided by the queuing system that will be considered
         as worker nodes by COMPSs.

      NETWORK
         Network interface (e.g. ib0)

      STORAGE_PROPS
         Storage properties file path (defined as ``enqueue_compss`` flag).


#. ``--storage-props=${path_to_the_storage_props_file}`` This must point
   to the ``storage_props.cfg`` specific for the storage framework that
   will be used by the start and stop scripts provided in the ``--storage-home``
   path.

#. ``--classpath=${path_to_SRI.jar}`` As in the previous section, the JAR with
   the Java SRI must be specified.

#. If you are running a Python application, also add the
   ``--pythonpath=${app_path}:${path_to_the_user_storage_folder}`` flag, where
   the SOI for Python must exist.
