Other task types
~~~~~~~~~~~~~~~~

In addition to this API functions, the programmer can use a set of
decorators for other purposes.

.. IMPORTANT::

    **NOTE:** If defined, these decorators must be placed after (below) the *@constraint* decorator, and before (on top of) the *@task* decorator.

The following subparagraphs describe their usage.

.. toctree::
    :maxdepth: 4
    :caption: Table of Contents

    06_Other_task_types/01_Binary_decorator
    06_Other_task_types/02_OmpSs_decorator
    06_Other_task_types/03_MPI_decorator
    06_Other_task_types/04_MPMD_MPI_decorator
    06_Other_task_types/05_IO_decorator
    06_Other_task_types/06_COMPSs_decorator
    06_Other_task_types/07_Multinode_decorator
    06_Other_task_types/08_HTTP_decorator
    06_Other_task_types/09_Reduction_decorator
    06_Other_task_types/10_Container_decorator
    06_Other_task_types/11_Software_decorator


Other task types summary
^^^^^^^^^^^^^^^^^^^^^^^^

Next tables summarizes the parameters of these decorators. Please note that 'working_dir' and 'params' ae the only decorator properties that can contain task parameters
defined in curly braces.

* :ref:`sections/02_app_development/02_python/01_1_task_definition/sections/06_Other_task_types/01_Binary_decorator:Binary decorator` (@binary)
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | Parameter              | Description                                                                                                                             |
    +========================+=========================================================================================================================================+
    | **binary**             | (Mandatory) String defining the full path of the binary that must be executed.                                                          |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **working_dir**        | Full path of the binary working directory inside the COMPSs Worker.                                                                     |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **params**             | Params string to be added to end of the execution command of the binary. It can contain python task parameters defined in curly braces. |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+

* :ref:`sections/02_app_development/02_python/01_1_task_definition/sections/06_Other_task_types/02_OmpSs_decorator:OmpSs decorator` (@ompss)
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | Parameter              | Description                                                                                                                       |
    +========================+===================================================================================================================================+
    | **binary**             | (Mandatory) String defining the full path of the binary that must be executed.                                                    |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | **working_dir**        | Full path of the binary working directory inside the COMPSs Worker.                                                               |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+

* :ref:`sections/02_app_development/02_python/01_1_task_definition/sections/06_Other_task_types/03_MPI_decorator:MPI decorator` (@mpi)
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | Parameter              | Description                                                                                                                             |
    +========================+=========================================================================================================================================+
    | **binary**             | String defining the full path of the binary that must be executed. Empty indicates python MPI code.                                     |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **working_dir**        | Full path of the binary working directory inside the COMPSs Worker.                                                                     |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **runner**             | (Mandatory) String defining the MPI runner command.                                                                                     |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **processes**          | Integer defining the number of MPI processes spawned by the task. (Default 1)                                                           |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **processes_per_node** | Integer defining the number of co-allocated MPI processses per node. The ``processes`` value should be multiple of this value           |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **params**             | Params string to be added to end of the execution command of the binary. It can contain python task parameters defined in curly braces. |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+

* :ref:`sections/02_app_development/02_python/01_1_task_definition/sections/06_Other_task_types/04_MPMD_MPI_decorator:MPMD MPI decorator` (@mpmd_mpi)
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | Parameter              | Description                                                                                                                             |
    +========================+=========================================================================================================================================+
    | **runner**             | (Mandatory) String defining the MPMD MPI runner command.                                                                                |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **working_dir**        | Defines mpi job's working directory.                                                                                                    |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **processes_per_node** | Integer defining the number of co-allocated MPI processses per node. The ``processes`` value should be multiple of this value           |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **fail_by_exit_value** | If set to 'False', and ``returns`` value of the 'task' definition is 'int', exit code of the MPI command will be returned.              |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **programs**           | List of single MPI program dictionaries where program specific parameters (``binary``, ``processes``, ``params``) are defined.          |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+

* :ref:`sections/02_app_development/02_python/01_1_task_definition/sections/06_Other_task_types/05_IO_decorator:I/O decorator` (@io)

* :ref:`sections/02_app_development/02_python/01_1_task_definition/sections/06_Other_task_types/06_COMPSs_decorator:COMPSs decorator` (@compss)
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

* :ref:`sections/02_app_development/02_python/01_1_task_definition/sections/06_Other_task_types/07_Multinode_decorator:Multinode decorator` (@multinode)
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | Parameter              | Description                                                                                                                       |
    +========================+===================================================================================================================================+
    | **computing_nodes**    | Integer defining the number of computing nodes reserved for the task execution (only a single node is reserved by default).       |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+

* :ref:`sections/02_app_development/02_python/01_1_task_definition/sections/06_Other_task_types/08_HTTP_decorator:HTTP decorator` (@http)
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | Parameter              | Description                                                                                                                       |
    +========================+===================================================================================================================================+
    | **service_name**       | (Mandatory) Name of the HTTP Service that included at least one HTTP resource in the resources file.                              |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | **resource**           | (Mandatory) URL extension to be concatenated with HTTP resource's base URL.                                                       |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | **request**            | (Mandatory) Type of the HTTP request (GET, POST, etc.).                                                                           |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | **produces**           | In case of JSON responses, produces string defines where the return value(s) is (are) stored in the retrieved JSON string.        |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | **payload**            | Payload string of POST requests if any.                                                                                           |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | **payload_type**       | Payload type of POST requests (e.g: 'application/json').                                                                          |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | **updates**            | To define INOUT parameter key to be updated with a value from HTTP response.                                                      |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+

* :ref:`sections/02_app_development/02_python/01_1_task_definition/sections/06_Other_task_types/09_Reduction_decorator:Reduction decorator` (@reduction)
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | Parameter              | Description                                                                                                                       |
    +========================+===================================================================================================================================+
    | **chunk_size**         |  Size of data fragments to be given as input parameter to the reduction function.                                                 |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+

* :ref:`sections/02_app_development/02_python/01_1_task_definition/sections/06_Other_task_types/10_Container_decorator:Container decorator` (@container)
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | Parameter              | Description                                                                                                                       |
    +========================+===================================================================================================================================+
    | **engine**             |  Container engine to use (e.g. DOCKER or SINGULARITY).                                                                            |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | **image**              |  Container image to be deployed and used for the task execution.                                                                  |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+

* :ref:`sections/02_app_development/02_python/01_1_task_definition/sections/06_Other_task_types/11_Software_decorator:Software decorator` (@software)
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | Parameter              | Description                                                                                                                       |
    +========================+===================================================================================================================================+
    | **config_file**        |  Path to the JSON configuration file.                                                                                             |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+


In addition to the parameters that can be used within the
*@task* decorator, :numref:`supported_streams`
summarizes the *StdIOStream* parameter that can be used within the
*@task* decorator for the function parameters when using the
@binary, @ompss and @mpi decorators. In
particular, the *StdIOStream* parameter is used to indicate that a parameter
is going to be considered as a *FILE* but as a stream (e.g. :math:`>`,
:math:`<` and :math:`2>` in bash) for the @binary,
@ompss and @mpi calls.

.. table:: Supported StdIOStreams for the @binary, @ompss and @mpi decorators
    :name: supported_streams

    +------------------------+-------------------+
    | Parameter              | Description       |
    +========================+===================+
    | **(default: empty)**   | Not a stream.     |
    +------------------------+-------------------+
    | **STDIN**              | Standard input.   |
    +------------------------+-------------------+
    | **STDOUT**             | Standard output.  |
    +------------------------+-------------------+
    | **STDERR**             | Standard error.   |
    +------------------------+-------------------+

Moreover, there are some shorcuts that can be used for files type
definition as parameters within the *@task* decorator (:numref:`file_parameter_definition`).
It is not necessary to indicate the *Direction* nor the *StdIOStream* since it may be already be indicated with
the shorcut.

.. table:: File parameters definition shortcuts
    :name: file_parameter_definition

    +-----------------------------+---------------------------------------------------------+
    | Alias                       | Description                                             |
    +=============================+=========================================================+
    | **COLLECTION(_IN)**         | Type: COLLECTION, Direction: IN                         |
    +-----------------------------+---------------------------------------------------------+
    | **COLLECTION_IN_DELETE**    | Type: COLLECTION, Direction: IN_DELETE                  |
    +-----------------------------+---------------------------------------------------------+
    | **COLLECTION_INOUT**        | Type: COLLECTION, Direction: INOUT                      |
    +-----------------------------+---------------------------------------------------------+
    | **COLLECTION_OUT**          | Type: COLLECTION, Direction: OUT                        |
    +-----------------------------+---------------------------------------------------------+
    | **DICTIONARY(_IN)**         | Type: DICTIONARY, Direction: IN                         |
    +-----------------------------+---------------------------------------------------------+
    | **DICTIONARY_IN_DELETE**    | Type: DICTIONARY, Direction: IN_DELETE                  |
    +-----------------------------+---------------------------------------------------------+
    | **DICTIONARY_INOUT**        | Type: DICTIONARY, Direction: INOUT                      |
    +-----------------------------+---------------------------------------------------------+
    | **COLLECTION_FILE(_IN)**    | Type: COLLECTION (File), Direction: IN                  |
    +-----------------------------+---------------------------------------------------------+
    | **COLLECTION_FILE_INOUT**   | Type: COLLECTION (File), Direction: INOUT               |
    +-----------------------------+---------------------------------------------------------+
    | **COLLECTION_FILE_OUT**     | Type: COLLECTION (File), Direction: OUT                 |
    +-----------------------------+---------------------------------------------------------+
    | **FILE(_IN)_STDIN**         | Type: File, Direction: IN, StdIOStream: STDIN           |
    +-----------------------------+---------------------------------------------------------+
    | **FILE(_IN)_STDOUT**        | Type: File, Direction: IN, StdIOStream: STDOUT          |
    +-----------------------------+---------------------------------------------------------+
    | **FILE(_IN)_STDERR**        | Type: File, Direction: IN, StdIOStream: STDERR          |
    +-----------------------------+---------------------------------------------------------+
    | **FILE_OUT_STDIN**          | Type: File, Direction: OUT, StdIOStream: STDIN          |
    +-----------------------------+---------------------------------------------------------+
    | **FILE_OUT_STDOUT**         | Type: File, Direction: OUT, StdIOStream: STDOUT         |
    +-----------------------------+---------------------------------------------------------+
    | **FILE_OUT_STDERR**         | Type: File, Direction: OUT, StdIOStream: STDERR         |
    +-----------------------------+---------------------------------------------------------+
    | **FILE_INOUT_STDIN**        | Type: File, Direction: INOUT, StdIOStream: STDIN        |
    +-----------------------------+---------------------------------------------------------+
    | **FILE_INOUT_STDOUT**       | Type: File, Direction: INOUT, StdIOStream: STDOUT       |
    +-----------------------------+---------------------------------------------------------+
    | **FILE_INOUT_STDERR**       | Type: File, Direction: INOUT, StdIOStream: STDERR       |
    +-----------------------------+---------------------------------------------------------+
    | **FILE_CONCURRENT**         | Type: File, Direction: CONCURRENT                       |
    +-----------------------------+---------------------------------------------------------+
    | **FILE_CONCURRENT_STDIN**   | Type: File, Direction: CONCURRENT, StdIOStream: STDIN   |
    +-----------------------------+---------------------------------------------------------+
    | **FILE_CONCURRENT_STDOUT**  | Type: File, Direction: CONCURRENT, StdIOStream: STDOUT  |
    +-----------------------------+---------------------------------------------------------+
    | **FILE_CONCURRENT_STDERR**  | Type: File, Direction: CONCURRENT, StdIOStream: STDERR  |
    +-----------------------------+---------------------------------------------------------+
    | **FILE_COMMUTATIVE**        | Type: File, Direction: COMMUTATIVE                      |
    +-----------------------------+---------------------------------------------------------+
    | **FILE_COMMUTATIVE_STDIN**  | Type: File, Direction: COMMUTATIVE, StdIOStream: STDIN  |
    +-----------------------------+---------------------------------------------------------+
    | **FILE_COMMUTATIVE_STDOUT** | Type: File, Direction: COMMUTATIVE, StdIOStream: STDOUT |
    +-----------------------------+---------------------------------------------------------+
    | **FILE_COMMUTATIVE_STDERR** | Type: File, Direction: COMMUTATIVE, StdIOStream: STDERR |
    +-----------------------------+---------------------------------------------------------+

These parameter keys, as well as the shortcuts, can be imported from the
PyCOMPSs library:

.. code-block:: python

    from pycompss.api.parameter import *
