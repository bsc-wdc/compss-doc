.. spelling:word-list::

   env

Hybrid execution example
------------------------

Application
~~~~~~~~~~~

In this section, we show how to execute a really simple Python application
for COMPSs in **batch mode** using two clusters. In particular, this example
uses the two MareNostrum 5 supercomputer partitions (one with powerful CPUs (GPP)
and another with GPUs (ACC)) from the local machine..

In this scenario, we have in our local machine, the application in
``/home/user/simple`` and inside the ``simple`` directory we only have the
file ``simple.py``. And in the remote machines (``glogin1.bsc.es`` for GPP and
``alogin1.bsc.es`` for GPP, we have the user ``bsc12345``. So we can access
these machines with ``ssh bsc12345@glogin1.bsc.es`` and
``ssh bsc12345@alogin1.bsc.es``.

The application that we are going to use is:

.. code-block:: python

    from pycompss.api.task import task
    from pycompss.api.constraint import constraint
    from pycompss.api.api import compss_wait_on

    @constraint(processors=[{'ProcessorType':'CPU', 'ComputingUnits':'100'}])
    @task(returns=1)
    def increment(value):
        # Code that uses 100 CPU cores
        return value + 1

    @constraint(processors=[{'ProcessorType':'CPU', 'ComputingUnits':'20'},
                            {'ProcessorType':'GPU', 'ComputingUnits':'1'}])
    @task(returns=1)
    def multiply(value):
        # Code that uses 20 CPU cores and 1 GPU
        return value * value

    def main():
        value = 2
        results = []
        for i in range(2):
            partial = increment(value)
            complete = multiply(partial)
            results.append(complete)
        results = compss_wait_on(results)
        print(results)

    if __name__=="__main__":
        main()

This application has two tasks defined (``increment`` and ``multiply``) with
different requirements. Since one of the MN5 partitions has GPUs, this example
illustrates how COMPSs is able to deal with two different clusters executing
the tasks respecting their constraints. The ``increment`` task is represents a
function with a high internal parallelism, requiring 100 CPU cores, and the
``multiply`` function represents a function with less internal parallelism, but
requiring one GPU. Consequently, the ``increment`` tasks can only be executed
in the GPP partition (the ACC partition CPUs have only 80 GPU cores), while
the ``multiply`` tasks can only be executed in the ACC partition (the GPP
partition although it has enough CPU cores, does not have GPUs).
The main function loops over two iterations invoking two times the
``increment`` and ``multiply`` tasks. Notice that there is a data dependency
between the tasks.

In the **first step**, we have to be sure that COMPSs and the application
is available in MN5. For this example, we assume that the application will be
deployed in the user home directory (``/home/bsc/bsc12345/simple``) which is
shared among partitions and COMPSs is installed in ``/apps/GPP/COMPSs/3.3.2``
in GPP and in ``/apps/ACC/COMPSs/3.3.2`` in ACC. The following command are used
to deploy the application and check the COMPSs installation:

.. code-block:: bash

    # In the local machine, copy the application data into MN5
    $ scp -r /home/user/simple bsc12345@glogin1.bsc.es:/home/bsc/bsc12345/.
    $ ssh bsc12345@glogin1.bsc.es
    # Inside the remote machine within GPP, check where COMPSs is installed
    $ module load COMPSs/3.3.2
    $ echo $(builtin cd $(dirname $(which runcompss))/../../..; pwd)
    /apps/GPP/COMPSs/3.3.2
    $ exit
    $ ssh bsc12345@alogin1.bsc.es
    # Inside the remote machine within ACC, check where COMPSs is installed
    $ module load COMPSs/3.3.2
    $ echo $(builtin cd $(dirname $(which runcompss))/../../..; pwd)
    /apps/ACC/COMPSs/3.3.2
    $ exit

In the **second step**, we create the required xml files and they will be
stored in ``/home/user/simple``. Next lines show the XML files for this example:

.. code-block:: xml
    :name: hybrid_gos_project_xml
    :caption: hybrid_project.xml

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
                                <ProjectName>bsc00</ProjectName>
                            </BatchProperties>
                        </Batch>
                    </SubmissionSystem>
                </Adaptor>
            </Adaptors>
            <InstallDir>/apps/GPP/COMPSs/3.3.2/</InstallDir>
            <WorkingDir>/home/bsc/bsc12345/simple/gpp/</WorkingDir>
            <User>bsc12345</User>
            <LimitOfTasks>1000</LimitOfTasks>
            <Application>
                <Classpath>/home/bsc/bsc12345/simple/</Classpath>
                <EnvironmentScript>/home/bsc/bsc12345/simple/env_gpp.sh</EnvironmentScript>
            </Application>
            <ClusterNode Name="compute_node_type">
                <NumberOfNodes>2</NumberOfNodes>
            </ClusterNode>
        </ComputingCluster>
        <ComputingCluster Name="alogin1.bsc.es">
            <Adaptors>
                <Adaptor Name="es.bsc.compss.gos.master.GOSAdaptor">
                    <SubmissionSystem>
                        <Batch>
                            <Queue>slurm</Queue>
                            <BatchProperties>
                                <Port>22</Port>
                                <MaxExecTime>2</MaxExecTime>
                                <Reservation>disabled</Reservation>
                                <QOS>acc_debug</QOS>
                                <FileCFG>mn5_acc.cfg</FileCFG>
                                <ProjectName>bsc00</ProjectName>
                            </BatchProperties>
                        </Batch>
                    </SubmissionSystem>
                </Adaptor>
            </Adaptors>
            <InstallDir>/apps/ACC/COMPSs/3.3.2/</InstallDir>
            <WorkingDir>/home/bsc/bsc12345/simple/acc/</WorkingDir>
            <User>bsc12345</User>
            <LimitOfTasks>1000</LimitOfTasks>
            <Application>
                <Classpath>/home/bsc/bsc12345/simple/</Classpath>
                <EnvironmentScript>/home/bsc/bsc12345/simple/env_acc.sh</EnvironmentScript>
            </Application>
            <ClusterNode Name="compute_node_type">
                <NumberOfNodes>2</NumberOfNodes>
            </ClusterNode>
        </ComputingCluster>
    </Project>



.. code-block:: xml
    :name: hybrid_gos_resources_xml
    :caption: hybrid_resources.xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <ResourcesList>
        <SharedDisk Name="Disk1">
            <Storage>
                <Size>100.0</Size>
            </Storage>
        </SharedDisk>
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
            <SharedDisks>
                <AttachedDisk Name="Disk1">
                    <MountPoint>/</MountPoint>
                </AttachedDisk>
            </SharedDisks>
            <ClusterNode Name="compute_node_type">
                <MaxNumNodes>4</MaxNumNodes>
                <Processor Name="CPU_MN5_GPP">
                    <Architecture>worker_gpp</Architecture>
                    <ComputingUnits>112</ComputingUnits>
                    <Type>CPU</Type>
                </Processor>
            </ClusterNode>
        </ComputingCluster>
        <ComputingCluster Name="alogin1.bsc.es">
            <Adaptors>
                <Adaptor Name="es.bsc.compss.gos.master.GOSAdaptor">
                    <SubmissionSystem>
                        <Batch>
                            <Queue>slurm</Queue>
                        </Batch>
                    </SubmissionSystem>
                </Adaptor>
            </Adaptors>
            <SharedDisks>
                <AttachedDisk Name="Disk1">
                    <MountPoint>/</MountPoint>
                </AttachedDisk>
            </SharedDisks>
            <ClusterNode Name="compute_node_type">
                <MaxNumNodes>4</MaxNumNodes>
                <Processor Name="GPU_MN5_ACC">
                    <Architecture>worker_acc</Architecture>
                    <ComputingUnits>4</ComputingUnits>
                    <Type>GPU</Type>
                </Processor>
                <Processor Name="CPU_MN5_ACC">
                    <Architecture>worker_acc</Architecture>
                    <ComputingUnits>80</ComputingUnits>
                    <Type>CPU</Type>
                </Processor>
            </ClusterNode>
        </ComputingCluster>
    </ResourcesList>


And the environment scripts for MN5 are ``/home/bsc/bsc12345/simple/env_gpp.sh``
and ``/home/bsc/bsc12345/simple/env_acc.sh``:


.. code-block:: text
    :name: env_mn_gpp
    :caption: env_gpp.sh

    export COMPSS_PYTHON_VERSION=3.12.1
    module load COMPSs/3.3.2

.. code-block:: text
    :name: env_mn_acc
    :caption: env_acc.sh

    export COMPSS_PYTHON_VERSION=3.12.1
    module load COMPSs/3.3.2


Finally, we launch the application in the **third step**.
It must be done using the following command within the local machine:

.. code-block:: console

    $ runcompss  --project=/home/user/simple/project.xml \
                 --resources=/home/user/simple/resources.xml \
                  --comm=es.bsc.compss.gos.master.GOSAdaptor \
                 simple.py

.. TIP::

    The same command can be used to run Java or C applications using the GOS
    adaptor (but take into account that the ``--classpath`` flag is will
    be needed for Java and ``--library_path`` will be needed for C).



Notebook
~~~~~~~~

In this section, we show how to execute the a Jupyter notebook in
**batch mode** using multiple computing clusters.

The **first step** requires to make sure that COMPSs is available in the remote
machines (e.g. ``glogin1.bsc.es`` and ``alogin1.bsc.es``). For this example,
we assume that COMPSs is installed in ``/apps/GPP/COMPSs/3.3.2`` within
``glogin1.bsc.es``, and ``/apps/ACC/COMPSs/3.3.2`` within ``alogin1.bsc.es``.

.. IMPORTANT::

    When using jupyter notebook it is not necessary to transfer the application
    to the remote machine, since COMPSs will deal with the code automatically.

In the **second step**, we create the required project and resources xml files
and they will be stored in ``/home/user/notebook``. They are the same as
defined in :ref:`hybrid_gos_project_xml` and :ref:`hybrid_gos_resources_xml`.

Finally, in the **third step** we can define in our local machine the notebook
``/home/user/notebook/simple.ipynb``. Note that the ``ipycompss.start`` call
includes the project and resources parameters, as well as the ``GOS``
communication adaptor.

.. code-block:: python

    import pycompss.interactive as ipycompss
    ipycompss.start(comm="GOS",
                    project_xml="/home/user/notebook/hybrid_project.xml",
                    resources_xml="/home/user/notebook/hybrid_resources.xml")

    # Now define your tasks and code within the following cells
