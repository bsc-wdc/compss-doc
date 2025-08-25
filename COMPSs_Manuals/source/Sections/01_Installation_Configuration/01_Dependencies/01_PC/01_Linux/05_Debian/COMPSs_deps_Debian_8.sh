#!/usr/bin/env bash

su -
echo "deb http://ppa.launchpad.net/webupd11team/java/ubuntu xenial main" | tee /etc/apt/sources.list.d/webupd11team-java.list
echo "deb-src http://ppa.launchpad.net/webupd11team/java/ubuntu xenial main" | tee -a /etc/apt/sources.list.d/webupd11team-java.list
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886
apt-get update
apt-get install oracle-java11-installer
apt-get install graphviz xdg-utils libtool automake build-essential python3 python3-decorator \
                python3-pip python3-dev libboost-serialization1.55.0 libboost-iostreams1.55.0 \
                libxml2 libxml2-dev libboost-dev csh gfortran papi-tools
wget https://services.gradle.org/distributions/gradle-8.7-bin.zip -O /opt/gradle-8.7-bin.zip
unzip /opt/gradle-8.7-bin.zip -d /opt
export JAVA_HOME=$(dirname $(dirname $(readlink -f $(which javac))))
echo $JAVA_HOME >> ~/.bashrc
echo 'export GRADLE_HOME=/opt/gradle-8.7' >> ~/.bashrc
export GRADLE_HOME=/opt/gradle-8.7
echo 'export PATH=/opt/gradle-8.7/bin:$PATH' >> ~/.bashrc
export PATH=/opt/gradle-8.7/bin:$PATH