.. Before installing it is important to have a proper ``JAVA_HOME`` environment
   variable definition. This variable must contain a valid path to a **Java JDK**
   (as a remark, it must point to a **JDK**, not JRE).
   So, please, export this variable and include it into your ``.bashrc``:

$ export JAVA_HOME=$(dirname $(dirname $(readlink -f $(which javac))))
$ echo $JAVA_HOME >> ~/.bashrc
