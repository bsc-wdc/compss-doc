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
    | COMPSs Python Binding   | libtool, automake, build-essential, python (>= 2.7 \| >=3.5), python-dev \| python3-dev, python-setuptools\|python3-setuptools, libpython2.7 |
    +-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
    | COMPSs C/C++ Binding    | libtool, automake, build-essential, libboost-all-dev, libxml2-dev                                                                            |
    +-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
    | COMPSs Autoparallel     | libgmp3-dev, flex, bison, libbison-dev, texinfo, libffi-dev, astor, sympy, enum34, islpy                                                     |
    +-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
    | COMPSs Tracing          | libxml2 (>= 2.5), libxml2-dev (>= 2.5), gfortran, papi                                                                                       |
    +-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+

As an example for some distributions:

.. content-tabs::

    .. tab-container:: Ubuntu_20_04
        :title: Ubuntu 20.04

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


    .. tab-container:: Ubuntu_18_04
        :title: Ubuntu 18.04

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


    .. tab-container:: Ubuntu_16_04
        :title: Ubuntu 16.04

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


    .. tab-container:: OpenSuse_Tumbleweed
        :title: OpenSuse Tumbleweed

        **OpenSuse Tumbleweed** dependencies installation commands:

        .. code-block:: console

            $ sudo zypper install --type pattern -y devel_basis
            $ sudo zypper install -y java-1_8_0-openjdk-headless java-1_8_0-openjdk java-1_8_0-openjdk-devel graphviz xdg-utils python python-devel python3 python3-devel python3-decorator libtool automake libboost_headers1_71_0-devel libboost_serialization1_71_0 libboost_iostreams1_71_0  libxml2-2 libxml2-devel tcsh gcc-fortran papi libpapi gcc-c++ papi-devel gmp-devel
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


    .. tab-container:: OpenSuse_Leap_15_1
        :title: OpenSuse Leap 15.1

        **OpenSuse Leap 15.1** dependencies installation commands:

        .. code-block:: console

            $ sudo zypper install --type pattern -y devel_basis
            $ sudo zypper install -y java-1_8_0-openjdk-headless java-1_8_0-openjdk java-1_8_0-openjdk-devel graphviz xdg-utils python python-devel python-decorator python3 python3-devel python3-decorator libtool automake libboost_headers1_66_0-devel libboost_serialization1_66_0 libboost_iostreams1_66_0  libxml2-2 libxml2-devel tcsh gcc-fortran papi libpapi gcc-c++ papi-devel gmp-devel
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


    .. tab-container:: OpenSuse_42_2
        :title: OpenSuse 42.2

        **OpenSuse 42.2** dependencies installation commands:

        .. code-block:: console

            $ sudo zypper install --type pattern -y devel_basis
            $ sudo zypper install -y java-1_8_0-openjdk-headless java-1_8_0-openjdk java-1_8_0-openjdk-devel graphviz xdg-utils python python-devel libpython2_7-1_0 python-decorator libtool automake boost-devel libboost_serialization1_54_0 libboost_iostreams1_54_0 libxml2-2 libxml2-devel tcsh gcc-fortran python-pip papi libpapi gcc-c++ papi-devel gmp-devel
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


    .. tab-container:: Fedora_32
        :title: Fedora 32

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


    .. tab-container:: Fedora_25
        :title: Fedora 25

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


    .. tab-container:: Debian_8
        :title: Debian 8

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


    .. tab-container:: CentOS_7
        :title: CentOS 7

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


.. ATTENTION::

    Before installing it is also necessary to export the ``GRADLE_HOME`` environment
    variable and include its binaries path into the ``PATH`` environment variable:

    .. code-block:: console

        $ echo 'export GRADLE_HOME=/opt/gradle-5.4.1' >> ~/.bashrc
        $ export GRADLE_HOME=/opt/gradle-5.4.1
        $ echo 'export PATH=/opt/gradle-5.4.1/bin:$PATH' >> ~/.bashrc
        $ export PATH=/opt/gradle-5.4.1/bin:$PATH


Build Dependencies
------------------

To build COMPSs from sources you will also need ``wget``, ``git`` and ``maven``.

To install with Pip, ``pip`` for the target Python version is required.


Optional Dependencies
---------------------

For the Python binding it is also recommended to have `dill <https://pypi.org/project/dill/>`_ and
`guppy <https://pypi.org/project/guppy/>`_/`guppy3 <https://pypi.org/project/guppy3/>`_ installed.
The ``dill`` package increases the variety of serializable objects by Python
(for example: lambda functions), and the ``guppy``/``guppy3`` package is needed to use the
``@local`` decorator. Both packages can be found in pyPI and can be installed via ``pip``.
