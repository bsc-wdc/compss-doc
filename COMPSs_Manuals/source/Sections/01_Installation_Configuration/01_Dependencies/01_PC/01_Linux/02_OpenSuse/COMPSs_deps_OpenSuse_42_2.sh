#!/usr/bin/env bash

sudo zypper install --type pattern -y devel_basis
sudo zypper install -y java-1_11_0-openjdk-headless java-1_11_0-openjdk java-1_11_0-openjdk-devel \
                       graphviz xdg-utils python3 python3-devel python3-decorator libtool automake \
                       boost-devel libboost_serialization1_54_0 libboost_iostreams1_54_0 libxml2-2 \
                       libxml2-devel tcsh gcc-fortran python-pip papi libpapi gcc-c++ libpapi papi \
                       papi-devel gmp-devel
sudo wget https://services.gradle.org/distributions/gradle-8.7-bin.zip -O /opt/gradle-8.7-bin.zip
sudo unzip /opt/gradle-8.7-bin.zip -d /opt
export JAVA_HOME=$(dirname $(dirname $(readlink -f $(which javac))))
echo $JAVA_HOME >> ~/.bashrc
echo 'export GRADLE_HOME=/opt/gradle-8.7' >> ~/.bashrc
export GRADLE_HOME=/opt/gradle-8.7
echo 'export PATH=/opt/gradle-8.7/bin:$PATH' >> ~/.bashrc
export PATH=/opt/gradle-8.7/bin:$PATH