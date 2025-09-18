.. _install_for_supercomputer:

Supercomputer
*************

The COMPSs Framework can be installed in any Supercomputer by installing
its packages as in a normal distribution. The packages are ready to be
reallocated so the administrators can choose the right location for the
COMPSs installation.

However, if the administrators are not willing to install COMPSs through
the packaging system, we also provide a **COMPSs zipped file**
containing a :spelling:ignore:`pre`-build script to easily install COMPSs. Next subsections
provide further information about this process.


.. _install_for_supercomputer_installation:

Installation
============

To perform the COMPSs Framework installation please execute the
following commands:

.. code-block:: console

     $ # Check out the last COMPSs release
     $ wget http://compss.bsc.es/repo/sc/stable/COMPSs_<version>.tar.gz

     $ # Unpackage COMPSs
     $ tar -xvzf COMPSs_<version>.tar.gz

     $ # Install COMPSs at your preferred target location
     $ cd COMPSs
     $ ./install [options] <targetDir> [<supercomputer.cfg>]

     $ # Clean downloaded files
     $ rm -r COMPSs
     $ rm COMPSs_<version>.tar.gz

The installation script will install COMPSs inside the given ``<targetDir>``
folder and it will copy the ``<supercomputer.cfg>`` as default configuration.
It also provides some options to skip the installation of optional features or
bound the installation to an specific python version. You can see the available
options with the following command.

.. code-block:: console

     $ ./install --help

.. attention::
   If the ``<targetDir>`` folder already exists it will be **automatically erased**.

After completing the previous steps, administrators must ensure that
the nodes have passwordless ssh access. If it is not the case, please
contact the COMPSs team at support-compss@bsc.es.

The COMPSs package also provides a *compssenv* file that loads the
required environment to allow users work more easily with COMPSs. Thus,
after the installation process we recommend to source the
``<targetDir>/compssenv`` into the users *.bashrc*.

Once done, remember to log out and back in again to end the
installation process.


.. ATTENTION::

  After the installation, it is **MANDATORY** to configure the installation
  with the supercomputer characteristics (e.g. queuing system, hardware, etc.).

  **The configuration is thoroughly described in Section** :ref:`Supercomputer configuration <Sections/01_Installation_Configuration/03_Configuration/02_Supercomputer:Configuration>`
