Pip
===

Pre-requisites
--------------

In order to be able to install COMPSs and PyCOMPSs with Pip the
following requirements must be met:

#. Have all the dependencies (excluding the COMPSs packages) mentioned
   in the :ref:`Dependencies` Section satisfied and Python
   ``pip``. As an example for some distributions:

   **Fedora 25** dependencies installation command:

   .. code-block:: console

              $ sudo dnf install -y java-1.8.0-openjdk java-1.8.0-openjdk-devel graphviz xdg-utils libtool automake python python-libs python-pip python-devel python2-decorator boost-devel boost-serialization boost-iostreams libxml2 libxml2-devel gcc gcc-c++ gcc-gfortran tcsh @development-tools redhat-rpm-config papi
              $ # If the libxml softlink is not created during the installation of libxml2, the COMPSs installation may fail.
              $ # In this case, the softlink has to be created manually with the following command:
              $ sudo ln -s /usr/include/libxml2/libxml/ /usr/include/libxml


   **Ubuntu 16.04** dependencies installation command:

   .. code-block:: console

              $ sudo apt-get install -y openjdk-8-jdk graphviz xdg-utils libtool automake build-essential python2.7 libpython2.7 libboost-serialization-dev libboost-iostreams-dev  libxml2 libxml2-dev csh gfortran python-pip libpapi-dev


   **Ubuntu 18.04** dependencies installation command:

   .. code-block:: console

              $ sudo apt-get install -y openjdk-8-jdk graphviz xdg-utils libtool automake build-essential python2.7 libpython2.7 python3 python3-dev libboost-serialization-dev libboost-iostreams-dev  libxml2 libxml2-dev csh gfortran libgmp3-dev flex bison texinfo python3-pip libpapi-dev


   **OpenSuse 42.2** dependencies installation command:

   .. code-block:: console

              $ sudo zypper install --type pattern -y devel_basis
              $ sudo zypper install -y java-1_8_0-openjdk-headless java-1_8_0-openjdk java-1_8_0-openjdk-devel graphviz xdg-utils python python-devel libpython2_7-1_0 python-decorator libtool automake  boost-devel libboost_serialization1_54_0 libboost_iostreams1_54_0  libxml2-2 libxml2-devel tcsh gcc-fortran python-pip papi libpapi


   **Debian 8** dependencies installation command:

   .. code-block:: console

               $ su -
               $ echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee /etc/apt/sources.list.d/webupd8team-java.list
               $ echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list
               $ apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886
               $ apt-get update
               $ apt-get install oracle-java8-installer
               $ apt-get install graphviz xdg-utils libtool automake build-essential python python-decorator python-pip python-dev libboost-serialization1.55.0 libboost-iostreams1.55.0 libxml2 libxml2-dev libboost-dev csh gfortran papi-tools


   **CentOS 7** dependencies installation command:

   .. code-block:: console

               $ sudo rpm -iUvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
               $ sudo yum -y update
               $ sudo yum install java-1.8.0-openjdk java-1.8.0-openjdk-devel graphviz xdg-utils libtool automake python python-libs python-pip python-devel python2-decorator boost-devel boost-serialization boost-iostreams libxml2 libxml2-devel gcc gcc-c++ gcc-gfortran tcsh @development-tools redhat-rpm-config papi
               $ sudo pip install decorator


#. Have a proper ``JAVA_HOME`` environment variable definition. This
   variable must contain a valid path to a Java JDK (as a remark, it
   must point to a JDK, not JRE). A possible value is the following:

   .. code-block:: console

         $ echo $JAVA_HOME
         /usr/lib64/jvm/java-openjdk/

Installation
------------

Depending on the machine, the installation command may vary. Some of the
possible scenarios and their proper installation command are:

#. Install systemwide:

   .. code-block:: console

        $ sudo -E pip install pycompss -v


   It is recommended to restart the user session once the installation
   process has finished. Alternatively, the following command sets all
   the COMPSs environment.

   .. code-block:: console

       $ source /etc/profile.d/compss.sh

   However, this command should be executed in every different terminal
   during the current user session.

#. Install in user home folder (.local):

   .. code-block:: console

        $ pip install pycompss -v


   It is recommended to restart the user session once the installation
   process has finished. Alternatively, the following command sets all
   the COMPSs environment.

   .. code-block:: console

       $ source ~/.bashrc

#. Within a Python virtual environment:

   .. code-block:: console

        $ pip install pycompss -v

   In this particular case, the installation includes the necessary
   variables in the activate script. So, restart the virtual environment
   in order to set all the COMPSs environment.

Configuration (using pip)
-------------------------

The steps mentioned in Section :ref:`Configure SSH passwordless` must be done
in order to have a functional COMPSs and PyCOMPSs installation.

Post installation (using pip)
-----------------------------

As mentioned in :ref:`Configure SSH passwordless` Section, it is recommended to
restart the user session or virtual environment once the installation
process has finished.
