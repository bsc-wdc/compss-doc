Running with persistent storage
-------------------------------

Local
~~~~~

In order to run a COMPSs application locally, the ``runcompss`` command is used.

The ``runcompss`` command includes some flags to execute the application
considering a running persistent storage framework. These flags are:
``--classpath``, ``--pythonpath`` and ``--storage_conf``.

Consequently, the ``runcompss`` requirements to run an application with a
running persistent storage backend are:

--classpath
    Add the ``--classpath=${path_to_storage_api.jar}`` flag to the
    ``runcompss`` command.

--pythonpath
    If you are running a python application, also add the
    ``--pythonpath=${path_to_the_storage_api}/python``
    flag to the ``runcompss`` command.

--storage_conf
    Add the flag ``--storage_conf=${path_to_your_storage_conf_dot_cfg_file}``
    to the ``runcompss`` command. The storage configuration file (usually
    ``storage_conf.cfg``) contains the configuration parameters needed by the
    storage framework for the execution (it depends on the storage framework).


As usual, the ``project.xml`` and ``resources.xml`` files must be correctly set.

Supercomputer
~~~~~~~~~~~~~

In order to run a COMPSs application in a Supercomputer or cluster, the
``enqueue_compss`` command is used.

The ``enqueue_compss`` command includes some flags to execute the application
considering a running persistent storage framework. These flags are:
``--classpath``, ``--pythonpath``, ``--storage-home`` and ``--storage-props``.

Consequently, the ``enqueue_compss`` requirements to run an application with a
running persistent storage backend are:

--classpath
    ``--classpath=${path_to_storage_interface.jar}`` As with the ``runcompss``
    command, the JAR with the storage API must be specified. It is usally
    available in a environment variable (check the persistent storage framework).

--pythonpath
    If you are running a Python application, also add the
    ``--pythonpath=${path_to_the_storage_api}/python`` flag.
    It is usally available in a environment variable (check the persistent
    storage framework).

--storage-home
    ``--storage-home=${path_to_the_storage_api}`` This must point to
    the root of the storage folder. This folder must contain a ``scripts``
    folder where the scripts to start and stop the persistent framework are.
    It is usally available in a environment variable (check the persistent
    storage framework).

--storage-props
    ``--storage-props=${path_to_the_storage_props_file}`` This must point
    to the storage properties configuration file (usually ``storage_props.cfg``)
    It contains the configuration parameters needed by the storage framework
    for the execution (it depends on the storage framework).
