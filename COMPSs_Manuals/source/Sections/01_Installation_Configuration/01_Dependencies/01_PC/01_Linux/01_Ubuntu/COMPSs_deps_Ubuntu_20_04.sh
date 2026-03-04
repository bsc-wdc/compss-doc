#!/usr/bin/env bash

sudo apt-get install -y openjdk-11-jdk graphviz xdg-utils libtool automake build-essential \
                        python3 python3-dev python3-pip libboost-serialization-dev libboost-iostreams-dev \
                        libxml2 libxml2-dev csh gfortran libgmp3-dev flex bison texinfo \
                        libpapi-dev
sudo wget https://services.gradle.org/distributions/gradle-8.7-bin.zip -O /opt/gradle-8.7-bin.zip
sudo unzip /opt/gradle-8.7-bin.zip -d /opt
export JAVA_HOME=$(dirname $(dirname $(readlink -f $(which javac))))
echo $JAVA_HOME >> ~/.bashrc
echo 'export GRADLE_HOME=/opt/gradle-8.7' >> ~/.bashrc
export GRADLE_HOME=/opt/gradle-8.7
echo 'export PATH=/opt/gradle-8.7/bin:$PATH' >> ~/.bashrc
export PATH=/opt/gradle-8.7/bin:$PATH