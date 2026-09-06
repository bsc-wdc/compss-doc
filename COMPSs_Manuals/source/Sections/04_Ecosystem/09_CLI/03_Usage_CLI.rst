.. spelling:word-list::

   Autosubmit
   Streamflow


Usage
*****

``pycompss-cli`` provides the ``pycompss`` command line tool (``compss``,
``dislib`` and ``qdislib`` are also alternatives to ``pycompss``).

This command line tool enables to deploy and manage multiple COMPSs infrastructures
from a single place and for 4 different types of environments (``local``, ``remote``, ``docker`` and ``unicore``).

The main help shows the supported flags:

.. code-block:: console

    $ pycompss -h
    usage: pycompss [-h] [-d] [-i] [-v] [-p] [-s] [-g]
                {tutorial,tut,environment,env,status,envs,activate,use,default,reset,wipe,dep_check,dc,install,ins,exec,e,run,r,monitor,m,jupyter,n,gengraph,gg,gentrace,gt,inspect,i} ...

    ==============
    PyCOMPSs CLI
    ==============

    A command-line tool to develop and run COMPSs applications with ease.

    Run applications locally, in Docker, or on distributed infrastructures such as
    clusters and supercomputers. The CLI handles environment setup, job submission,
    and execution management for you.

    Built for usability and reproducibility, it streamlines parallel and distributed
    computing workflows using COMPSs.

    Resources:
    • COMPSs Website             : http://compss.bsc.es
    • COMPSs Repository          : https://github.com/bsc-wdc/compss
    • COMPSs Documentation       : https://compss.readthedocs.io/
    • pycompss-cli Documentation : https://compss.readthedocs.io/en/stable/Sections/04_Ecosystem/09_CLI.html

    Supported environments in this machine:
    ✔ local: Use local COMPSs installation.
    ✔ remote: Use a remote HPC COMPSs installation.
    ✘ docker: Docker environment NOT AVAILABLE.
        Install Docker and its Python bindings ('docker') in order to enable this environment type.
    ✘ unicore: UNICORE environment NOT AVAILABLE.
        Install 'pyunicore' in order to enable this environment type.

    Current environment:
    • Name : default
    • Type : local

    positional arguments:
    {tutorial,tut,environment,env,status,envs,activate,use,default,reset,wipe,dep_check,dc,install,ins,exec,e,run,r,monitor,m,jupyter,n,gengraph,gg,gentrace,gt,inspect,i}
        tutorial (tut)      Configure the environment for COMPSs training.
        environment (env)   Manage COMPSs environments.
        status (envs)       Show current COMPSs environment status (alias of 'environment list').
        activate (use)      Activate a COMPSs environment (alias of 'environment change').
        default             Change to 'default' environment (alias of 'environment change default').
        reset (wipe)        Remove all COMPSs environments (reset state).
                            Next actions will be applied using the current environment:
        dep_check (dc)      COMPSs dependency checker.
        install (ins)       COMPSs install.
        exec (e)            Execute command within COMPSs environment.
        run (r)             Run application (with runcompss).
        monitor (m)         Start/stop monitor.
        jupyter (n)         Start Jupyter notebook.
        gengraph (gg)       Convert graph to PDF.
        gentrace (gt)       Merge traces to Paraver trace.
        inspect (i)         Inspect RO-Crate(s) from a COMPSs application run.

    options:
    -h, --help            show this help message and exit
    -d, --debug           Enable debug mode.
    -i, --info            Enable info mode.
    -v, --version         Get version.
    -p, --plain           Plain mode (no color).
    -s, --sanitize        Avoid sensitive information in logs, out and err.
    -g, --gui             Graphical interface.


As shown in the help output, ``pycompss-cli`` is organized into several functional groups to simplify the lifecycle of a COMPSs application:

- **Environment Management**: Actions like ``environment``, ``status``, and ``activate`` allow users to switch between different execution contexts (local, remote, docker or unicore).
- **Application Execution**: The ``run`` and ``exec`` actions are the primary entry points to execute COMPSs applications and scripts within the selected environment.
- **Setup & Maintenance**: Tools such as ``install`` and ``dep_check`` ensure that all necessary dependencies are present in the environment before execution.
- **Analysis & Debugging**: Advanced utilities like ``gengraph``, ``gentrace``, and ``inspect`` provide insights into the application's execution graph and performance traces.
- **Interactive Development**: Integration with ``jupyter`` allows for an interactive development process.
- **Training**: The ``tutorial`` action creates and configures automatically the training environments.

.. IMPORTANT::

   Not all environments support all actions, and some environments may have more actions (e.g. remote environments provide ``app`` and ``job`` actions).
   The supported actions will be shown when the environment is active.

.. TIP::

   Most commands provide a short alias (e.g., ``env`` for ``environment``, ``r`` for ``run``) to speed up the workflow in the terminal.

.. TIP::

    There is also a Graphical User Interface that can be triggered with:

    .. code-block:: console

        $ pycompss --gui

    And all the actions can be performed with the mouse.


Create a new COMPSs environment
===============================

First go to your development directory:

.. code-block:: console

    mkdir pycompss_projects
    cd pycompss_projects

The creation of new environments can be done in two ways:

  1) Automatically with the ``tutorial`` (``tut``) action:
      .. code-block:: console

        $ pycompss tutorial <TUTORIAL_NAME>

    * If ``<TUTORIAL_NAME>`` is empty, the generic PyCOMPSs tutorial docker environment will be deployed.


  2) Manually  with the ``environment`` (``env``) action.
      .. code-block:: console

        $ pycompss environment init

And any necessary information will be requested (e.g. environment type, name, etc.).

.. dropdown:: Advanced environment initialization

  .. tab-set::

    .. tab-item:: Local
        :sync: local

        Creates a local type environment and initializes COMPSs in the current working dir.

        .. code-block:: console

                $ pycompss environment init local


        Alternatively, you can specify the working directory:

        .. code-block:: console

            $ pycompss init local -w /home/user/replace/path/


    .. tab-item:: Docker
        :sync: docker

        Creates a docker type environment and deploy a COMPSs container.

        .. code-block:: console

            $ pycompss environment init docker

        .. TIP::

            The command initializes COMPSs in the current working dir allowing to share it with
            the container (you can develop locally and test within docker) or in ``WORK_DIR`` if ``-w`` is set.
            The COMPSs docker image to be used can be specified with ``-i``.

        .. IMPORTANT::

            For Mac users:
            If command ``pycompss init docker`` is giving this error:

            .. code-block:: console

                "ERROR: Docker service is not running. Please, start docker service and try again"

            Despite having docker running fine could be caused by ``pycompss-cli`` not being able to find docker socket in the default path.
            Open **Docker Desktop** > **Settings** > **In the left panel scroll down to Advanced** > **Enable default Docker socket**

        .. NOTE::

                The first time needs to download the docker image from the
                repository, and it may take a while.

    .. tab-item:: Remote
        :sync: remote

        Creates a remote type environment where COMPSs is available.
        It will ask for any needed information.

        .. code-block:: console

            $ pycompss environment init remote

        .. TIP::

            It is possible to define a configuration file that will be used to setup the remote environment
            with the ``--setup_file``. For example, to load the required modules:

            .. code-block:: text

                $ cat remote_setup.sh
                module load python/3.12.1
                module load COMPSs/3.4
                module load <ANY_OTHER_MODULE>
                $ pycompss environment init remote --setup_file remote_setup.sh

    .. tab-item:: UNICORE
        :sync: unicore

        Creates a UNICORE type environment where COMPSs is available.
        It will ask for any needed information.

        .. code-block:: console

            $ pycompss environment init unicore



Managing environments
=====================

The environments can be:

- **Listed**: it is possible to check the environments with the ``environment list`` arguments (shortcuts are ``env l``, ``status`` and ``envs``).

    .. code-block:: console

        $ pycompss env list
        ┌──────────┬────────┬────────┐
        │ Name     │ Type   │ Active │
        ├──────────┼────────┼────────┤
        │ test_env │ remote │   -    │
        │ tutorial │ docker │   -    │
        │ default  │ local  │   ✔   │
        └──────────┴────────┴────────┘

- **Changed**: Activate the desired environment with the ``environment change <NAME>`` arguments  (shortcuts are ``env c``, ``activate`` and ``use`` followed by the environment name, or ``default`` to switch to the default environment).

    .. code-block:: console

        $ pycompss env change tutorial
        ⚠️  WARNING: The 'tutorial' container is not running. Starting...
        ⚠️  WARNING: No master container running.
        Starting pycompss-master-tutorial container in dir /home/user/temp
        This may take a while because it needs to download the docker image. Please be patient. ✔
        Environment `tutorial` is now active

- **Analized**: Check the details of the currently active environment with the ``environment show`` arguments  (or ``env s`` as shortcut).

    .. code-block:: console

        $ pycompss environment show
        ⚙️  Environment `tutorial` configuration:
        - name: tutorial
        - specific:
        - image: compss/compss-tutorial:3.4
        - restart: True
        - privileged: False
        - update_image: False
        - master_ip: 172.17.0.3
        - working_dir: /home/user/temp
        - log_dir: /home/user/temp/.COMPSs/
        - env: docker

        🛠️  Environment `tutorial` setup script:
        echo 'not needed'

- **Removed**: Remove the desired environment with the ``environment remove`` arguments  (or ``env r`` as shortcut).

    .. code-block:: console

        $ pycompss environment remove test_env
        ⚠️  Are you sure to remove the 'test_env' environment? [y/n]: y
        Deleting environment `test_env`. ..

- **Reset**: Remove all environments with the ``reset`` or ``wipe`` arguments (**USE WITH CAUTION**).

    .. code-block:: console

        $ pycompss reset
        ⚠️  The /home/user/temp/.COMPSs folder will be removed. Do you want to continue? [y/n]: y
        ⚠️  The /home/user/temp/.compss_docker_cfg file will be removed. Do you want to continue? [y/n]: y
        ⚠️  Are you sure to remove the 'tutorial' environment? [y/n]: y
        Removing current active environment. Changing to default environment.
        Environment `default` is now active
        Deleting environment `tutorial`. ..



Actions
=======

This section show all available actions. But all actions are supported in all environments.

+-----------------------------------------------+---------+---------+---------+---------+
| Action\\Environment                           | Local   | Docker  | Remote  | Unicore |
+===============================================+=========+=========+=========+=========+
| Check COMPSs dependencies (``dep_check``)     |    ✔    |         |         |         |
+-----------------------------------------------+---------+---------+---------+---------+
| Install COMPSs (``install``)                  |    ✔    |         |         |         |
+-----------------------------------------------+---------+---------+---------+---------+
| Execute command (``exec``)                    |    ✔    |    ✔    |    ✔    |         |
+-----------------------------------------------+---------+---------+---------+---------+
| Execute COMPSs application (``run``)          |    ✔    |    ✔    |         |         |
+-----------------------------------------------+---------+---------+---------+---------+
| Manage application (``app``)                  |         |         |    ✔    |    ✔    |
+-----------------------------------------------+---------+---------+---------+---------+
| Manage job (``job``)                          |         |         |    ✔    |    ✔    |
+-----------------------------------------------+---------+---------+---------+---------+
| COMPSs Monitor (``monitor``)                  |    ✔    |    ✔    |    ✔    |         |
+-----------------------------------------------+---------+---------+---------+---------+
| Jupyter Notebook (``jupyter``)                |    ✔    |    ✔    |    ✔    |         |
+-----------------------------------------------+---------+---------+---------+---------+
| Generate the task graph (``gengraph``)        |    ✔    |    ✔    |    ✔    |         |
+-----------------------------------------------+---------+---------+---------+---------+
| Tracing applications/notebooks (``gentrace``) |    ✔    |    ✔    |    ✔    |         |
+-----------------------------------------------+---------+---------+---------+---------+
| Add/Remove COMPSs workers (``components``)    |         |    ✔    |         |         |
+-----------------------------------------------+---------+---------+---------+---------+
| Inspect workflow provenance (``inspect``)     |    ✔    |    ✔    |         |         |
+-----------------------------------------------+---------+---------+---------+---------+


Check COMPSs dependencies
-------------------------

This action checks the COMPSs dependencies within the active environment.
It is important to ensure that the system has all COMPSs required dependencies before installing it
in order to avoid installation errors.

Since COMPSs supports multiple programming languages and has a rich ecosystem, the dependency
check can be performed for different profiles.

.. code-block:: console

        $ pycompss dep_check
        ❓ Select your profile [minimal | full | Python | C | custom] (default: Python): Python

        SYSTEM PACKAGES
        ---------------
        ✔ java (21.0.1)
        ✔ uuidgen (2.31.1)
        ✔ ssh (15.0)
        ✔ autoreconf (2.69)
        ✔ libtool (15.0)
        ✔ gfortran (7.4.1)
        ✔ libxml2-dev (15.0)
        ✔ make (4.2.1)
        ✔ build-essential (15.0)
        ✔ python (3.12.13)
        ✔ python3-pip (26.0.1)
        ✔ python3-dev (15.0)

        OTHER PACKAGES
        --------------
        ✔ docker (26.1.5)
        ⚠ nodejs [OPTIONAL] NodeJS>=12 Required for the new COMPSs monitor

        PYTHON PACKAGES
        ---------------
        ✔ setuptools (84.0.0)
        ✔ wheel (0.47.0)
        ✖ cython
        ✔ dill (0.4.1)
        ⚠ guppy3 [OPTIONAL] Enables the memory usage reporting
        ⚠ tabulate [OPTIONAL] Enables the runtime status data tables in notebooks
        ⚠ matplotlib [OPTIONAL] Enables the runtime status plots in notebooks and the object tracker report plot
        ⚠ numpy [OPTIONAL] Enables the runtime status information in notebooks
        ✔ memory_profiler (0.61.0)
        ⚠ mpi4py [OPTIONAL] Enables the usage of the MPI Python worker
        ✔ mypy (2.3.1)
        ✔ jupyter (2.3.1)
        ✔ jupyterlab (4.6.3)

        R PACKAGES
        ----------

        ENVIRONMENT VARIABLES
        ---------------------
        ✔ JAVA_HOME

        ------------------------------------------
        | Missing REQUIRED dependencies detected |
        ------------------------------------------
        HINT! Here are the commands to install them:

        python3 -m pip install "cython"

        ------------------------------------------
        | Missing OPTIONAL dependencies detected |
        ------------------------------------------
        HINT! Here are the commands to install them:

        sudo zypper install nodejs
        python3 -m pip install "guppy3>=3.0.1"
        python3 -m pip install "tabulate>=0.8.8"
        python3 -m pip install "matplotlib>=3.5.0"
        python3 -m pip install "numpy>=2.2.0"
        python3 -m pip install "mpi4py>=3.1.1"


        ⚠️  Do you want to attempt to install REQUIRED missing dependencies? [y/n]: n
        ⚠️  Do you want to attempt to install OPTIONAL missing dependencies? [y/n]: n


        ☠️  ERROR: Missing REQUIRED dependencies found! ❌

The output shows if the system has all required dependencies, and if not, which ones are missing.
Additionally, it also show the importance of the dependency (mandatory or optional -- and the reason),
and requests if you want to run the commands for the required and optional dependencies installation.


Install COMPSs
--------------

This action installs COMPSs within the active environment.

Since COMPSs supports multiple programming languages and has a rich ecosystem, the dependency
check must success in order to perform the installation:


.. code-block:: console

    $ pycompss install
    ❓ Select the installation profile [full | minimal | C | Python | R] (default: Python): Python
    Installing COMPSs with profile: Python
    1. Check dependencies...

    SYSTEM PACKAGES
    ---------------
    ✔ java (21.0.1)
    ✔ uuidgen (2.31.1)
    ✔ ssh (15.0)
    ✔ autoreconf (2.69)
    ✔ libtool (15.0)
    ✔ gfortran (7.4.1)
    ✔ libxml2-dev (15.0)
    ✔ make (4.2.1)
    ✔ build-essential (15.0)
    ✔ python (3.12.13)
    ✔ python3-pip (26.0.1)
    ✔ python3-dev (15.0)

    OTHER PACKAGES
    --------------
    ✔ docker (26.1.5)
    ⚠ nodejs [OPTIONAL] NodeJS>=12 Required for the new COMPSs monitor

    PYTHON PACKAGES
    ---------------
    ✔ setuptools (84.0.0)
    ✔ wheel (0.47.0)
    ✔ cython (3.3.0)
    ✔ dill (0.4.1)
    ⚠ guppy3 [OPTIONAL] Enables the memory usage reporting
    ⚠ tabulate [OPTIONAL] Enables the runtime status data tables in notebooks
    ⚠ matplotlib [OPTIONAL] Enables the runtime status plots in notebooks and the object tracker report plot
    ⚠ numpy [OPTIONAL] Enables the runtime status information in notebooks
    ✔ memory_profiler (0.61.0)
    ⚠ mpi4py [OPTIONAL] Enables the usage of the MPI Python worker
    ✔ mypy (2.3.1)
    ✔ jupyter (2.3.1)
    ✔ jupyterlab (4.6.3)

    R PACKAGES
    ----------

    ENVIRONMENT VARIABLES
    ---------------------
    ✔ JAVA_HOME

    ------------------------------------------
    | Missing OPTIONAL dependencies detected |
    ------------------------------------------
    HINT! Here are the commands to install them:

    sudo zypper install nodejs
    python3 -m pip install "guppy3>=3.0.1"
    python3 -m pip install "tabulate>=0.8.8"
    python3 -m pip install "matplotlib>=3.5.0"
    python3 -m pip install "numpy>=2.2.0"
    python3 -m pip install "mpi4py>=3.1.1"


    ⚠️  Do you want to attempt to install OPTIONAL missing dependencies? [y/n]: n


    All REQUIRED dependencies satisfied! ✅
    ❓ 🏷️  Which COMPSs version? (default: 3.4): 
    COMPSs version: 3.4
    2. Downloading package...
    Downloading [██████████████████████████████] 100.0% (863.6 MB / 882.2 MB) | 57.7 MB/s
    3. Extracting package...
    Extracting  [█████████████████████████░░░░░]  84.8% (20.6 KB / 24.3 KB) | 2.3 KB/
    ...
    ...
    ...

The output requests for example, the COMPSs version to be installed and the installation path.


Execute command
---------------

This action executes the given command (and parameters) within the active environment.

For example, within local environment:

.. code-block:: console

    $ pycompss exec whoami
    user

And the same command having a docker environment active:

.. code-block:: console

    $ pycompss exec whoami
    root



Execute application with COMPSs
-------------------------------

This action executes the given application (and parameters) with COMPSs within the active environment.

.. code-block:: console

    $ # pycompss run [COMPSs FLAGS] [APPLICATION] [APPLICATION PARAMETERS]
    $ pycompss run --graph --tracing examples/mandelbrot/src/mandel.py 2
    [...]


Manage application
------------------

Remote environments require the deployment of the application. In order to manage the application
deployment, listing and removal, the argument ``app`` becomes handy (only available when a remote environment
is active).

Deploy application
^^^^^^^^^^^^^^^^^^

The ``app deploy`` action will copy the current directory in the remote machine, so that it becomes
ready to be executed (as a job in the queuing system).

.. code-block:: console

    $ pycompss app deploy notebooks
    Deploying app...

.. TIP::

    You can re-deploy overwriting the remote contents by adding the ``--overwrite`` flag.


Listing applications
^^^^^^^^^^^^^^^^^^^^

It is possible to check the already deployed applications in the remote environment with the ``app list`` action:

.. code-block:: console

    $ pycompss app list
    ┌───────────┐
    │ Name      │
    ├───────────┤
    │ notebooks │
    └───────────┘


Remove application
^^^^^^^^^^^^^^^^^^

And remove an application with the ``app remove`` action (this will remove it **ONLY** from the remote machine).

.. code-block:: console

    $ pycompss app remove notebooks
    ⚠️  Are your sure that you want to remove notebooks app? [y/n]: y
    Application `notebooks` removed successfully


Manage job
----------

Remote environments require the execution of applications through a job management system (e.g. SLURM).
This can be managed with the ``jobs`` action, that allows to submit, check the status, cancel, list and check
history of jobs.

Submit job
^^^^^^^^^^

The ``job submit`` action enables to launch the execution of a COMPSs application in remote environments.
Before submitting the job, the deployment of the application is required.

.. code-block:: console

   $ # pycompss job submit --app_name [APPLICATION NAME] [ENQUEUE_COMPSS_FLAGS] [APLICATION MAIN FILE] [APPLICATION FLAGS]
   $ pycompss job submit --app_name examples --exec_time=10 --qos=debug --num_nodes=2 --project_name=bsc main.py 2 3
   [...]
   1234 # [JOB_IDENTIFIER]


Check job status
^^^^^^^^^^^^^^^^

The status of the job can be consulted (e.g running, waiting, etc.) with the ``job status`` action:

.. code-block:: console

   $ # pycompss job status [JOB_IDENTIFIER]
   $ pycompss job status 1234
   RUNNING

Cancel job
^^^^^^^^^^

The job can be canceled while waiting or running if you notice any issue with the ``job cancel`` action:

.. code-block:: console

   $ # pycompss job cancel [JOB_IDENTIFIER]
   $ pycompss job cancel 1234


List current jobs
^^^^^^^^^^^^^^^^^

The submitted jobs that are in the queue (waiting) or in execution can be consulted with the ``job list`` action:

.. code-block:: console

    $ pycompss job list
    [...]


Check jobs history
^^^^^^^^^^^^^^^^^^

It is also possible to check the history of all jobs with the ``job history`` action:

.. code-block:: console

    $ pycompss job history
    [...]

.. TIP::

    The history can be limited to a single job by specifying the ``--job_id`` flag followed by the job identifier.


COMPSs Monitor
--------------

The COMPSs monitor can be started within the currently active environment
using the ``pycompss monitor start`` command.
This will start the COMPSs monitoring facility which enables to
check the application status while running. Once started, it will show
the url to open the monitor in your web browser (i.e. http://127.0.0.1:8080/compss-monitor)

.. IMPORTANT::

    Include the ``--monitoring=<REFRESH_RATE_MS>`` flag in the execution before
    the binary to be executed.

.. code-block:: console

    $ pycompss monitor start
    $ pycompss run --monitoring=1000 -g matmul_files.py 4 4
    $ # During the execution, go to the URL in your web browser
    $ pycompss monitor stop

If running a notebook, just add the monitoring parameter into the COMPSs runtime start call.

Once finished, it is possible to stop the monitoring facility by using the ``pycompss monitor stop`` command.

.. TIP::

    The new monitor can be chosen instead of the traditional by adding the ``--new_monitor`` flag.
    Take into account that it requires Docker or Apptainer in the active environment.


Jupyter Notebook
----------------


Jupyter notebooks can be run using the ``pycompss jupyter`` command.
Run the following snippet from the root of the project:

.. code-block:: console

    $ cd tutorial_apps/python
    $ pycompss jupyter ./notebooks

And access interactively to your notebook by opening following the
http://127.0.0.1:8888/ URL in your web browser.


In order to run a jupyter notebook in remote, it must be bound to an already deployed application.

.. code-block:: console

    $ pycompss jupyter --app_name notebooks --exec_time=20 --qos=gp_debug --num_nodes=1 --project_name=bsc
    Job submitted: 19320191
    Waiting for jupyter to start...
    Connecting to jupyter server...
    Connection established. Please use the following URL to connect to the job.
    http://localhost:8888/?token=35199bb8917a97ef2ed0e7a79fbfb6e4c727983bb3a87483
    Ready to work!
    To force quit: CTRL + C


Inside the notebook, PyCOMPSs must be imported, its runtime started, tasks defined, etc.

**Please, check the documentation to get help and examples:**

- `PyCOMPSs programming model <https://pycompss.readthedocs.io/en/stable/Sections/02_App_Development/02_Python/01_Programming_model.html>`_
- `Jupyter API (pycompss start, stop, etc.) <https://pycompss.readthedocs.io/en/stable/Sections/TO_RELOCATE/PYTHON/03_Jupyter_integration.html>`_
- `Sample notebooks <https://pycompss.readthedocs.io/en/stable/Sections/08_PyCOMPSs_Notebooks.html>`_
- `Tutorial <https://pycompss.readthedocs.io/en/stable/Sections/08_Tutorial/02_PyCOMPSs.html>`_

.. CAUTION::

    If the walltime of the job is reached, the job will be killed by the
    queuing system and the notebook will stop working.

Once finished working with the notebook, press ``CTRL+C`` in the console where you
launched the ``pycompss jupyter`` command. This will trigger the job cancellation.


Generate the task graph
-----------------------

COMPSs is able to produce the task graph showing the dependencies that have been respected.
In order to produce it, include the ``--graph`` flag in the execution command:

.. code-block:: console

    $ cd python/matmul_files/src
    $ pycompss run --graph matmul_files.py 4 4

Once the application finishes, the graph will be stored into the
``.COMPSs\app_name_XX\monitor\complete_graph.dot`` file. This dot file
can be converted to pdf (or other formats) for easier visualization through
the use of the ``gengraph`` action:

.. code-block:: console

    $ pycompss gengraph .COMPSs/matmul_files.py_01/monitor/complete_graph.dot

The resulting pdf file will be stored into the
``.COMPSs\app_name_XX\monitor\complete_graph.pdf`` file, that is, the
same folder where the dot file is.


Tracing applications or notebooks
---------------------------------

COMPSs is able to produce tracing profiles of the application execution through the use of EXTRAE.
In order to enable it, include the ``--tracing`` flag in the execution command:

.. code-block:: console

    $ cd python/matmul_files/src
    $ pycompss run --tracing matmul_files.py 4 4

If running a notebook, just add the tracing parameter into ``pycompss jupyter`` call.

Once the application finishes, the trace will be stored into the  ``~\.COMPSs\app_name_XX\trace`` folder.
It can then be analyzed with Paraver.

However, when running in remote environments, the trace folder will contain a set of ``tar.gz`` files
with the trace raw contents. In order to process and merge the traces produced in remote environments,
``gentrace`` becomes necessary. It will convert ``tar.gz`` files into final trace files (``prv``, ``pcf`` and ``row``).

.. code-block:: console

    $ pycompss gentrace ~\.COMPSs\app_name_XX\trace


Add/Remove COMPSs workers
-------------------------

The ``pycompss-cli`` is able to add and remove worker nodes in Docker environments.
This is enabled with the ``components`` argument, followed by ``list`` to show the current containers,
``add`` to add new worker containers, and ``remove`` to remove a worker container.

These actions can be done before running any application.

Listing nodes
^^^^^^^^^^^^^

.. code-block:: console

    $ pycompss components list
    pycompss-master-tutorial

Add nodes
^^^^^^^^^

.. NOTE::
    Adding more nodes is still in beta phase. Please report issues, suggestions, or feature requests on
    `Github <https://github.com/bsc-wdc/>`__.

To add more computing nodes, just issue the desired number of workers to be added.
For example, to add 2 docker workers:

.. code-block:: console

    $ pycompss components add worker 2
    Started 2 worker/s
	Working dir: /home/user/examples
	CPUs: 4


You can check that both new computing nodes are up:

.. code-block:: console

    $ pycompss components list
    pycompss-master-tutorial
    pycompss-worker-tutorial-9ab82397
    pycompss-worker-tutorial-7c0a9326


Remove nodes
^^^^^^^^^^^^

.. NOTE::
    Removing nodes is still in beta phase. Please report issues, suggestions, or feature requests on
    `Github <https://github.com/bsc-wdc/>`__.

To remove computing nodes, just issue the desired number of workers to be removed.
For example, to remove 1 docker workers:

.. code-block:: console

    $ pycompss components remove worker 2
    Removed 1 workers.

You can check that the worker has been removed with:

.. code-block:: console

    $ pycompss components list
    pycompss-master-tutorial
    pycompss-worker-tutorial-7c0a9326


Inspect workflow provenance
---------------------------

As explained in the :ref:`Sections/04_Ecosystem/05_Workflow_Provenance:|:spy:| Workflow Provenance` Section,
COMPSs is able to generate the workflow
provenance of an application execution as metadata stored using the RO-Crate specification. The PyCOMPSs CLI includes
the option ``pycompss inspect`` to read an existing WMS's generated RO-Crate and print its content by the screen in a friendly way.
The RO-Crate passed as a parameter can be either a subdirectory or a zip file with all the crate content, and which
has the ``ro-crate-metadata.json`` file in its root. Note that Docker and Remote options in this command are not implemented.

The ``inspect`` option has several specific flags that can be used:

.. code-block:: console

    $ pycompss inspect -h
    usage: pycompss inspect ro_crate [ro_crate ...] [-v] [-d] [-f] [-m [METHODS ...]] [-t [TASKS]]

    positional arguments:
    ro_crate              Folder or zip file(s) containing the RO-Crate(s)

    options:
    -h, --help            show this help message and exit
    -v, --verbose         Print extra information about tasks
    -d, --data_assets     Print data assets
    -f, --failing_tasks   Print info about failing tasks only
    -t [TASKS ...], --tasks [TASKS ...]
                            Print all information about one or more tasks (e.g. 4 7 10-11 15-18
    -m [METHODS ...], --methods [METHODS ...]
                            Print all tasks executing the specified method(s)

If no extra flags are used, the standard output is like shown in the next Figure. It shows the ``Name`` and ``Description`` provided for the application,
who are their ``Authors`` (printing their name, organization and e-mail when available), the ``License`` of the code and the ``Date Published`` referring to
the moment when the crate was generated. Additionally, the ``Main entity`` identifies the main file of the application, and the ``Programming language`` field
shows the WMS used for programming, with its specific version. Regarding the ``Execution details``, the ``Status`` of the run is shown, with a
summary of the executed tasks' status in ``Executed Tasks``, the total ``Execution Time``, the ``Host`` where the application ran (showing the
hostname, the number of nodes used for the run, and if a queuing system was used also the captured job id of the run). The ``Resource Usage`` field
is an average of the CPU and Memory percentage used by the nodes (not considering the master). The field ``Agent`` refers to the individual that
executed the application (organization and e-mail also included when available), and the ``Environment`` and ``Data assets`` fields provide a count
of the details captured in those matters.

.. TIP::

    Wildcards can be used when calling ``pycompss inspect``, thus getting details of may runs at the same time. Also, the output produced can be easily filtered
    with the ``grep`` command (e.g. ``pycompss inspect *.zip | grep -e CRATE -e "Execution Time"``)

.. figure:: ./Figures/inspect.png
    :name: Inspect without flags
    :alt: Inspect without flags
    :align: center
    :width: 60.0%

    Inspect without flags


**Verbose mode:**

The ``-v/--verbose`` flag can be used to print detailed general information about a run. In particular, when used,
the fields ``Software Requirements`` and ``RO-Crate compliance`` will appear in the general description. They list the
application's software dependencies, and the RO-Crate specifications that the metadata complies with, respectively. On the other hand,
in the ``Execution details`` much richer information will be printed, showing ``Start Time`` and ``End Time`` of the
application (in Coordinated Universal Time (UTC) format), the ``Submission`` field that contains the command that
was used to run the experiment and the ``Environment``
field that has some relevant environment variables captured during the execution.

Moreover, the ``Resource Usage`` section is
largely expanded showing resource and method statistics per node used in the computation, and a summary in the
``Overall Statistics`` field. In detail, the ``Overall Statistics`` section includes statistics on all the methods executed during
the experiment: for each method, number of invocations, average, maximum and minimum execution times are also recorded in milliseconds;
a general calculation of resource usage is also done by providing the average % CPU and memory usage, obtained from averaging all the worker nodes
involved in the computation (excluding the master). After that, details per node are provided, first providing the hostname (and if it is the
master of the computation) together with the total number of tasks the node executed. Then, inside each node, statistics per method are provided (again
number of invocations, average, maximum and minimum execution times in milliseconds) together with CPU and memory statistics, this time including
average and maximum % of use of the CPU, and average, maximum and minimum % for the memory. This information can be very useful to do a quick
assessment on the usage of resources during the computation, where methods taking too much time to execute can be identified, or even also large
load balance differences between the nodes can be discovered.

.. figure:: ./Figures/soft_req.png
    :name: Inspect extra details
    :alt: Inspect extra details
    :align: center
    :width: 30.0%

    Inspect extra general details


.. figure:: ./Figures/verbose.png
    :name: Inspect verbose
    :alt: Inspect verbose
    :align: center
    :width: 60.0%

    Inspect verbose, providing method and resource usage statistics

.. figure:: ./Figures/submission.png
    :name: Submission
    :alt: Submission and environment variables
    :align: center
    :width: 90.0%

    Detail on submission command and environment variables inside the Execution details section

**List data assets:**

A ``-d/--data_assets`` flag is available to get details on the inputs used and outputs generated by the workflow execution. This listing is disabled
by default because experiments can have very large sets of files and datasets involved in the computation, and therefore listing them every time can 
become annoying. Each data asset
can be specified either with a relative path inside the crate when data is persisted, or a URL referencing
where to find the file when data is not persisted. For directories, only the root name is listed, and in the case of individual files,
the size of the file is also shown.

.. figure:: ./Figures/datasets_persist.png
    :name: Datasets persist
    :alt: Datasets persist
    :align: center
    :width: 70.0%

    Detail on datasets needed (Inputs) and generated (Outputs) by the workflow application. Since relative paths are used, the datasets are
    persisted in the crate

.. figure:: ./Figures/datasets_nonpersist.png
    :name: Datasets nonpersist
    :alt: Datasets nonpersist
    :align: center
    :width: 70.0%

    Detail on datasets needed (Inputs) and generated (Outputs) by the workflow application. Since URLs are used, the datasets are
    not persisted in the crate


**Get details of tasks by number:**

The ``-t/--tasks`` flag can be used to print detailed information about each selected task individually. The flag accepts individual numbers
separated by spaces (e.g. ``3 4 10``), ranges of tasks (e.g. ``20-30``) and combinations of both.
Details such as its status, what specific method was executed, the execution time, the host where the task ran, what parameters were used
(together with their type and value and a brief generated description for complex types) and the task's related log files (if the task
failed or debug mode is used). The ``Type`` field shows first the corresponding ``schema.org`` type mapped for the parameter, and later any
other type captured from the original programming model (e.g. ``float64``, ``dict``, etc.).
For tasks that failed or were canceled, we do not capture output parameters since they cannot be relied upon. This means that, when listing
their details, no ``Outputs`` will be listed. In case of failure, the ``Execution Time`` will correspond to the run time the task was running ok
before reaching the failure.

.. TIP::

    We **STRONGLY** recommend to use the workflow diagram (i.e. ``complete_graph.svg``) to easily understand task id numbers for later selection with ``-t``.


.. figure:: ./Figures/task_details_1.png
    :name: Task details 1
    :alt: Task details 1
    :align: center
    :width: 90.0%

    Task details: examples on Array of Files and File parameters. Corresponding task execution log files are also listed

.. figure:: ./Figures/task_details_2.png
    :name: Task details 2
    :alt: Task details 2
    :align: center
    :width: 90.0%

    Task details: examples with Integer, Dictionary and Numpy array parameters


**Get details of tasks by method name:**

Similarly to the previous flag ``-t``, the ``-m/--methods`` flag provides a way to filter all the tasks executed but this time using a pattern to filter
them by the name of the method the tasks have executed. In this case, only a single pattern can be passed to the flag.

**Get details of the tasks that failed:**

The function of the ``-f/--failing_tasks`` flag is to provide a way to list only the details of the tasks that have failed during the execution.
Since the provenance is generated even when failures occur, this information can help users to debug the application run and easily identify
the source of a problem. Failing tasks always include their related execution logs, where failures can be tracked down. Besides, provenance
records the exact values of the inputs used to call the invoked method, which is also a very nice way to clarify to the user how the
method was called and if it was as it was expected.

.. figure:: ./Figures/failure.png
    :name: Failing task
    :alt: Failing task
    :align: center
    :width: 70.0%

    Details on Task 385 that failed. We can see that both Inputs and execution logs are indicated so the user can check them to look for errors


**Compatibility with other WMSs:**

Thanks to being compliant with RO-Crate, and specifically with the Workflow Run RO-Crate collection of profiles (Workflow Run and Provenance Run),
the pycompss inspect functionality is **interoperable with other Workflow Management Systems (WMSs)** that generate metadata in this format.
Some examples are: **CWL, nextflow, Galaxy, Autosubmit, WfExS, Streamflow, Snakemake, Sapporo, and more**. Each WMS generates a certain level of 
metadata details, that is the reason why the level of details printed with pycompss inspect can vary from one system to another.

.. figure:: ./Figures/streamflow.png
    :name: Streamflow pipeline
    :alt: Streamflow pipeline
    :align: center
    :width: 70.0%

    Streamflow pipeline details obtained with pycompss inspect

.. figure:: ./Figures/autosubmit.png
    :name: Autosubmit pipeline
    :alt: Autosubmit pipeline
    :align: center
    :width: 80.0%

    Autosubmit pipeline details obtained with pycompss inspect

.. figure:: ./Figures/wfexs.png
    :name: WfExS pipeline
    :alt: WfExS pipeline
    :align: center
    :width: 90.0%

    WfExS pipeline details obtained with pycompss inspect

