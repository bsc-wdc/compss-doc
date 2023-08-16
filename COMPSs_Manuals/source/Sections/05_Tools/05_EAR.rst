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

    Please, report any issue that may appear so that we can improve the integration.


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
the Kmeans application shown in :ref:`Sections/07_Sample_Applications/02_Python/03_Kmeans:Kmeans`.

The second step is to create a submission script, for example `launch_kmeans_ear.sh`. This script
loads all necessary modules as well as invokes the `enqueue_compss` command to submit
the ``kmeans.py`` application execution to SLURM with the required ``--ear`` flag for power
consumption measurement:

.. code-block:: bash
    :emphasize-lines: 8,10-23,46
    :caption: `launch_kmeans_ear.sh`
    :name: launch_kmeans_ear_script

    #!/bin/bash -e

    # Load COMPSs module
    export COMPSS_PYTHON_VERSION=3
    module load COMPSs/Trunk

    # Load EAR module
    module load ear/4.2

    export EAR_LOGS=${HOME}/ear_compss_logs/
    mkdir -p ${EAR_LOGS}
    mkdir -p ${EAR_LOGS}/metrics
    mkdir -p ${EAR_LOGS}/logs
    export EAR_CPU_TDP=150
    export EAR_VERBOSE="--ear-verbose=2"                    # Comment this line to disable EAR verbosity
    export EAR_METRICS="--ear-user-db=${EAR_LOGS}/metrics"  # Comment this line to disable EAR CSV files with metrics
    export SLURM_HACK_EARL_VERBOSE=2
    export SLURM_EARL_VERBOSE_PATH=${EAR_LOGS}/logs/
    export EAR_ROOT=/apps/EAR/ear4.2/
    export SLURM_HACK_LOADER_FILE=${EAR_ROOT}/lib/libearld.so
    export SLURM_HACK_EARL_INSTALL_PATH=${EAR_ROOT}/lib
    export EAR_LOGS_PATH=${EAR_LOGS}
    export LD_LIBRARY_PATH=${EAR_ROOT}/lib/:${LD_LIBRARY_PATH}

    # Define script variables
    scriptDir=$(pwd)/$(dirname $0)
    execFile=${scriptDir}/kmeans.py
    appPythonpath=${scriptDir}/

    # Retrieve arguments
    numNodes=$1
    executionTime=$2
    tracing=$3

    # Leave application args on $@
    shift 3

    # Enqueue the application
    enqueue_compss \
        --num_nodes=${numNodes} \
        --exec_time=${executionTime} \
        --worker_working_dir=$(pwd) \
        --tracing=${tracing} \
        --pythonpath=$appPythonpath \
        --lang=python \
        --ear=\"--ear=on\" \
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


So we can then give execution permission to the submission script and launch our kmeans execution with EAR:

.. code-block:: console

    $ chmod 744 launch_kmeans_ear.sh
    $ ./launch_kmeans_ear.sh 2 10 false 72000 3 4 72

This will submit the job to SLURM and we will have to wait for its completion.


Result
------

Once the application has finished, a new folder containing the EAR logs will be created
in the ``${HOME}/ear_compss_logs/`` (defined with the ``EAR_LOGS`` environment variable).
Its contents will look like:

.. code-block:: console

    $ cd ${HOME}/ear_compss_logs/
    $ ear_compss_logs> tree
    .
    └── logs
        ├── earl_log.0.0.2.29835918.306780
        ├── earl_log.0.0.2.29835918.306784
        ├── earl_log.0.0.2.29835918.306787
        ├── earl_log.0.0.2.29835918.306793
        ├── earl_log.0.0.2.29835918.306794
        ├── earl_log.0.0.2.29835918.306795
        ├── earl_log.0.0.2.29835918.306802
        ├── earl_log.0.0.2.29835918.306803
        ├── earl_log.0.0.2.29835918.306804
        ├── earl_log.0.0.2.29835918.306805
        ├── earl_log.0.0.2.29835918.306806
        ├── earl_log.0.0.2.29835918.306807
        ├── earl_log.0.0.2.29835918.306808
        ├── earl_log.0.0.2.29835918.306809
        ├── earl_log.0.0.2.29835918.306810
        ├── earl_log.0.0.2.29835918.306814
        ├── earl_log.0.0.2.29835918.306816
        ├── earl_log.0.0.2.29835918.306817
        ├── earl_log.0.0.2.29835918.306821
        ├── earl_log.0.0.2.29835918.306825
        ├── earl_log.0.0.2.29835918.306826
        ├── earl_log.0.0.2.29835918.306831
        ├── earl_log.0.0.2.29835918.306836
        ├── earl_log.0.0.2.29835918.306840
        ├── earl_log.0.0.2.29835918.306847
        ├── earl_log.0.0.2.29835918.306848
        ├── earl_log.0.0.2.29835918.306849
        ├── earl_log.0.0.2.29835959.308534
        ├── earl_log.0.0.2.29835959.308538
        ├── earl_log.0.0.2.29835959.308541
        ├── earl_log.0.0.2.29835959.308547
        ├── earl_log.0.0.2.29835959.308548
        ├── earl_log.0.0.2.29835959.308549
        ├── earl_log.0.0.2.29835959.308556
        ├── earl_log.0.0.2.29835959.308557
        ├── earl_log.0.0.2.29835959.308558
        ├── earl_log.0.0.2.29835959.308559
        ├── earl_log.0.0.2.29835959.308560
        ├── earl_log.0.0.2.29835959.308561
        ├── earl_log.0.0.2.29835959.308562
        ├── earl_log.0.0.2.29835959.308563
        ├── earl_log.0.0.2.29835959.308564
        ├── earl_log.0.0.2.29835959.308565
        ├── earl_log.0.0.2.29835959.308566
        ├── earl_log.0.0.2.29835959.308567
        ├── earl_log.0.0.2.29835959.308570
        ├── earl_log.0.0.2.29835959.308577
        ├── earl_log.0.0.2.29835959.308578
        ├── earl_log.0.0.2.29835959.308579
        ├── earl_log.0.0.2.29835959.308580
        ├── earl_log.0.0.2.29835959.308586
        ├── earl_log.0.0.2.29835959.308594
        ├── earl_log.0.0.2.29835959.308595
        ├── earl_log.0.0.2.29835959.308596
        ├── earl_log.0.0.3.29835918.305236
        ├── earl_log.0.0.3.29835918.305245
        ├── earl_log.0.0.3.29835918.305252
        ├── earl_log.0.0.3.29835918.305258
        ├── earl_log.0.0.3.29835918.305259
        ├── earl_log.0.0.3.29835918.305260
        ├── earl_log.0.0.3.29835918.305267
        ├── earl_log.0.0.3.29835918.305268
        ├── earl_log.0.0.3.29835918.305269
        ├── earl_log.0.0.3.29835918.305270
        ├── earl_log.0.0.3.29835918.305271
        ├── earl_log.0.0.3.29835918.305272
        ├── earl_log.0.0.3.29835918.305273
        ├── earl_log.0.0.3.29835918.305274
        ├── earl_log.0.0.3.29835918.305275
        ├── earl_log.0.0.3.29835918.305276
        ├── earl_log.0.0.3.29835918.305277
        ├── earl_log.0.0.3.29835918.305280
        ├── earl_log.0.0.3.29835918.305283
        ├── earl_log.0.0.3.29835918.305284
        ├── earl_log.0.0.3.29835918.305285
        ├── earl_log.0.0.3.29835918.305286
        ├── earl_log.0.0.3.29835918.305287
        ├── earl_log.0.0.3.29835918.305295
        ├── earl_log.0.0.3.29835918.305303
        ├── earl_log.0.0.3.29835918.305304
        ├── earl_log.0.0.3.29835918.305305
        ├── earl_log.0.0.3.29835918.305312
        ├── earl_log.0.0.3.29835918.305319
        ├── earl_log.0.0.3.29835918.305322
        ├── earl_log.0.0.3.29835918.305327
        ├── earl_log.0.0.3.29835918.305328
        ├── earl_log.0.0.3.29835918.305329
        ├── earl_log.0.0.3.29835918.305331
        ├── earl_log.0.0.3.29835918.305332
        ├── earl_log.0.0.3.29835918.305333
        ├── earl_log.0.0.3.29835918.305336
        ├── earl_log.0.0.3.29835918.305341
        ├── earl_log.0.0.3.29835918.305342
        ├── earl_log.0.0.3.29835918.305343
        ├── earl_log.0.0.3.29835918.305344
        ├── earl_log.0.0.3.29835918.305345
        ├── earl_log.0.0.3.29835918.305346
        ├── earl_log.0.0.3.29835918.305349
        ├── earl_log.0.0.3.29835918.305356
        ├── earl_log.0.0.3.29835918.305357
        ├── earl_log.0.0.3.29835918.305358
        ├── earl_log.0.0.3.29835918.305359
        ├── earl_log.0.0.3.29835918.305362
        ├── earl_log.0.0.3.29835918.305363
        ├── earl_log.0.0.3.29835918.305365
        ├── earl_log.0.0.3.29835959.306553
        ├── earl_log.0.0.3.29835959.306565
        ├── earl_log.0.0.3.29835959.306571
        ├── earl_log.0.0.3.29835959.306577
        ├── earl_log.0.0.3.29835959.306578
        ├── earl_log.0.0.3.29835959.306579
        ├── earl_log.0.0.3.29835959.306586
        ├── earl_log.0.0.3.29835959.306587
        ├── earl_log.0.0.3.29835959.306588
        ├── earl_log.0.0.3.29835959.306589
        ├── earl_log.0.0.3.29835959.306590
        ├── earl_log.0.0.3.29835959.306591
        ├── earl_log.0.0.3.29835959.306592
        ├── earl_log.0.0.3.29835959.306593
        ├── earl_log.0.0.3.29835959.306594
        ├── earl_log.0.0.3.29835959.306595
        ├── earl_log.0.0.3.29835959.306596
        ├── earl_log.0.0.3.29835959.306599
        ├── earl_log.0.0.3.29835959.306608
        ├── earl_log.0.0.3.29835959.306611
        ├── earl_log.0.0.3.29835959.306612
        ├── earl_log.0.0.3.29835959.306614
        ├── earl_log.0.0.3.29835959.306618
        ├── earl_log.0.0.3.29835959.306619
        ├── earl_log.0.0.3.29835959.306621
        ├── earl_log.0.0.3.29835959.306627
        ├── earl_log.0.0.3.29835959.306628
        ├── earl_log.0.0.3.29835959.306629
        ├── earl_log.0.0.3.29835959.306630
        ├── earl_log.0.0.3.29835959.306631
        ├── earl_log.0.0.3.29835959.306632
        ├── earl_log.0.0.3.29835959.306634
        ├── earl_log.0.0.3.29835959.306640
        ├── earl_log.0.0.3.29835959.306641
        ├── earl_log.0.0.3.29835959.306642
        ├── earl_log.0.0.3.29835959.306644
        ├── earl_log.0.0.3.29835959.306646
        ├── earl_log.0.0.3.29835959.306647
        ├── earl_log.0.0.3.29835959.306648
        ├── earl_log.0.0.3.29835959.306649
        ├── earl_log.0.0.3.29835959.306650
        ├── earl_log.0.0.3.29835959.306655
        ├── earl_log.0.0.3.29835959.306663
        ├── earl_log.0.0.3.29835959.306665
        ├── earl_log.0.0.3.29835959.306666
        ├── earl_log.0.0.3.29835959.306667
        ├── earl_log.0.0.3.29835959.306668
        ├── earl_log.0.0.3.29835959.306669
        ├── earl_log.0.0.3.29835959.306670
        ├── earl_log.0.0.3.29835959.306671
        └── earl_log.0.0.3.29835959.306680

Each file contains the power consumption among other metrics gathered by EAR per process.
In particular, this execution has been performed with two MN4 nodes, where the first node
contains 24 worker processes and the second 48 worker processes.

These log files can be visualized with EAR for a more convenient power consumption and
performance analysis.