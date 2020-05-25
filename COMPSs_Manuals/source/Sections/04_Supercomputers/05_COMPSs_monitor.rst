Enabling COMPSs Monitor
=======================

Configuration
-------------

As supercomputer nodes are connection restricted, the better way to
enable the *COMPSs Monitor* is from the users local machine. To do so
please install the following packages:

-  COMPSs Runtime

-  COMPSs Monitor

-  sshfs

For further details about the COMPSs packages installation and
configuration please refer to :ref:`Sections/01_Installation:Installation and Administration` Section.
If you are not willing to install COMPSs in your local machine please
consider to download our Virtual Machine available at our webpage.

Once the packages have been installed and configured, users need to
mount the sshfs directory as follows. The ``SC_USER`` stands for your
supercomputer’s user, the ``SC_ENDPOINT`` to the supercomputer’s public
endpoint and the ``TARGET_LOCAL_FOLDER`` to the local folder where you
wish to deploy the supercomputer files):

.. code-block:: console

    compss@bsc:~$ scp $HOME/.ssh/id_rsa.pub ${SC_USER}@mn1.bsc.es:~/id_rsa_local.pub
    compss@bsc:~$ ssh SC_USER@SC_ENDPOINT \
                      "cat ~/id_rsa_local.pub >> ~/.ssh/authorized_keys; \
                      rm ~/id_rsa_local.pub"
    compss@bsc:~$ mkdir -p TARGET_LOCAL_FOLDER/.COMPSs
    compss@bsc:~$ sshfs -o IdentityFile=$HOME/.ssh/id_rsa -o allow_other \
                       SC_USER@SC_ENDPOINT:~/.COMPSs \
                       TARGET_LOCAL_FOLDER/.COMPSs

Whenever you wish to unmount the sshfs directory please run:

.. code-block:: console

    compss@bsc:~$ sudo umount TARGET_LOCAL_FOLDER/.COMPSs

Execution
---------

Access the COMPSs Monitor through its webpage
(http://localhost:8080/compss-monitor by default) and log in with the
``TARGET_LOCAL_FOLDER`` to enable the COMPSs Monitor for MareNostrum.

Please remember that to enable **all** the COMPSs Monitor features
applications must be ran with the *-m* flag. For further details please check the
:ref:`Sections/03_App_Execution:Application execution` Section.

:numref:`mn_monitor1` illustrates how to login and :numref:`mn_monitor2`
shows the COMPSs Monitor main page for an application
run inside a Supercomputer.

.. figure:: ./Figures/mn_monitor1.jpeg
   :name: mn_monitor1
   :alt: COMPSs Monitor login for Supercomputers
   :align: center
   :width: 50.0%

   COMPSs Monitor login for Supercomputers

.. figure:: ./Figures/mn_monitor2.jpeg
   :name: mn_monitor2
   :alt: COMPSs Monitor main page for a test application at Supercomputers
   :align: center
   :width: 95.0%

   COMPSs Monitor main page for a test application at Supercomputers
