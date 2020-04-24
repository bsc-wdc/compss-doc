Dependencies
============

Next we provide a list of dependencies for installing COMPSs package.
The exact names may vary depending on the Linux distribution but this
list provides a general overview of the COMPSs dependencies. For
specific information about your distribution please check the *Depends*
section at your package manager (apt, yum, zypper, etc.).

.. table:: COMPSs dependencies
    :name: COMPSs_dependencies
    :widths: auto

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

    .. tab-container:: Fedora_25
        :title: Fedora 25

        **Fedora 25** dependencies installation command:

        .. code-block:: console

             $ sudo dnf install -y java-1.8.0-openjdk java-1.8.0-openjdk-devel graphviz xdg-utils libtool automake python python-libs python-pip python-devel python2-decorator boost-devel boost-serialization boost-iostreams libxml2 libxml2-devel gcc gcc-c++ gcc-gfortran tcsh @development-tools redhat-rpm-config papi
             $ # If the libxml softlink is not created during the installation of libxml2, the COMPSs installation may fail.
             $ # In this case, the softlink has to be created manually with the following command:
             $ sudo ln -s /usr/include/libxml2/libxml/ /usr/include/libxml

    .. tab-container:: Ubuntu_16_04
        :title: Ubuntu 16.04

        **Ubuntu 16.04** dependencies installation command:

        .. code-block:: console

             $ sudo apt-get install -y openjdk-8-jdk graphviz xdg-utils libtool automake build-essential python2.7 libpython2.7 libboost-serialization-dev libboost-iostreams-dev  libxml2 libxml2-dev csh gfortran python-pip libpapi-dev

    .. tab-container:: Ubuntu_18_04
        :title: Ubuntu 18.04

        **Ubuntu 18.04** dependencies installation command:

        .. code-block:: console

             $ sudo apt-get install -y openjdk-8-jdk graphviz xdg-utils libtool automake build-essential python2.7 libpython2.7 python3 python3-dev libboost-serialization-dev libboost-iostreams-dev  libxml2 libxml2-dev csh gfortran libgmp3-dev flex bison texinfo python3-pip libpapi-dev

    .. tab-container:: OpenSuse_42_2
        :title: OpenSuse 42.2

        **OpenSuse 42.2** dependencies installation command:

        .. code-block:: console

            $ sudo zypper install --type pattern -y devel_basis
            $ sudo zypper install -y java-1_8_0-openjdk-headless java-1_8_0-openjdk java-1_8_0-openjdk-devel graphviz xdg-utils python python-devel libpython2_7-1_0 python-decorator libtool automake boost-devel libboost_serialization1_54_0 libboost_iostreams1_54_0 libxml2-2 libxml2-devel tcsh gcc-fortran python-pip papi libpapi gcc-c++ papi-devel gmp-devel

    .. tab-container:: Debian_8
        :title: Debian 8

        **Debian 8** dependencies installation command:

        .. code-block:: console

              $ su -
              $ echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee /etc/apt/sources.list.d/webupd8team-java.list
              $ echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list
              $ apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886
              $ apt-get update
              $ apt-get install oracle-java8-installer
              $ apt-get install graphviz xdg-utils libtool automake build-essential python python-decorator python-pip python-dev libboost-serialization1.55.0 libboost-iostreams1.55.0 libxml2 libxml2-dev libboost-dev csh gfortran papi-tools

    .. tab-container:: CentOS_7
        :title: CentOS 7

        **CentOS 7** dependencies installation command:

        .. code-block:: console

              $ sudo rpm -iUvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
              $ sudo yum -y update
              $ sudo yum install java-1.8.0-openjdk java-1.8.0-openjdk-devel graphviz xdg-utils libtool automake python python-libs python-pip python-devel python2-decorator boost-devel boost-serialization boost-iostreams libxml2 libxml2-devel gcc gcc-c++ gcc-gfortran tcsh @development-tools redhat-rpm-config papi
              $ sudo pip install decorator


.. ATTENTION::

    Before installing it is important to have a proper ``JAVA_HOME`` environment
    variable definition. This variable must contain a valid path to a Java JDK
    (as a remark, it must point to a JDK, not JRE).
    A possible value is the following:

    .. code-block:: console

          $ echo $JAVA_HOME
          /usr/lib64/jvm/java-openjdk/


Build Dependencies
------------------

To build COMPSs from sources you will also need ``wget``, ``openjdk-8-jdk`` and ``maven``.
And to install with Pip, ``pip`` for the target Python version is required.


Optional Dependencies
---------------------

For the Python binding it is also recommended to have `dill <https://pypi.org/project/dill/>`_ and
`guppy <https://pypi.org/project/guppy/>`_/`guppy3 <https://pypi.org/project/guppy3/>`_ installed.
The ``dill`` package increases the variety of serializable objects by Python
(for example: lambda functions), and the ``guppy`` package is needed to use the
``@local`` decorator. Both packages can be found in pyPI and can be installed via ``pip``.
