Other task types
~~~~~~~~~~~~~~~~

In addition to this API functions, the programmer can use a set of
decorators for other purposes.

For instance, there is a set of decorators that can be placed over the
*@task* decorator in order to define the task methods as a
**binary invocation** (with the :ref:`Sections/02_App_Development/02_Python/01_Programming_model/06_Other_task_types:Binary decorator`), as a **OmpSs
invocation** (with the :ref:`Sections/02_App_Development/02_Python/01_Programming_model/06_Other_task_types:OmpSs decorator`), as a **MPI invocation**
(with the :ref:`Sections/02_App_Development/02_Python/01_Programming_model/06_Other_task_types:MPI decorator`), as a **COMPSs application** (with the
:ref:`Sections/02_App_Development/02_Python/01_Programming_model/06_Other_task_types:COMPSs decorator`), as a **task that requires multiple
nodes** (with the :ref:`Sections/02_App_Development/02_Python/01_Programming_model/06_Other_task_types:Multinode decorator`), or as a **Reduction task** that
can be executed in parallel having a subset of the original input data as input (with the
:ref:`Sections/02_App_Development/02_Python/01_Programming_model/06_Other_task_types:Reduction decorator`). These decorators must be placed over the
*@task* decorator, and under the *@constraint* decorator if defined.

Consequently, the task body will be empty and the function parameters
will be used as invocation parameters with some extra information that
can be provided within the *@task* decorator.

The following subparagraphs describe their usage.

Binary decorator
^^^^^^^^^^^^^^^^

The *@binary* (or @Binary) decorator shall be used to define that a task is
going to invoke a binary executable.

In this context, the *@task* decorator parameters will be used
as the binary invocation parameters (following their order in the
function definition). Since the invocation parameters can be of
different nature, information on their type can be provided through the
*@task* decorator.

:numref:`binary_task_python` shows the most simple binary task definition
without/with constraints (without parameters); please note that @constraint decorator has to be provided on top of the others.

.. code-block:: python
    :name: binary_task_python
    :caption: Binary task example

    from pycompss.api.task import task
    from pycompss.api.binary import binary

    @binary(binary="mybinary.bin")
    @task()
    def binary_func():
         pass

    @constraint(computingUnits="2")
    @binary(binary="otherbinary.bin")
    @task()
    def binary_func2():
         pass

The invocation of these tasks would be equivalent to:

.. code-block:: console

    $ ./mybinary.bin
    $ ./otherbinary.bin   # in resources that respect the constraint.

The ``@binary`` decorator supports the ``working_dir`` parameter to define
the working directory for the execution of the defined binary.

:numref:`complex_binary_task_python` shows a more complex binary invocation, with files
as parameters:

.. code-block:: python
    :name: complex_binary_task_python
    :caption: Binary task example 2

    from pycompss.api.task import task
    from pycompss.api.binary import binary
    from pycompss.api.parameter import *

    @binary(binary="grep", working_dir=".")
    @task(infile={Type:FILE_IN_STDIN}, result={Type:FILE_OUT_STDOUT})
    def grepper():
         pass

    # This task definition is equivalent to the following, which is more verbose:

    @binary(binary="grep", working_dir=".")
    @task(infile={Type:FILE_IN, StdIOStream:STDIN}, result={Type:FILE_OUT, StdIOStream:STDOUT})
    def grepper(keyword, infile, result):
         pass

    if __name__=='__main__':
        infile = "infile.txt"
        outfile = "outfile.txt"
        grepper("Hi", infile, outfile)

The invocation of the *grepper* task would be equivalent to:

.. code-block:: console

    $ # grep keyword < infile > result
    $ grep Hi < infile.txt > outfile.txt

Please note that the *keyword* parameter is a string, and it is
respected as is in the invocation call.

Thus, PyCOMPSs can also deal with prefixes for the given parameters. :numref:`complex2_binary_task_python`
performs a system call (ls) with specific prefixes:

.. code-block:: python
    :name: complex2_binary_task_python
    :caption: Binary task example 3

    from pycompss.api.task import task
    from pycompss.api.binary import binary
    from pycompss.api.parameter import *

    @binary(binary="ls")
    @task(hide={Type:FILE_IN, Prefix:"--hide="}, sort={Prefix:"--sort="})
    def myLs(flag, hide, sort):
        pass

    if __name__=='__main__':
        flag = '-l'
        hideFile = "fileToHide.txt"
        sort = "time"
        myLs(flag, hideFile, sort)

The invocation of the *myLs* task would be equivalent to:

.. code-block:: console

    $ # ls -l --hide=hide --sort=sort
    $ ls -l --hide=fileToHide.txt --sort=time

This particular case is intended to show all the power of the
*@binary* decorator in conjuntion with the *@task*
decorator. Please note that although the *hide* parameter is used as a
prefix for the binary invocation, the *fileToHide.txt* would also be
transfered to the worker (if necessary) since its type is defined as
FILE_IN. This feature enables to build more complex binary invocations.

In addition, the ``@binary`` decorator also supports the ``fail_by_exit_value``
parameter to define the failure of the task by the exit value of the binary
(:numref:`binary_task_python_exit`).
It accepts a boolean (``True`` to consider the task failed if the exit value is
not 0, or ``False`` to ignore the failure by the exit value (**default**)), or
a string to determine the environment variable that defines the fail by
exit value (as boolean).
The default behaviour (``fail_by_exit_value=False``) allows users to receive
the exit value of the binary as the task return value, and take the
necessary decissions based on this value.

.. code-block:: python
    :name: binary_task_python_exit
    :caption: Binary task example with ``fail_by_exit_value``

    @binary(binary="mybinary.bin", fail_by_exit_value=True)
    @task()
    def binary_func():
         pass

OmpSs decorator
^^^^^^^^^^^^^^^

The *@ompss* (or @OmpSs) decorator shall be used to define that a task is
going to invoke a OmpSs executable (:numref:`ompss_task_python`).

.. code-block:: python
    :name: ompss_task_python
    :caption: OmpSs task example

    from pycompss.api.ompss import ompss

    @ompss(binary="ompssApp.bin")
    @task()
    def ompss_func():
         pass

The OmpSs executable invocation can also be enriched with parameters,
files and prefixes as with the *@binary* decorator through the
function parameters and *@task* decorator information. Please,
check :ref:`Sections/02_App_Development/02_Python/01_Programming_model/06_Other_task_types:Binary decorator` for more details.

MPI decorator
^^^^^^^^^^^^^

The *@mpi* (or @Mpi) decorator shall be used to define that a task is
going to invoke a MPI executable (:numref:`mpi_task_python`).

.. code-block:: python
    :name: mpi_task_python
    :caption: MPI task example

    from pycompss.api.mpi import mpi

    @mpi(binary="mpiApp.bin", runner="mpirun", processes=2)
    @task()
    def mpi_func():
         pass

The MPI executable invocation can also be enriched with parameters,
files and prefixes as with the *@binary* decorator through the
function parameters and *@task* decorator information. Please,
check :ref:`Sections/02_App_Development/02_Python/01_Programming_model/06_Other_task_types:Binary decorator` for more details.

The *@mpi* decorator can be also used to execute a MPI for python (mpi4py) code.
To indicate it, developers only need to remove the binary field and include
the Python MPI task implementation inside the function body as shown in the
following example (:numref:`mpi_for_python`).

.. code-block:: python
    :name: mpi_for_python
    :caption: MPI task example with collections and data layout

    from pycompss.api.mpi import mpi

    @mpi(processes=4)
    @task()
    def layout_test_with_all():
       from mpi4py import MPI
       rank = MPI.COMM_WORLD.rank
       return rank

In both cases, users can also define, MPI + OpenMP tasks by using ``processes``
property to indicate the number of MPI processes and ``computing_units`` in the
Task Constraints to indicate the number of OpenMP threads per MPI process.

The *@mpi* decorator can be combined with collections to allow the process of
a list of parameters in the same MPI execution. By the default, all parameters
of the list will be deserialized to all the MPI processes. However, a common
pattern in MPI is that each MPI processes performs the computation in a subset
of data. So, all data serialization is not needed. To indicate the subset used
by each MPI process, developers can use the ``data_layout`` notation inside the
MPI task declaration.

.. code-block:: python
    :name: mpi_data_layout_python
    :caption: MPI task example with collections and data layout

    from pycompss.api.mpi import mpi

    @mpi(processes=4, col_layout={block_count: 4, block_length: 2, stride: 1})
    @task(col=COLLECTION_IN, returns=4)
    def layout_test_with_all(col):
       from mpi4py import MPI
       rank = MPI.COMM_WORLD.rank
       return data[0]+data[1]+rank

Figure (:numref:`mpi_data_layout_python`) shows an example about how to combine
MPI tasks with collections and data layouts. In this example, we have define a
MPI task with an input collection (``col``). We have also defined a data layout
with the property ``<arg_name>_layout`` and we specify the number of blocks
(``block_count``), the elements per block (``block_length``), and the number of
element between the starting block points (``stride``).

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

Multinode decorator
^^^^^^^^^^^^^^^^^^^

The *@multinode* (or @Multinode) decorator shall be used to define that a task
is going to use multiple nodes (e.g. using internal parallelism) (:numref:`multinode_task_python`).

.. code-block:: python
    :name: multinode_task_python
    :caption: Multinode task example

    from pycompss.api.multinode import multinode

    @multinode(computing_nodes="2")
    @task()
    def multinode_func():
         pass

The only supported parameter is *computing_nodes*, used to define the
number of nodes required by the task (the default value is 1). The
mechanism to get the number of nodes, threads and their names to the
task is through the *COMPSS_NUM_NODES*, *COMPSS_NUM_THREADS* and
*COMPSS_HOSTNAMES* environment variables respectively, which are
exported within the task scope by the COMPSs runtime before the task
execution.

HTTP decorator
^^^^^^^^^^^^^^^^^^^

The *@http* decorator can be used for the tasks to be executed on a remote
Web Service via HTTP requests. In order to create HTTP tasks, it is obligatory to
define HTTP resource(s) in ``resources`` and ``project`` files (see
:ref:`Sections/01_Installation/06_Configuration_files:HTTP configuration`).
Following code snippet (:numref:`http_task_python_basic`) is a basic HTTP task
with all required parameters. At the time of execution, the runtime will search
for HTTP resource from resources file which allows execution of 'service_1' and
send a GET request to its 'Base URL'. Moreover, python parameters can be added to
the request query as shown in the example (between double curly brackets).


.. code-block:: python
    :name: http_task_python_basic
    :caption: HTTP Task example.

    from pycompss.api.task import task
    from pycompss.api.http import http

    @http(service_name="service_1", request="GET",
          resource="get_length/{{message}}")
    @task(returns=int)
    def an_example(message):
        pass


For POST requests it is possible to  send a parameter as the request body by adding
it to the ``payload`` arg. In this case, payload type can also be
specified ('application/json' by default). If the parameter is a FILE type, then
the content of the file is read in the master and added to the request as request
body.


.. code-block:: python
    :name: http_task_python_post
    :caption: HTTP Task with POST request.

    from pycompss.api.task import task
    from pycompss.api.http import http

    @http(service_name="service_1", request="POST", resource="post_json/",
          payload="{{payload}}", payload_type="application/json")
    @task(returns=str)
    def post_with_param(payload):
        pass


For the cases where the response body is a JSON formatted string, PyCOMPSs' HTTP
decorator allows response string formatting by defining the return values within
the ``produces`` parameter. In the following example, the return value of the task
would be extracted from 'length' key of the JSON response string:


.. code-block:: python
    :name: http_task_python_produces
    :caption: HTTP Task with return value to be extracted from a JSON string.

    from pycompss.api.task import task
    from pycompss.api.http import http


    @http(service_name="service_1", request="GET",
          resource="produce_format/{{message}}",
          produces="{'length':'{{return_0}}'}")
    @task(returns=int)
    def an_example(message):
        pass

Note that if the task has multiple returns, 'return_0', 'return_1', return_2, etc.
all must be defined in the ``produces`` string.


Reduction decorator
^^^^^^^^^^^^^^^^^^^

The *@reduction* (or @Reduction) decorator shall be used to define that a task
is going to be subdivided into smaller tasks that take as input
a subset of the input data. (:numref:`reduction_task_python`).

.. code-block:: python
    :name: reduction_task_python
    :caption: Reduction task example

    from pycompss.api.reduction import reduction

    @reduction(chunk_size="2")
    @task()
    def myreduction():
        pass

The only supported parameter is *chunk_size*, used to define the
size of the data that the generated tasks will get as input parameter.
The data given as input to the main reduction task is subdivided into chunks
of the set size.

Container decorator
^^^^^^^^^^^^^^^^^^^

The ``@container`` (or ``@Container``) decorator shall be used to define that a
task is going to be executed within a container (:numref:`container_task_python`).

.. code-block:: python
    :name: container_task_python
    :caption: Container task example

    from pycompss.api.compss import container
    from pycompss.api.task import task
    from pycompss.api.parameter import *
    from pycompss.api.api import compss_wait_on

    @container(engine="DOCKER",
               image="compss/compss")
    @task(returns=1, num=IN, in_str=IN, fin=FILE_IN)
    def container_fun(num, in_str, fin):
        # Sample task body:
        with open(fin, "r") as fd:
            num_lines = len(fd.readlines())
        str_len = len(in_str)
        result = num * str_len * num_lines

        # You can import and use libraries available in the container

        return result

    if __name__=='__main__':
        result = container_fun(5, "hello", "dataset.txt")
        result = compss_wait_on(result)
        print("result: %s" % result)


The *container_fun* task will be executed within the container defined in the
*@container* decorator using the *docker* engine with the compss/compss *image*.
This task is pure python and you can import and use any library available in
the container

This feature allows to use specific containers for tasks where the library
dependencies are met.

.. TIP::

    Singularity is also supported, and can be selected by setting the engine to
    SINGULARITY:

    .. code-block::

        @container(engine=SINGULARITY)


In addition, the *@container* decorator can be placed on top of the
*@binary*, *@ompss* or *@mpi* decorators. :numref:`container_task_python_binary`
shows how to execute the same example described in the
:ref:`Sections/02_App_Development/02_Python/01_Programming_model/06_Other_task_types:Binary decorator`
section, but within the ``compss/compss`` container using docker.
This will execute the binary/ompss/mpi binary within the container.


.. code-block:: python
    :name: container_task_python_binary
    :caption: Container binary task example

    from pycompss.api.compss import container
    from pycompss.api.task import task
    from pycompss.api.binary import binary
    from pycompss.api.parameter import *

    @container(engine="DOCKER",
               image="compss/compss")
    @binary(binary="grep", working_dir=".")
    @task(infile={Type:FILE_IN_STDIN}, result={Type:FILE_OUT_STDOUT})
    def grepper():
         pass

    if __name__=='__main__':
        infile = "infile.txt"
        outfile = "outfile.txt"
        grepper("Hi", infile, outfile)

Other task types summary
^^^^^^^^^^^^^^^^^^^^^^^^

Next tables summarizes the parameters of these decorators.

* @binary
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | Parameter              | Description                                                                                                                       |
    +========================+===================================================================================================================================+
    | **binary**             | (Mandatory) String defining the full path of the binary that must be executed.                                                    |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | **working_dir**        | Full path of the binary working directory inside the COMPSs Worker.                                                               |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+

* @ompss
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | Parameter              | Description                                                                                                                       |
    +========================+===================================================================================================================================+
    | **binary**             | (Mandatory) String defining the full path of the binary that must be executed.                                                    |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | **working_dir**        | Full path of the binary working directory inside the COMPSs Worker.                                                               |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+

* @mpi
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | Parameter              | Description                                                                                                                       |
    +========================+===================================================================================================================================+
    | **binary**             | (Optional) String defining the full path of the binary that must be executed. Empty indicates python MPI code.                    |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | **working_dir**        | Full path of the binary working directory inside the COMPSs Worker.                                                               |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | **runner**             | (Mandatory) String defining the MPI runner command.                                                                               |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | **processes**          | Integer defining the number of computing nodes reserved for the MPI execution (only a single node is reserved by default).        |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+

* @compss
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

* @http
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

* @multinode
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | Parameter              | Description                                                                                                                       |
    +========================+===================================================================================================================================+
    | **computing_nodes**    | Integer defining the number of computing nodes reserved for the task execution (only a single node is reserved by default).       |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+

* @reduction
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | Parameter              | Description                                                                                                                       |
    +========================+===================================================================================================================================+
    | **chunk_size**         |  Size of data fragments to be given as input parameter to the reduction function.                                                 |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+

* @container
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | Parameter              | Description                                                                                                                       |
    +========================+===================================================================================================================================+
    | **engine**             |  Container engine to use (e.g. DOCKER or SINGULARITY).                                                                            |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | **image**              |  Container image to be deployed and used for the task execution.                                                                  |
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
