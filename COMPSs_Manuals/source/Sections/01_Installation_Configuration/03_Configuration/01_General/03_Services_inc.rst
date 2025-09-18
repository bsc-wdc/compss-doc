Services
========

This section will show you how to configure the COMPSs framework to use web services.

Configuration
-------------

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
^^^^^^^^^^^^^^^^^^

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
