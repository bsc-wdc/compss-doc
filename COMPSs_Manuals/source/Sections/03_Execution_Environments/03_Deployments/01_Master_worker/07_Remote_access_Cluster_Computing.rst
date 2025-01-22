Remote Access to Computing Servers and Clusters
===============================================

This COMPSs execution environment allow users to execute a COMPSs application
using several remote machines and computing clusters. This access to remote
resources is done through the SSH (Secure Shell) and SCP (Secure Copy)
protocols which are the most used protocols to establishing a secure,
encrypted connection between a client computer and a remote server within
a cluster.

Although, this feature has been designed to work with resources that have a
job submission queue. It can also be used to work with any other type of
machine that can be accessed by an SSH connection.


Requirements
------------

In order to use COMPSs with remote clusters some requirements must be fulfilled:

-  Generate a **public-private key pair** and authorize it in any Cluster that
   will be used (more details in section
   :ref:`Sections/01_Installation/05_Additional_configuration:Configure SSH passwordless`).
-  Have this remote resources in the **known hosts** file situated in
   **~/.ssh/known_hosts**.
-  **COMPSs** must be installed in both in the master and all the remote
   Clusters.

.. IMPORTANT::

    Both, the client and the remote computing resource should have the same or
    a compatible version of **COMPSs**, which must be **3.2 or higher**.


Execution
---------

The execution of an application using this method **consists of 3 steps**:

Step 1: Deployment
~~~~~~~~~~~~~~~~~~

The very first step is to copy the application and its necessary files to the
remote machines. If the application uses **JAVA** or **C** languages, the
compiled files must be also transferred or compiled to the remote machines.

This can be easily accomplished with the ``scp`` command as follows:

.. code-block:: console

    $ scp -r /local/path/application/ myUser@remoteMachine:/remote/path/.

This **must be done for every new application**, and then you can run it as
many times as needed. If the application is updated this step will be necessary
again in order to **keep the same application locally and in the remote
machines**.

Step 2: Configuration
~~~~~~~~~~~~~~~~~~~~~

In order to run the application, COMPSs needs the descriptions of the remote
machines (e.g. clusters) used for the execution. This information must be
provided in two XML files: resources and project XML files (more details in
:ref:`Sections/01_Installation/06_Configuration_files:resources file` and
:ref:`Sections/01_Installation/06_Configuration_files:project file`).
The resources file, has to include the description of the available clusters
and the :ref:`Sections/03_Execution_Environments/03_Deployments/01_Master_worker/07_Remote_access_Cluster_Computing:Submission Modes`,
and the project file has to provide the access information (user, keys) and the
location where COMPSs and the application is installed in every cluster.

The following code shows the basic structure of the ``resources.xml`` file
using interactive submission mode (a working example of the ``resources.xml``
file using batch submission mode for MN5 in the
:ref:`Sections/03_Execution_Environments/03_Deployments/01_Master_worker/07_Remote_access_Cluster_Computing:Execution example`).

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

The following code shows the structure of the ``project.xml`` file using
interactive submission mode (a working example of the ``project.xml`` file using
batch submission mode for MN5 in the
:ref:`Sections/03_Execution_Environments/03_Deployments/01_Master_worker/07_Remote_access_Cluster_Computing:Execution example`).

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

The ``Name`` given to the Computing cluster equals the host name of the remote
cluster and the ``User`` tag is the user for that host. For example, if we want
to access the remote machine with ``myUser@remoteMachine`` the xml should be
indicated as follows:

.. code-block:: xml

    <ComputingCluster Name="remoteMachine">
        [... ExtraInformation ...]
        <User>myUser</User>
    </ComputingCluster>

.. CAUTION::

   If an user is not provided, the current user in the local node will be used
   for the remote nodes.

As shown before, the ``InstallDir`` tag is necessary and must be the absolute
path to the folder where COMPSs is installed in the remote cluster.


Submission Modes
^^^^^^^^^^^^^^^^

The `SubmissionSystem` tag of the `resources.xml` and `project.xml` is used to
define how to submit the tasks to the remote resources.

This adaptor supports two different forms for submitting the tasks generated
by COMPSs:

- :ref:`Sections/03_Execution_Environments/03_Deployments/01_Master_worker/07_Remote_access_Cluster_Computing:Interactive Mode`
- :ref:`Sections/03_Execution_Environments/03_Deployments/01_Master_worker/07_Remote_access_Cluster_Computing:Batch Mode`

.. IMPORTANT::

   If both submission systems are defined as possible, the application will run
   in interactive mode.

Interactive Mode
""""""""""""""""

This mode directly launches the execution of tasks to remote machines, and
should be used if we have direct access to the computing hardware (**NO queuing
system in the remote machine**).

Example of setting the interactive mode, this code **MUST** be in
``resources.xml`` and **OPTIONALLY** be in ``project.xml``:

.. code-block:: xml

    <Adaptors>
        <Adaptor Name="es.bsc.compss.gos.master.GOSAdaptor">
            <SubmissionSystem>
                <Interactive/>
            </SubmissionSystem>
        </Adaptor>
    </Adaptors>

Batch Mode
""""""""""

Computing clusters are usually shared by different users and to enable a proper
sharing of resources the computations are spawn using a job submission system
(e.g. SLURM).
The *Batch Mode* option handles that aspect and manages the execution of the
application tasks as jobs in the cluster. Consequently, the user has to provide
the following information in the `project` and `resources` XML files.

Port
    The port used for SSH Communication.

    *Optional* ; *Default: 22*

MaxExecTime
    Expected execution time of the application (in minutes).

    *Optional* ; *Default: 10*

Queue
    Specifies which type of queue system the remote resource has.
    This queue must have a corresponding cfg file in
    ``<installation_dir>/Runtime/scripts/queues/queue_systems`` folder.
    For more information, please read this section
    (:ref:`Sections/01_Installation/04_Supercomputers:Configuration Files`).

    *Optional* ; *Default: computing cluster's user default queue*

FileCFG
    To further customize the supercomputers cfg files contains a set of
    variables to indicate the queue system used by a supercomputer, paths where
    the shared disk is mounted, the default values that COMPSs will set in the
    project and resources files when they are not set by the user and flags to
    indicate if a functionality is available or not in a supercomputer.
    This file must have either a corresponding cfg file in
    ``<installation_dir>/Runtime/scripts/queues/supercomputers/`` folder or an
    absolute path to a file.
    For more information, please read this section
    (:ref:`Sections/01_Installation/04_Supercomputers:Configuration Files`).

    *Optional*

    .. IMPORTANT::

        Inside this file, you can also specify which queue system is going to
        be used instead with the previous parameter.

    .. CAUTION::

        The **.cfg** files for queues and supercomputers must be in the remote
        machine.

Reservation
    Some **queue systems** have the ability to reserve resources for jobs being
    executed by selected users accounts.
    A resource reservation identifies the resources in that reservation and a
    time period during which the reservation is available.
    Reservation to use when submitting the job.

    *Optional* ; *Default: disabled*

QOS
    One can specify a Quality of Service (QOS) for each job submitted to the
    corresponding queue.
    The quality of service associated with a job might affect the job
    scheduling priority.

    *Optional* ; *Default: computing cluster's user default qos*

ProjectName
    It is possible to define the project name required by the **queue system**
    of the computing cluster.

    *Optional* ; *Default: computing cluster's user default project name*

The following code snippet shows an example for the batch submission system
of *nord3* cluster:

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
                        <ProjectName>bsc</ProjectName>
                    </BatchProperties>
                </Batch>
            </SubmissionSystem>
            <BrokerAdaptor>sshtrilead</BrokerAdaptor>
        </Adaptor>
    </Adaptors>

.. IMPORTANT::

    If batch mode is selected, an environment script is probably necessary.
    This script will be executed in any computing nodes that the execution will
    ask to the job submission queue.
    In this nodes user defined variables **can NOT** be used.
    Calling your own ``.bashrc`` might help with some of these problems.
    However, you might have to redefine this variables in the script.

    .. code-block:: bash

        source /path/to/userDirectory/.bashrc
        [... Rest of the environment script ]

Step 3: Run the application
~~~~~~~~~~~~~~~~~~~~~~~~~~~

For further details of the ``runcompss`` command check its dedicated Section
(:ref:`Sections/03_Execution_Environments/03_Deployments/01_Master_worker/01_Local/01_Executing:Runcompss command`).

.. code-block:: console

    $ runcompss  --project=/local/path/application/project.xml \
                 --resources=/local/path/application/resources.xml \
                 --comm="es.bsc.compss.gos.master.GOSAdaptor" \
                 [options] \
                 application_name [application_arguments]

Execution results
^^^^^^^^^^^^^^^^^

The execution result follows the same pattern as other execution environments
(see further details in its section,
:ref:`Sections/03_Execution_Environments/03_Deployments/01_Master_worker/01_Local/02_Results_and_logs:results`).

Regarding the logs when debug is enabled, the ``out`` and ``err`` logs from
each task are stored in the corresponding log directory within the local
node when each task ends.

.. CAUTION::

    In case of an error that prevents bringing the execution logs, for example,
    a lose of connection with the remote resources.
    The logs will be located in ``<WorkingDir>/BatchOutput/task_ID`` in the
    remote machine.


Execution example
-----------------

Application
~~~~~~~~~~~

In this section, we show how to execute the :ref:`Sections/07_Sample_Applications/02_Python/03_Kmeans:Kmeans`
Python COMPSs application in **batch mode** using MareNostrum 5 supercomputer.

In this scenario, we have in our local machine, the Kmeans application in
``/home/user/kmeans`` and inside the ``kmeans`` directory we only have the
file ``kmeans.py``. And in the remote machine is called ``glogin1.bsc.es``,
we have the user ``bsc12345``. So we can access this machine with
``ssh bsc12345@glogin1.bsc.es``.

In the **first step**, we have to be sure that COMPSs and all the application
files are available in MN5 (``glogin1.bsc.es``). For this example, we assume
that the application will be deployed in the user home directory
(``/home/bsc/bsc12345/kmeans``) and COMPSs is installed in
``/apps/GPP/COMPSs/3.3.2``. The following command are used to deploy the
application and check the COMPSs installation:

.. code-block:: bash

    # In the local machine, copy the application data into MN5
    $ scp -r /home/user/kmeans bsc12345@glogin1.bsc.es:/home/bsc/bsc12345/.
    $ ssh bsc12345@glogin1.bsc.es
    # Inside the remote machine, check where COMPSs is installed
    $ module load COMPSs/3.3.2
    $ echo $(builtin cd $(dirname $(which runcompss))/../../..; pwd)
    /apps/GPP/COMPSs/3.3.2
    $ exit

In the **second step**, we create the required xml files and they will be
stored in ``/home/user/kmeans``. Next lines show the XML files for this example:

.. code-block:: xml
    :name: gos_project_xml
    :caption: project.xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <Project>
        <MasterNode/>
        <ComputingCluster Name="glogin1.bsc.es">
            <Adaptors>
                <Adaptor Name="es.bsc.compss.gos.master.GOSAdaptor">
                    <SubmissionSystem>
                        <Batch>
                            <Queue>slurm</Queue>
                            <BatchProperties>
                                <Port>22</Port>
                                <MaxExecTime>2</MaxExecTime>
                                <Reservation>disabled</Reservation>
                                <QOS>gp_debug</QOS>
                                <FileCFG>mn5.cfg</FileCFG>
                                <ProjectName>bsc19</ProjectName>
                            </BatchProperties>
                        </Batch>
                    </SubmissionSystem>
                  </Adaptor>
            </Adaptors>
            <InstallDir>/apps/GPP/COMPSs/3.3.2/</InstallDir>
            <WorkingDir>/home/bsc/bsc12345/kmeans/tmp/</WorkingDir>
            <User>bsc12345</User>
            <LimitOfTasks>1000</LimitOfTasks>
            <Application>
                <Classpath>/home/bsc/bsc12345/kmeans</Classpath>
                <EnvironmentScript>/home/bsc/bsc12345/kmeans/env_mn.sh</EnvironmentScript>
            </Application>
            <ClusterNode Name="compute_node_type">
                <NumberOfNodes>2</NumberOfNodes>
            </ClusterNode>
        </ComputingCluster>
    </Project>


.. code-block:: xml
    :name: gos_resources_xml
    :caption: resources.xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <ResourcesList>
    <ComputingCluster Name="glogin1.bsc.es">
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

And the environment script for MN5 (``/home/bsc/bsc12345/kmeans/env_mn.sh``):

.. code-block:: text
    :name: env_mn
    :caption: env_mn.sh

    export COMPSS_PYTHON_VERSION=3.12.1
    module load COMPSs/3.3.2


Finally, we launch the application in the **third step**.
It must be done using the following command within the local machine:

.. code-block:: console

    $ runcompss  --project=/home/user/kmeans/project.xml \
                 --resources=/home/user/kmeans/resources.xml \
                 kmeans.py -n 10240000 -f 8 -d 3 -c 8 -i 10

.. TIP::

    The same command can be used to run Java or C applications using the GOS
    adaptor (but take into account that the ``--classpath`` flag is will
    be needed for Java and ``--library_path`` will be needed for C).


Jupyter notebook
~~~~~~~~~~~~~~~~

In this section, we show how to execute the a Jupyter notebook in
**batch mode**.

The **first step** requires to make sure that COMPSs is available in the remote
machine (e.g. ``glogin1.bsc.es``). For this example, we assume that COMPSs is
installed in ``/apps/GPP/COMPSs/3.3.2``.

.. IMPORTANT::

    When using jupyter notebook it is not necessary to transfer the application
    to the remote machine, since COMPSs will deal with the code automatically.

In the **second step**, we create the required project and resources xml files
and they will be stored in ``/home/user/notebook``. They are the same as
defined in :ref:`gos_project_xml` and :ref:`gos_resources_xml`.

Finally, in the **third step** we can define in our local machine the notebook
``/home/user/notebook/simple.ipynb``. Note that the ``ipycompss.start`` call
includes the project and resources parameters, as well as the ``GOS``
communication adaptor.

.. code-block:: python

    import pycompss.interactive as ipycompss
    ipycompss.start(comm="GOS",
                    project_xml="/home/user/notebook/project.xml",
                    resources_xml="/home/user/notebook/resources.xml")

    # Now define your tasks and code within the following cells
