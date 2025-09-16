Nord 3
^^^^^^

Basic queue commands
""""""""""""""""""""

The *Nord3* supercomputer uses the **LSF** (Load Sharing Facility) workload
manager. The basic commands to manage jobs are listed below:

-  **bsub** Submit a batch job to the LSF system

-  **bkill** Kill a running job

-  **bjobs** See the status of jobs in the LSF queue

-  **bqueues** Information about LSF batch queues

For more extended information please check the *IBM Platform LSF Command Reference* at
https://www.ibm.com/support/knowledgecenter/en/SSETD4_9.1.2/lsf_kc_cmd_ref.html
.

Tracking COMPSs jobs
""""""""""""""""""""

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
    #BSUB -J COMPSs
    #BSUB -cwd .
    #BSUB -oo compss-%J.out
    #BSUB -eo compss-%J.err
    #BSUB -n 3
    #BSUB -R "span[ptile=1]"
    #BSUB -W 00:15
    ...

Users can run the following command in order to track of the jobs state:

.. code-block:: console

    $ bjobs
    JOBID  USER   STAT  QUEUE  FROM_HOST  EXEC_HOST  JOB_NAME  SUBMIT_TIME
    XXXX   bscXX  PEND  XX     login1     XX         COMPSs    Month Day Hour

The specific COMPSs logs are stored under the ``~/.COMPSs/`` folder;
saved as a local *runcompss* execution. For further details please check the
:ref:`Sections/03_Execution/01_Local:Executing COMPSs applications` Section.
