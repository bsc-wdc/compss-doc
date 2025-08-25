Chameleon
=========

What is Chameleon?
------------------

The Chameleon project is a configurable experimental environment for
large-scale cloud research based on a *OpenStack* KVM Cloud. With
funding from the *National Science Foundation (NSF)*, it provides a
large-scale platform to the open research community allowing them
explore transformative concepts in deeply programmable cloud services,
design, and core technologies. The Chameleon testbed, is deployed at the
*University of Chicago* and the *Texas Advanced Computing Center* and
consists of 650 multi-core cloud nodes, 5PB of total disk space, and
leverage 100 Gbps connection between the sites.

The project is led by the *Computation Institute* at the *University of
Chicago* and partners from the *Texas Advanced Computing Center* at the
*University of Texas* at Austin, the *International Center for Advanced
Internet Research* at *Northwestern University*, the *Ohio State
University*, and *University of Texas* at *San Antoni*, comprising a
highly qualified and experienced team. The team includes members from
the *NSF* supported *FutureGrid* project and from the *GENI* community,
both forerunners of the *NSFCloud* solicitation under which this project
is funded. Chameleon will also sets of partnerships with commercial and
academic clouds, such as *Rackspace*, *CERN* and *Open Science Data
Cloud (OSDC)*.

For more information please check https://www.chameleoncloud.org/ .

Execution in Chameleon
----------------------

Currently, COMPSs can only handle the Chameleon infrastructure as a
cluster (deployed inside a lease). Next, we provide the steps needed to
execute COMPSs applications at Chameleon:

-  Make a lease reservation with 1 minimum node (for the COMPSs master
   instance) and a maximum number of nodes equal to the number of COMPSs
   workers needed plus one

-  Instantiate the master image (based on the published image
   *COMPSs__CC-CentOS7*)

-  Attach a public IP and login to the master instance (the instance is
   correctly contextualized for COMPSs executions if you see a COMPSs
   login banner)

-  Set the instance as COMPSs master by running
   ``/etc/init.d/chameleon_init start``

-  Copy your CH file (API credentials) to the Master and source it

-  Run the ``chameleon_cluster_setup`` script and fill the information
   when prompted (you will be asked for the name of the master instance,
   the reservation id and number of workers). This scripts may take
   several minutes since it sets up the all cluster.

-  Execute your COMPSs applications normally using the ``runcompss``
   script

As an example you can check this `video <https://www.youtube.com/watch?v=BrQ6anPHjAU>`_
performing a full setup and execution of a COMPSs application at Chameleon.

.. youtube:: BrQ6anPHjAU