Remote access to Cluster computing
==================================

What is remote access?
----------------------

COMPSs supports access to cluster computing using the SSH (Secure Shell)
protocol which involves establishing a secure, encrypted connection between a
client computer and a remote server within a cluster. This allows users
to access and control the computing resources of  different clusters from a remote
location.

To access a cluster computing system using SSH a public-private key pair with those
computing resources that will be used in the application.

COMPSs supports




Requirements
------------

In order to use COMPSs with the ssh adaptor, some requirements must be fulfilled:

-  Have a **public-private key pair** shared with the cluster that will be used, as
   detail in the section (:ref:`Sections/01_Installation/05_Additional_configuration:Configure SSH passwordless`).
-  Have this remote resources in the **known hosts** file.
-  **COMPSs** must be installed in both in the master and all the remote resources.

.. important::
   Both, the client and the remote computing resource must have a version of **COMPSs** 3.2 or higher.


Execution in Client
-------------------

The runcompss workflow uses GOSAdaptor, which is

The execution of an application using Docker containers with COMPSs
**consists of 3 steps**:

Execution step 1: Make sure that remote resources can execute the application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The very first step to execute a COMPSs application in Docker is
copy all the necessary files to the remote resources. If the application uses **JAVA** or **C** the compiled
files must be also transferred.

This can be easily accomplished by a command.

.. code-block:: console

    $ scp -r USER@your.remote.resource.com:/path/to/application /home/user/application/


This must be done **only once** for every new application, and then
you can run it as many times as needed. If the application is updated
this step might be also necessary.


.. IMPORTANT::

   Be sure to write down the absolute context-directory and the absolute
   classpath (the absolute path to the executable jar). You will need it to fulfill the next step.


Execution step 2: Create the XML files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To correctly run the application, COMPSs needs some information. This information must be provided in the xml files
for resources and project.

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
                <NumberOfNodes>1</NumberOfNodes>
            </ClusterNode>
        </ComputingCluster>
    </Project>

The **Name** given to the Computing cluster equals the host of the remote cluster and the **User** tag is the
user for that host.

As shown before, the **InstallDir** tag is necessary and must point to the folder that COMPSs is installed
in the remote resources.

.. caution::
   If an user is not provided, the current user will be used as default. If the classpath is not provided in the
   xml files, it must be provided as **arguments** in the execution command.

Execution step 3: Run the application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

    $ runcompss  --project="${base_app_dir}"/project.xml \
                 --resources="${base_app_dir}"/resources.xml \
                 --comm="es.bsc.compss.gos.master.GOSAdaptor" \
                 "${app_name}" 1 > >(tee "${output_log}") 2> >(tee "${error_log}" >&2)


Submission Modes
----------------

This adaptor supports two different forms two submit the tasks generated by COMPSs: **interactive mode** and
**submission mode**.

Interactive Mode
~~~~~~~~~~~~~~~~

This mode directly launches the execution of the tasks, and should be used if we have direct access to the computing
hardware.

.. figure:: ./Figures/interactive_diagram.jpeg
   :name: interactive
   :alt: Interactive diagram
   :align: center
   :width: 50.0%

Example of interactive mode:

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
those jobs.

.. figure:: ./Figures/batch_diagram.jpeg
   :name: batch
   :alt: Batch diagram
   :align: center
   :width: 50.0%

To correctly performs the aforementioned features and to offer some configuration to the user, some aspects are
customizable.

--MaxExecTime
    Default: 10 min.

--Queue
    Specifies which type of queue system the remote resource has. This queue must have a corresponding cfg file in
    ``<installation_dir>/Runtime/scripts/queues/queue_systems`` folder. For more information, please read this
    (:ref:`Sections/01_Installation/04_Supercomputers#compss-queue-structure-overview:section`).

--FileCFG
    Specifies the number of **worker containers** the app will execute
    on. One more container will be created to host the **master**. If you
    have enough nodes in the Swarm cluster, each container will be
    executed by one node. This is the default schedule strategy used by
    Swarm.

--Reservation
    Specifies the number of **worker containers** the app will execute
    on. One more container will be created to host the **master**. If you
    have enough nodes in the Swarm cluster, each container will be
    executed by one node. This is the default schedule strategy used by
    Swarm.

--QOS
    Specifies the number of **worker containers** the app will execute
    on. One more container will be created to host the **master**. If you
    have enough nodes in the Swarm cluster, each container will be
    executed by one node. This is the default schedule strategy used by
    Swarm.

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

.. caution::
   If both submission systems are marked as possible, it will run in interactive mode.

Execution results
-----------------

The execution results will be retrieved from the remote resources of
your application.

If your context-directory name is **’matmul’**, then your results will
be saved in the **’matmul-results’** directory, which will be located
in the same directory you executed runcompss-docker on.

Inside the **’matmul-results’** directory you will have:

-  A folder named **’matmul’** with all the result files that were in
   the same directory as the executable when the application execution
   ended. More precisely, this will contain the context-directory state
   right after finishing your application execution.
   Additionally, and for more advanced debug purposes, you will have
   some intermediate files created by runcompss-docker (Dockerfile,
   project.xml, resources.xml), in case you want to check for more
   complex errors or details.

-  A folder named **’debug’**, which (in case you used the runcompss
   debug option (**-d**)), will contain the **’.COMPSs’** directory,
   which contains another directory in which there are the typical debug
   files runtime.log, jobs, etc.
   Remember **.COMPSs** is a **hidden** directory, take this into
   account if you do **ls** inside the debug directory (add the **-a**
   option).


Execution examples
------------------

The execution results will be retrieved from the remote resources of
your application.