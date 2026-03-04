#!/usr/bin/env bash

sudo rpm -iUvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
sudo yum -y update
sudo yum install java-1.11.0-openjdk java-1.11.0-openjdk-devel graphviz xdg-utils libtool \
                 automake python3 python3-libs python3-pip python3-devel python3-decorator \
                 boost-devel boost-serialization boost-iostreams libxml2 libxml2-devel gcc \
                 gcc-c++ gcc-gfortran tcsh @development-tools redhat-rpm-config papi
sudo pip install decorator
export JAVA_HOME=$(dirname $(dirname $(readlink -f $(which javac))))
echo $JAVA_HOME >> ~/.bashrc
echo 'export GRADLE_HOME=/opt/gradle-8.7' >> ~/.bashrc
export GRADLE_HOME=/opt/gradle-8.7
echo 'export PATH=/opt/gradle-8.7/bin:$PATH' >> ~/.bashrc
export PATH=/opt/gradle-8.7/bin:$PATH