Building from sources
=====================

This section describes the steps to install COMPSs from the sources.

The first step is downloading the source code from the Git repository and select the version to compile:

.. code-block:: console

    $ git clone https://github.com/bsc-wdc/compss.git
    $ cd compss
    $ git checkout <version>

Then, you need to download the embedded dependencies from the git submodules (from the ``compss/`` folder):

.. code-block:: console

    $ ./submodules_get.sh

.. WARNING::

        Before running the installation script in macOS distributions, some previous definitions need to be done:

        .. code-block:: console

            $ alias readlink=/opt/homebrew/bin/greadlink
            $ export LIBTOOL=`which glibtool`
            $ export LIBTOOLIZE=`which glibtoolize`
            $ export JAVA_HOME=/opt/homebrew/opt/openjdk@11/libexec/openjdk.jdk/Contents/Home


Finally you just need to run the installation script. You have two options:

.. tabs::

    .. tab:: For all users

        For installing COMPSs for all users run the following commands (from the ``compss/`` folder):

        .. code-block:: console

            $ cd builders/
            $ export INSTALL_DIR=/opt/COMPSs/
            $ sudo -E ./buildlocal -X -S --skip-tests ${INSTALL_DIR}

        .. ATTENTION::

            Root access is required.

    .. tab:: For the current user

        For installing COMPSs for the current user run the following commands (from the ``compss/`` folder):

        .. code-block:: console

            $ cd builders/
            $ export INSTALL_DIR=$HOME/opt/COMPSs/
            $ ./buildlocal -X -S --skip-tests ${INSTALL_DIR}

.. WARNING::

        In macOS distributions, the System Integrity Protection (SIP) does not allow to modify the ``/System`` folder
        even with root permissions. This means the installation building from sources can only be installed for the
        current user.

.. TIP::

    The ``buildlocal`` script allows to disable the installation of
    components. The options can be found in the command help:

    .. code-block:: console

        $ cd builders/
        $ ./buildlocal -h

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

              --kafka, -k                 Enable Kafka module installation
              --no-kafka, -K              Disable Kafka module installation
                                          Default: true

              --jacoco, -j                Enable Jacoco module installation
              --no-jacoco, -J             Disable Jacoco module installation
                                          Default: true

              --dlb, -d                   Enable dlb module installation
              --no-dlb, -D                Disable dlb module installation
                                          Default: true

              --cli, -c                   Enable Command Line Interface module installation
              --no-cli, -C                Disable Command Line Interface module installation
                                          Default: true

              --pycompss-compile, -x      Enable PyCOMPSs compilation with MyPy check
              --no-pycompss-compile, -X   Disable PyCOMPSs compilation with MyPy check
                                          Default: true

              --python-style, -s          Enable Python style check
              --no-python-style, -S       Disable Python style check
                                          Default: true

              --nothing, -N               Disable all previous options
                                          Default: unused

              --user-exec=<str>           Enables a specific user execution for maven compilation
                                          When used the maven install is not cleaned.
                                          Default: false

              --skip-tests                Disables MVN and Python unit tests
                                          Default: true

          * Parameters:
              targetDir                   COMPSs installation directory
                                          Default: /opt/COMPSs

    .. WARNING::

        Components Tracing, Kafka, Jacoco and DLB cannot be installed in macOS distributions. Therefore,
        at least options ``-T -K -J -D`` must be used when invoking ``buildlocal``

    .. CAUTION::

        The Python unit tests, PyCOMPSs compilation and Python style check require extra
        dependencies that can be installed automatically for each purpose by running the following scripts
        (add sudo before the scripts if you want them to be installed system wide). From the ``builders/`` folder:

        .. code-block:: console

            $ ../compss/programming_model/bindings/python/scripts/./install_testing_deps.sh
            $ ../compss/programming_model/bindings/python/scripts/./install_compilation_deps.sh
            $ ../compss/programming_model/bindings/python/scripts/./install_style_deps.sh


        .. CAUTION::

            The ``mpi4py`` package requires to have the MPI header/development package available,
            which has to be installed with the OS package manager. From the ``compss/`` folder:

            $ sudo apt-get install libopenmpi-dev  # Adapt for your OS package manager


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

In addition, COMPSs **REQUIRES ssh passwordless access**.
If you need to set up your machine for the first time please take a look
at :ref:`Sections/01_Installation/05_Additional_configuration:Additional Configuration`
Section for a detailed description of the additional configuration.
