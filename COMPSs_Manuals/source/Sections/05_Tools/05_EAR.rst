Energy Measurement with EAR
===========================

The COMPSs Framework includes the integration with the
`Energy Management Framework for HPC (EAR) <https://www.bsc.es/research-and-development/software-and-apps/software-list/ear-energy-management-framework-hpc>`_
for **energy consumption** measurement of your workflows.

.. WARNING::

    The power consumption measurement is **ONLY AVAILABLE** for HPC environments
    (i.e. using ``enqueue_compss``) where EAR is available and with Python applications.

    It is **NOT SUPPORTED** using agents, local machines (i.e. using ``runcompss``),
    nor Java/C/C++ COMPSs applications.


.. ATTENTION::

    The integration is on its very first steps and may be *unstable*.

    Please, report any issue that may appear to support-compss@bsc.es so that we can improve the integration.


Software dependencies
---------------------

Power consumption with COMPSs depends on the `Energy Management Framework for HPC (EAR)
<https://www.bsc.es/research-and-development/software-and-apps/software-list/ear-energy-management-framework-hpc>`_.
Consequently, it must be `installed <https://gitlab.bsc.es/ear_team/ear/-/wikis/Admin-guide>`_
before EAR can be used with COMPSs.


Usage
-----

The way of activating the energy measurement of a Workflow with COMPSs is very simple.
One must only set the ``--ear`` flag followed by ``true`` or by the EAR parameters when
using ``enqueue_compss`` to submit a COMPSs application, as shown in the help option:

.. code-block:: console

    $ enqueue_compss -h

    (...)
    --ear=<bool|string>                     Activate the usage of EAR for power consumption measurement.
                                            The value of string are the parameter to be used with EAR.
                                            Default: false


In addition to the boolean, this flag also accepts a ``<string>``, whose value is passed directly to EAR.
Consequently, any EAR parameter desired by the user can be defined through the flag.

.. TIP::

    EAR also supports some parameters through the environment variables definition
    (`check EAR documentation <https://gitlab.bsc.es/ear_team/ear/-/wikis/User-guide>`_).

The resulting metrics will be stored in ``<log_dir>/.COMPSs/<job_id>/energy`` folder,
where a set of ``csv`` files will be populated with the monitorization values.
In particular, there will be **two files per worker node**: one containing the
accumulated values per process, and other (ending with \"loops\") that contains
the values recorded per process at each timestep (by default every 10 seconds).

.. IMPORTANT::

    EAR is also able to harvest hardware counters and record their value during
    the application execution. In some HPCs (e.g. MareNostrum V), it is necessary
    to define the ``perfparanoid`` constraint in the ``enqueue_compss`` command:

    .. code-block:: console

        --constraints=perfparanoid

Example
-------

This section illustrates how to measure the power consumption of a sample application
(:ref:`Sections/07_Sample_Applications/02_Python/03_KMeans:KMeans`) in MareNostrum V.

The first step is to connect to MareNostrum V and create a ``kmeans.py`` file containing the
the KMeans application shown in :ref:`Sections/07_Sample_Applications/02_Python/03_KMeans:KMeans`
example.

The second step is to create a submission script, for example ``launch_kmeans_ear.sh``.
This script loads all necessary MN5 modules as well as invokes the ``enqueue_compss``
command to submit the ``src/kmeans.py`` application execution to SLURM with the
required ``--ear`` flag for power consumption measurement:

.. code-block:: bash
    :emphasize-lines: 29-30
    :caption: `launch_kmeans_ear.sh script on MN5`
    :name: launch_kmeans_ear_script

    #!/bin/bash -e

    export COMPSS_PYTHON_VERSION=3.12.1
    module load COMPSs/Trunk

    # Define script variables
    scriptDir=$(pwd)/$(dirname $0)
    execFile=${scriptDir}/src/kmeans.py
    appPythonpath=${scriptDir}/src/

    # Retrieve arguments
    numNodes=$1
    executionTime=$2

    # Leave application args on $@
    shift 2

    # Enqueue the application
    enqueue_compss \
        --qos=gp_debug \
        --project_name=bsc19 \
        --log_level=off \
        --num_nodes=$numNodes \
        --exec_time=$executionTime \
        --worker_working_dir=$(pwd) \
        --pythonpath=$appPythonpath \
        --lang=python \
        --tracing=true \
        --ear=true \
        --constraints=perfparanoid \
        $execFile $@


    ######################################################
    # APPLICATION EXECUTION EXAMPLE
    # Call:
    #       ./launch_kmeans_ear.sh <NUMBER_OF_NODES> <EXECUTION_TIME> -n <POINTS> -d <DIMENSIONS> -c <CENTERS> -f <FRAGMENTS>
    #
    # Example:
    #       ./launch_kmeans_ear.sh 2 10 -n 72000 -d 3 -c 4 -f 72
    #
    #####################################################

.. IMPORTANT::

    The ``--constraints=perfparanoid`` is required in MN5 in order to get some
    of the performance metrics that EAR is able to harvest during the application
    execution. It may not be needed in other clusters or HPCs.

Next, we can then give execution permission to the submission script and launch
our kmeans execution with EAR:

.. code-block:: console

    $ chmod 744 launch_kmeans_ear.sh
    $ ./launch_kmeans_ear.sh 2 10 -n 224000 -d 3 -c 8 -f 224

This will submit the job to SLURM and we will have to wait for its completion.


Result metrics
--------------

Once the application has finished, the EAR metrics will be created in the
``${HOME}/.COMPSs/<JOB_ID>/energy/`` folder. Its contents will look like:

.. code-block:: console

    $ cd ${HOME}/.COMPSs/123456/energy/
    $ energy> tree
    .
    ├── ear.gs23r3b48.time.csv
    ├── ear.gs23r3b48.time.loops.csv
    ├── ear.gs23r3b54.time.csv
    └── ear.gs23r3b54.time.loops.csv

Note that with the ``launch_kmeans_ear.sh`` script also enables de trace
generation:

.. code-block:: console

    $ cd ${HOME}/.COMPSs/123456/trace/
    $ trace> tree
    .
    ├── master_compss_trace.tar.gz
    ├── static_gs23r3b48-ib0_compss_trace.tar.gz
    └── static_gs23r3b54-ib0_compss_trace.tar.gz


Graphical analysis
------------------

The result metrics can be visualized with Paraver tool. However, in order to
do that, it is necessary to create the trace that can contain only the EAR
harvested metrics or both trace events and EAR metrics in a single trace.

.. IMPORTANT::

    EAR is required in order to generate the traces since its
    ``ear-job-analytics`` tool is used.

Only EAR metrics
~~~~~~~~~~~~~~~~

Since EAR can be used independently of tracing, it is possible to consolidate
the energy ``csv`` files in a trace. To this end, we provide the ``compss_genenergy``
script that converts them automatically. For example, in MareNostrum V:

.. code-block:: console

    $ cd ${HOME}/.COMPSs/123456/energy/
    $ energy> export COMPSS_PYTHON_VERSION=3.12.1
    $ energy> module load COMPSs/Trunk
    $ energy> compss_genenergy
      Merging energy metrics...
      - Found 2 app files.
      - Found 2 loops files.
      - Joining app files... out_jobs.loops.csv
      - Joining loop files... loops.csv
      - Generating average power plot.
        - Total Average Power : 921.8664859999999 Watts (W)
      - Generating accumulated energy plot.
        - Total Accumulated Energy : 50128.568967418585 Joules (J)
      Generating EAR trace:
      - Command: module load ear ear-tools/ear-lite/5.0 ear-tools/ear-job-analytics/5.0; ear-job-analytics --format ear2prv -j 5054023 --input loops.csv
      Using /apps/GPP/EAR-TOOLS/5.0/python3.12/site-packages/ear_analytics/config.json as configuration file...
      reading file out_jobs.loops.csv
      reading file loops.csv
      Warning! Job data hasn't information about job 5054023 step 0 app 1343342. This job-step-app won't be on the output trace.
      Warning! Job data hasn't information about job 5054023 step 1 app 1318032. This job-step-app won't be on the output trace.
      Number of nodes: 2. Total trace duration: 59000000
      Number of applications (job-step): 214
      [...]
    $ energy> ls
      accumulated_energy.png  ear.gs23r3b48.time.csv        ear.gs23r3b54.time.csv        loops.csv  loops.prv  out_jobs.loops.csv
      average_power.png       ear.gs23r3b48.time.loops.csv  ear.gs23r3b54.time.loops.csv  loops.pcf  loops.row

As a result, the ``loops.prv`` file is created and ready to be analyzed.
This trace contains the EAR pre-defined structure and EAR provides a set of
configuration files for their analysis. These configuration files are also
available in the COMPSs installation directory:


.. code-block:: console

    $ ls -l /apps/GPP/COMPSs/Trunk/Dependencies/paraver/cfgs/energy/ear_cfgs
    -rw-r--r-- 1 user users 102387 ago 22 15:50 basic_and_gpu_5.0.cfg
    -rw-r--r-- 1 user users  24311 ago 22 15:50 basic_metrics_5.0.cfg


Both EAR and Trace
~~~~~~~~~~~~~~~~~~

The most interesting visualization analysis can be performed if we merge
the generated trace with the EAR trace. Consequently, it is possible to
visualize the tasks/runtime/communications concurrently with
the EAR monitoring metrics, and see their behavior over time.

To this end, we provide a tool that does all work in a single command:
``compss_gentrace_full`` as an extension of ``compss_gentrace``.
The ``compss_gentrace_full`` command generates the COMPSs trace, then the EAR
trace, and finally merges and synchronizes the events.

.. code-block:: console

    $ cd ${HOME}/.COMPSs/123456/
    $ 123456> export COMPSS_PYTHON_VERSION=3.12.1
    $ 123456> module load COMPSs/Trunk
    $ 123456> compss_gentrace_full
      [...]
    $ 123456> cd final_trace
    $ final_trace> ls -l
      -rw-r--r-- 1 user users    12685 ago 28 16:21 trace.pcf
      -rw-r--r-- 1 user users 65090849 ago 28 16:21 trace.prv
      -rw-r--r-- 1 user users     7252 ago 28 16:21 trace.row


This trace can be analyzed with both EAR cfgs and COMPSs cfgs files in Paraver.
However, in order to improve the correlation between tasks and energy behavior,
we provide specific Paraver cfg files:

.. code-block:: console

    $ ls -l /apps/GPP/COMPSs/Trunk/Dependencies/paraver/cfgs/energy/
    -rw-r--r-- 1 user users 7804 ago 27 16:02 tasks_energy_io.cfg
