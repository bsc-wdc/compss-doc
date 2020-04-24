Building from sources
=====================

This section describes the steps to install COMPSs from the sources.

The first step is downloading the source code from the Git repository.

.. code-block:: console

    $ git clone https://github.com/bsc-wdc/compss.git
    $ cd compss

Then, you need to download the embedded dependencies from the git
submodules.

.. code-block:: console

    $ compss> ./submodules_get.sh
    $ compss> ./submodules_patch.sh

Finally you just need to run the installation script. You have to options:

.. content-tabs::

    .. tab-container:: For_all_users
        :title: For all users

        For installing COMPSs for all users run the following command:

        .. code-block:: console

            $ compss> cd builders/
            $ builders> export INSTALL_DIR=/opt/COMPSs/
            $ builders> sudo -E ./buildlocal [options] ${INSTALL_DIR}

        .. ATTENTION::
        
            Root access is required.

    .. tab-container:: For_current_user
        :title: For the current user

        For installing COMPSs for the current user run the following command:

        .. code-block:: console

            $ compss> cd builders/
            $ builders> INSTALL_DIR=$HOME/opt/COMPSs/
            $ builders> ./buildlocal [options] ${INSTALL_DIR}

The different installation options can be found in the command help.

.. code-block:: console

    $ compss> cd builders/
    $ builders> ./buildlocal -h

Post installation
-----------------

Once your COMPSs package has been installed remember to log out and back
in again to end the installation process.

If you need to set up your machine for the first time please take a look
at :ref:`Additional Configuration` Section for a detailed description of
the additional configuration.
