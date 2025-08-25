.. spelling:word-list::

   centric
   Wi
   Fi

Agents Deployments
******************

Opposing to well-established deployments with an almost-static set of computing resources and hardly-varying interconnection conditions such as a single-computer, a cluster or a supercomputer; dynamic infrastructures, like Fog environments, require a different kind of deployment able to adapt to rapidly-changing conditions. Such infrastructures are likely to comprise several mobile devices whose connectivity to the infrastructure is temporary. When the device is within the network range, it joins an already existing COMPSs deployment and interacts with the other resources to offload tasks onto them or vice-versa. Eventually, the connectivity of that mobile device could be disrupted to never reestablish. If the leaving device was used as a worker node, the COMPSs master needs to react to the departure and reassign the tasks running on that node. If the device was the master node, it should be able to carry on with the computation being isolated from the rest of the infrastructure or with another set of available resources.

COMPSs Agents is a deployment approach especially designed to fit in this kind of environments. Each device is an autonomous individual with processing capabilities hosting the execution of a COMPSs runtime as a background service. Applications - running on that device or on another - can contact this service to request the execution of a function in a serverless, stateless manner (resembling the Function-as-a-Service model). If the requested function follows the COMPSs programming model, the runtime will parallelize its execution as if it were the main function of a regular COMPSs application.

Agents can associate with other agents by offering their embedded computing resources to execute functions to achieve a greater purpose; in exchange, they receive a platform where they can offload their computation in the same manner, and, thus, achieve lower response times. As opposed to the master-worker approach followed by the classic COMPSs deployment, where a single node produces the all the workload, in COMPSs Agents deployments, any of the nodes within the platform becomes a potential source of computation to distribute. Therefore, this master-centric approach where workload producer to orchestrate holistically the execution is no longer valid. Besides, concentrating all the knowledge of several applications and handling the changes of infrastructure represents an important computational burden for the resource assuming the master role, especially if it is a resource-scarce device like a mobile. For this two reasons, COMPSs agents proposes a hierarchic approach to organize the nodes. Each node will only be aware of some devices with which it has direct connection and only decides whether the task runs on its embedded computing devices or if the responsibility of executing the task is delegated onto one of the other agents. In the latter case, the receiver node will face the same problem and decide whether it should host the execution or forward it to a different node.

The following image illustrates an example of a COMPSs agents hierarchy that could be deployed in any kind of facilities; for instance, a university campus. In this case, students only interact directly with their mobile phones and laptops to run their applications; however, the computing workload produced by them is distributed across the whole system. To do so, the mobile devices need to connect to one of the edge devices devices scattered across the facilities acting as a Wi-Fi Hotspot (in the example, raspberry Pi) which runs a COMPSs agent. To submit the operation execution to the platform, mobile devices can either contact a COMPSs agent running in the device or the application can directly contact the remote agent running on the rPi. All rPi agents are connected to an on-premise server within the campus that also runs a COMPSs Agent. Upon an operation request by a user device, the rPi can host the computation on its own devices or forward the request to one of its neighboring agents: the on-premise server or another user's device running a COMPSs agent. In the case that the rPi decides to move up the request through the hierarchy, the on-premise server faces a similar problem: hosting the computation on its local devices, delegating the execution onto one of the rPi -- which in turn could forward the execution back to another user's device --, or submit the request to a cloud. Internally, the Cloud can also be organized with COMPSs Agents hierarchy; thus, one of its nodes can act as the gateway to receive external requests and share the workload across the whole system.

.. figure:: ./03_Agents/Figures/agents_infra_example.png
   :alt: Agents hierarchy example
   :align: center
   :width: 500px


.. toctree::
    :maxdepth: 3
    :caption: Table of Contents

    03_Agents/01_Local
    03_Agents/02_Supercomputers
