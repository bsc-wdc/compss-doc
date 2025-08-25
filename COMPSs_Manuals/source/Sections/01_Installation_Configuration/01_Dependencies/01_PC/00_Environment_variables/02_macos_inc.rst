$ export JAVA_HOME=$(dirname $(readlink $(which javac)))/java_home
$ echo $JAVA_HOME >> ~/.bashrc
