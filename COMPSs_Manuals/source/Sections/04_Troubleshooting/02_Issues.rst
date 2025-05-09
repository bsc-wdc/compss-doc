Common Issues
=============

Tasks are not executed
----------------------

If the tasks remain in **Blocked** state probably there are no existing
resources matching the specific task constraints. This error can be
potentially caused by two facts: the resources are not correctly loaded
into the runtime, or the task constraints do not match with any
resource.

In the first case, users should take a look at the ``resouces.log`` and
check that all the resources defined in the ``project.xml`` file are
available to the runtime. In the second case users should re-define the
task constraints taking into account the resources capabilities defined
into the ``resources.xml`` and ``project.xml`` files.

Jobs fail
---------

If all the application's tasks fail because all the submitted jobs fail,
it is probably due to the fact that there is a resource
miss-configuration. In most of the cases, the resource that the
application is trying to access has no passwordless access through the
configured user. This can be checked by:

-  Open the ``project.xml``. (The default file is stored under
   ``/opt/COMPSs/ Runtime/configuration/xml/projects/project.xml``)

-  For each resource annotate its name and the value inside the ``User``
   tag. Remember that if there is no ``User`` tag COMPSs will try to
   connect this resource with the same username than the one that
   launches the main application.

-  For each annotated resourceName - user please try
   ``ssh user@resourceName``. If the connection asks for a password then
   there is an error in the configuration of the ssh access in the
   resource.

The problem can be solved running the following commands:

.. code-block:: console

    compss@bsc:~$ scp ~/.ssh/id_rsa.pub user@resourceName:./myRSA.pub
    compss@bsc:~$ ssh user@resourceName "cat myRSA.pub >> ~/.ssh/authorized_keys; rm ./myRSA.pub"

These commands are a quick solution, for further details please check
the :ref:`Sections/01_Installation/05_Additional_configuration:Additional Configuration` Section.


Exceptions when starting the Worker processes
---------------------------------------------

When the COMPSs master is not able to communicate with one of the COMPSs
workers described in the `project.xml` and `resources.xml` files, different
exceptions can be raised and logged on the `runtime.log` of the application.
All of them are raised during the worker start up and contain the
*[WorkerStarter]* prefix. Next we provide a list with the common
exceptions:

InitNodeException
    Exception raised when the remote SSH process to start the worker has failed.

UnstartedNodeException
    Exception raised when the worker process has aborted.

Connection refused
    Exception raised when the master cannot communicate with the worker process (NIO).

All these exceptions encapsulate an error when starting the worker process.
This means that **the worker machine is not properly configured** and thus,
you need to check the environment of the failing worker. Further information
about the specific error can be found on the worker log, available at the
working directory path in the remote worker machine (the worker working
directory specified in the `project.xml`}
file).

Next, we list the most common errors and their solutions:

java command not found
    Invalid path to the java binary. Check the `JAVA_HOME` definition at the
    remote worker machine.

Cannot create WD
    Invalid working directory. Check the rw permissions of the worker's working
    directory.

No exception
    The worker process has started normally and there is no exception.
    In this case the issue is normally due to the firewall configuration
    preventing the communication between the COMPSs master and worker.
    Please check that the worker firewall has in and out permissions for TCP
    and UDP in the adaptor ports (the adaptor ports are specified in the
    ``resources.xml`` file. By default the port rank is 43000-44000.


Compilation error: @Method not found
------------------------------------

When trying to compile Java applications users can get some of the
following compilation errors:

.. code-block:: text

    error: package es.bsc.compss.types.annotations does not exist
    import es.bsc.compss.types.annotations.Constraints;
                                              ^
    error: package es.bsc.compss.types.annotations.task does not exist
    import es.bsc.compss.types.annotations.task.Method;
                                              ^
    error: package es.bsc.compss.types.annotations does not exist
    import es.bsc.compss.types.annotations.Parameter;
                                              ^
    error: package es.bsc.compss.types.annotations.Parameter does not exist
    import es.bsc.compss.types.annotations.parameter.Direction;
                                                        ^
    error: package es.bsc.compss.types.annotations.Parameter does not exist
    import es.bsc.compss.types.annotations.parameter.Type;
                                                        ^
    error: cannot find symbol
    @Parameter(type = Type.FILE, direction = Direction.INOUT)
    ^
      symbol:   class Parameter
      location: interface APPLICATION_Itf

    error: cannot find symbol
    @Constraints(computingUnits = "2")
    ^
      symbol:   class Constraints
      location: interface APPLICATION_Itf

    error: cannot find symbol
    @Method(declaringClass = "application.ApplicationImpl")
    ^
      symbol:   class Method
      location: interface APPLICATION_Itf

All these errors are raised because the ``compss-engine.jar`` is not
listed in the CLASSPATH. The default COMPSs installation automatically
inserts this package into the CLASSPATH but it may have been overwritten
or deleted. Please check that your environment variable CLASSPATH
contains the ``compss-engine.jar`` location by running the following
command:

.. code-block:: console

    $ echo $CLASSPATH | grep compss-engine

If the result of the previous command is empty it means that you are
missing the ``compss-engine.jar`` package in your CLASSPATH.

The easiest solution is to manually export the CLASSPATH variable into
the user session:

.. code-block:: console

    $ export CLASSPATH=$CLASSPATH:/opt/COMPSs/Runtime/compss-engine.jar

However, you will need to remember to export this variable every time
you log out and back in again. Consequently, we recommend to add this
export to the ``.bashrc`` file:

.. code-block:: console

    $ echo "# COMPSs variables for Java compilation" >> ~/.bashrc
    $ echo "export CLASSPATH=$CLASSPATH:/opt/COMPSs/Runtime/compss-engine.jar" >> ~/.bashrc

.. warning::
   The ``compss-engine.jar`` is installed inside the COMPSs
   installation directory. If you have performed a custom installation,
   the path of the package may be different.


Jobs failed on method reflection
--------------------------------

When executing an application the main code gets stuck executing a task.
Taking a look at the ``runtime.log`` users can check that the job
associated to the task has failed (and all its resubmissions too). Then,
opening the ``jobX_NEW.out`` or the ``jobX_NEW.err`` files users find
the following error:

.. code-block:: text

    [ERROR|es.bsc.compss.Worker|Executor] Can not get method by reflection
    es.bsc.compss.nio.worker.executors.Executor$JobExecutionException: Can not get method by reflection
            at es.bsc.compss.nio.worker.executors.JavaExecutor.executeTask(JavaExecutor.java:142)
            at es.bsc.compss.nio.worker.executors.Executor.execute(Executor.java:42)
            at es.bsc.compss.nio.worker.JobLauncher.executeTask(JobLauncher.java:46)
            at es.bsc.compss.nio.worker.JobLauncher.processRequests(JobLauncher.java:34)
            at es.bsc.compss.util.RequestDispatcher.run(RequestDispatcher.java:46)
            at java.lang.Thread.run(Thread.java:745)
    Caused by: java.lang.NoSuchMethodException: simple.Simple.increment(java.lang.String)
            at java.lang.Class.getMethod(Class.java:1678)
            at es.bsc.compss.nio.worker.executors.JavaExecutor.executeTask(JavaExecutor.java:140)
            ... 5 more

This error is due to the fact that COMPSs cannot find one of the tasks
declared in the Java Interface. Commonly this is triggered by one of the
following errors:

-  The *declaringClass* of the tasks in the Java Interface has not been
   correctly defined.

-  The parameters of the tasks in the Java Interface do not match the
   task call.

-  The tasks have not been defined as *public*.

Jobs failed on reflect target invocation null pointer
-----------------------------------------------------

When executing an application the main code gets stuck executing a task.
Taking a look at the ``runtime.log`` users can check that the job
associated to the task has failed (and all its resubmissions too). Then,
opening the ``jobX_NEW.out`` or the ``jobX_NEW.err`` files users find
the following error:

.. code-block:: text

    [ERROR|es.bsc.compss.Worker|Executor]
    java.lang.reflect.InvocationTargetException
            at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
            at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
            at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
            at java.lang.reflect.Method.invoke(Method.java:606)
            at es.bsc.compss.nio.worker.executors.JavaExecutor.executeTask(JavaExecutor.java:154)
            at es.bsc.compss.nio.worker.executors.Executor.execute(Executor.java:42)
            at es.bsc.compss.nio.worker.JobLauncher.executeTask(JobLauncher.java:46)
            at es.bsc.compss.nio.worker.JobLauncher.processRequests(JobLauncher.java:34)
            at es.bsc.compss.util.RequestDispatcher.run(RequestDispatcher.java:46)
            at java.lang.Thread.run(Thread.java:745)
    Caused by: java.lang.NullPointerException
            at simple.Ll.printY(Ll.java:25)
            at simple.Simple.task(Simple.java:72)
            ... 10 more

This cause of this error is that the Java object accessed by the task
has not been correctly transferred and one or more of its fields is
null. The transfer failure is normally caused because the transferred
object is not serializable.

Users should check that all the object parameters in the task are either
implementing the serializable interface or following the *java beans*
model (by implementing an empty constructor and getters and setters for
each attribute).

Tracing merge failed: too many open files
-----------------------------------------

When too many nodes and threads are instrumented, the tracing merge can
fail due to an OS limitation, namely: the maximum open files. This
problem usually happens when using advanced mode due to the larger
number of threads instrumented. To overcome this issue users have two
choices. **First option**, use *Extrae* parallel MPI merger. This merger
is automatically used if COMPSs was installed with MPI support. In
Ubuntu you can install the following packets to get MPI support:

.. code-block:: console

    $ sudo apt-get install libcr-dev mpich2 mpich2-doc

Please note that Extrae is never compiled with MPI support when building
it locally (with buildlocal command).

To check if COMPSs was deployed with MPI support, you can check the
installation log and look for the following *Extrae* configuration
output:

.. code-block:: text

    Package configuration for Extrae VERSION based on extrae/trunk rev. 3966:
    -----------------------
    Installation prefix: /gpfs/apps/MN3/COMPSs/Trunk/Dependencies/extrae
    Cross compilation: no
    CC: gcc
    CXX: g++
    Binary type: 64 bits

    MPI instrumentation: yes
    	MPI home: /apps/OPENMPI/1.8.1-mellanox
    	MPI launcher: /apps/OPENMPI/1.8.1-mellanox/bin/mpirun

On the other hand, if you already installed COMPSs, you can check
*Extrae* configuration executing the script
``/opt/COMPSs/Dependencies/extrae/etc/configured.sh``. Users should
check that flags ``--with-mpi=/usr`` and ``--enable-parallel-merge`` are
present and that MPI path is correct and exists. Sample output:

.. code-block:: text

    EXTRAE_HOME is not set. Guessing from the script invoked that Extrae was installed in /opt/COMPSs/Dependencies/extrae
    The directory exists .. OK
    Loaded specs for Extrae from /opt/COMPSs/Dependencies/extrae/etc/extrae-vars.sh

    Extrae SVN branch extrae/trunk at revision 3966

    Extrae was configured with:
    $ ./configure --enable-gettimeofday-clock --without-mpi --without-unwind --without-dyninst --without-binutils --with-mpi=/usr --enable-parallel-merge --with-papi=/usr --with-java-jdk=/usr/lib/jvm/java-7-openjdk-amd64/ --disable-openmp --disable-nanos --disable-smpss --prefix=/opt/COMPSs/Dependencies/extrae --with-mpi=/usr --enable-parallel-merge --libdir=/opt/COMPSs/Dependencies/extrae/lib

    CC was gcc
    CFLAGS was -g -O2 -fno-optimize-sibling-calls -Wall -W
    CXX was g++
    CXXFLAGS was -g -O2 -fno-optimize-sibling-calls -Wall -W

    MPI_HOME points to /usr and the directory exists .. OK
    LIBXML2_HOME points to /usr and the directory exists .. OK
    PAPI_HOME points to /usr and the directory exists .. OK
    DYNINST support seems to be disabled
    UNWINDing support seems to be disabled (or not needed)
    Translating addresses into source code references seems to be disabled (or not needed)

    Please, report bugs to tools@bsc.es

.. IMPORTANT::

    **Disclaimer:** the parallel merge with MPI will not bypass the system's
    maximum number of open files, just distribute the files among the
    resources. If all resources belong to the same machine, the merge will
    fail anyways.

The **second option** is to increase the OS maximum number of open
files. For instance, in Ubuntu add `` ulimit -n 40000 `` just before the
start-stop-daemon line in the do_start section.


Performance issues
------------------

Different work directories
~~~~~~~~~~~~~~~~~~~~~~~~~~

Having different work directories (for master and workers) may lead to
performance issues. In particular, if the work directories belong to different
mount points and with different performance, where the copy of files may be
required.
For example, using folders that are shared across nodes in a supercomputer
but with different performance (e.g. ``scratch`` and ``projects`` in MareNostrum 4)
for the master and worker workspaces.
