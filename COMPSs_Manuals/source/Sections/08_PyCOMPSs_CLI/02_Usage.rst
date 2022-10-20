Usage
=====

``pycompss-cli`` provides the ``pycompss`` command line tool (``compss``
and ``dislib`` are also alternatives to ``pycompss``).

This command line tool enables to deploy and manage multiple COMPSs infrastructures
from a single place and for 3 different types of environments (``docker``, ``local`` and ``remote``)

The supported flags are:

.. code-block:: console

    $ pycompss
    PyCOMPSs|COMPSS CLI:

    Usage: pycompss COMMAND  |  compss COMMAND  |  dislib COMMAND

    Available commands:
        init -n [NAME]:                             initialize COMPSs environment (default local).
                                                    If -n is set it will initialize with NAME as name or else with a random id.
        environment:                                lists, switch a remove COMPSs environments.
        exec CMD:                                   executes the CMD within the current COMPSs environment.
        run [--app_name] [OPTIONS] FILE [PARAMS]:   runs FILE with COMPSs, where OPTIONS are COMPSs options and PARAMS are application parameters.
                                                    --app_name parameter is only required for remote environments
        monitor [start|stop]:                       starts or stops the COMPSs monitoring.
        jupyter [--app_name] [PATH|FILE]:           starts jupyter-notebook in the given PATH or FILE.
                                                    --app_name parameter is only required for remote environments
        job:                                        submits, cancel and list jobs on remote and local environments.
        app:                                        deploy, list and remove applications on remote and local environments.
        gengraph [FILE.dot]:                        converts the .dot graph into .pdf
        components list:                            lists COMPSs actives components.
        components add RESOURCE:                    adds the RESOURCE to the pool of workers of the COMPSs.
            Example given: pycompss components add worker 2 # to add 2 local workers.
            Example given: pycompss components add worker <IP>:<CORES> # to add a remote worker
                        Note: compss and dislib can be used instead of pycompss in both examples.
        components remove RESOURCE:   removes the RESOURCE to the pool of workers of the COMPSs.
            Example given: pycompss components remove worker 2 # to remove 2 local workers.
            Example given: pycompss components remove worker <IP>:<CORES> # to remove a remote worker
                        Note: compss and dislib can be used instead of pycompss in both examples.


Create a new COMPSs environment in your development directory
-------------------------------------------------------------

.. tabs::

   .. group-tab:: Docker

        Creates a docker type evironment and deploy a COMPSs container

        .. code-block:: console

            $ pycompss init docker -w [WORK_DIR] -i [IMAGE]

        The command initializes COMPSs in the current working dir or in WORK_DIR if -w is set.
        The COMPSs docker image to be used can be specified with -i (it can also be
        specified with the COMPSS_DOCKER_IMAGE environment variable).

        Initialize the COMPSs infrastructure where your source code will be.
        This will allow docker to access your local code
        and run it inside the container.

        .. code-block:: console

                $ pycompss init docker  # operates on the current directory as working directory.

        .. NOTE::

                The first time needs to download the docker image from the
                repository, and it may take a while.

        Alternatively, you can specify the working directory, the COMPSs docker image
        to use, or both at the same time:

        .. code-block:: console

            $ # You can also provide a path
            $ pycompss init docker -w /home/user/replace/path/
            $
            $ # Or the COMPSs docker image to use
            $ pycompss init docker -i compss/compss-tutorial:3.0
            $
            $ # Or both
            $ pycompss init docker -w /home/user/replace/path/ -i compss/compss-tutorial:3.0

   .. group-tab:: Local

        .. code-block:: console

                $ pycompss init local -w [WORK_DIR] -m [MODULES ...]

        Creates a local type evironment and initializes COMPSs in the current working dir
        or in WORK_DIR if -w is set. The modules to be loaded automatically can be specified with -m.

        Initialize the COMPSs infrastructure where your source code will be.

        .. code-block:: console

                $ pycompss init local  # operates on the current directory as working directory.

        Alternatively, you can specify the working directory, the modules to
        automatically load or both at the same time:

        .. code-block:: console

            $ # You can also provide a path
            $ pycompss init local -w /home/user/replace/path/
            $
            $ # Or a list of modules to load automatically before every command
            $ pycompss init local -m COMPSs/3.0 ANACONDA/5.1.0_py3
            $
            $ # Or both
            $ pycompss init local -w /home/user/replace/path/ -m COMPSs/3.0 ANACONDA/5.1.0_py3

   .. group-tab:: Remote

        .. code-block:: console

            $ pycompss init remote -l [LOGIN] -m [FILE | MODULES ...]

        Creates a remote type evironment with the credentials specified in LOGIN. 
        The modules to be loaded automatically can be specified with -m.

        Parameter LOGIN is necessary to connect to the remote host and must follow
        standard format i.e. [user]@[hostname]:[port]. ``port`` is optional and defaults to 22 for ssh.
    
        .. code-block:: console
    
            $ pycompss init remote -l username@mn1.bsc.es
            $
            $ # Or with list of modules 
            $ pycompss init remote -l username@mn1.bsc.es -m COMPSs/3.0 ANACONDA/5.1.0_py3

        .. NOTE::
            
            The SSH access to the remote should be configured to work without password.
            If you need to set up your machine for the first time please take a look
            at :ref:`Sections/01_Installation/05_Additional_configuration:Additional Configuration`
            Section for a detailed description of the additional configuration.


        The parameter ``-m`` also supports passing a file containing not only modules but any kind of commands
        that you need to execute for the remote environment.
        Suppose we have a file ``modules.sh`` with the following content:

        .. code-block:: text

            export ComputingUnits=1
            export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
            module load COMPSs/3.0
            module load ANACONDA/5.1.0_py3

        .. code-block:: console
    
            $ pycompss init remote -l username@mn1.bsc.es -m /path/to/modules.sh


Managing environments
---------------------

Every time command ``pycompss init`` is executed, a new environment is created and becomes the active
environment in wich the rest of the commands will be executed.
The subcommands ``pycompss environment`` will help inspecting, removing and switching between the environments.

You can list all the environments created with ``pycompss environment list`` and inspect which one is active,
the types of each one and the ID.

.. code-block:: console

    $ pycompss environment list
                      ID           Type         Active
        -   5eeb858c2b10         remote            *
        -        default          local                
        -  container-b54         docker    

The ID of the environments is what you will use to switch between them.

.. code-block:: console

    $ pycompss environment change container-b54
        Environment `container-b54` is now active

Every environment can also be deleted, except ``default`` environment.

.. code-block:: console

    $ pycompss environment remove container-b54
        Deleting environment `container-b54`...
    $ pycompss environment remove default
        ERROR: `default` environment is required and cannot be deleted.

Also every remote environment can have multiple applications deployed in remote.
So if you want to delete the environment all the data associated with them will be aslo deleted.

.. code-block:: console

    $ pycompss environment remove 5eeb858c2b10     # deleting a remote env with 2 apps deployed
        WARNING: There are still applications binded to this environment
        Do you want to delete this environment and all the applications? (y/N) y   # default is no
        Deleting app1...
        Deleting app2...
        Deleting environment `5eeb858c2b10`...


Deploying applications
----------------------

For a remote environment is required to deploy any application before executing it.

.. code-block:: console

        $ pycompss app deploy [APP_NAME] --source_dir [SOURCE_DIR] --destination_dir [DESTINATION_DIR]

APP_NAME is required and must be unique.
SOURCE_DIR and DESTINATION_DIR are optional
the command copies the application from the current directory or from SOURCE_DIR if --source_dir is set
to the remote directory specified with DESTINATION_DIR.
if DESTINATION_DIR is not set, the application will be deployed in ``$HOME/.COMPSsApps``

In order to show how to deploy an application, clone the PyCOMPSs' tutorial apps repository:

.. code-block:: console

    $ git clone https://github.com/bsc-wdc/tutorial_apps.git


.. tabs::

   .. group-tab:: Docker

      This is not necessary for docker environments since the working directory is set
      at the initialization of the environment.

   .. group-tab:: Local

        On ``local`` environment deploying an application wil just copy the ``--source_dir`` directory to another location.
        Let's deploy the matrix multiplication tutorial application.

        .. code-block:: console

            $ pycompss app deploy matmul --source_dir tutorial_apps/python/matmul_files

        Also you could specify the path where to copy the files.

        .. code-block:: console

            $ pycompss app deploy matmul --source_dir tutorial_apps/python/matmul_files/src/ --destination_dir /home/user/matmul_copy

        If the parameter ``--destination_dir`` is missing then the files will be copied to ``~/.COMPSsApps/%env_name%/%app_name%/``

        Each deployed application  can be listed using the command:

        .. code-block:: console

                $ pycompss app list
                    Name          Source                                                           Destination
                    ------------  ------------------------------------------------------------     ---------------------------------------
                    matmul        /home/user/tutorial_apps/python/matmul_files                     /home/user/.COMPSsApps/default/matmul
                    test_jenkins  /jenkins/tests_execution_sandbox/apps/app009/.COMPSsWorker       /tmp/test_jenkins

        Also every app can be deleted using the command:

        .. code-block:: console

                $ pycompss app remove matmul
                    Deleting application `matmul`...
                    
        .. CAUTION::
            
                Removing an applocation will delete the copied app directory and every valuable results generated inside.

   .. group-tab:: Remote

        Let's deploy the matrix multiplication tutorial application.

        .. code-block:: console

            $ pycompss app deploy matmul --source_dir tutorial_apps/python/matmul_files

        Also you could specify the path where to copy the files on the remote host.

        .. code-block:: console

            $ pycompss app deploy matmul --source_dir tutorial_apps/python/matmul_files/src/ --destination_dir /path/cluster/my_app

        Each deployed application within a remote environment can be listed using the command:

        .. code-block:: console

                $ pycompss app list
                                Name
                    -         matmul
                    -           app1

        Also every app can be deleted using the command:

        .. code-block:: console

                $ pycompss app remove matmul
                    Deleting application `matmul`...

        .. CAUTION::

                Removing an applocation will delete the entire app directory and every valuable results generated inside.


Executing applications
----------------------

.. tabs::

   .. group-tab:: Docker

        .. tabs::

            .. tab:: Run application

                .. code-block:: console

                        $ pycompss run [COMPSS_ARGS] APP_FILE [APP_ARGS]

                APP_FILE is required and must be a valid python file.
                APP_ARGS is optional and can be used to pass any argument to the application.

                .. collapse:: COMPSS_ARGS is optional and can accept the following arguments

                    .. literalinclude:: runcompss_args.txt
                        :language: text
                        :linenos:

                Init a docker environment in the root of the repository. The source
                files path are resolved from the init directory which sometimes can be
                confusing. As a rule of thumb, initialize the library in a current
                directory and check the paths are correct running the file with
                ``python3 path_to/file.py`` (in this case
                ``python3 python/matmul_files/src/matmul_files.py``).

                .. code-block:: console

                    $ cd tutorial_apps
                    $ pycompss init docker

                Now we can run the ``matmul_files.py`` application:

                .. code-block:: console

                    $ pycompss run python/matmul_files/src/matmul_files.py 4 4

                The log files of the execution can be found at ``$HOME/.COMPSs``.

                You can also init the docker environment inside the examples folder.
                This will mount the examples directory inside the container so you can
                execute it without adding the path:

                .. code-block:: console

                    $ pycompss init docker -w python/matmul_files/src
                    $ pycompss run matmul_files.py 4 4

            .. tab:: Submit application execution (job) to queuing system

                **Not available**

                Not available.
                Submitting jobs for applications is only possible for remote and local environments.

   .. group-tab:: Local

        .. tabs::

            .. tab:: Run application

                .. code-block:: console

                        $ pycompss run [COMPSS_ARGS] APP_FILE [APP_ARGS]

                APP_FILE is required and must be a valid python file.
                APP_ARGS is optional and can be used to pass any argument to the application.

                .. collapse:: COMPSS_ARGS is optional and can accept the following arguments

                    .. literalinclude:: runcompss_args.txt
                        :language: text
                        :linenos:

                Init a local environment in the root of the repository. The source
                files path are resolved from the init directory which sometimes can be
                confusing. As a rule of thumb, initialize the library in a current
                directory and check the paths are correct running the file with
                ``python3 path_to/file.py`` (in this case
                ``python3 python/matmul_files/src/matmul_files.py``).

                .. code-block:: console

                    $ cd tutorial_apps
                    $ pycompss init local

                Now we can run the ``matmul_files.py`` application:

                .. code-block:: console

                    $ pycompss run python/matmul_files/src/matmul_files.py 4 4

                The log files of the execution can be found at ``$HOME/.COMPSs``.

                You can also init the local environment inside the examples folder.
                This will mount the examples directory inside the container so you can
                execute it without adding the path:

                .. code-block:: console

                    $ pycompss init local -w python/matmul_files/src
                    $ pycompss run matmul_files.py 4 4

            .. tab:: Submit application execution (job) to queuing system

                .. IMPORTANT::

                    To be able to submit a job in a local environment you must have installed
                    some cluster management/job scheduling system .i.e SLURM, SGE, PBS, etc.

                The ``pycompss job`` command can be used to submit, cancel and list jobs to a remote environment.
                It is only available for local and remote environments.

                .. code-block:: console

                    $ pycompss job submit -e [ENV_VAR...] [COMPSS_ARGS] APP_FILE [APP_ARGS]

                ENV_VAR is optional and can be used to pass any environment variable to the application.
                APP_FILE is required and must be a valid python file inside app directory.
                APP_ARGS is optional and can be used to pass any argument to the application.

                .. collapse:: COMPSS_ARGS is optional and can accept the following arguments

                    .. literalinclude:: enqueue_compss_args.txt
                        :language: text
                        :linenos:


                The command will submit a job and return the Job ID.
                In order to run a COMPSs program on the local machine we can use the command:

                .. code-block:: console

                    $ cd tutorial_apps/python/matmul_files/src
                    $ pycompss job submit -e ComputingUnits=1 --num_nodes=2 --exec_time=10 --worker_working_dir=local_disk --tracing=false --lang=python --qos=debug matmul_files.py 4 4


   .. group-tab:: Remote


        .. tabs::

            .. tab:: Submit application execution (job) to queuing system

                The ``pycompss job`` command can be used to submit, cancel and list jobs to a remote environment.
                It is only available for local and remote environments.

                .. code-block:: console

                    $ pycompss job submit -e [ENV_VAR...] -app APP_NAME [COMPSS_ARGS] APP_FILE [APP_ARGS]

                ENV_VAR is optional and can be used to pass any environment variable to the application.
                APP_NAME is required and must be a valid application name previously deployed.
                APP_FILE is required and must be a valid python file inside app directory.
                APP_ARGS is optional and can be used to pass any argument to the application.

                .. collapse:: COMPSS_ARGS is optional and can accept the following arguments

                    .. literalinclude:: enqueue_compss_args.txt
                        :language: text
                        :linenos:



                **Set environment variables (-e, --env_var)**

                .. code-block:: console

                    $ pycompss job submit -e MYVAR1 --env MYVAR2=foo APPNAME EXECFILE ARGS

                Use the -e, --env_var flags to set simple (non-array) environment variables in the remote environment.
                Or overwrite variables that are defined in the `init` command of the environment.

                **Submitting Jobs**

                The command will submit a job and return the Job ID.
                In order to run a COMPSs program on the local machine we can use the command:

                .. code-block:: console

                    $ pycompss job submit -e ComputingUnits=1 -app matmul --num_nodes=2 --exec_time=10 --master_working_dir={COMPS_APP_PATH} --worker_working_dir=local_disk --tracing=false --pythonpath={COMPS_APP_PATH}/src --lang=python --qos=debug {COMPS_APP_PATH}/src/matmul_files.py 4 4


                .. NOTE::

                        We can also use a macro specific to this CLI in order to use absolute paths:
                        ``{COMPS_APP_PATH}`` will be resolved by the CLI and replaced with the /absolute/path/to/app on the remote cluster.


            .. tab:: Run application

                **Not available**

                Not available.
                A remote type environment only accepts submitting jobs for deployed applications.
                See ``Job`` tab for more information.

Managing jobs
-------------

Once the job is submitted, it can be inspected using the ``pycompss job list`` command.


The command will list all pending/running jobs subbmited in this environment.

.. code-block:: console

    $ pycompss job list
            SUCCESS
            19152612        - RUNNING       - COMPSs

Every subbmited job that didn't finish yet can be cancelled using the ``pycompss job cancel`` command.

.. code-block:: console

    $ pycompss job cancel 19152612 # JOBID
        Job `19152612` cancelled

You can also check the status of a particular job with the ``pycompss job status`` command.

.. code-block:: console

    $ pycompss job status 19152612 # JOBID
        SUCCESS:RUNNING

Also we can query the history of past jobs and we'll get the app name, the environment variables and
the enqueue_compss arguments used to submit the job.

.. code-block:: console

    $ pycompss job history --job_id 19152612
        Environment Variables: ComputingUnits=1
        Enqueue Args:   --num_nodes=2
                        --exec_time=10
                        --worker_working_dir=local_disk
                        --tracing=false
                        --lang=python
                        --qos=debug
                        matmul_files.py 4 4


Running the COMPSs monitor
--------------------------

.. tabs::

   .. group-tab:: Docker

        The COMPSs monitor can be started using the ``pycompss monitor start``
        command. This will start the COMPSs monitoring facility which enables to
        check the application status while running. Once started, it will show
        the url to open the monitor in your web browser
        (i.e. http://127.0.0.1:8080/compss-monitor)

        .. IMPORTANT::

            Include the ``--monitor=<REFRESH_RATE_MS>`` flag in the execution before
            the binary to be executed.

        .. code-block:: console

            $ pycompss monitor start
            $ pycompss run --monitor=1000 -g matmul_files.py 4 4
            $ # During the execution, go to the URL in your web browser
            $ pycompss monitor stop

        If running a notebook, just add the monitoring parameter into the COMPSs
        runtime start call.

        Once finished, it is possible to stop the monitoring facility by using
        the ``pycompss monitor stop`` command.

   .. group-tab:: Local

        The COMPSs monitor can be started using the ``pycompss monitor start``
        command. This will start the COMPSs monitoring facility which enables to
        check the application status while running. Once started, it will show
        the url to open the monitor in your web browser
        (i.e. http://127.0.0.1:8080/compss-monitor)

        .. IMPORTANT::

            Include the ``--monitor=<REFRESH_RATE_MS>`` flag in the execution before
            the binary to be executed.

        .. code-block:: console

            $ pycompss monitor start
            $ pycompss run --monitor=1000 -g matmul_files.py 4 4
            $ # During the execution, go to the URL in your web browser
            $ pycompss monitor stop

        If running a notebook, just add the monitoring parameter into the ``pycompss jupyter`` call.

        Once finished, it is possible to stop the monitoring facility by using
        the ``pycompss monitor stop`` command.

   .. group-tab:: Remote

        Not implemented yet.



Running Jupyter notebooks
-------------------------

.. tabs::

   .. group-tab:: Docker

        Notebooks can be run using the ``pycompss jupyter`` command. Run the
        following snippet from the root of the project:

        .. code-block:: console

            $ cd tutorial_apps/python
            $ pycompss jupyter ./notebooks

        And access interactively to your notebook by opening following the
        http://127.0.0.1:8888/ URL in your web browser.


   .. group-tab:: Local

        Notebooks can be run using the ``pycompss jupyter`` command. Run the
        following snippet from the root of the project:

        .. code-block:: console

            $ cd tutorial_apps/python
            $ pycompss jupyter ./notebooks

        A web browser will opened automatically with the notebook.

        You could also add any jupyter argument to the command, like for example
        the port number:

        .. code-block:: console

            $ pycompss jupyter --port 9999 ./notebooks

   .. group-tab:: Remote

        In order to run a jupyter notebook in remote, it must be bound to an already deployed app

        Let's deploy another application that contains jupyter notebooks:

        .. code-block:: console

            $ pycompss app deploy synchronization --source_dir tutorial_apps/python/notebooks/syntax/

        The command will be executed inside the remote directory specified at deployment.
        The path for the selected application will be automatically resolved and the jupyter server
        will be started and you'll be promted with the URL of the jupyter web page.

        .. code-block:: console

            $ pycompss jupyter -app synchronization --port 9999
                Job submitted: 19320191
                Waiting for jupyter to start...
                Connecting to jupyter server...
                Connection established. Please use the following URL to connect to the job.
                http://localhost:9999/?token=35199bb8917a97ef2ed0e7a79fbfb6e4c727983bb3a87483
                Ready to work!
                To force quit: CTRL + C

        .. dropdown:: How to use Jupyter in MN4 from local machine with PyCOMPSs CLI?
          :container: + shadow
          :title: bg-primary text-white text-center font-weight-bold
          :body: bg-light font-italic

          .. dropdown:: **1st Step (to be done in your laptop)**
              :open:

              Create the MN4 environment in the PyCOMPSs CLI:

              .. code-block:: console

                  pycompss init -n mn4 cluster -l <MN4_USER>@mn1.bsc.es


              By default, ``pycompss`` creates the local environment, and since the objective
              is to run in MN4, this command will create the MN4 environment and set it by
              default.

              .. IMPORTANT::

                  This environment will use the ``mn1.bsc.es`` login node to submit the
                  job, and the notebook will be started within a MN4 compute node.


          .. dropdown:: **2nd Step (to be done in your laptop)**
              :open:

              Go to the folder where your notebook is in your local machine.

              .. code-block:: console

                  cd /path/to/notebook/


          .. dropdown:: **3rd Step (to be done in your laptop)**
              :open:

              Deploy the current folder to MN4 with the following command:

              .. code-block:: console

                  pycompss app deploy mynotebook

              This command will copy the whole current folder into your ``$HOME/.COMPSsApps/``
              folder, and will be used from jupyter notebook.

              It will register ``mynotebook`` name (choose the name that you want), so
              that it can be used in the next step.


          .. dropdown:: **4th Step (to be done in your laptop)**
              :open:

              Launch a jupyter job into MN4 using the deployed folder with name
              ``mynotebook`` (or the name defined in previous step):

              .. code-block:: console

                  pycompss jupyter -app mynotebook --qos=debug --exec_time=20

              A job will be submitted to MN4 queueing system within the ``debug`` queue and
              with a ``20 minutes`` walltime. **Please, wait for it to start**.
              It can be checked with ``squeue`` from MN4 while waiting, and its expected
              start time with ``squeue --start`` command.

              This job **will deploy the PyCOMPSs infrastructure** in the given nodes.

              Once started, the URL to open jupyter from your web browser will automatically
              appear a few seconds after the job started. Output example:

              .. code-block:: console

                  Job submitted: 20480430
                  Waiting for jupyter to start...
                  Jupyter started
                  Connecting to jupyter server...
                  Connection established. Please use the following URL to connect to the job.
                  http://localhost:8888/?token=c653b02a899265ad6c9cf075d4882f91d9d372b06132d1fe
                  Ready to work!
                  To force quit: CTRL + C


          .. dropdown:: **5th Step (to be done in your laptop)**
              :open:

              Open the given URL (*in some consoles with CTRL + left click*) in your local web
              browser and you can start working with the notebook.

              Inside the notebook, PyCOMPSs must be imported, its runtime started, tasks
              defined, etc.

              **Please, check the documentation to get help and examples:**

                - `PyCOMPSs programming model <https://pycompss.readthedocs.io/en/stable/Sections/02_App_Development/02_Python/01_Programming_model.html>`_
                - `Jupyter API (pycompss start, stop, etc.) <https://pycompss.readthedocs.io/en/stable/Sections/02_App_Development/02_Python/03_Jupyter_integration.html>`_
                - `Sample notebooks <https://pycompss.readthedocs.io/en/stable/Sections/09_PyCOMPSs_Notebooks.html>`_
                - `Tutorial <https://pycompss.readthedocs.io/en/stable/Sections/10_Tutorial/02_PyCOMPSs.html>`_

              .. CAUTION::

                  If the walltime of the job is reached, the job will be killed by the
                  queuing system and the notebook will stop working.


          .. dropdown:: **6th Step (to be done in your laptop)**
              :open:

              Once finished working with the notebook, press ``CTRL+C`` in the console where you
              launched the ``pycompss jupyter`` command. This will trigger the job
              cancellation.


Generating the task graph
-------------------------

COMPSs is able to produce the task graph showing the dependencies that
have been respected. In order to producee it, include the ``--graph`` flag in
the execution command:

.. tabs::

   .. group-tab:: Docker

        .. code-block:: console

            $ cd tutorial_apps/python/simple/src
            $ pycompss init docker
            $ pycompss run --graph simple.py 1

        Once the application finishes, the graph will be stored into the
        ``.COMPSs\app_name_XX\monitor\complete_graph.dot`` file. This dot file
        can be converted to pdf for easier visualilzation through the use of the
        ``gengraph`` parameter:

        .. code-block:: console

            $ pycompss gengraph .COMPSs/simple.py_01/monitor/complete_graph.dot

        The resulting pdf file will be stored into the
        ``.COMPSs\app_name_XX\monitor\complete_graph.pdf`` file, that is, the
        same folder where the dot file is.


   .. group-tab:: Local

        .. code-block:: console

            $ cd tutorial_apps/python/simple/src
            $ pycompss run --graph simple.py 1

        Once the application finishes, the graph will be stored into the
        ``~\.COMPSs\app_name_XX\monitor\complete_graph.dot`` file. This dot file
        can be converted to pdf for easier visualilzation through the use of the
        ``gengraph`` parameter:

        .. code-block:: console

            $ pycompss gengraph ~/.COMPSs/simple.py_01/monitor/complete_graph.dot

        The resulting pdf file will be stored into the
        ``~\.COMPSs\app_name_XX\monitor\complete_graph.pdf`` file, that is, the
        same folder where the dot file is.

   .. group-tab:: Remote

        Not implemented yet!



Tracing applications or notebooks
---------------------------------

COMPSs is able to produce tracing profiles of the application execution
through the use of EXTRAE. In order to enable it, include the ``--tracing``
flag in the execution command:

.. code-block:: console

    $ cd python/matmul_files/src
    $ pycompss run --tracing matmul_files.py 4 4

If running a notebook, just add the tracing parameter into ``pycompss jupyter`` call.

Once the application finishes, the trace will be stored into the
``~\.COMPSs\app_name_XX\trace`` folder. It can then be analysed with
Paraver.


Adding more nodes
-----------------

.. tabs::

   .. group-tab:: Docker

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

        -  '127.0.0.1': is the IP used for ssh (can also be a hostname like 'localhost' as long as it can be resolved).
        -  '6': desired number of available computing units for the new node.


        .. IMPORTANT::

            Please be aware** that ``pycompss components`` will not list your
            custom nodes because they are not docker processes and thus it can't be
            verified if they are up and running.


   .. group-tab:: Local

        Environment not compatible with this feature.

   .. group-tab:: Remote

        Environment not compatible with this feature.


Removing existing nodes
-----------------------

.. tabs::

   .. group-tab:: Docker

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


   .. group-tab:: Local

        Environment not compatible with this feature.

   .. group-tab:: Remote

        Environment not compatible with this feature.
