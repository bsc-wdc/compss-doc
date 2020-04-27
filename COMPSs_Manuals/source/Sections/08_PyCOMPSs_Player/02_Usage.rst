Usage
=====

Start ``pycompss`` in your development directory
------------------------------------------------

Initialize the COMPSs infrastructure where your source code will be (you
can re-init anytime). This will allow docker to access your local code
and run it inside the container.

.. code-block:: console

        $ pycompss init  # operates on the current directory as working directoyr.

.. NOTE::

    The first time needs to download the docker image from the
    repository, and it may take a while.

Alternatively, you can specify the working directory, the COMPSs docker image
to use, or both at the same time:

.. code-block:: console

    $ # You can also provide a path
    $ pycompss init -w /home/user/replace/path/
    $
    $ # Or the COMPSs docker image to use
    $ pycompss init -i compss/compss-tutorial:2.6
    $
    $ # Or both
    $ pycompss init -w /home/user/replace/path/ -i compss/compss-tutorial:2.6


Running applications
--------------------

In order to show how to run an application, clone the PyCOMPSs' tutorial apps repository:

.. code-block:: console

    $ git clone https://github.com/bsc-wdc/tutorial_apps.git

Init the COMPSs environment in the root of the repository. The source
files path are resolved from the init directory which sometimes can be
confusing. As a rule of thumb, initialize the library in a current
directory and check the paths are correct running the file with
``python3 path_to/file.py`` (in this case
``python3 python/simple/src/simple.py``).

.. code-block:: console

    $ cd tutorial_apps
    $ pycompss init

Now we can run the ``simple.py`` application:

.. code-block:: console

    $ pycompss run python/simple/src/simple.py 1

The log files of the execution can be found at $HOME/.COMPSs.

You can also init the COMPSs environment inside the examples folder.
This will mount the examples directory inside the container so you can
execute it without adding the path:

.. code-block:: console

    $ cd python/simple/src
    $ pycompss init
    $ pycompss run simple.py 1


Running the COMPSs monitor
--------------------------

The COMPSs monitor can be started using the ``pycompss monitor start``
command. This will start the COMPSs monitoring facility which enables to
check the application status while running. Once started, it will show
the url to open the monitor in your web browser
(i.e. http://127.0.0.1:8080/compss-monitor)

.. IMPORTANT::

    Include the ``--monitor=<REFRESH_RATE_MS>`` flag in the execution before
    the binary to be executed.

.. code-block:: console

    $ cd python/simple/src
    $ pycompss init
    $ pycompss monitor start
    $ pycompss run --monitor=1000 -g simple.py 1
    $ # During the execution, go to the URL in your web browser
    $ pycompss monitor stop

If running a notebook, just add the monitoring parameter into the COMPSs
runtime start call.

Once finished, it is possible to stop the monitoring facility by using
the ``pycompss monitor stop`` command.


Running Jupyter notebooks
-------------------------

Notebooks can be run using the ``pycompss jupyter`` command. Run the
following snippet from the root of the project:

.. code-block:: console

    $ cd tutorial_apps/python
    $ pycompss init
    $ pycompss jupyter ./notebooks

An alternative and more flexible way of starting jupyter is using the
``pycompss run`` command in the following way:

.. code-block:: console

    $ pycompss run jupyter-notebook ./notebooks --ip=0.0.0.0 --NotebookApp.token='' --allow-root

And access interactively to your notebook by opening following the
http://127.0.0.1:8888/ URL in your web browser.

.. CAUTION::

    If the notebook process is not properly closed, you might get the
    following warning when trying to start jupyter notebooks again:

    ``The port 8888 is already in use, trying another port.``

    To fix it, just restart the container with ``pycompss init``.


Generating the task graph
-------------------------

COMPSs is able to produce the task graph showing the dependencies that
have been respected. In order to producee it, include the ``--graph`` flag in
the execution command:

.. code-block:: console

    $ cd python/simple/src
    $ pycompss init
    $ pycompss run --graph simple.py 1

Once the application finishes, the graph will be stored into the
``~\.COMPSs\app_name_XX\monitor\complete_graph.dot`` file. This dot file
can be converted to pdf for easier visualilzation through the use of the
``gengraph`` parameter:

.. code-block:: console

    $ pycompss gengraph .COMPSs/simple.py_01/monitor/complete_graph.dot

The resulting pdf file will be stored into the
``~\.COMPSs\app_name_XX\monitor\complete_graph.pdf`` file, that is, the
same folder where the dot file is.


Tracing applications or notebooks
---------------------------------

COMPSs is able to produce tracing profiles of the application execution
through the use of EXTRAE. In order to enable it, include the ``--tracing``
flag in the execution command:

.. code-block:: console

    $ cd python/simple/src
    $ pycompss init
    $ pycompss run --tracing simple.py 1

If running a notebook, just add the tracing parameter into the COMPSs
runtime start call.

Once the application finishes, the trace will be stored into the
``~\.COMPSs\app_name_XX\trace`` folder. It can then be analysed with
Paraver.


Adding more nodes
-----------------

.. NOTE::
    Adding more nodes is still in beta phase. Please report
    issues, suggestions, or feature requests on
    `Github <https://github.com/bsc-wdc/>`__.

To add more computing nodes, you can either let docker create more
workers for you or manually create and config a custom node.

For docker just issue the desired number of workers to be added. For
example, to add 2 docker workers:

.. code-block:: console

    $ pycompss components add worker 2

You can check that both new computing nodes are up with:

.. code-block:: console

    $ pycompss components list

If you want to add a custom node it needs to be reachable through ssh
without user. Moreover, pycompss will try to copy the ``working_dir``
there, so it needs write permissions for the scp.

For example, to add the local machine as a worker node:

.. code-block:: console

    $ pycompss components add worker '127.0.0.1:6'

-  '127.0.0.1': is the IP used for ssh (can also be a hostname like
   'localhost' as long as it can be resolved).
-  '6': desired number of available computing units for the new node.


.. IMPORTANT::

    Please be aware** that ``pycompss components`` will not list your
    custom nodes because they are not docker processes and thus it can't be
    verified if they are up and running.


Removing existing nodes
-----------------------

.. NOTE::
    Removing nodes is still in beta phase. Please report issues,
    suggestions, or feature requests on
    `Github <https://github.com/bsc-wdc/>`__.

For docker just issue the desired number of workers to be removed. For
example, to remove 2 docker workers:

.. code-block:: console

    $ pycompss components remove worker 2

You can check that the workers have been removed with:

.. code-block:: console

    $ pycompss components list

If you want to remove a custom node, you just need to specify its IP and
number of computing units used when defined.

.. code-block:: console

    $ pycompss components remove worker '127.0.0.1:6'


Stop ``pycompss``
-----------------

The infrastructure deployed can be easily stopped and the docker instances
closed with the following command:

.. code-block:: console

    $ pycompss kill
