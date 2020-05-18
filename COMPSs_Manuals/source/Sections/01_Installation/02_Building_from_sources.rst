Building from sources
=====================

This section describes the steps to install COMPSs from the sources.

The first step is downloading the source code from the Git repository.

.. code-block:: console

    $ git clone https://github.com/bsc-wdc/compss.git
    $ cd compss

Then, you need to download the embedded dependencies from the git submodules.

.. code-block:: console

    $ compss> ./submodules_get.sh
    $ compss> ./submodules_patch.sh

Finally you just need to run the installation script. You have two options:

.. content-tabs::

    .. tab-container:: For_all_users
        :title: For all users

        For installing COMPSs for all users run the following command:

        .. code-block:: console

            $ compss> cd builders/
            $ builders> export INSTALL_DIR=/opt/COMPSs/
            $ builders> sudo -E ./buildlocal ${INSTALL_DIR}

        .. ATTENTION::

            Root access is required.

    .. tab-container:: For_current_user
        :title: For the current user

        For installing COMPSs for the current user run the following commands:

        .. code-block:: console

            $ compss> cd builders/
            $ builders> INSTALL_DIR=$HOME/opt/COMPSs/
            $ builders> ./buildlocal ${INSTALL_DIR}


.. TIP::

    The ``buildlocal`` script allows to disable the installation of
    components. The options can be foun in the command help:

    .. code-block:: console

        $ compss> cd builders/
        $ builders> ./buildlocal -h

          Usage: ./buildlocal [options] targetDir
          * Options:
              --help, -h                  Print this help message

              --opts                      Show available options

              --version, -v               Print COMPSs version

              --monitor, -m               Enable Monitor installation
              --no-monitor, -M            Disable Monitor installation
                                          Default: true

              --bindings, -b              Enable bindings installation
              --no-bindings, -B           Disable bindings installation
                                          Default: true

              --pycompss, -p              Enable PyCOMPSs installation
              --no-pycompss, -P           Disable PyCOMPSs installation
                                          Default: true

              --tracing, -t               Enable tracing system installation
              --no-tracing, -T            Disable tracing system installation
                                          Default: true

              --autoparallel, -a          Enable autoparallel module installation
              --no-autoparallel, -A       Disable autoparallel module installation
                                          Default: true

              --kafka, -k                 Enable Kafka module installation
              --no-kafka, -K              Disable Kafka module installation
                                          Default: true

              --nothing, -N               Disable all previous options
                                          Default: unused

              --user-exec=<str>           Enables a specific user execution for maven compilation
                                          When used the maven install is not cleaned.
                                          Default: false

              --skip-tests                Disables MVN unit tests
                                          Default:

          * Parameters:
              targetDir                   COMPSs installation directory
                                          Default: /opt/COMPSs


Post installation
-----------------

Once your COMPSs package has been installed remember to log out and back
in again to end the installation process.

.. CAUTION::

    Using Ubuntu version 18.04 or higher requires to comment the following
    lines in your ``.bashrc`` in order to have the appropriate environment
    after logging out and back again (which in these distributions it must be
    from the complete system (e.g. gnome) not only from the terminal,
    or restart the whole machine).

    .. code-block:: bash

        # If not running interactively, don't do anything
        # case $- in          #
        #     *i*) ;;         # Comment these lines before logging out
        #       *) return;;   # from the whole gnome (or restart the machine).
        # esac                #

In addition, COMPSs requires **ssh passwordless access**.
If you need to set up your machine for the first time please take a look
at :ref:`Sections/01_Installation/05_Additional_configuration:Additional Configuration`
Section for a detailed description of the additional configuration.
