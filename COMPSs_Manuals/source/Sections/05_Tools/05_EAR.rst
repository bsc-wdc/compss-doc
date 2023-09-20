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

Power consumption with COMPSs depends on the `Energy Management Framework for HPC (EAR) <https://www.bsc.es/research-and-development/software-and-apps/software-list/ear-energy-management-framework-hpc>`_
thus, it must be `installed <https://gitlab.bsc.es/ear_team/ear/-/wikis/Admin-guide>`_ before the ear option can be used.


Usage
-----

The way of activating the energy measurement of a Workflow with COMPSs is very simple.
One must only enable the ``--ear`` flag followed by ``true`` or the EAR parameters when
using ``enqueue_compss`` to submit a COMPSs application. As shown in the help option:

.. code-block:: console

    $ enqueue_compss -h

    (...)
    --ear=<string>                          Activate the usage of EAR for power consumption measurement.
                                            The value of string are the parameter to be used with EAR.
                                            Default: false


In particular, the ``<string>`` defined for the ``--ear`` flag is passed directly to EAR.
Consequently, any EAR parameter desired by the user can be defined through the flag.

.. IMPORTANT::

    EAR also supports some parameters through the environment variables definition
    (`check EAR documentation <https://gitlab.bsc.es/ear_team/ear/-/wikis/User-guide>`_).

    The following example shows some of these parameters.


Example
-------

This section illustrates how to measure the power consumption of a sample application
(:ref:`Sections/07_Sample_Applications/02_Python/03_Kmeans:Kmeans`) in MareNostrum 4.

The first step is to connect to MareNostrum 4 and create a ``kmeans.py`` file containing the
the Kmeans application shown in :ref:`Sections/07_Sample_Applications/02_Python/03_Kmeans:Kmeans`
example.

The second step is to create a submission script, for example `launch_kmeans_ear.sh`. This script
loads all necessary MN4 modules as well as invokes the `enqueue_compss` command to submit
the ``kmeans.py`` application execution to SLURM with the required ``--ear`` flag for power
consumption measurement:

.. code-block:: bash
    :emphasize-lines: 5,8,10,15-17,42,43
    :caption: `launch_kmeans_ear.sh script on MN4`
    :name: launch_kmeans_ear_script

    #!/bin/bash -e

    export COMPSS_PYTHON_VERSION=3
    module load COMPSs/Trunk
    module load ear/4.3-compss

    # Add earld.so to LD_LIBRARY_PATH
    export LD_LIBRARY_PATH=${EAR_INSTALL_PATH}/lib/:$LD_LIBRARY_PATH

    export EAR_CPU_TDP=150
    # Uncomment the next line to enable EAR verbosity
    #export EAR_VERBOSE="--ear-verbose=1"
    # The next lines define the path where EAR metrics will be stored
    # (note that ends with the prefix for the metrics file name).
    export EAR_METRICS_PATH=$HOME/ear_compss_metrics/kmeans/
    mkdir -p $EAR_METRICS_PATH
    export EAR_METRICS="--ear-user-db=$EAR_METRICS_PATH/kmeans"

    # Define script variables
    scriptDir=$(pwd)/$(dirname $0)
    execFile=${scriptDir}/src/kmeans.py
    appPythonpath=${scriptDir}/src/

    # Retrieve arguments
    numNodes=$1
    executionTime=$2
    tracing=$3

    # Leave application args on $@
    shift 3

    # Enqueue the application
    enqueue_compss \
        --qos=debug \
        --num_nodes=$numNodes \
        --exec_time=$executionTime \
        --worker_working_dir=$(pwd) \
        --tracing=$tracing \
        --graph=$tracing \
        --pythonpath=$appPythonpath \
        --lang=python \
        --constraints=perfparanoid \
        --ear="\"--ear=on ${EAR_METRICS} \"" \
        $execFile $@


    ######################################################
    # APPLICATION EXECUTION EXAMPLE
    # Call:
    #       ./launch_kmeans_ear.sh <NUMBER_OF_NODES> <EXECUTION_TIME> <TRACING> <POINTS> <DIMENSIONS> <CENTERS> <FRAGMENTS>
    #
    # Example:
    #       ./launch_kmeans_ear.sh 2 10 false 72000 3 4 72
    #
    #####################################################


Next, we can then give execution permission to the submission script and launch our kmeans execution with EAR:

.. code-block:: console

    $ chmod 744 launch_kmeans_ear.sh
    $ ./launch_kmeans_ear.sh 2 10 false 72000 3 4 72

This will submit the job to SLURM and we will have to wait for its completion.


Result metrics
--------------

Once the application has finished, a new folder containing the EAR metrics will be created
in the ``${HOME}/ear_compss_metrics/kmeans/`` (defined with the ``EAR_METRICS_PATH`` environment variable).
Its contents will look like:

.. code-block:: console

    $ cd ${HOME}/ear_compss_metrics/
    $ ear_compss_metrics> tree
    .
    └── kmeans
        ├── kmeans.s10r2b48.time.csv
        ├── kmeans.s10r2b48.time.loops.csv
        ├── kmeans.s14r2b24.time.csv
        └── kmeans.s14r2b24.time.loops.csv


Each file contains the power consumption among other metrics gathered by EAR per process.
In particular, this execution has been performed with two MN4 nodes, where the first node
contains 24 worker processes and the second 48 worker processes.

These log files can be visualized with `Grafana <https://grafana.com/>`_ for a more convenient
power consumption and performance analysis.

.. WARNING::

    **Metrics Visualization is under construction.**
