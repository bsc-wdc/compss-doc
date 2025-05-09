The following environment variables must be defined before executing a
COMPSs C/C++ application:

JAVA_HOME
   Java JDK installation directory (e.g. /usr/lib/jvm/java-11-openjdk/)

After compiling the application, two directories, master and worker, are
generated. The master directory contains a binary called as the main
file, which is the master application, in our example is called Matmul.
The worker directory contains another binary called as the main file
followed by the suffix "-worker", which is the worker application, in
our example is called Matmul-worker.

The ``runcompss`` script has to be used to run the application:

.. code-block:: console

    $ runcompss /home/compss/tutorial_apps/c/matmul_objects/master/Matmul 3 4 2.0

The complete list of options of the runcompss command is available in
Section :ref:`Sections/03_Execution_Environments/03_Deployments/01_Master_worker/01_Local/01_Executing:Executing COMPSs applications`.
