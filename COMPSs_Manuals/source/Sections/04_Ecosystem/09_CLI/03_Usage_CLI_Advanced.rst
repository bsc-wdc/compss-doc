.. spelling:word-list::

   Subcommand


Advanced User Guide
===================

This document provides a comprehensive technical guide for the PyCOMPSs Command Line Interface (CLI). It is designed to take users from foundational concepts to advanced deployment strategies and industry best practices.

Architecture
~~~~~~~~~~~~

The PyCOMPSs CLI leverages a modular architecture tailored for diverse execution backends:

- **Environment Manager**: Orchestrates multiple execution contexts (Local, Docker, Remote, UNICORE).
- **Argument Parser**: Handles the parsing of complex command-line inputs and flags.
- **Action Dispatcher**: Routes commands to their respective internal handlers.
- **Environment Backends**: Provides specific implementations for the nuances of each environment.
- **GUI Interface**: An optional graphical layer for visual resource management.

Execution Workflow
~~~~~~~~~~~~~~~~~~

The CLI follows a deterministic execution pipeline:

1. **Global Argument Parsing**: Evaluation of system-wide flags (e.g., version, debug, plain).
2. **Logging Initialization**: Configuration of telemetry and logs based on user preferences.
3. **Environment Validation**: Verification of the current and default environments.
4. **Host Initialization**: Setup of environment-specific parameters.
5. **Subcommand Parsing**: Analysis of the specific action requested.
6. **Action Dispatch**: Routing the request to the corresponding backend handler.
7. **Execution & Error Handling**: Final execution with integrated exception management.

Command Structure
-----------------

The CLI employs a hierarchical command structure. Its availability is dynamic, adapting automatically to the currently active environment.


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

.. pycompss-command:: pycompss

    **PyCOMPSs Command Line Interface**
    The primary entry point for managing COMPSs applications across diverse environments.

    .. pycompss-argument:: pycompss_global_debug
        :name: -d, --debug
        :action: store_true
        :help: Enables debug mode for detailed troubleshooting and verbosity.

    .. pycompss-argument:: pycompss_global_info
        :name: -i, --info
        :action: store_true
        :help: Enables info mode to provide high-level execution summaries.

    .. pycompss-argument:: pycompss_global_plain
        :name: -p, --plain
        :action: store_true
        :help: Disables ANSI colors and formatting for plain-text output.

    .. pycompss-argument:: pycompss_global_sanitize
        :name: -s, --sanitize
        :action: store_true
        :help: Sanitizes output to prevent sensitive data from appearing in logs or standard error.

    .. pycompss-argument:: pycompss_global_version
        :name: -v, --version
        :action: store_true
        :help: Displays the current CLI version.

    .. pycompss-argument:: pycompss_global_gui
        :name: -g, --gui
        :action: store_true
        :help: Launches the graphical user interface.

Environments
------------

PyCOMPSs CLI supports various execution environments, each providing different levels of isolation and scalability.

.. pycompss-command:: environment
    :aliases: env

    **Environment Management**

    Facilitates the creation, auditing, and modification of COMPSs environments. The CLI dynamically adjusts available subcommands based on the environment type.

    **Subcommand Matrix:**

    ==========  ==========================  ==============================
    Subcommand  Description                 Available Environments
    ==========  ==========================  ==============================
    init        Initialize new environment  local, docker, remote, unicore
    list        List all environments       local, docker, remote, unicore
    show        Audit environment details   local, docker, remote, unicore
    change      Switch active environment   local, docker, remote, unicore
    remove      Decommission environment    local, docker, remote, unicore
    ==========  ==========================  ==============================

.. pycompss-subcommand:: environment_init
    :aliases: i

    **Environment Initialization**

    Provisions a new COMPSs environment. The chosen type defines the subsequent operational capabilities.

    .. pycompss-argument:: env_init_name
        :name: -n, --name
        :type: str
        :default: unique_uuid
        :help: A unique identifier for the environment.

    **Environment Profiles:**

    **Local**

    Executes on the current host. Recommended for rapid prototyping and unit testing.

    .. code-block:: bash

        pycompss environment init -n my_local_env local

    **Docker**

    Provides full containerization for maximum reproducibility. Requires a running Docker daemon.

    .. code-block:: bash

        pycompss environment init -n my_docker_env docker

    **Remote**

    Targets external clusters or supercomputers, enabling large-scale distributed execution.

    .. code-block:: bash

        pycompss environment init -n my_cluster remote

    **UNICORE**

    A specialized environment for high-security HPC resource management.

    .. code-block:: bash

        pycompss environment init -n my_unicore_env unicore

Dynamic Command Availability
----------------------------

To reduce complexity, the CLI only exposes commands pertinent to the active environment.

**Local Environment Capabilities:**

.. code-block:: bash

  pycompss environment list   # Audit environments
  pycompss environment show   # Inspect environment details
  pycompss dep_check          # COMPSs dependency validation
  pycompss install            # Install COMPSs runtime
  pycompss run                # Application execution
  pycompss exec               # Direct command execution
  pycompss status             # Environments status
  pycompss components list    # Infrastructure management
  pycompss inspect            # RO-Crate analysis
  pycompss monitor            # Telemetry control
  pycompss jupyter            # Jupyter environment setup
  pycompss gengraph           # Graph generation
  pycompss gentrace           # Paraver trace generation
  pycompss tutorial           # Tutorial configuration

**Docker Environment Capabilities:**

.. code-block:: bash

  pycompss environment list
  pycompss environment show
  pycompss run
  pycompss exec
  pycompss status
  pycompss components list
  pycompss tutorial
  pycompss monitor --new_monitor  # Requires Docker/Apptainer

**Remote Environment Capabilities:**

.. code-block:: bash

  pycompss environment list
  pycompss environment show
  pycompss exec
  pycompss status
  pycompss app deploy              # Remote deployment
  pycompss app remove              # Application decommissioning
  pycompss app list                # Deployed apps inventory
  pycompss job submit              # Job submission
  pycompss job status              # Job tracking
  pycompss job cancel              # Job termination
  pycompss job list                # Job inventory
  pycompss job history             # Historical audit
  pycompss jupyter
  pycompss monitor

Execution Commands
------------------

.. pycompss-command:: run
    :aliases: r

    **Application Execution**

    Launches a PyCOMPSs application via ``runcompss``. This command allows fine-grained control over resource allocation and monitoring.

    .. pycompss-argument:: run_app_name
        :name: -app, --app_name
        :type: str
        :default: ""
        :help: Target application name (required for remote environments).

    **Usage Examples:**

    .. code-block:: bash

        # Execute application
        pycompss run my_app.py

    **Advanced Configurations:**

    .. code-block:: bash

        # Complex resource specification
        pycompss run my_app.py \\
            --target=16 \\
            --resources='cores=16,memory=32GB,disk=100GB' \\
            --profile=full
        # High-verbosity execution for debugging
        pycompss run my_app.py \\
            --target=4 \\
            --log_level=debug \\
            --trace_level=ALL

.. pycompss-command:: exec
    :aliases: e

    **Contextual Command Execution**

    Executes a shell command directly within the COMPSs runtime context. This is essential for utilizing environment-aware tools.

    **Usage Examples:**

    .. code-block:: bash

        # Execute scripts within the runtime
        pycompss exec python script.py
        pycompss exec bash prepare_environment.sh
        # Direct system calls
        pycompss exec ls -la /tmp
        # Internal COMPSs tool execution
        pycompss exec compss_status
        pycompss exec compss_monitor --start

.. pycompss-command:: install
    :aliases: ins

    **Runtime Installation**

    Installs the COMPSs runtime in the active environment using predefined profiles.

    **Options:**

    .. pycompss-argument:: install_profile
        :name: --profile
        :choices: full, minimal, C, Python, R
        :help: The installation profile to apply.

    .. pycompss-argument:: install_release
        :name: --release
        :type: str
        :help: Specific version string (e.g., 3.4.5).

    **Usage Examples:**

    .. code-block:: bash

        # Standard full installation (recommended)
        pycompss install --profile full
        # Minimal footprint installation
        pycompss install --profile minimal
        # Language-specific installation (Python)
        pycompss install --profile Python
        # Targeted version installation
        pycompss install --release 3.4.5

.. pycompss-command:: dep_check
    :aliases: dc

    **Dependency Validation**

    Performs a comprehensive audit of the system to ensure all COMPSs prerequisites are met.

    **Options:**

    .. pycompss-argument:: dep_check_profile
        :name: --profile
        :choices: full, minimal, C, Python, R
        :help: The dependency profile to validate.

    **Usage Examples:**

    .. code-block:: bash

        # Full dependency audit
        pycompss dep_check --profile full
        # Lightweight validation
        pycompss dep_check --profile minimal
        # HPC-optimized mode (reporting only)
        pycompss dep_check --hpc

Remote Application Management
-----------------------------

.. pycompss-command:: app
    :aliases: a

    **Remote Application Management**

    Provides tools for the deployment and lifecycle management of applications in remote environments.

    **Subcommands:**

    .. pycompss-subcommand:: app_deploy
        :aliases: d

        **Application Deployment**

        Synchronizes and deploys the application to the remote target.

        .. pycompss-argument:: app_deploy_name
            :name: app_name
            :type: str
            :help: The name of the application to deploy.

        .. pycompss-argument:: app_deploy_source
            :name: -sd, --source_dir
            :type: str
            :default: current directory
            :help: Source directory for file transfer.

        .. pycompss-argument:: app_deploy_destination
            :name: -dd, --destination_dir
            :type: str
            :help: Remote destination path.

        .. pycompss-argument:: app_deploy_setup_file
            :name: -sf, --setup_file
            :type: str
            :help: Path to the setup file for environment variables/modules.

        **Usage Examples:**

        .. code-block:: bash

            # Standard deployment from current directory
            pycompss app deploy my_app
            # Explicit path deployment
            pycompss app deploy my_app \\
                --source_dir=/path/to/app \\
                --destination_dir=/opt/com/apps/my_app

    .. pycompss-subcommand:: app_remove
        :aliases: rm

        **Application Decommissioning**

        Removes one or more deployed applications from the remote environment.

        **Usage Examples:**

        .. code-block:: bash

            # Remove application with confirmation
            pycompss app remove my_app
            # Force removal without confirmation
            pycompss app remove --yes my_app

    .. pycompss-subcommand:: app_list
        :aliases: l

        **Application Inventory**

        Lists all applications currently deployed on the remote target.

        **Options:**

        .. pycompss-argument:: app_list_no_table
            :name: --no_table
            :action: store_true
            :help: Outputs the list as plain text instead of a formatted table.

Remote Job Management
---------------------

.. pycompss-command:: job
    :aliases: j

    **Remote Job Orchestration**

    Manages the submission, monitoring, and termination of remote jobs.

    **Subcommands:**

    .. pycompss-subcommand:: job_submit
        :aliases: sub

        **Job Submission**

        Submits an application to the remote scheduler for execution.

        **Runcompss Integration:**
        All standard ``runcompss`` arguments are supported and passed through directly.

        **Options:**

        .. pycompss-argument:: job_submit_verbose
            :name: --verbose, -v
            :action: store_true
            :help: Prints the final shell command executed on the remote host.

        .. pycompss-argument:: job_submit_extra_env_vars
            :name: -eev, --extra_env_vars
            :action: append
            :nargs: +
            :type: str
            :help: Append additional environment variables.

        .. pycompss-argument:: job_submit_extra_env_modules
            :name: -eem, --extra_env_modules
            :action: append
            :nargs: +
            :type: str
            :help: Append additional environment modules.

        **Usage Examples:**

        .. code-block:: bash

            # Submit job with resource target
            pycompss job submit my_app --target=8
            # Submit with custom environment variables
            pycompss job submit my_app \\
                --extra_env_vars MY_VAR=value1 \\
                --extra_env_vars ANOTHER_VAR=value2

    .. pycompss-subcommand:: job_status
        :aliases: st

        **Job Tracking**

        Queries the current state of a specific job.

        **Arguments:**

        .. pycompss-argument:: job_status_id
            :name: job_id
            :type: str
            :help: The unique ID of the job.

    .. pycompss-subcommand:: job_cancel
        :aliases: cj

        **Job Termination**

        Immediately cancels a running or pending job.

    .. pycompss-subcommand:: job_list
        :aliases: lj

        **Job Inventory**

        Displays all jobs submitted to the remote target.

    .. pycompss-subcommand:: job_history
        :aliases: hj

        **Job Audit Trail**

        Provides a historical log of submitted jobs and their associated parameters.

Infrastructure Management
-------------------------
.. pycompss-command:: components
    :aliases: c

    **Infrastructure Resource Management**

    Allows dynamic scaling of the COMPSs infrastructure by adding or removing worker nodes.

    **Subcommands:**

    .. pycompss-subcommand:: components_list
        :aliases: l

        **Active Components Audit**

        Lists all active workers and resources currently available in the cluster.

    .. pycompss-subcommand:: components_add
        :aliases: a

        **Resource Scaling (Up)**

        Integrates new worker nodes into the COMPSs pool.

        .. pycompss-subsubcommand:: add_worker
            :aliases: w

            **Add Worker Nodes**

            **Arguments:**

            .. pycompss-argument:: add_worker_num
                :name: worker
                :type: str
                :default: "1"
                :help: Number of workers to add (Integer or <IP>:<CORES>).

    .. pycompss-subcommand:: components_remove
        :aliases: r

        **Resource Scaling (Down)**

        Removes worker nodes from the infrastructure.

Monitoring and Analysis
-----------------------

.. pycompss-command:: inspect
    :aliases: i

    **RO-Crate Inspection**

    Analyzes RO-Crate files to extract granular execution data, including task dependencies and data asset lineage.

    **Arguments:**

    .. pycompss-argument:: inspect_ro_crate
        :name: ro_crate
        :type: str
        :nargs: +
        :help: Directory or ZIP file(s) containing the RO-Crate.

    **Options:**

    .. pycompss-argument:: inspect_verbose
        :name: -v, --verbose
        :action: store_true
        :help: Enables verbose output for task details.

    .. pycompss-argument:: inspect_failing_tasks
        :name: -f, --failing_tasks
        :action: store_true
        :help: Filters output to show only failed tasks.

.. pycompss-command:: monitor
    :aliases: m

    **Telemetry Control**

    Manages the COMPSs monitoring service for real-time application tracking.

    **Options:**

    .. pycompss-argument:: monitor_new_monitor
        :name: --new_monitor
        :action: store_true
        :help: Launches the next-generation monitor (Requires Docker/Apptainer).

.. pycompss-command:: jupyter
    :aliases: n

    **Jupyter Integration**

    Provisions a Jupyter Notebook instance within the COMPSs environment.

.. pycompss-command:: gengraph
    :aliases: gg

    **Graph Visualization**

    Converts DOT representation files into PDF or other visual formats.

.. pycompss-command:: gentrace
    :aliases: gt

    **Trace Synthesis**

    Aggregates multiple trace files into a unified Paraver-compatible trace.

Advanced Workflows
------------------

Production Deployment
~~~~~~~~~~~~~~~~~~~~~

Recommended pipeline for production-grade deployment:

.. code-block:: bash

  # 1. System Audit
  pycompss status
  pycompss dep_check --profile full
  # 2. Context Setup
  pycompss environment init -n prod_env local
  pycompss environment change prod_env
  # 3. Execution & Validation
  pycompss run my_prod_app --target=32
  # 4. Telemetry
  pycompss monitor start
  # 5. Post-Mortem Analysis
  pycompss inspect ro-crate.file

Distributed Execution
~~~~~~~~~~~~~~~~~~~~~

Workflow for large-scale distributed processing:

.. code-block:: bash

  # Initialize Cluster Environment
  pycompss environment init -n cluster remote
  # Deploy Application
  pycompss app deploy distributed_app
  # Submit with High-Performance Tuning
  pycompss job submit \
      --app_name distributed_app \
      --exec_time=10 \
      --qos=gp_debug \
      --num_nodes=2 \
      --project_name=bscXX \
      my_app.py param1 param2

Troubleshooting
---------------

Common Issues and Solutions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Environment Not Found**
   - **Solution**: Provision a new environment using ``pycompss environment init``.
   - **Verification**: Run ``pycompss status``.
2. **Missing Dependencies**
   - **Solution**: Execute ``pycompss dep_check`` to pinpoint missing libraries.
   - **Fix**: Run ``pycompss install --profile full``.
3. **Remote Connection Failures**
   - **Solution**: Verify SSH credentials and network routing.
   - **Verification**: Use ``pycompss exec ping <remote_host>``.
4. **Permission Denied**
   - **Solution**: Ensure the user has write permissions to COMPSs directories.
   - **Note**: Some installation tasks require ``sudo`` privileges.

Debugging
~~~~~~~~~

To isolate issues, enable high-verbosity logging:

.. code-block:: bash

  # Debug mode for execution
  pycompss --debug run my_app.py
  # Clean debug logs (no colors)
  pycompss --plain --debug run my_app.py

Best Practices
--------------

1. **Environment Isolation**: Use distinct environments for development, testing, and production to avoid configuration drift.
2. **Dynamic Resource Scaling**: Use ``pycompss components list`` to monitor load and scale worker nodes dynamically.
3. **Execution Auditing**: Always maintain logs and use the ``inspect`` command on RO-Crates to ensure reproducibility.
4. **Proactive Monitoring**: Launch the monitor *prior* to execution to capture the full application lifecycle.
5. **Dependency Management**: Use the ``full`` profile during installation to minimize runtime errors in distributed environments.