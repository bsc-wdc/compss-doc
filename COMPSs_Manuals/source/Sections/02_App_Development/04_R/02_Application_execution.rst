Application Execution
---------------------

The next subsections describe how to execute applications with the
COMPSs R binding.

Environment
~~~~~~~~~~~

The following environment variables must be defined before executing a
COMPSs Python application:

JAVA_HOME
    Java JDK installation directory (e.g. ``/usr/lib/jvm/java-11-openjdk/``)

Command
~~~~~~~

In order to run a R application with COMPSs, the ``runcompss`` script
can be used, like for Java, C/C++ and Python applications. An example of an
invocation of the script is:

.. code-block:: console

    compss@bsc:~$ runcompss \
                    --lang=r \
                    $TEST_DIR/application.R arg1 arg2

.. IMPORTANT::

    The ``runcompss`` command is able to detect the application language
    for Java, C/C++ and Python applications, but not for R applications.

    Consequently, the ``--lang=r`` is mandatory.


For full description about the options available for the runcompss
command please check the :ref:`Sections/03_Execution_Environments/03_Deployments/01_Master_worker/01_Local/01_Executing:Executing COMPSs applications` Section.
