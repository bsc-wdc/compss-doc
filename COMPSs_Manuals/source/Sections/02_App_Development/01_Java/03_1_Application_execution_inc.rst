A Java COMPSs application is executed through the *runcompss* script. An
example of an invocation of the script is:

.. code-block:: console

    $ runcompss --classpath=/home/compss/tutorial_apps/java/simple/jar/simple.jar simple.Simple 1

A comprehensive description of the *runcompss* command is available in
the :ref:`Sections/03_Execution_Environments/01_Master_worker/01_Local/01_Executing:Executing COMPSs applications` section.  

In addition to Java, COMPSs supports the execution of applications
written in other languages by means of bindings. A binding manages the
interaction of the no-Java application with the COMPSs Java runtime,
providing the necessary language translation.
