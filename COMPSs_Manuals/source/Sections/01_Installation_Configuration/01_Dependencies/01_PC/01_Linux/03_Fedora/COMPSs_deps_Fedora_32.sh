#!/usr/bin/env bash

sudo dnf install -y java-1.11.0-openjdk java-1.11.0-openjdk-devel graphviz xdg-utils libtool automake \
                    python3 python3-devel boost-devel boost-serialization boost-iostreams libxml2 \
                    libxml2-devel gcc gcc-c++ gcc-gfortran tcsh @development-tools bison flex texinfo \
                    papi papi-devel gmp-devel
# If the libxml softlink is not created during the installation of libxml2, the COMPSs installation may fail.
# In this case, the softlink has to be created manually with the following command:
sudo ln -s /usr/include/libxml2/libxml/ /usr/include/libxml
sudo wget https://services.gradle.org/distributions/gradle-8.7-bin.zip -O /opt/gradle-8.7-bin.zip
sudo unzip /opt/gradle-8.7-bin.zip -d /opt
export JAVA_HOME=$(dirname $(dirname $(readlink -f $(which javac))))
echo $JAVA_HOME >> ~/.bashrc
echo 'export GRADLE_HOME=/opt/gradle-8.7' >> ~/.bashrc
export GRADLE_HOME=/opt/gradle-8.7
echo 'export PATH=/opt/gradle-8.7/bin:$PATH' >> ~/.bashrc
export PATH=/opt/gradle-8.7/bin:$PATH