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

