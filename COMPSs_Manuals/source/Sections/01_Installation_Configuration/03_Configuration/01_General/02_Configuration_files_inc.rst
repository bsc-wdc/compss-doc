.. _configuration_files:

Configuration Files
*******************

The COMPSs runtime has two configuration files: ``resources.xml`` and
``project.xml`` . These files contain information about the execution
environment and are completely independent from the application.

For each execution users can load the default configuration files or
specify their custom configurations by using, respectively, the
``--resources=<absolute_path_to_resources.xml>`` and the
``--project=<absolute_path_to_project.xml>`` in the ``runcompss``
command. The default files are located in the
``/opt/COMPSs/Runtime/configuration/xml/`` path.

Next sections describe in detail the ``resources.xml`` and the
``project.xml`` files, explaining the available options.

.. _resources_file:

Resources file
==============

The ``resources`` file provides information about all the available
resources that can be used for an execution. This file should normally
be managed by the system administrators. Its full definition schema
can be found at ``/opt/COMPSs/Runtime/configuration/xml/resources/resource_schema.xsd``.

For the sake of clarity, users can also check the SVG schema located at
``/opt/COMPSs/Runtime/configuration/xml/resources/resource_schema.svg``.

This file contains one entry per available resource defining its name
and its capabilities. Administrators can define several resource
capabilities (see example in the next listing) but we would like to
underline the importance of **ComputingUnits**. This capability
represents the number of available cores in the described resource and
it is used to schedule the correct number of tasks. Thus, it becomes
essential to define it accordingly to the number of cores in the
physical resource.

.. code-block:: xml

    compss@bsc:~$ cat /opt/COMPSs/Runtime/configuration/xml/resources/default_resources.xml
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <ResourcesList>
        <ComputeNode Name="localhost">
            <Processor Name="P1">
                <ComputingUnits>4</ComputingUnits>
                <Architecture>amd64</Architecture>
                <Speed>3.0</Speed>
            </Processor>
            <Processor Name="P2">
                <ComputingUnits>2</ComputingUnits>
            </Processor>
            <Adaptors>
                <Adaptor Name="es.bsc.compss.nio.master.NIOAdaptor">
                    <SubmissionSystem>
                        <Interactive/>
                    </SubmissionSystem>
                    <Ports>
                        <MinPort>43001</MinPort>
                        <MaxPort>43002</MaxPort>
                    </Ports>
                </Adaptor>
            </Adaptors>
            <Memory>
                <Size>16</Size>
            </Memory>
            <Storage>
                <Size>200.0</Size>
            </Storage>
            <OperatingSystem>
                <Type>Linux</Type>
                <Distribution>OpenSUSE</Distribution>
            </OperatingSystem>
            <Software>
                <Application>Java</Application>
                <Application>Python</Application>
            </Software>
        </ComputeNode>
    </ResourcesList>

.. _project_file:

Project file
============

The project file provides information about the resources used in a
specific execution. Consequently, the resources that appear in this file
are a subset of the resources described in the ``resources.xml`` file.
This file, that contains one entry per worker, is usually edited by the
users and changes from execution to execution. Its full definition
schema can be found at
``/opt/COMPSs/Runtime/configuration/xml/projects/project_schema.xsd``.

For the sake of clarity, users can also check the SVG schema located at
``/opt/COMPSs/Runtime/configuration/xml/projects/project_schema.xsd``.

We emphasize the importance of correctly defining the following entries:

installDir
    Indicates the path of the COMPSs installation **inside the
    resource** (not necessarily the same than in the local machine).

User
    Indicates the username used to connect via ssh to the resource. This
    user **must** have passwordless access to the resource (see
    :ref:`additional_configuration_ssh_passwordless` Section).
    If left empty COMPSs will automatically try to access the resource with
    the **same username as the one that lauches the COMPSs main application**.

LimitOfTasks
    The maximum number of tasks that can be simultaneously scheduled to
    a resource. Considering that a task can use more than one core of a
    node, this value must be lower or equal to the number of available
    cores in the resource.


.. code-block:: xml

    compss@bsc:~$ cat /opt/COMPSs/Runtime/configuration/xml/projects/default_project.xml
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <Project>
        <!-- Description for Master Node -->
        <MasterNode></MasterNode>

        <!--Description for a physical node-->
        <ComputeNode Name="localhost">
            <InstallDir>/opt/COMPSs/</InstallDir>
            <WorkingDir>/tmp/Worker/</WorkingDir>
            <Application>
                <AppDir>/home/user/apps/</AppDir>
                <LibraryPath>/usr/lib/</LibraryPath>
                <Classpath>/home/user/apps/jar/example.jar</Classpath>
                <Pythonpath>/home/user/apps/</Pythonpath>
            </Application>
            <LimitOfTasks>4</LimitOfTasks>
            <Adaptors>
                <Adaptor Name="es.bsc.compss.nio.master.NIOAdaptor">
                    <SubmissionSystem>
                        <Interactive/>
                    </SubmissionSystem>
                    <Ports>
                        <MinPort>43001</MinPort>
                        <MaxPort>43002</MaxPort>
                    </Ports>
                    <User>user</User>
                </Adaptor>
            </Adaptors>
        </ComputeNode>
    </Project>

.. _configuration_files_examples:

Configuration examples
======================

In the next subsections we provide specific information about the
services, shared disks, cluster and cloud configurations and several
``project.xml`` and ``resources.xml`` examples.

Parallel execution on one single process configuration
------------------------------------------------------

The most basic execution that COMPSs supports is using no remote workers
and running all the tasks internally within the same process that hosts
the application execution. To enable the parallel execution of the
application, the user needs to set up the runtime and provide a
description of the resources available on the node. For that purpose,
the user describes within the ``<MasterNode>`` tag of the
``project.xml`` file the resources in the same way it describes other
nodes' resources on the using the ``resources.xml`` file. Since there is
no inter-process communication, adaptors description is not allowed. In
the following example, the master will manage the execution of tasks on
the MainProcessor CPU of the local node - a quad-core amd64 processor at
3.0GHz - and use up to 16 GB of RAM memory and 200 GB of storage.

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <Project>
        <MasterNode>
            <Processor Name="MainProcessor">
                <ComputingUnits>4</ComputingUnits>
                <Architecture>amd64</Architecture>
                <Speed>3.0</Speed>
            </Processor>
            <Memory>
                <Size>16</Size>
            </Memory>
            <Storage>
                <Size>200.0</Size>
            </Storage>
        </MasterNode>
    </Project>

If no other nodes are available, the list of resources on the
``resources.xml`` file is empty as shown in the following file sample.
Otherwise, the user can define other nodes besides the master node as
described in the following section, and the runtime system will
orchestrate the task execution on both the local process and on the
configured remote nodes.

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <ResourcesList>
    </ResourcesList>

Cluster and grid configuration (static resources)
-------------------------------------------------

In order to use external resources to execute the applications, the
following steps have to be followed:

#. Install the *COMPSs Worker* package (or the full *COMPSs Framework*
   package) on all the new resources.

#. Set SSH passwordless access to the rest of the remote resources.

#. Create the *WorkingDir* directory in the resource (remember this path
   because it is needed for the ``project.xml`` configuration).

#. Manually deploy the application on each node.

The ``resources.xml`` and the ``project.xml`` files must be configured
accordingly. Here we provide examples about configuration files for Grid
and Cluster environments.



.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <ResourcesList>
        <ComputeNode Name="hostname1.domain.es">
            <Processor Name="MainProcessor">
                <ComputingUnits>4</ComputingUnits>
            </Processor>
            <Adaptors>
                <Adaptor Name="es.bsc.compss.nio.master.NIOAdaptor">
                    <SubmissionSystem>
                        <Interactive/>
                    </SubmissionSystem>
                    <Ports>
                        <MinPort>43001</MinPort>
                        <MaxPort>43002</MaxPort>
                    </Ports>
                </Adaptor>
                <Adaptor Name="es.bsc.compss.gat.master.GATAdaptor">
                    <SubmissionSystem>
                        <Batch>
                            <Queue>sequential</Queue>
                        </Batch>
                        <Interactive/>
                    </SubmissionSystem>
                    <BrokerAdaptor>sshtrilead</BrokerAdaptor>
                </Adaptor>
            </Adaptors>
        </ComputeNode>

        <ComputeNode Name="hostname2.domain.es">
          ...
        </ComputeNode>
    </ResourcesList>

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <Project>
        <MasterNode/>
        <ComputeNode Name="hostname1.domain.es">
            <InstallDir>/opt/COMPSs/</InstallDir>
            <WorkingDir>/tmp/COMPSsWorker1/</WorkingDir>
            <User>user</User>
            <LimitOfTasks>2</LimitOfTasks>
        </ComputeNode>
        <ComputeNode Name="hostname2.domain.es">
          ...
        </ComputeNode>
    </Project>

Shared Disks configuration example
----------------------------------

Configuring shared disks might reduce the amount of data transfers
improving the application performance. To configure a shared disk the
users must:

#. Define the shared disk and its capabilities

#. Add the shared disk and its mount-point to each worker

#. Add the shared disk and its mount-point to the master node

Next example illustrates steps 1 and 2. The ``<SharedDisk>`` tag adds a
new shared disk named ``sharedDisk0`` and the ``<AttachedDisk>`` tag
adds the mount-point of a named shared disk to a specific worker.

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <ResourcesList>
        <SharedDisk Name="sharedDisk0">
            <Storage>
                <Size>100.0</Size>
                <Type>Persistent</Type>
            </Storage>
        </SharedDisk>

        <ComputeNode Name="localhost">
          ...
          <SharedDisks>
            <AttachedDisk Name="sharedDisk0">
              <MountPoint>/tmp/SharedDisk/</MountPoint>
            </AttachedDisk>
          </SharedDisks>
        </ComputeNode>
    </ResourcesList>

On the other side, to add the shared disk to the **master node**, the
users must edit the ``project.xml`` file. Next example shows how to
attach the previous ``sharedDisk0`` to the master node:

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <Project>
        <MasterNode>
            <SharedDisks>
                <AttachedDisk Name="sharedDisk0">
                    <MountPoint>/home/sharedDisk/</MountPoint>
                </AttachedDisk>
            </SharedDisks>
        </MasterNode>

        <ComputeNode Name="localhost">
          ...
        </ComputeNode>
    </Project>

Notice that the ``resources.xml`` file can have multiple ``SharedDisk``
definitions and that the ``SharedDisks`` tag (either in the
``resources.xml`` or in the ``project.xml`` files) can have multiple
``AttachedDisk`` children to mount several shared disks on the same
worker or master.



Cloud configuration (dynamic resources)
---------------------------------------

In order to use cloud resources to execute the applications, the
following steps have to be followed:

#. Prepare cloud images with the *COMPSs Worker* package or the full
   *COMPSs Framework* package installed.

#. The application will be deployed automatically during execution but
   the users need to set up the configuration files to specify the
   application files that must be deployed.

The COMPSs runtime communicates with a cloud manager by means of
connectors. Each connector implements the interaction of the runtime
with a given provider's API, supporting four basic operations: ask for
the price of a certain VM in the provider, get the time needed to create
a VM, create a new VM and terminate a VM. This design allows connectors
to abstract the runtime from the particular API of each provider and
facilitates the addition of new connectors for other providers.

The ``resources.xml`` file must contain one or more
``<CloudProvider>`` tags that include the information about a
particular provider, associated to a given connector. The tag **must**
have an attribute **Name** to uniquely identify the provider. Next
example summarizes the information to be specified by the user inside
this tag.

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <ResourcesList>
        <CloudProvider Name="PROVIDER_NAME">
            <Endpoint>
                <Server>https://PROVIDER_URL</Server>
                <ConnectorJar>CONNECTOR_JAR</ConnectorJar>
                <ConnectorClass>CONNECTOR_CLASS</ConnectorClass>
            </Endpoint>
            <Images>
                <Image Name="Image1">
                    <Adaptors>
                        <Adaptor Name="es.bsc.compss.nio.master.NIOAdaptor">
                            <SubmissionSystem>
                                <Interactive/>
                            </SubmissionSystem>
                            <Ports>
                                <MinPort>43001</MinPort>
                                <MaxPort>43010</MaxPort>
                            </Ports>
                        </Adaptor>
                    </Adaptors>
                    <OperatingSystem>
                        <Type>Linux</Type>
                    </OperatingSystem>
                    <Software>
                        <Application>Java</Application>
                    </Software>
                    <Price>
                        <TimeUnit>100</TimeUnit>
                        <PricePerUnit>36.0</PricePerUnit>
                    </Price>
                </Image>
                <Image Name="Image2">
                    <Adaptors>
                        <Adaptor Name="es.bsc.compss.nio.master.NIOAdaptor">
                            <SubmissionSystem>
                                <Interactive/>
                            </SubmissionSystem>
                            <Ports>
                                <MinPort>43001</MinPort>
                                <MaxPort>43010</MaxPort>
                            </Ports>
                        </Adaptor>
                    </Adaptors>
                </Image>
            </Images>

            <InstanceTypes>
                <InstanceType Name="Instance1">
                    <Processor Name="P1">
                        <ComputingUnits>4</ComputingUnits>
                        <Architecture>amd64</Architecture>
                        <Speed>3.0</Speed>
                    </Processor>
                    <Processor Name="P2">
                        <ComputingUnits>4</ComputingUnits>
                    </Processor>
                    <Memory>
                        <Size>1000.0</Size>
                    </Memory>
                    <Storage>
                        <Size>2000.0</Size>
                    </Storage>
                </InstanceType>
                <InstanceType Name="Instance2">
                    <Processor Name="P1">
                        <ComputingUnits>4</ComputingUnits>
                    </Processor>
                </InstanceType>
             </InstanceTypes>
      </CloudProvider>
    </ResourcesList>

The ``project.xml`` complements the information about a provider listed
in the ``resources.xml`` file. This file can contain a ``<Cloud>``
tag where to specify a list of providers, each with a
``<CloudProvider>`` tag, whose **name** attribute must match one of
the providers in the ``resources.xml`` file. Thus, the ``project.xml``
file **must** contain a subset of the providers specified in the
``resources.xml`` file. Next example summarizes the information to be
specified by the user inside this ``<Cloud>`` tag.

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <Project>
        <Cloud>
            <InitialVMs>1</InitialVMs>
            <MinimumVMs>1</MinimumVMs>
            <MaximumVMs>4</MaximumVMs>
            <CloudProvider Name="PROVIDER_NAME">
                <LimitOfVMs>4</LimitOfVMs>
                <Properties>
                    <Property Context="C1">
                        <Name>P1</Name>
                        <Value>V1</Value>
                    </Property>
                    <Property>
                        <Name>P2</Name>
                        <Value>V2</Value>
                    </Property>
                </Properties>

                <Images>
                    <Image Name="Image1">
                        <InstallDir>/opt/COMPSs/</InstallDir>
                        <WorkingDir>/tmp/Worker/</WorkingDir>
                        <User>user</User>
                        <Application>
                            <Pythonpath>/home/user/apps/</Pythonpath>
                        </Application>
                        <LimitOfTasks>2</LimitOfTasks>
                        <Package>
                            <Source>/home/user/apps/</Source>
                            <Target>/tmp/Worker/</Target>
                            <IncludedSoftware>
                                <Application>Java</Application>
                                <Application>Python</Application>
                            </IncludedSoftware>
                        </Package>
                        <Package>
                            <Source>/home/user/apps/</Source>
                            <Target>/tmp/Worker/</Target>
                        </Package>
                        <Adaptors>
                            <Adaptor Name="es.bsc.compss.nio.master.NIOAdaptor">
                                <SubmissionSystem>
                                    <Interactive/>
                                </SubmissionSystem>
                                <Ports>
                                    <MinPort>43001</MinPort>
                                    <MaxPort>43010</MaxPort>
                                </Ports>
                            </Adaptor>
                        </Adaptors>
                    </Image>
                    <Image Name="Image2">
                        <InstallDir>/opt/COMPSs/</InstallDir>
                        <WorkingDir>/tmp/Worker/</WorkingDir>
                    </Image>
                </Images>
                <InstanceTypes>
                    <InstanceType Name="Instance1"/>
                    <InstanceType Name="Instance2"/>
                </InstanceTypes>
            </CloudProvider>

            <CloudProvider Name="PROVIDER_NAME2">
                ...
            </CloudProvider>
        </Cloud>
    </Project>

For any connector the Runtime is capable to handle the next list of properties:

.. table:: Connector supported properties in the ``project.xml`` file
    :name: jclouds_properties

    +--------------------------+------------------------------------------------------------------------------+
    | **Name**                 | **Description**                                                              |
    +==========================+==============================================================================+
    | provider-user            | Username to login in the provider                                            |
    +--------------------------+------------------------------------------------------------------------------+
    | provider-user-credential | Credential to login in the provider                                          |
    +--------------------------+------------------------------------------------------------------------------+
    | time-slot                | Time slot                                                                    |
    +--------------------------+------------------------------------------------------------------------------+
    | estimated-creation-time  | Estimated VM creation time                                                   |
    +--------------------------+------------------------------------------------------------------------------+
    | max-vm-creation-time     | Maximum VM creation time                                                     |
    +--------------------------+------------------------------------------------------------------------------+


Additionally, for any connector based on SSH, the Runtime automatically
handles the next list of properties:

.. table:: Properties supported by any SSH based connector in the ``project.xml`` file
    :name: ssh_properties

    +--------------------------+------------------------------------------------------------------------------+
    | **Name**                 | **Description**                                                              |
    +==========================+==============================================================================+
    | vm-user                  | User to login in the VM                                                      |
    +--------------------------+------------------------------------------------------------------------------+
    | vm-password              | Password to login in the VM                                                  |
    +--------------------------+------------------------------------------------------------------------------+
    | vm-keypair-name          | Name of the Keypair to login in the VM                                       |
    +--------------------------+------------------------------------------------------------------------------+
    | vm-keypair-location      | Location (in the master) of the Keypair to login in the VM                   |
    +--------------------------+------------------------------------------------------------------------------+

Finally, the next sections provide a more accurate description of each
of the currently available connector and its specific properties.

Cloud connectors: rOCCI
^^^^^^^^^^^^^^^^^^^^^^^

The connector uses the `rOCCI binary client <https://appdb.egi.eu/store/software/rocci.cli>`_
(version newer or equal than 4.2.5) which has to be installed in the node where the COMPSs main
application is executed.

This connector needs additional files providing details about the
resource templates available on each provider. This file is located
under
``<COMPSs_INSTALL_DIR>/configuration/xml/templates`` path.
Additionally, the user must define the virtual images flavors and
instance types offered by each provider; thus, when the runtime
decides the creation of a VM, the connector selects the appropriate
image and resource template according to the requirements (in terms of
CPU, memory, disk, etc) by invoking the rOCCI client through Mixins
(heritable classes that override and extend the base templates).

:numref:`rOCCI_extensions` contains the rOCCI specific properties
that must be defined under the ``Provider`` tag in the ``project.xml``
file and :numref:`rOCCI_configuration` contains the specific properties
that must be defined under the ``Instance`` tag.

.. table:: rOCCI extensions in the ``project.xml`` file
    :name: rOCCI_extensions

    +--------------------------+------------------------------------------------------------------------------+
    | **Name**                 | **Description**                                                              |
    +==========================+==============================================================================+
    | auth                     | Authentication method, x509 only supported                                   |
    +--------------------------+------------------------------------------------------------------------------+
    | user-cred                | Path of the VOMS proxy                                                       |
    +--------------------------+------------------------------------------------------------------------------+
    | ca-path                  | Path to CA certificates directory                                            |
    +--------------------------+------------------------------------------------------------------------------+
    | ca-file                  | Specific CA filename                                                         |
    +--------------------------+------------------------------------------------------------------------------+
    | owner                    | Optional. Used by the PMES Job-Manager                                       |
    +--------------------------+------------------------------------------------------------------------------+
    | jobname                  | Optional. Used by the PMES Job-Manager                                       |
    +--------------------------+------------------------------------------------------------------------------+
    | timeout                  | Maximum command time                                                         |
    +--------------------------+------------------------------------------------------------------------------+
    | username                 | Username to connect to the back-end cloud provider                           |
    +--------------------------+------------------------------------------------------------------------------+
    | password                 | Password to connect to the back-end cloud provider                           |
    +--------------------------+------------------------------------------------------------------------------+
    | voms                     | Enable VOMS authentication                                                   |
    +--------------------------+------------------------------------------------------------------------------+
    | media-type               | Media type                                                                   |
    +--------------------------+------------------------------------------------------------------------------+
    | resource                 | Resource type                                                                |
    +--------------------------+------------------------------------------------------------------------------+
    | attributes               | Extra resource attributes for the back-end cloud provider                    |
    +--------------------------+------------------------------------------------------------------------------+
    | context                  | Extra context for the back-end cloud provider                                |
    +--------------------------+------------------------------------------------------------------------------+
    | action                   | Extra actions for the back-end cloud provider                                |
    +--------------------------+------------------------------------------------------------------------------+
    | mixin                    | Mixin definition                                                             |
    +--------------------------+------------------------------------------------------------------------------+
    | link                     | Link                                                                         |
    +--------------------------+------------------------------------------------------------------------------+
    | trigger-action           | Adds a trigger                                                               |
    +--------------------------+------------------------------------------------------------------------------+
    | log-to                   | Redirect command logs                                                        |
    +--------------------------+------------------------------------------------------------------------------+
    | skip-ca-check            | Skips CA checks                                                              |
    +--------------------------+------------------------------------------------------------------------------+
    | filter                   | Filters command output                                                       |
    +--------------------------+------------------------------------------------------------------------------+
    | dump-model               | Dumps the internal model                                                     |
    +--------------------------+------------------------------------------------------------------------------+
    | debug                    | Enables the debug mode on the connector commands                             |
    +--------------------------+------------------------------------------------------------------------------+
    | verbose                  | Enables the verbose mode on the connector commands                           |
    +--------------------------+------------------------------------------------------------------------------+


.. table:: Configuration of the ``<resources>.xml`` templates file
    :name: rOCCI_configuration

    +----------------+----------------------------------------------------------------------------------------+
    | **Instance**   | Multiple entries of resource templates.                                                |
    +================+========================================================================================+
    | Type           | Name of the resource template. It has to be the same name than in the previous files   |
    +----------------+----------------------------------------------------------------------------------------+
    | CPU            | Number of cores                                                                        |
    +----------------+----------------------------------------------------------------------------------------+
    | Memory         | Size in GB of the available RAM                                                        |
    +----------------+----------------------------------------------------------------------------------------+
    | Disk           | Size in GB of the storage                                                              |
    +----------------+----------------------------------------------------------------------------------------+
    | Price          | Cost per hour of the instance                                                          |
    +----------------+----------------------------------------------------------------------------------------+


Cloud connectors: JClouds
^^^^^^^^^^^^^^^^^^^^^^^^^

The JClouds connector is based on the JClouds API version *1.9.1*. Table
:numref:`jclouds_extensions` shows the extra available options under the
*Properties* tag that are used by this connector.

.. table:: JClouds extensions in the  ``<project>.xml`` file
    :name: jclouds_extensions

    +----------------+----------------------------------------------------------------------------------------+
    | **Instance**   | **Description**                                                                        |
    +================+========================================================================================+
    | provider       | Back-end provider to use with JClouds (i.e. aws-ec2)                                   |
    +----------------+----------------------------------------------------------------------------------------+

Cloud connectors: Docker
^^^^^^^^^^^^^^^^^^^^^^^^

This connector uses a Java API client from
https://github.com/docker-java/docker-java, version *3.0.3*. It has not
additional options. Make sure that the image/s you want to load are
pulled before running COMPSs with ``docker pull IMAGE``. Otherwise, the
connector will throw an exception.

Cloud connectors: Mesos
^^^^^^^^^^^^^^^^^^^^^^^

The connector uses the v0 Java API for Mesos which has to be installed
in the node where the COMPSs main application is executed. This
connector creates a Mesos framework and it uses Docker images to deploy
workers, each one with an own IP address.

By default it does not use authentication and the timeout timers are set
to 3 minutes (180.000 milliseconds). The list of **optional** properties
available from connector is shown in :numref:`Mesos_options`.

.. table:: Mesos connector options in the  ``<project>.xml`` file
    :name: Mesos_options

    +----------------------------------------+----------------------------------------------------------------+
    | **Instance**                           | **Description**                                                |
    +========================================+================================================================+
    | mesos-framework-name                   | Framework name to show in Mesos.                               |
    +----------------------------------------+----------------------------------------------------------------+
    | mesos-worker-name                       | Worker names to show in Mesos.                                |
    +----------------------------------------+----------------------------------------------------------------+
    | mesos-framework-hostname               | Framework hostname to show in Mesos.                           |
    +----------------------------------------+----------------------------------------------------------------+
    | mesos-checkpoint                       | Checkpoint for the framework.                                  |
    +----------------------------------------+----------------------------------------------------------------+
    | mesos-authenticate                     | Uses authentication? (``true``/``false``)                      |
    +----------------------------------------+----------------------------------------------------------------+
    | mesos-principal                        | Principal for authentication.                                  |
    +----------------------------------------+----------------------------------------------------------------+
    | mesos-secret                           | Secret for authentication.                                     |
    +----------------------------------------+----------------------------------------------------------------+
    | mesos-framework-register-timeout       | Timeout to wait for Framework to register.                     |
    +----------------------------------------+----------------------------------------------------------------+
    | mesos-framework-register-timeout-units | Time units to wait for register.                               |
    +----------------------------------------+----------------------------------------------------------------+
    | mesos-worker-wait-timeout              | Timeout to wait for worker to be created.                      |
    +----------------------------------------+----------------------------------------------------------------+
    | mesos-worker-wait-timeout-units        | Time units for waiting creation.                               |
    +----------------------------------------+----------------------------------------------------------------+
    | mesos-worker-kill-timeout              | Number of units to wait for killing a worker.                  |
    +----------------------------------------+----------------------------------------------------------------+
    | mesos-worker-kill-timeout-units        | Time units to wait for killing.                                |
    +----------------------------------------+----------------------------------------------------------------+
    | mesos-docker-command                   | Command to use at start for each worker.                       |
    +----------------------------------------+----------------------------------------------------------------+
    | mesos-containerizer                    | Containers to use: (``MESOS``/``DOCKER``)                      |
    +----------------------------------------+----------------------------------------------------------------+
    | mesos-docker-network-type              | Network type to use: (``BRIDGE``/``HOST``/``USER``)            |
    +----------------------------------------+----------------------------------------------------------------+
    | mesos-docker-network-name              | Network name to use for workers.                               |
    +----------------------------------------+----------------------------------------------------------------+
    | mesos-docker-mount-volume              | Mount volume on workers? (``true``/``false``)                  |
    +----------------------------------------+----------------------------------------------------------------+
    | mesos-docker-volume-host-path          | Host path for mounting volume.                                 |
    +----------------------------------------+----------------------------------------------------------------+
    | mesos-docker-volume-container-path     | Container path to mount volume.                                |
    +----------------------------------------+----------------------------------------------------------------+

TimeUnit available values: ``DAYS``, ``HOURS``, ``MICROSECONDS``,
``MILLISECONDS``, ``MINUTES``, ``NANOSECONDS``, ``SECONDS``.

Services configuration
======================

To allow COMPSs applications to use WebServices as tasks, the
``resources.xml`` can include a special type of resource called
*Service*. For each WebService it is necessary to specify its wsdl, its
name, its namespace and its port.

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <ResourcesList>
        <ComputeNode Name="localhost">
          ...
        </ComputeNode>

        <Service wsdl="http://bscgrid05.bsc.es:20390/hmmerobj/hmmerobj?wsdl">
            <Name>HmmerObjects</Name>
            <Namespace>http://hmmerobj.worker</Namespace>
            <Port>HmmerObjectsPort</Port>
        </Service>
    </ResourcesList>

When configuring the ``project.xml`` file it is necessary to include the
service as a worker by adding an special entry indicating only the name
and the limit of tasks as shown in the following example:

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <Project>
        <MasterNode/>
        <ComputeNode Name="localhost">
          ...
        </ComputeNode>

        <Service wsdl="http://bscgrid05.bsc.es:20390/hmmerobj/hmmerobj?wsdl">
            <LimitOfTasks>2</LimitOfTasks>
        </Service>
    </Project>

.. _http_configuration:

HTTP configuration
------------------

To enable execution of HTTP tasks, *Http* resources must be included in the
``resources`` file as shown in the following example. Please note that the *BaseUrl*
attribute is the unique identifier of each Http resource. However, it's possible to
assign a single resource to multiple *services* and in the same way one *service*
can be executed on various *resources*.


.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <ResourcesList>
        <ComputeNode Name="localhost">
          ...
        </ComputeNode>

        <Http BaseUrl="http://remotehost:1992/test/">
            <ServiceName>service_1</ServiceName>
            <ServiceName>service_2</ServiceName>
        </Http>

        <Http BaseUrl="http://remotehost:2020/print/">
            <ServiceName>service_2</ServiceName>
            <ServiceName>service_3</ServiceName>
        </Http>

    </ResourcesList>

Configuration of the ``project`` file must have the Http worker(s) as well, in order
to let the runtime know limit of tasks to be executed in parallel on resources.

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <Project>
        <MasterNode/>
        <ComputeNode Name="localhost">
          ...
        </ComputeNode>

        <Http BaseUrl="http://remotehost:1992/test/">
            <LimitOfTasks>1</LimitOfTasks>
        </Http>

        <Http BaseUrl="http://remotehost:2020/print/">
            <LimitOfTasks>1</LimitOfTasks>
        </Http>

    </Project>
