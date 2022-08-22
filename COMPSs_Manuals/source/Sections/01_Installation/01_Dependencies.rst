Dependencies
============

Next we provide a list of dependencies for installing COMPSs package.
The exact names may vary depending on the Linux distribution but this
list provides a general overview of the COMPSs dependencies. For
specific information about your distribution please check the *Depends*
section at your package manager (apt, yum, zypper, etc.).

.. table:: COMPSs dependencies
    :name: COMPSs_dependencies

    +-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
    | Module                  | Dependencies                                                                                                                                 |
    +=========================+==============================================================================================================================================+
    | **COMPSs Runtime**      | **openjdk-8-jre, graphviz, xdg-utils, openssh-server**                                                                                       |
    +-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
    | COMPSs Python Binding   | libtool, automake, build-essential, python (>=3.6), python3-dev, python3-setuptools                                                          |
    +-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
    | COMPSs C/C++ Binding    | libtool, automake, build-essential, libboost-all-dev, libxml2-dev                                                                            |
    +-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
    | COMPSs Tracing          | libxml2 (>= 2.5), libxml2-dev (>= 2.5), gfortran, papi                                                                                       |
    +-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+

.. TIP::

    For macOS, we strongly recommend to use the `Homebrew package manager <https://brew.sh/>`_, since it includes
    the majority of dependencies needed. In other package managers, such as MacPorts, quite some dependencies
    may be missing as packages, which will force you to have to install them from their source codes.

As an example for some distributions and versions:

.. tabs::

  .. tab:: Ubuntu

    .. tabs::

      .. tab:: 20.04

        **Ubuntu 20.04** dependencies installation commands:

        .. code-block:: console

            $ sudo apt-get install -y openjdk-8-jdk graphviz xdg-utils libtool automake build-essential python python-dev libpython2.7 python3 python3-dev libboost-serialization-dev libboost-iostreams-dev  libxml2 libxml2-dev csh gfortran libgmp3-dev flex bison texinfo python3-pip libpapi-dev
            $ sudo wget https://services.gradle.org/distributions/gradle-5.4.1-bin.zip -O /opt/gradle-5.4.1-bin.zip
            $ sudo unzip /opt/gradle-5.4.1-bin.zip -d /opt


        .. ATTENTION::

            Before installing it is important to have a proper ``JAVA_HOME`` environment
            variable definition. This variable must contain a valid path to a Java JDK
            (as a remark, it must point to a JDK, not JRE).
            So, please, export this variable and include it into your ``.bashrc``:

            .. code-block:: console

                $ echo 'export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/' >> ~/.bashrc
                $ export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/


      .. tab:: 18.04

        **Ubuntu 18.04** dependencies installation commands:

        .. code-block:: console

            $ sudo apt-get install -y openjdk-8-jdk graphviz xdg-utils libtool automake build-essential python python-dev libpython2.7 python3 python3-dev libboost-serialization-dev libboost-iostreams-dev  libxml2 libxml2-dev csh gfortran libgmp3-dev flex bison texinfo python3-pip libpapi-dev
            $ sudo wget https://services.gradle.org/distributions/gradle-5.4.1-bin.zip -O /opt/gradle-5.4.1-bin.zip
            $ sudo unzip /opt/gradle-5.4.1-bin.zip -d /opt

        .. ATTENTION::

            Before installing it is important to have a proper ``JAVA_HOME`` environment
            variable definition. This variable must contain a valid path to a Java JDK
            (as a remark, it must point to a JDK, not JRE).
            So, please, export this variable and include it into your ``.bashrc``:

            .. code-block:: console

                $ echo 'export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/' >> ~/.bashrc
                $ export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/


      .. tab:: 16.04

        **Ubuntu 16.04** dependencies installation commands:

        .. code-block:: console

             $ sudo apt-get install -y openjdk-8-jdk graphviz xdg-utils libtool automake build-essential python2.7 libpython2.7 libboost-serialization-dev libboost-iostreams-dev  libxml2 libxml2-dev csh gfortran python-pip libpapi-dev
             $ sudo wget https://services.gradle.org/distributions/gradle-5.4.1-bin.zip -O /opt/gradle-5.4.1-bin.zip
             $ sudo unzip /opt/gradle-5.4.1-bin.zip -d /opt

        .. ATTENTION::

            Before installing it is important to have a proper ``JAVA_HOME`` environment
            variable definition. This variable must contain a valid path to a Java JDK
            (as a remark, it must point to a JDK, not JRE).
            So, please, export this variable and include it into your ``.bashrc``:

            .. code-block:: console

                $ echo 'export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/' >> ~/.bashrc
                $ export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/


  .. tab:: OpenSuse

    .. tabs::

      .. tab:: Tumbleweed

        **OpenSuse Tumbleweed** dependencies installation commands:

        .. code-block:: console

            $ sudo zypper install --type pattern -y devel_basis
            $ sudo zypper install -y java-1_8_0-openjdk-headless java-1_8_0-openjdk java-1_8_0-openjdk-devel graphviz xdg-utils python python-devel python3 python3-devel python3-decorator libtool automake libboost_headers1_71_0-devel libboost_serialization1_71_0 libboost_iostreams1_71_0  libxml2-2 libxml2-devel tcsh gcc-fortran papi libpapi gcc-c++ libpapi papi papi-devel gmp-devel
            $ sudo wget https://services.gradle.org/distributions/gradle-5.4.1-bin.zip -O /opt/gradle-5.4.1-bin.zip
            $ sudo unzip /opt/gradle-5.4.1-bin.zip -d /opt

        .. ATTENTION::

            Before installing it is important to have a proper ``JAVA_HOME`` environment
            variable definition. This variable must contain a valid path to a Java JDK
            (as a remark, it must point to a JDK, not JRE).
            So, please, export this variable and include it into your ``.bashrc``:

            .. code-block:: console

                $ echo 'export JAVA_HOME=/usr/lib64/jvm/java-1.8.0-openjdk/' >> ~/.bashrc
                $ export JAVA_HOME=/usr/lib64/jvm/java-1.8.0-openjdk/


      .. tab:: Leap 15.X

        **OpenSuse Leap 15.X** dependencies installation commands:

        .. code-block:: console

            $ sudo zypper install --type pattern -y devel_basis
            $ sudo zypper install -y java-1_8_0-openjdk-headless java-1_8_0-openjdk java-1_8_0-openjdk-devel graphviz xdg-utils python python-devel python-decorator python3 python3-devel python3-decorator libtool automake libboost_headers1_66_0-devel libboost_serialization1_66_0 libboost_iostreams1_66_0  libxml2-2 libxml2-devel tcsh gcc-fortran papi libpapi gcc-c++ libpapi papi papi-devel gmp-devel
            $ sudo wget https://services.gradle.org/distributions/gradle-5.4.1-bin.zip -O /opt/gradle-5.4.1-bin.zip
            $ sudo unzip /opt/gradle-5.4.1-bin.zip -d /opt

        .. ATTENTION::

            Before installing it is important to have a proper ``JAVA_HOME`` environment
            variable definition. This variable must contain a valid path to a Java JDK
            (as a remark, it must point to a JDK, not JRE).
            So, please, export this variable and include it into your ``.bashrc``:

            .. code-block:: console

                $ echo 'export JAVA_HOME=/usr/lib64/jvm/java-1.8.0-openjdk/' >> ~/.bashrc
                $ export JAVA_HOME=/usr/lib64/jvm/java-1.8.0-openjdk/


      .. tab:: 42.2

        **OpenSuse 42.2** dependencies installation commands:

        .. code-block:: console

            $ sudo zypper install --type pattern -y devel_basis
            $ sudo zypper install -y java-1_8_0-openjdk-headless java-1_8_0-openjdk java-1_8_0-openjdk-devel graphviz xdg-utils python python-devel libpython2_7-1_0 python-decorator libtool automake boost-devel libboost_serialization1_54_0 libboost_iostreams1_54_0 libxml2-2 libxml2-devel tcsh gcc-fortran python-pip papi libpapi gcc-c++ libpapi papi papi-devel gmp-devel
            $ sudo wget https://services.gradle.org/distributions/gradle-5.4.1-bin.zip -O /opt/gradle-5.4.1-bin.zip
            $ sudo unzip /opt/gradle-5.4.1-bin.zip -d /opt

        .. WARNING::

            OpenSuse provides Python 3.4 from its repositories, which is not supported
            by the COMPSs python binding.
            Please, update Python 3 (``python`` and ``python-devel``) to a higher
            version if you expect to install COMPSs from sources.

            Alternatively, you can use a virtual environment.

        .. ATTENTION::

            Before installing it is important to have a proper ``JAVA_HOME`` environment
            variable definition. This variable must contain a valid path to a Java JDK
            (as a remark, it must point to a JDK, not JRE).
            So, please, export this variable and include it into your ``.bashrc``:

            .. code-block:: console

                $ echo 'export JAVA_HOME=/usr/lib64/jvm/java-1.8.0-openjdk/' >> ~/.bashrc
                $ export JAVA_HOME=/usr/lib64/jvm/java-1.8.0-openjdk/


  .. tab:: Fedora

    .. tabs::

      .. tab:: 32

        **Fedora 32** dependencies installation commands:

        .. code-block:: console

             $ sudo dnf install -y java-1.8.0-openjdk java-1.8.0-openjdk-devel graphviz xdg-utils libtool automake python27 python3 python3-devel boost-devel boost-serialization boost-iostreams libxml2 libxml2-devel gcc gcc-c++ gcc-gfortran tcsh @development-tools bison flex texinfo papi papi-devel gmp-devel
             $ # If the libxml softlink is not created during the installation of libxml2, the COMPSs installation may fail.
             $ # In this case, the softlink has to be created manually with the following command:
             $ sudo ln -s /usr/include/libxml2/libxml/ /usr/include/libxml
             $ sudo wget https://services.gradle.org/distributions/gradle-5.4.1-bin.zip -O /opt/gradle-5.4.1-bin.zip
             $ sudo unzip /opt/gradle-5.4.1-bin.zip -d /opt

        .. ATTENTION::

            Before installing it is important to have a proper ``JAVA_HOME`` environment
            variable definition. This variable must contain a valid path to a Java JDK
            (as a remark, it must point to a JDK, not JRE).
            So, please, export this variable and include it into your ``.bashrc``:

            .. code-block:: console

                $ echo 'export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk/' >> ~/.bashrc
                $ export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk/


      .. tab:: 25

        **Fedora 25** dependencies installation commands:

        .. code-block:: console

             $ sudo dnf install -y java-1.8.0-openjdk java-1.8.0-openjdk-devel graphviz xdg-utils libtool automake python python-libs python-pip python-devel python2-decorator boost-devel boost-serialization boost-iostreams libxml2 libxml2-devel gcc gcc-c++ gcc-gfortran tcsh @development-tools redhat-rpm-config papi
             $ # If the libxml softlink is not created during the installation of libxml2, the COMPSs installation may fail.
             $ # In this case, the softlink has to be created manually with the following command:
             $ sudo ln -s /usr/include/libxml2/libxml/ /usr/include/libxml
             $ sudo wget https://services.gradle.org/distributions/gradle-5.4.1-bin.zip -O /opt/gradle-5.4.1-bin.zip
             $ sudo unzip /opt/gradle-5.4.1-bin.zip -d /opt

        .. ATTENTION::

            Before installing it is important to have a proper ``JAVA_HOME`` environment
            variable definition. This variable must contain a valid path to a Java JDK
            (as a remark, it must point to a JDK, not JRE).
            So, please, export this variable and include it into your ``.bashrc``:

            .. code-block:: console

                $ echo 'export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk/' >> ~/.bashrc
                $ export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk/


  .. tab:: Debian

    .. tabs::

      .. tab:: 8

        **Debian 8** dependencies installation commands:

        .. code-block:: console

              $ su -
              $ echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee /etc/apt/sources.list.d/webupd8team-java.list
              $ echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list
              $ apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886
              $ apt-get update
              $ apt-get install oracle-java8-installer
              $ apt-get install graphviz xdg-utils libtool automake build-essential python python-decorator python-pip python-dev libboost-serialization1.55.0 libboost-iostreams1.55.0 libxml2 libxml2-dev libboost-dev csh gfortran papi-tools
              $ wget https://services.gradle.org/distributions/gradle-5.4.1-bin.zip -O /opt/gradle-5.4.1-bin.zip
              $ unzip /opt/gradle-5.4.1-bin.zip -d /opt

        .. ATTENTION::

            Before installing it is important to have a proper ``JAVA_HOME`` environment
            variable definition. This variable must contain a valid path to a Java JDK
            (as a remark, it must point to a JDK, not JRE). A possible value is the following:

            .. code-block:: console

                $ echo $JAVA_HOME
                /usr/lib64/jvm/java-openjdk/

            So, please, check its location, export this variable and include it into your ``.bashrc``
            if it is not already available with the previous command.

            .. code-block:: console

                $ echo 'export JAVA_HOME=/usr/lib64/jvm/java-openjdk/' >> ~/.bashrc
                $ export JAVA_HOME=/usr/lib64/jvm/java-openjdk/


  .. tab:: CentOS

    .. tabs::

      .. tab:: 7

        **CentOS 7** dependencies installation commands:

        .. code-block:: console

            $ sudo rpm -iUvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
            $ sudo yum -y update
            $ sudo yum install java-1.8.0-openjdk java-1.8.0-openjdk-devel graphviz xdg-utils libtool automake python python-libs python-pip python-devel python2-decorator boost-devel boost-serialization boost-iostreams libxml2 libxml2-devel gcc gcc-c++ gcc-gfortran tcsh @development-tools redhat-rpm-config papi
            $ sudo pip install decorator

        .. ATTENTION::

            Before installing it is important to have a proper ``JAVA_HOME`` environment
            variable definition. This variable must contain a valid path to a Java JDK
            (as a remark, it must point to a JDK, not JRE). A possible value is the following:

            .. code-block:: console

                $ echo $JAVA_HOME
                /usr/lib64/jvm/java-openjdk/

            So, please, check its location, export this variable and include it into your ``.bashrc``
            if it is not already available with the previous command.

            .. code-block:: console

                $ echo 'export JAVA_HOME=/usr/lib64/jvm/java-openjdk/' >> ~/.bashrc
                $ export JAVA_HOME=/usr/lib64/jvm/java-openjdk/

    .. tab-container:: macOS_Monterey
        :title: macOS Monterey

        **macOS Monterey** dependencies installation commands:

        Although many packages can be installed with Homebrew, some of them will have to be installed manually
        from their source files. It is also important to mention that, some package names may be slightly different
        in Homebrew, compared to Linux distributions, thus, some previous search for equivalences may be required.
        Our tested installation sequence was:

        .. code-block:: console

            $ brew install openjdk@8 graphviz libxslt xmlto libtool automake coreutils util-linux boost
            $ sudo ln -sfn /usr/local/opt/openjdk@8/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-8.jdk

        And xdg-utils had to be installed by hand (after installing libxslt and xmlto):

        .. code-block:: console

            $ export XML_CATALOG_FILES="/usr/local/etc/xml/catalog"
            $ git clone git://anongit.freedesktop.org/xdg/xdg-utils
            $ cd xdg-utils
            $ ./configure --prefix=/usr/local
            $ make ; make install

        .. WARNING::
            Tracing is not yet available for macOS, therefore, its dependencies do not need
            to be installed.

.. ATTENTION::

    Before installing it is also necessary to export the ``GRADLE_HOME`` environment
    variable and include its binaries path into the ``PATH`` environment variable:

    .. code-block:: console

        $ echo 'export GRADLE_HOME=/opt/gradle-5.4.1' >> ~/.bashrc
        $ export GRADLE_HOME=/opt/gradle-5.4.1
        $ echo 'export PATH=/opt/gradle-5.4.1/bin:$PATH' >> ~/.bashrc
        $ export PATH=/opt/gradle-5.4.1/bin:$PATH


.. IMPORTANT::

    Python version 3.8 or higher is recommended since some of the Python
    binding features are only supported in these Python versions (e.g.
    worker cache)


Build Dependencies
------------------

To build COMPSs from sources you will also need ``wget``, ``git`` and
``maven`` (`maven web <https://maven.apache.org/>`_).
To install with Pip, ``pip`` for the target Python version is required.


Optional Dependencies
---------------------

For the Python binding it is recommended to have ``dill`` (`dill project <https://pypi.org/project/dill/>`_),
``guppy3`` (`guppy3 project <https://pypi.org/project/guppy3/>`_) and
``numpy`` (`numpy` project <https://pypi.org/project/numpy/>) installed:

* The ``dill`` package increases the variety of serializable objects by Python (for example: lambda functions)
* The ``guppy3`` package is needed to use the ``@local`` decorator.
* The ``numpy`` package is useful to improve the serialization/deserialization performance since its internal mechanisms are used by the Python binding.

These packages can be found in PyPI and can be installed via ``pip``.

Since it is possible to execute python applications using workers spawning
MPI processes instead of multiprocessing, it is necessary to have ``openmpi``,
``openmpi-devel`` and ``openmpi-libs`` system packages installed and ``mpi4py`` with pip.
