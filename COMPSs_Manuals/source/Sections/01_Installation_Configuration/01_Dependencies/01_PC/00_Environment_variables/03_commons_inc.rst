.. It is also necessary to export the ``GRADLE_HOME`` environment variable and
   include its binaries path into the ``PATH`` environment variable:

$ echo 'export GRADLE_HOME=/opt/gradle-8.7' >> ~/.bashrc
$ export GRADLE_HOME=/opt/gradle-8.7
$ echo 'export PATH=/opt/gradle-8.7/bin:$PATH' >> ~/.bashrc
$ export PATH=/opt/gradle-8.7/bin:$PATH