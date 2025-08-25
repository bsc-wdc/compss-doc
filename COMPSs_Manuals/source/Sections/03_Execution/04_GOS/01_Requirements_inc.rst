Requirements
------------

In order to use COMPSs with remote clusters some requirements must be fulfilled:

-  Generate a **public-private key pair** and authorize it in any Cluster that
   will be used (more details in section
   :ref:`additional_configuration_ssh_passwordless`).
-  Have this remote resources in the **known hosts** file situated in
   **~/.ssh/known_hosts**.
-  **COMPSs** must be installed in both in the master and all the remote
   Clusters.

.. IMPORTANT::

    Both, the client and the remote computing resource should have the same or
    a compatible version of **COMPSs**, which must be **3.2 or higher**.
