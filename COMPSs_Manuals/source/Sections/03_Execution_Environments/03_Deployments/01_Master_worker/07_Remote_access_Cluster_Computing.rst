Remote access to Cluster computing
==================================

What is remote access?
----------------------

COMPSs supports access to cluster computing using the SSH (Secure Shell) protocol which involves establishing a secure,
encrypted connection between a client computer and a remote server within a cluster. This type of execution permits
using various supercomputers from a single lightweight client to execute a COMPSs application.

Although, this feature has been designed to work with resources that have a job submission queue. It can also be used
to work with any other type of machine that can be accessed by an SSH connection.

Requirements
------------

In order to use COMPSs with the ssh adaptor, some requirements must be fulfilled:

-  Have a **public-private key pair** shared with the any resource that will be used, as
   detail in the section (:ref:`Sections/01_Installation/05_Additional_configuration:Configure SSH passwordless`).
-  Have this remote resources in the **known hosts** file situated in **~/.ssh/known_hosts**.
-  **COMPSs** must be installed in both in the master and all the remote resources.

.. caution::
    The port 22 of the client must be available for the communication via SSH.

.. important::
    Both, the client and the remote computing resource should have the same version of **COMPSs**, which
    must be 3.2 or higher.


Execution
---------

The execution of an application using this method **consists of 3 steps**:

Execution step 1: Make sure that remote resources can execute the application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The very first step to execute a COMPSs application in remote is copy all the necessary files to the remote resources.
If the application uses **JAVA** or **C** the compiled files must be also transferred, or compiled in the remote machine.

This can be easily accomplished by a command.

.. code-block:: console

    $ scp -r USER@your.remote.resource.com:/remote/path/application /client/path/application/


This must be done **only once** for every new application, and then you can run it as many times as needed.
If the application is updated this step might be also necessary again.

.. IMPORTANT::

    Be sure to write down the absolute context-directory and the absolute classpath (the absolute path to the executable
    jar). You will need it to fulfill the next step.


Execution step 2: Create the XML files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To correctly run the application, COMPSs needs some information. This information must be provided in the xml files
for :ref:`Sections/01_Installation/06_Configuration_files:resources file` and :ref:`Sections/01_Installation/06_Configuration_files:project file`.

An example for the resources XML file:

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
        <ClusterNode Name="compute_node1">
            <MaxNumNodes>1</MaxNumNodes>
            <Processor Name="P1">
                <ComputingUnits>8</ComputingUnits>
                <Type>CPU</Type>
            </Processor>
        </ClusterNode>
    </ComputingCluster>
    </ResourcesList>

An example for the project XML file:

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

The ``Name`` given to the Computing cluster equals the host of the remote cluster and the ``User`` tag is the
user for that host. For example, if we want to access the remote machine with ``myUser@remoteMachine`` the xml should be

.. code-block:: xml

    <ComputeNode Name="remoteMachine">
        [... ExtraInformation ...]
        <User>myUser</User>
    </ComputeNode>

.. caution::
   If an user is not provided, the current user in the client will be used as default one.

As shown before, the ``InstallDir`` tag is necessary and must be the absolute path to the folder that COMPSs is installed
in the remote resources. If this information is not known, it can be obtain by executing the following command in the remote
machine.

.. code-block:: console

   $ echo $(builtin cd $(dirname $(which runcompss))/../../..; pwd)


Execution step 3: Run the application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For further details of the ``runcompss`` command check its dedicated section
(:ref:`Sections/03_Execution_Environments/03_Deployments/01_Master_worker/01_Local/01_Executing:Runcompss command`).

.. code-block:: console

    $ runcompss  --project=path/to/application/project.xml \
                 --resources=path/to/application/resources.xml \
                 [options] \
                 application_name [application_arguments]


Submission Modes
----------------

This adaptor supports two different forms for submitting the tasks generated by COMPSs: **interactive mode** and
**submission mode**.

.. important::
   If both submission systems are marked as possible, the application will run in interactive mode.

Interactive Mode
~~~~~~~~~~~~~~~~

This mode directly launches the execution of the tasks, and should be used if we have direct access to the computing
hardware.

Example of setting the interactive mode, this code must go in resources.xml:

.. code-block:: xml

    <Adaptors>
        <Adaptor Name="es.bsc.compss.gos.master.GOSAdaptor">
            <SubmissionSystem>
                <Interactive/>
            </SubmissionSystem>
            <BrokerAdaptor>sshtrilead</BrokerAdaptor>
        </Adaptor>
    </Adaptors>

Batch Mode
~~~~~~~~~~

Usually, the user doesn't have direct access two the computing hardware and must ask for resources from the
job submission system of the corresponding cluster. This mode handles that aspect and constantly checks the status of
those jobs to ensure a fast execution.

To correctly performs the aforementioned features and to offer some configuration to the user, some aspects are
customizable.

--MaxExecTime
    | Expected execution time of the application (in minutes).
    | *Optional* ; *Default: 10*

--Queue
    | Specifies which type of queue system the remote resource has. This queue must have a corresponding cfg file in
    ``<installation_dir>/Runtime/scripts/queues/queue_systems`` folder. For more information, please read this section
    (:ref:`Sections/01_Installation/04_Supercomputers:Configuration Files`).
    | *Mandatory*

--FileCFG
    | To further customize the supercomputers cfg files contains a set of variables to
    indicate the queue system used by a supercomputer, paths where the shared disk
    is mounted, the default values that COMPSs will set in the project and resources
    files when they are not set by the user and flags to indicate if a functionality
    is available or not in a supercomputer. This file must have either a corresponding cfg file in
    ``<installation_dir>/Runtime/scripts/queues/supercomputers/`` folder or an absolute path to a file.
    For more information, please read this section (:ref:`Sections/01_Installation/04_Supercomputers:Configuration Files`).
    | *Optional*

--Reservation
    Some **queue systems** have the ability to reserve resources for jobs being executed by select users and/or select
    bank accounts. A resource reservation identifies the resources in that reservation and a time period during which
    the reservation is available. Reservation to use when submitting the job.
    | *Optional* ; *Default: disabled*

--QOS
    One can specify a Quality of Service (QOS) for each job submitted to the corresponding queue.
    The quality of service associated with a job might affect the job scheduling priority. |
    | *Optional* ; *Default: default*

.. caution::
    The **.cfg** files for queues and supercomputers must be in the remote machine to be able to be read.

.. code-block:: xml

    <Adaptors>
        <Adaptor Name="es.bsc.compss.gos.master.GOSAdaptor">
            <SubmissionSystem>
                <Batch>
                    <Queue>slurm</Queue>
                    <BatchProperties>
                        <MaxExecTime>30</MaxExecTime>
                        <Reservation>disabled</Reservation>
                        <QOS>debug</QOS>
                        <FileCFG>nord3.cfg</FileCFG>
                    </BatchProperties>
                </Batch>
            </SubmissionSystem>
            <BrokerAdaptor>sshtrilead</BrokerAdaptor>
        </Adaptor>
    </Adaptors>

.. important::
    If batch mode is selected, a environment script is almost certainly necessary. This script will be executed in **both**
    the login node and in any computing nodes that the execution will

    .. code-block:: bash

        example code of environment script


Execution results
-----------------

The execution result follows the same pattern that the execution as Local does (see further details
in its section, (:ref:`Sections/03_Execution_Environments/03_Deployments/01_Master_worker/01_Local/02_Results_and_logs:results`).

It additionally adds a compressed folder with the generated logs that were created in the remote execution that do
not correspond to the task.

.. caution::
    In case of an error outside of the application, for example, lose of connection with the remote resources.
    The logs will be located in ``<WorkingDir>`` in the remote machine. This is specially true if the application
    is launched in batch mode, because the logs generated in the remote machine are not brought to the client until the task has finished,
    this logs will be situated in ``<WorkingDir>/BatchOutput/task_ID``.


