Cloud
*****

This section will show you how to configure the COMPSs framework in Cloud environments.

Configure the COMPSs Cloud Connectors
=====================================

This section provides information about the additional configuration
needed for some Cloud Connectors.

OCCI (Open Cloud Computing Interface) connector
-----------------------------------------------

In order to execute a COMPSs application using cloud resources, the
rOCCI (Ruby OCCI) connector [1]_ has to be configured properly. The connector
uses the rOCCI CLI client (upper versions from 4.2.5) which has to be
installed in the node where the COMPSs main application runs. The client
can be installed following the instructions detailed at
http://appdb.egi.eu/store/software/rocci.cli


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


.. [1]
   https://appdb.egi.eu/store/software/rocci.cli
