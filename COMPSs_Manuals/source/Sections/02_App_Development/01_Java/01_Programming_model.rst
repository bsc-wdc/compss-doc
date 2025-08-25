Programming Model
*****************

This section shows how the COMPSs programming model is used to develop
a Java task-based parallel application for distributed computing. First,
We introduce the structure of a COMPSs Java application and with a simple
example. Then, we will provide a complete guide about how to define the
application tasks. Finally, we will show special API calls and other
optimization hints.

Application Overview
====================

.. include:: ./01_Programming_model/01_Java_application_overview_inc.rst

The following sections show a detailed guide of how to implement complex
applications.


Task definition reference guide
===============================

The task definition interface is a Java annotated interface where developers
define tasks as annotated methods in the interfaces. Annotations can be of
three different types:

#. Task-definition annotations are method annotations to indicate which
   type of task is a method declared in the interface.

#. The Parameter annotation provides metadata about the task parameters,
   such as data type, direction and other property for runtime optimization.

#. The Constraints annotation describes the minimum capabilities that a
   given resource must fulfill to execute the task, such as the number of
   processors or main memory size.

#. The Prolog/Epilog annotations are definitions of binaries to be run
   before/after the task execution.

#. Scheduler hint annotation provides information about how to deal with
   tasks of this type at scheduling and execution.

A complete and detailed explanation of the usage of the metadata
includes:

Task-definition Annotations
===========================

For each declared methods, developers has to define a task type.
The following list enumerates the possible task types:

-  **@Method:** Defines the Java method as a task

      -  **declaringClass** (Mandatory) String specifying the class that
         implements the Java method.

      -  **targetDirection** This field specifies the direction of the
         target object of an object method. It can be defined as: INOUT"
         (default value) if the method modifies the target object,
         "CONCURRENT" if this object modification can be done
         concurrently, or "IN" if the method does not modify the target
         object. ().

      -  **priority** "true" if the task takes priority and "false"
         otherwise. This parameter is used by the COMPSs scheduler (it
         is a String not a Java boolean).

      -  **onFailure** Expected behavior if the task fails.
         *OnFailure.RETRY* (default value) makes the task be executed
         again, *OnFailure.CANCEL_SUCCESSORS* ignores the failure and
         cancels the successor tasks, *OnFailure.FAIL* stops the whole
         application in a save mode once a task fails or
         *OnFailure.IGNORE* ignores the failure and continues with
         normal runtime execution.

-  **@Binary:** Defines the Java method as a binary invocation

      -  **binary** (Mandatory) String defining the full path of the
         binary that must be executed.

      -  **workingDir** Full path of the binary working directory inside
         the COMPSs Worker.

      -  **priority** "true" if the task takes priority and "false"
         otherwise. This parameter is used by the COMPSs scheduler (it
         is a String not a Java boolean).

-  **@MPI:** Defines the Java method as a MPI invocation

      -  **mpiRunner** (Mandatory) String defining the mpi runner
         command.

      -  **binary** (Mandatory) String defining the full path of the
         binary that must be executed.

      -  **processes** String defining the number of MPI processes spawn
         in the task execution. This can be combined with the constraints
         annotation to create define a MPI+OpenMP task. (Default is 1)

      -  **scaleByCU** It indicates that the defined *processes* will be
         scaled by the defined *computingUnits* in the constraints. So, the
         total MPI processes will be *processes* multiplied by *computingUnits*.
         This functionality is used to groups MPI processes per node. Number
         of groups will be set in processes and the number of processes per
         node will be indicated by *computingUnits*

      -  **workingDir** Full path of the binary working directory inside
         the COMPSs Worker.

      -  **priority** "true" if the task takes priority and "false"
         otherwise. This parameter is used by the COMPSs scheduler (it
         is a String not a Java boolean).

-  **@OmpSs:** Defines the Java method as a OmpSs invocation

      -  **binary** (Mandatory) String defining the full path of the
         binary that must be executed.

      -  **workingDir** Full path of the binary working directory inside
         the COMPSs Worker.

      -  **priority** "true" if the task takes priority and "false"
         otherwise. This parameter is used by the COMPSs scheduler (it
         is a String not a Java boolean).

-  **@Http:** It specifies the HTTP task properties.

      -  **serviceName** Mandatory. Name of the HTTP Service that included at least one HTTP resource in the resources file.

      -  **resource** Mandatory. URL extension to be concatenated with HTTP resource's base URL.

      -  **request** Mandatory. Type of the HTTP request (GET, POST, etc.).

      -  **payload** Payload string of POST requests if any. Payload strings can contain any kind of a COMPSs Parameter as long as it is defined between double curly brackets as '{{parameter_name}}'. File parameters can also be used simply by including only the file parameter name.

      -  **payloadType** Payload type of POST requests (e.g: 'application/json').

      -  **produces** In case of JSON responses, produces string can be used as a template to define 2 things; the first one is where the return value(s) is (are) stored in the retrieved JSON string. Returns are meant to be defined as '{{return_0}}','{{return_1}}', etc. And the second one is for additional parameters to be used 'updates' string. The user assign a value from the JSON response to a parameter and use that param to update an INOUT dictionary.

      - **updates** (PyCOMPSs only) In case of INOUT dictionaries, the user can update the INOUT dict with a value extracted from the JSON response.

For task which are not methods, a representative method has to be defined in an specific class depending on the task type (binary.BINARY in the case of binary tasks, mpi.MPI for mpi tasks, ...). This is required just for compilation and to enable the invocation of the task from the main code, the runtime will substitute this code by the real execution of the defined task. An example of this representative method can be found in :numref:`MPI_task_dummy_java`

.. code-block:: java
    :name: MPI_task_dummy_java
    :caption: Representative method for an MPI task

    package mpi;

    public class MPI {
      public static int mpiExecution(int i, String outFile) {
        // Nothing to do
        return 0
      }



Parameter-level annotations
---------------------------

For each parameter of task (method declared in the interface), the user
must include a **@Parameter** annotation. The properties

   -  **Direction:** Describes how a task uses the parameter (Default is IN).

      -  **Direction.IN:** Task only reads the data.

      -  **Direction.INOUT:** Task reads and modifies

      -  **Direction.OUT:** Task completely modify the data, or previous content
         or not modified data is not important.

      -  **Direction.COMMUTATIVE:** An INOUT usage of the data which can be
         re-ordered with other executions of the defined task.

      -  **Direction.CONCURRENT:** The task allow concurrent modifications
         of this data. It requires a storage backend that manages concurrent
         modifications.

   -  **Type:** Describes the data type of the task parameter. By default,
      the runtime infers the type according to the Java datatype. However,
      it is mandatory to define it for files, directories and Streams.

      COMPSs supports the following types for task parameters:

      -  **Basic types:** To indicate a parameter is a Java primitive type
         use the following types: *Type.BOOLEAN, Type.CHAR, Type.BYTE,
         Type.SHORT, Type.INT, Type.LONG, Type.FLOAT, Type.DOUBLE*. They
         can only have **IN** direction, since primitive types in Java
         are always passed by value.

      -  **String:** To indicate a parameter is a Java String use *Type.STRING*.
         It can only have **IN** direction, since Java Strings are immutable.

      -  **File:** The real Java type associated with a file parameter is a
         String that contains the path to the file. However, if the user
         specifies a parameter as *Type.FILE*, COMPSs will treat it as such.
         It can have any direction (IN, OUT, INOUT, CONMMUTATIVE or CONCURRENT).

      -  **Directory:** The real Java type associated with a directory parameter
         is a String that contains the path to the directory. However, if the
         user specifies a parameter as *Type.DIRECTORY*, COMPSs will treat it
         as such. It can have any direction (IN, OUT, INOUT, CONMMUTATIVE or
         CONCURRENT).

      -  **Object:** An object parameter is defined with *Type.Object*. It can
         have any direction (IN, INOUT, COMMUTATIVE or CONCURRENT).

      -  **Streams:** A Task parameters can be defined as stream with
         Type.STREAM. It can have direction IN, if the task pull data from
         the stream, or OUT if the task pushes data to the stream.

   -  **Return type:** Any object or a generic class object. In this
      case the direction is always OUT.
      Basic types are also supported as return types. However, we do
      not recommend to use them because they cause an implicit
      synchronization

   -  **StdIOStream:** For non-native tasks (binaries, MPI, and OmpSs) COMPSs
      supports the automatic redirection of the Linux streams by
      specifying StdIOStream.STDIN, StdIOStream.STDOUT or StdIOStream.STDERR. Notice
      that any parameter annotated with the stream annotation must be of
      type *Type.FILE*, and with direction *Direction.IN* for
      *StdIOStream.STDIN* or *Direction.OUT/ Direction.INOUT* for
      *StdIOStream.STDOUT* and *StdIOStream.STDERR*.

   -  **Prefix:** For non-native tasks (binaries, MPI, and OmpSs) COMPSs
      allows to prepend a constant String to the parameter value to use
      the Linux joint-prefixes as parameters of the binary execution.

   -  **Weight:** Provides a hint of the size of this parameter compared to
      a default one. For instance, if a parameters is 3 times larger than the
      others, set the weigh property of this parameter to 3.0. (Default is 1.0).

   -  **keepRename:** Runtime rename files to avoid some data dependencies.
      It is transparent to the final user because we rename back the filename
      when invoking the task at worker. This management creates an overhead,
      if developers know that the task is not name nor extension sensitive
      (i.e can work with rename), they can set this property to true to
      reduce the overhead.

Constraints annotations
-----------------------

   -  **@Constraints:** The user can specify the capabilities that a
      resource must have in order to run a method. For example, in a
      cloud execution the COMPSs runtime creates a VM that fulfills the
      specified requirements in order to perform the execution.

.. include:: ./01_Programming_model/02_Java_constraints_inc.rst


Prolog & Epilog annotations
---------------------------

   -  **@Prolog:** Defines a binary to be run right before the task execution.

         -  **binary**: the binary to be executed.

         -  **params**: describe the command line arguments of the binary.

         -  **failByExitValue**: is used to indicate the behavior when the prolog or epilog
            returns an exit value different than zero. Users can set the ```failByExitValue``` to
            *True*, if they want to consider the exit value as a task failure.

   -  **@Epilog:** Defines a binary to be run right after the task execution finishes.

         -  **binary** , **params**, **failByExitValue** with the same behaviors as Prolog.


Scheduler annotations
---------------------

   -  **@SchedulerHints:** It specifies hints for the scheduler about how to
      treat the task.

         -  **isReplicated** "true" if the method must be executed in all
            the worker nodes when invoked from the main application (it is
            a String not a Java boolean).

         -  **isDistributed** "true" if the method must be scheduled in a
            forced round robin among the available resources (it is a
            String not a Java boolean).

Alternative method implementations
==================================

Since version 1.2, the COMPSs programming model allows developers to
define sets of alternative implementations of the same method in the
Java annotated interface. :numref:`alternative_implementations_java` depicts an example where
the developer sorts an integer array using two different methods: merge
sort and quick sort that are respectively hosted in the
*packagepath.Mergesort* and *packagepath.Quicksort* classes.

.. code-block:: java
    :name: alternative_implementations_java
    :caption: Alternative sorting method definition example

    @Method(declaringClass - "packagepath.Mergesort")
    @Method(declaringClass - "packagepath.Quicksort")
    void sort(
        @Parameter(type - Type.OBJECT, direction - Direction.INOUT)
        int[] array
    );

As depicted in the example, the name and parameters of all the
implementations must coincide; the only difference is the class where
the method is implemented. This is reflected in the attribute
*declaringClass* of the *@Method* annotation. Instead of stating that
the method is implemented in a single class, the programmer can define
several instances of the *@Method* annotation with different declaring
classes.

As independent remote methods, the sets of equivalent methods might have
common restrictions to be fulfilled by the resource hosting the
execution. Or even, each implementation can have specific constraints.
Through the *@Constraints* annotation, developers can specify the common
constraints for a whole set of methods. In the following example (:numref:`constraint_java`) only
one core is required to run the method of both sorting algorithms.

.. code-block:: java
    :name: constraint_java
    :caption: Alternative sorting method definition with constraint example

    @Constraints(computingUnits - "1")
    @Method(declaringClass - "packagepath.Mergesort")
    @Method(declaringClass - "packagepath.Quicksort")
    void sort(
        @Parameter(type - Type.OBJECT, direction - Direction.INOUT)
        int[] array
    );

However, these sorting algorithms have different memory consumption,
thus each algorithm might require a specific amount of memory and that
should be stated in the implementation constraints. For this purpose,
the developer can add a *@Constraints* annotation inside each *@Method*
annotation containing the specific constraints for that implementation.
Since the Mergesort has a higher memory consumption than the quicksort,
the :numref:`specific_implementation_constraints_java` sets a requirement of 1 core and 2GB of memory for
the mergesort implementation and 1 core and 500MB of memory for the
quicksort.

.. code-block:: java
    :name: specific_implementation_constraints_java
    :caption: Alternative sorting method definition with specific constraints example

    @Constraints(computingUnits - "1")
    @Method(declaringClass - "packagepath.Mergesort", constraints - @Constraints(memorySize - "2.0"))
    @Method(declaringClass - "packagepath.Quicksort", constraints - @Constraints(memorySize - "0.5"))
    void sort(
        @Parameter(type - Type.OBJECT, direction - Direction.INOUT)
        int[] array
    );

Java API calls
==============

COMPSs also provides a explicit synchronization call, namely *barrier*,
which can be used through the COMPSs Java API. The use of *barrier*
forces to wait for all tasks that have been submitted before the barrier
is called. When all tasks submitted before the *barrier* have finished,
the execution continues (:numref:`barrier_java`).

.. code-block:: java
    :name: barrier_java
    :caption: COMPSs.barrier() example

    import es.bsc.compss.api.COMPSs;

    public class Main {
        public static void main(String[] args) {
            // Setup counterName1 and counterName2 files
            // Execute task increment 1
            SimpleImpl.increment(counterName1);
            // API Call to wait for all tasks
            COMPSs.barrier();
            // Execute task increment 2
            SimpleImpl.increment(counterName2);
        }
    }

When an object is used in a task, COMPSs runtime store the references of
these object in the runtime data structures and generate replicas and
versions in remote workers. COMPSs is automatically removing these
replicas for obsolete versions. However, the reference of the last
version of these objects could be stored in the runtime data-structures
preventing the garbage collector to remove it when there are no
references in the main code. To avoid this situation, developers can
indicate the runtime that an object is not going to use any more by
calling the *deregisterObject* API call. :numref:`deregisterObject_java`
shows a usage example of this API call.

.. code-block:: java
    :name: deregisterObject_java
    :caption: COMPSs.deregisterObject() example

    import es.bsc.compss.api.COMPSs;

    public class Main {
        public static void main(String[] args) {
            final int ITERATIONS - 10;
            for (int i - 0; i < ITERATIONS; ++i) {
                Dummy d - new Dummy(d);
                TaskImpl.task(d);
                /*Allows garbage collector to delete the
                  object from memory when the task is finished */
                COMPSs.deregisterObject((Object) d);
            }
        }
    }

To synchronize files, the *getFile* API call synchronizes a file,
returning the last version of file with its original name. :numref:`getFile_java`
contains an example of its usage.

.. code-block:: java
    :name: getFile_java
    :caption: COMPSs.getFile() example

    import es.bsc.compss.api.COMPSs;

    public class Main {
        public static void main(String[] args) {
            for (int i-0; i<1; i++) {
                TaskImpl.task(FILE_NAME, i);
            }
            /*Waits until all tasks have finished and
              synchronizes the file with its last version*/
            COMPSs.getFile(FILE_NAME);
    	}
    }

Managing Failures in Tasks
==========================

COMPSs provide mechanism to manage failures in tasks. Developers can specify two
properties in the task definition what the runtime should do when a task is
blocked or failed.

The *timeOut* property indicates the runtime that a task of this type is considered failed
when its duration is larger than the value specified in the property (in seconds)

The *onFailure* property indicates what to do when a task of this type is failed.
The possible values are:

- *OnFaiure.RETRY* (Default): The task is executed twice in the same worker and a different worker.
- *OnFailure.CANCEL_SUCCESSORS*: All successors of this task are canceled.
- *OnFailure.FAIL*: The task failure produces a failure of the whole application.
- *OnFailure.IGNORE*: The task failure is ignored and the output parameters are set with empty values.

Usage examples of these properties are shown in :numref:`failures_java`

.. code-block:: java
    :name: failures_java
    :caption: Failure example

    public interface FailuresItf{
       @Method(declaringClass - "example.Example", timeOut - "3000", onFailure - OnFailure.IGNORE)
       void task_example(@Parameter(type - Type.FILE, direction - Direction.OUT) String fileName);
    }


Tasks Groups and COMPSs exceptions
==================================

COMPSs allows users to define task groups which can be combined with an special exception (``COMPSsException``) that the user can use
to achieve parallel distributed try/catch blocks; :numref:`compss_exception_java`
shows an example of *COMPSsException* raising. In this case, the group
definition is blocking, and waits for all task groups to finish.
If a task of the group raises a *COMPSsException*, it will be captured by the
runtime which reacts to it by canceling the running and pending tasks of the
group and forwarding the COMPSsException to enable the execution
except clause.
Consequently, the *COMPSsException* must be combined with task groups.

.. code-block:: java
    :name: compss_exception_java
    :caption: COMPSs Exception example

    ...
        try (COMPSsGroup a - new COMPSsGroup("GroupA")) {
            for (int j - 0; j < N; j++) {
                Test.taskWithCOMPSsException(FILE_NAME);
            }
        } catch (COMPSsException e) {
            Test.otherTask(FILE_NAME);
        }
    ...

It is possible to use a non-blocking task group for asynchronous behavior
(see :numref:`compss_exception_java_async`).
In this case, the try/catch can be defined later in the code surrounding
the *COMPSs.barrierGroup*, enabling to check exception from the defined
groups without retrieving data while other tasks are being executed.

.. code-block:: java
    :name: compss_exception_java_async
    :caption: COMPSs Exception example

    ...
    for (int i-0; i<10; i++){
        try (COMPSsGroup a - new COMPSsGroup("Group" + i, false)) {
            for (int j - 0; j < N; j++) {
                Test.taskWithCOMPSsException(FILE_NAME);
            }
        } catch (Exception e) {
            //This is just for compilation. Exception not catch here!
        }
    }
    for (int i-0; i<10; i++){
        // The group exception will be thrown from the barrier
        try {
            COMPSs.barrierGroup(""Group" + i");
        } catch (COMPSsException e) {
            System.out.println("Exception caught in barrier!!");
            Test.otherTask(FILE_NAME);
        }
    }

Finally, users can also programmatically cancel tasks associated to a task group
using the *COMPSs.cancelGroup* function. :numref:`compss_cancel_group_java`
shows an example of how to use this method.

.. code-block:: java
    :name: compss_cancel_group_java
    :caption: Programmatic task group cancellation example

    ...
    try (COMPSsGroup a - new COMPSsGroup("Group_to_cancel", false)) {
        for (int j - 0; j < N; j++) {
            Test.taskWithCOMPSsException(FILE_NAME);
        }
    }
    ...
    COMPSs.barrierGroup("Group_to_cancel");
    ...

.. ATTENTION::

   Method tasks are executed on top of Java threads, to perform a secure cancellation of a running task in a thread when using the time *timeout* property and *COMPSsExceptions, you have to use the *COMPSsWorker.cancellationPoint* method to indicate the points where it is secure to cancel a task. When the task code reaches this method, it will check if the current task must be canceled and perform a save cancellation, otherwise it will continue with this. An example about how to use the cancellation point is shown in :numref:`cancellation_point_java`

   .. code-block:: java
    :name: cancellation_point_java
    :caption: COMPSs Exception example

    import es.bsc.compss.worker.COMPSsWorker;

    public class TasksImpl {

      public static void cancellableTask(String fileName) throws Exception {
        boolean condition - true
        while (condition) {
            COMPSsWorker.cancellationPoint();
            condition - computeIteration(...);
        }
      }
    }
