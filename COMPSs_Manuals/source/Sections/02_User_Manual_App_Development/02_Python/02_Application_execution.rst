Application Execution
---------------------

The next subsections describe how to execute applications with the
COMPSs Python binding.

Environment
~~~~~~~~~~~

The following environment variables must be defined before executing a
COMPSs Python application:

JAVA_HOME
    Java JDK installation directory (e.g. ``/usr/lib/jvm/java-8-openjdk/``)

Command
~~~~~~~

In order to run a Python application with COMPSs, the runcompss script
can be used, like for Java and C/C++ applications. An example of an
invocation of the script is:

.. code-block:: console

    compss@bsc:~$ runcompss \
                    --lang=python \
                    --pythonpath=$TEST_DIR \
                    $TEST_DIR/application.py arg1 arg2

Or alternatively, use the ``pycompss`` module:

.. code-block:: console

    compss@bsc:~$ python -m pycompss \
                    --pythonpath=$TEST_DIR \
                    $TEST_DIR/application.py arg1 arg2

For full description about the options available for the runcompss
command please check the :ref:`Sections/03_User_Manual_App_Exec/01_Executing:Executing COMPSs applications` Section.
