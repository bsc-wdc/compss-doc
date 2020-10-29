MinoTauro
=========

Basic queue commands
--------------------

The MinoTauro supercomputer uses the SLURM (Simple Linux Utility for
Resource Management) workload manager. The basic commands to manage jobs
are listed below:

-  **sbatch** Submit a batch job to the SLURM system

-  **scancel** Kill a running job

-  **squeue -u <username>** See the status of jobs
   in the SLURM queue

For more extended information please check the *SLURM: Quick start user
guide* at https://slurm.schedmd.com/quickstart.html .

Tracking COMPSs jobs
--------------------

When submitting a COMPSs job a temporal file will be created storing the
job information. For example:

.. code-block:: console

    $ enqueue_compss \
      --exec_time=15 \
      --num_nodes=3 \
      --cpus_per_node=16 \
      --master_working_dir=. \
      --worker_working_dir=shared_disk \
      --lang=python \
      --log_level=debug \
      <APP> <APP_PARAMETERS>


    SC Configuration:          default.cfg
    Queue:                     default
    Reservation:               disabled
    Num Nodes:                 3
    Num Switches:              0
    GPUs per node:             0
    Job dependency:            None
    Exec-Time:                 00:15
    Storage Home:              null
    Storage Properties:        null
    Other:
            --sc_cfg=default.cfg
            --cpus_per_node=16
            --master_working_dir=.
            --worker_working_dir=shared_disk
            --lang=python
            --classpath=.
            --library_path=.
            --comm=es.bsc.compss.nio.master.NIOAdaptor
            --tracing=false
            --graph=false
            --pythonpath=.
            <APP> <APP_PARAMETERS>
    Temp submit script is: /scratch/tmp/tmp.pBG5yfFxEo

    $ cat /scratch/tmp/tmp.pBG5yfFxEo
    #!/bin/bash
    #
    #SBATCH --job-name=COMPSs
    #SBATCH --workdir=.
    #SBATCH -o compss-%J.out
    #SBATCH -e compss-%J.err
    #SBATCH -N 3
    #SBATCH -n 48
    #SBATCH --exclusive
    #SBATCH -t00:15:00
    ...

In order to trac the jobs state users can run the following command:

.. code-block:: console

    $ squeue
    JOBID  PARTITION   NAME    USER  ST  TIME    NODES  NODELIST (REASON)
    XXXX   projects    COMPSs   XX   R   00:02       3  nvb[6-8]

The specific COMPSs logs are stored under the ``~/.COMPSs/`` folder;
saved as a local *runcompss* execution. For further details please check the
:ref:`Sections/03_Execution_Environments/01_Local/01_Executing:Executing COMPSs applications` Section.
