.. spelling:word-list::

   env
   mn

Execution example
-----------------

Application
~~~~~~~~~~~

In this section, we show how to execute the :ref:`Sections/07_Sample_Applications/02_Python/03_KMeans:KMeans`
Python COMPSs application in **batch mode** using MareNostrum 5 supercomputer.

In this scenario, we have in our local machine, the KMeans application in
``/home/user/kmeans`` and inside the ``kmeans`` directory we only have the
file ``kmeans.py``. And in the remote machine (``glogin1.bsc.es``),
we have the user ``bsc12345``. So we can access this machine with
``ssh bsc12345@glogin1.bsc.es``.

In the **first step**, we have to be sure that COMPSs and all the application
files are available in MN5 (``glogin1.bsc.es``). For this example, we assume
that the application will be deployed in the user home directory
(``/home/bsc/bsc12345/kmeans``) and COMPSs is installed in
``/apps/GPP/COMPSs/3.3.3``. The following command are used to deploy the
application and check the COMPSs installation:

.. code-block:: bash

    # In the local machine, copy the application data into MN5
    $ scp -r /home/user/kmeans bsc12345@glogin1.bsc.es:/home/bsc/bsc12345/.
    $ ssh bsc12345@glogin1.bsc.es
    # Inside the remote machine, check where COMPSs is installed
    $ module load COMPSs/3.3.3
    $ echo $(builtin cd $(dirname $(which runcompss))/../../..; pwd)
    /apps/GPP/COMPSs/3.3.3
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
            <InstallDir>/apps/GPP/COMPSs/3.3.3/</InstallDir>
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
    module load COMPSs/3.3.3


Finally, we launch the application in the **third step**.
It must be done using the following command within the local machine:

.. code-block:: console

    $ runcompss  --project=/home/user/kmeans/project.xml \
                 --resources=/home/user/kmeans/resources.xml \
                 --comm=es.bsc.compss.gos.master.GOSAdaptor \
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
installed in ``/apps/GPP/COMPSs/3.3.3``.

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
