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

In order to run a Python application with COMPSs, the ``runcompss`` script
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

.. TIP::

    The ``runcompss`` command is able to detect the application language.
    Consequently, the ``--lang=python`` is not mandatory.

.. TIP::

    The ``--pythonpath`` flag enables the user to add directories to the
    ``PYTHONPATH`` environment variable and export them into the workers, so
    that the tasks can resolve successfully its imports.

.. TIP::

    PyCOMPSs applications can also be launched without parallelization
    (as a common python script) by avoiding the ``-m pycompss`` and its flags
    when using ``python``:

    .. code-block:: console

        compss@bsc:~$ python $TEST_DIR/application.py arg1 arg2

    The main limitation is that the application must only contain ``@task``,
    ``@binary`` and/or ``@mpi`` decorators and PyCOMPSs needs to be installed.



For full description about the options available for the runcompss
command please check the :ref:`Sections/03_Execution_Environments/01_Local/01_Executing:Executing COMPSs applications` Section.
