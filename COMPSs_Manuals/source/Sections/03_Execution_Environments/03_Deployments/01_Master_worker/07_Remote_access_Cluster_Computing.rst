Remote Access to Computing Servers and Clusters
===============================================

This COMPSs execution environment allow users to execute a COMPSs application using several remote machines and computing clusters.
This access to remote resources is done through the SSH (Secure Shell) and SCP (Secure Copy) protocols which are the most used
protocols to establishing a secure, encrypted connection between a client computer and a remote server within a cluster.

Although, this feature has been designed to work with resources that have a job submission queue.
It can also be used to work with any other type of machine that can be accessed by an SSH connection.


Requirements
------------

In order to use COMPSs with remote clusters some requirements must be fulfilled:

-  Generate a **public-private key pair** and authorize it in any Cluster that will be used
   (more details in section :ref:`Sections/01_Installation/05_Additional_configuration:Configure SSH passwordless`).
-  Have this remote resources in the **known hosts** file situated in **~/.ssh/known_hosts**.
-  **COMPSs** must be installed in both in the master and all the remote Clusters.

.. IMPORTANT::

    Both, the client and the remote computing resource should have the same or a compatible version of **COMPSs**, which must be **3.2 or higher**.


Execution
---------

The execution of an application using this method **consists of 3 steps**:

Step 1: Deployment
~~~~~~~~~~~~~~~~~~

The very first step to execute a COMPSs application in remote is copy all the necessary files to the remote resources.
If the application uses **JAVA** or **C** the compiled files must be also transferred or compiled in the remote machine.

This can be easily accomplished with the ``scp`` command as follows:

.. code-block:: console

    $ scp -r /client/path/application/ myUser@remoteMachine:/remote/path/.

This must be done **only once** for every new application, and then you can run it as many times as needed.
If the application is updated this step might be also necessary again.

.. IMPORTANT::

    Be sure to write down the absolute path of directory where the application has been installed and other absolute path
    for classes (``classpath``) or libraries (``library_path``). You will need it to fulfill the next step.

Step 2: Configuration
~~~~~~~~~~~~~~~~~~~~~

To correctly run the application, COMPSs needs the descriptions of the Clusters used for the execution.
This information must be provided in the resources and project XML files
(more details in :ref:`Sections/01_Installation/06_Configuration_files:resources file` and
:ref:`Sections/01_Installation/06_Configuration_files:project file`).
The resources file, has to include the description of the available clusters, and the project file has to provide
the access information (user, keys) and the location where COMPSs and the application is installed in every cluster.

The following code provides an example for the ``resources.xml`` file.

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <ResourcesList>
    <ComputingCluster Name="COMPSsWorker01">
        <Adaptors>
            <Adaptor Name="es.bsc.compss.gos.master.GOSAdaptor">
                <SubmissionSystem>
                    <Interactive/>
                </SubmissionSystem>
                <BrokerAdaptor>sshtrilead</BrokerAdaptor>
            </Adaptor>
        </Adaptors>
        <ClusterNode Name="compute_node_type1">
            <MaxNumNodes>10</MaxNumNodes>
            <Processor Name="P1">
                <ComputingUnits>8</ComputingUnits>
                <Type>CPU</Type>
            </Processor>
            ...
        </ClusterNode>
    </ComputingCluster>
    </ResourcesList>

The following code provide an example for the ``project.xml`` file.

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <Project>
        <MasterNode/>
        <ComputingCluster Name="COMPSsWorker01">
            <LimitOfTasks>10</LimitOfTasks>
            <Adaptors>
                <Adaptor Name="es.bsc.compss.gos.master.GOSAdaptor">
                    <SubmissionSystem>
                        <Interactive/>
                    </SubmissionSystem>
                    <BrokerAdaptor>sshtrilead</BrokerAdaptor>
                </Adaptor>
            </Adaptors>
            <InstallDir>/opt/COMPSs/</InstallDir>
            <WorkingDir>/tmp/COMPSsWorker01/</WorkingDir>
            <User>myUser</User>
            <ClusterNode Name="compute_node1">
                <NumberOfNodes>2</NumberOfNodes>
            </ClusterNode>
        </ComputingCluster>
    </Project>

The ``Name`` given to the Computing cluster equals the host name of the remote cluster and the ``User`` tag is the user for that host.
For example, if we want to access the remote machine with ``myUser@remoteMachine`` the xml should be indicated as follows

.. code-block:: xml

    <ComputingCluster Name="remoteMachine">
        [... ExtraInformation ...]
        <User>myUser</User>
    </ComputingCluster>

.. CAUTION::

   If an user is not provided, the current user in the client will be used as default one.

As shown before, the ``InstallDir`` tag is necessary and must be the absolute path to the folder where COMPSs is installed in the remote cluster.
If this information is not known, it can be obtain by executing the following command in the remote machine.

.. code-block:: console

   $ echo $(builtin cd $(dirname $(which runcompss))/../../..; pwd)

Step 3: Run the application
~~~~~~~~~~~~~~~~~~~~~~~~~~~

For further details of the ``runcompss`` command check its dedicated Section
(:ref:`Sections/03_Execution_Environments/03_Deployments/01_Master_worker/01_Local/01_Executing:Runcompss command`).

.. code-block:: console

    $ runcompss  --project=path/to/application/project.xml \
                 --resources=path/to/application/resources.xml \
                 [options] \
                 application_name [application_arguments]


Submission Modes
----------------

This adaptor supports two different forms for submitting the tasks generated by COMPSs:

- :ref:`Sections/03_Execution_Environments/03_Deployments/01_Master_worker/07_Remote_access_Cluster_Computing:Interactive Mode`
- :ref:`Sections/03_Execution_Environments/03_Deployments/01_Master_worker/07_Remote_access_Cluster_Computing:Batch Mode`

.. IMPORTANT::

   If both submission systems are marked as possible, the application will run in interactive mode.

Interactive Mode
~~~~~~~~~~~~~~~~

This mode directly launches the execution of tasks to remote machines, and should be used if we have direct access to the computing hardware.

Example of setting the interactive mode, this code must go in ``resources.xml``:

.. code-block:: xml

    <Adaptors>
        <Adaptor Name="es.bsc.compss.gos.master.GOSAdaptor">
            <SubmissionSystem>
                <Interactive/>
            </SubmissionSystem>
        </Adaptor>
    </Adaptors>

Batch Mode
~~~~~~~~~~

Computing clusters are usually shared by different users and to enable a proper sharing of resources the computations are spawn using a job submission system.
The Batch Mode option handles that aspect and manages the execution of the application tasks as jobs in the cluster.
To perform this feature, the user has to provide the following configuration in the project and resources XML files.

Port
    The port used for SSH Communication.
    *Optional* ; *Default: 22*

MaxExecTime
    Expected execution time of the application (in minutes).
    *Optional* ; *Default: 10*

Queue
    Specifies which type of queue system the remote resource has.
    This queue must have a corresponding cfg file in ``<installation_dir>/Runtime/scripts/queues/queue_systems`` folder.
    For more information, please read this section (:ref:`Sections/01_Installation/04_Supercomputers:Configuration Files`).

FileCFG
    To further customize the supercomputers cfg files contains a set of variables to indicate the queue system used by a supercomputer,
    paths where the shared disk is mounted, the default values that COMPSs will set in the project and resources files when they are
    not set by the user and flags to indicate if a functionality is available or not in a supercomputer.
    This file must have either a corresponding cfg file in ``<installation_dir>/Runtime/scripts/queues/supercomputers/`` folder or an absolute path to a file.
    For more information, please read this section (:ref:`Sections/01_Installation/04_Supercomputers:Configuration Files`).
    *Optional*

    .. IMPORTANT::

        Inside this file, you can specify which queue system is going to be used.

Reservation
    Some **queue systems** have the ability to reserve resources for jobs being executed by select users and/or select bank accounts.
    A resource reservation identifies the resources in that reservation and a time period during which the reservation is available.
    Reservation to use when submitting the job.
    *Optional* ; *Default: disabled*

QOS
    One can specify a Quality of Service (QOS) for each job submitted to the corresponding queue.
    The quality of service associated with a job might affect the job scheduling priority.
    *Optional* ; *Default: default*

.. CAUTION::

    The **.cfg** files for queues and supercomputers must be in the remote machine to be able to be read.

.. code-block:: xml

    <Adaptors>
        <Adaptor Name="es.bsc.compss.gos.master.GOSAdaptor">
            <SubmissionSystem>
                <Batch>
                    <Queue>slurm</Queue>
                    <BatchProperties>
                        <Port>200</Port>
                        <MaxExecTime>30</MaxExecTime>
                        <Reservation>myReservation</Reservation>
                        <QOS>debug</QOS>
                        <FileCFG>nord3.cfg</FileCFG>
                    </BatchProperties>
                </Batch>
            </SubmissionSystem>
            <BrokerAdaptor>sshtrilead</BrokerAdaptor>
        </Adaptor>
    </Adaptors>

.. IMPORTANT::

    If batch mode is selected, a environment script is almost certainly necessary.
    This script will be executed in any computing nodes that the execution will ask to the job submission queue.
    In this nodes user defined variables can not be used.
    Calling your own ``.bashrc`` might help with some of these problems.
    However, you might have to redefine this variables in the script.

    .. code-block:: bash

        source /path/to/userDirectory/.bashrc
        [... Rest of the environment script ]


Execution results
-----------------

The execution result follows the same pattern as other execution environments
(see further details in its section, :ref:`Sections/03_Execution_Environments/03_Deployments/01_Master_worker/01_Local/02_Results_and_logs:results`).

Regarding debugging logs, at the end of each task, out and err logs are stored in the corresponding jobs folder and, at the end of the execution,
a compressed folder with other generated logs are copied to the master node.

.. CAUTION::

    In case of an error that prevents bringing the execution logs, for example, a lose of connection with the remote resources.
    The logs will be located in ``<WorkingDir>`` in the remote machine. This is specially true if the application is launched in batch mode,
    because the logs generated in the remote machine are not brought to the client until the task has finished, this logs for the tasks
    will be situated in ``<WorkingDir>/BatchOutput/task_ID``.


Execution example
-----------------

In this section, we show how to execute the *Simple* Java COMPSs application in **batch mode**.

In this scenario, we have in our local machine, the Simple application in ``/home/jane/simple`` and
inside the ``simple`` directory we only have the file ``simple.jar``.
And in the remote machine is called ``remote.bsc.es``, we have the user ``janeSmith``.
So we can access this machine with ``ssh janeSmith@remote.bsc.es``.

In the **first step**, we have to be sure that COMPSs and all the application files are available in ``remote.bsc.es``.
For this example, we assume that the application will be deployed in ``/home/users/janeSmith/simple`` and
COMPSs is installed in ``/apps/COMPSs/3.2``.
The following command are used to deploy the application and check the COMPSs installation.

.. code-block:: bash

    # In the local machine, copy the application data
    $ scp -r /home/jane/simple/ janeSmith@remote.bsc.es:/home/users/janeSmith/simple
    $ ssh janeSmith@remote.bsc.es
    # Inside the remote machine, check where COMPSs is installed
    $ echo $(builtin cd $(dirname $(which runcompss))/../../..; pwd)
    /apps/COMPSs/3.2
    $ exit

In the **second step**, we create the required xml files and they will be stored in ``/home/jane/simple``.
Next lines show the XML files for this example.

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <Project>
        <MasterNode/>
        <ComputingCluster Name="remote.bsc.es">
            <Adaptors>
                <Adaptor Name="es.bsc.compss.gos.master.GOSAdaptor">
                    <SubmissionSystem>
                        <Batch>
                            <Queue>slurm</Queue>
                            <BatchProperties>
                                <Port>22</Port>
                                <MaxExecTime>2</MaxExecTime>
                                <Reservation>disabled</Reservation>
                                <QOS>debug</QOS>
                                <FileCFG>nord3.cfg</FileCFG>
                            </BatchProperties>
                        </Batch>
                    </SubmissionSystem>
                </Adaptor>
            </Adaptors>
            <InstallDir>/apps/COMPSs/3.2/</InstallDir>
            <WorkingDir>/tmp/COMPSsWorkerTMP/</WorkingDir>
            <User>janeSmith</User>
            <LimitOfTasks>1000</LimitOfTasks>
            <Application>
                <Classpath>/home/users/janeSmith/simple/simple.jar</Classpath>
                <EnvironmentScript>/home/users/janeSmith/env.sh</EnvironmentScript>
            </Application>
            <ClusterNode Name="compute_node_type">
                <NumberOfNodes>2</NumberOfNodes>
            </ClusterNode>
        </ComputingCluster>
    </Project>

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <ResourcesList>
    <ComputingCluster Name="remote.bsc.es">
        <Adaptors>
            <Adaptor Name="es.bsc.compss.gos.master.GOSAdaptor">
                <SubmissionSystem>
                    <Batch>
                        <Queue>slurm</Queue>
                    </Batch>
                </SubmissionSystem>
            </Adaptor>
        </Adaptors>
        <ClusterNode Name="compute_node_type">
            <MaxNumNodes>4</MaxNumNodes>
            <Processor Name="P1">
                <ComputingUnits>8</ComputingUnits>
                <Type>CPU</Type>
            </Processor>
        </ClusterNode>
    </ComputingCluster>
    </ResourcesList>

Finally, in the **third step** we have to launch the application.
It must be done using the following command:

.. code-block:: console

    $ runcompss  --project=/home/jane/simple/project.xml \
                 --resources=/home/jane/simple/resources.xml \
                 --classpath=/home/jane/simple/simple.jar \
                 simple
