Java
====

This section illustrates the steps to develop a Java COMPSs application,
to compile and to execute it. The *Simple* application will be used as
reference code. The user is required to select a set of methods, invoked
in the sequential application, that will be run as remote tasks on the
available resources.

Programming Model
-----------------

A COMPSs application is composed of three parts:

-  **Main application code:** the code that is executed sequentially and
   contains the calls to the user-selected methods that will be executed
   by the COMPSs runtime as asynchronous parallel tasks.

-  **Remote methods code:** the implementation of the tasks.

-  **Java annotated interface:** It declares the methods to be run as
   remote tasks along with metadata information needed by the runtime to
   properly schedule the tasks.

The main application file name has to be the same of the main class and
starts with capital letter, in this case it is **Simple.java**. The Java
annotated interface filename is *application name + Itf.java*, in this
case it is **SimpleItf.java**. And the code that implements the remote
tasks is defined in the *application name + Impl.java* file, in this
case it is **SimpleImpl.java**.

All code examples are in the ``/home/compss/tutorial_apps/java/`` folder
of the development environment.

Main application code
~~~~~~~~~~~~~~~~~~~~~

In COMPSs, the user’s application code is kept unchanged, no API calls
need to be included in the main application code in order to run the
selected tasks on the nodes.

The COMPSs runtime is in charge of replacing the invocations to the
user-selected methods with the creation of remote tasks also taking care
of the access to files where required. Let’s consider the Simple
application example that takes an integer as input parameter and
increases it by one unit.

The main application code of Simple app (:numref:`simple_java` **Simple.java**) is executed
sequentially until the call to the **increment()** method. COMPSs, as
mentioned above, replaces the call to this method with the generation of
a remote task that will be executed on an available node.

.. code-block:: java
    :name: simple_java
    :caption: Simple in Java (Simple.java)

    package simple;

    import java.io.FileInputStream;
    import java.io.FileOutputStream;
    import java.io.IOException;
    import simple.SimpleImpl;

    public class Simple {

      public static void main(String[] args) {
        String counterName = "counter";
        int initialValue = args[0];

        //--------------------------------------------------------------//
        // Creation of the file which will contain the counter variable //
        //--------------------------------------------------------------//
        try {
           FileOutputStream fos = new FileOutputStream(counterName);
           fos.write(initialValue);
           System.out.println("Initial counter value is " + initialValue);
           fos.close();
        }catch(IOException ioe) {
           ioe.printStackTrace();
        }

        //----------------------------------------------//
        //           Execution of the program           //
        //----------------------------------------------//
        SimpleImpl.increment(counterName);

        //----------------------------------------------//
        //    Reading from an object stored in a File   //
        //----------------------------------------------//
        try {
           FileInputStream fis = new FileInputStream(counterName);
           System.out.println("Final counter value is " + fis.read());
           fis.close();
        }catch(IOException ioe) {
           ioe.printStackTrace();
        }
      }
    }

Remote methods code
~~~~~~~~~~~~~~~~~~~

The following code contains the implementation of the remote method of
the *Simple* application (:numref:`simple_impl_java` **SimpleImpl.java**) that will be executed
remotely by COMPSs.

.. code-block:: java
    :name: simple_impl_java
    :caption: Simple Implementation (SimpleImpl.java)

    package simple;

    import  java.io.FileInputStream;
    import  java.io.FileOutputStream;
    import  java.io.IOException;
    import  java.io.FileNotFoundException;

    public class SimpleImpl {
      public static void increment(String counterFile) {
        try{
          FileInputStream fis = new FileInputStream(counterFile);
          int count = fis.read();
          fis.close();
          FileOutputStream fos = new FileOutputStream(counterFile);
          fos.write(++count);
          fos.close();
        }catch(FileNotFoundException fnfe){
          fnfe.printStackTrace();
        }catch(IOException ioe){
          ioe.printStackTrace();
        }
      }
    }

Java annotated interface
~~~~~~~~~~~~~~~~~~~~~~~~

The Java interface is used to declare the methods to be executed
remotely along with Java annotations that specify the necessary metadata
about the tasks. The metadata can be of three different types:

#. For each parameter of a method, the data type (currently *File* type,
   primitive types and the *String* type are supported) and its
   directions (IN, OUT, INOUT or CONCURRENT).

#. The Java class that contains the code of the method.

#. The constraints that a given resource must fulfill to execute the
   method, such as the number of processors or main memory size.

A complete and detailed explanation of the usage of the metadata
includes:

-  **Method-level Metadata:** for each selected method, the following
   metadata has to be defined:

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

      -  **onFailure** Expected behaviour if the task fails.
         *OnFailure.RETRY* (default value) makes the task be executed
         again, *OnFailure.CANCEL_SUCCESSORS* ignores the failure and
         cancels the succesor tasks, *OnFailure.FAIL* stops the whole
         application in a save mode once a task fails or
         *OnFailure.IGNORE* ignores the failure and continues with
         normal runtime execution.

   -  **@Binary:** Defines the Java method as a binary invokation

      -  **binary** (Mandatory) String defining the full path of the
         binary that must be executed.

      -  **workingDir** Full path of the binary working directory inside
         the COMPSs Worker.

      -  **priority** "true" if the task takes priority and "false"
         otherwise. This parameter is used by the COMPSs scheduler (it
         is a String not a Java boolean).

   -  **@MPI:** Defines the Java method as a MPI invokation

      -  **mpiRunner** (Mandatory) String defining the mpi runner
         command.

      -  **binary** (Mandatory) String defining the full path of the
         binary that must be executed.

      -  **computingNodes** String defining the number of computing
         nodes reserved for the MPI execution (only a single node is
         reserved by default).

      -  **workingDir** Full path of the binary working directory inside
         the COMPSs Worker.

      -  **priority** "true" if the task takes priority and "false"
         otherwise. This parameter is used by the COMPSs scheduler (it
         is a String not a Java boolean).

   -  **@OmpSs:** Defines the Java method as a OmpSs invokation

      -  **binary** (Mandatory) String defining the full path of the
         binary that must be executed.

      -  **workingDir** Full path of the binary working directory inside
         the COMPSs Worker.

      -  **priority** "true" if the task takes priority and "false"
         otherwise. This parameter is used by the COMPSs scheduler (it
         is a String not a Java boolean).

   -  **@Constraints:** The user can specify the capabilities that a
      resource must have in order to run a method. For example, in a
      cloud execution the COMPSs runtime creates a VM that fulfils the
      specified requirements in order to perform the execution. A full
      description of the supported constraints can be found in :numref:`supported_constraints`.

   -  **@SchedulerHints:** It specifies the class that implements the
      method.

      -  **isReplicated** "true" if the method must be executed in all
         the worker nodes when invoked from the main application (it is
         a String not a Java boolean).

      -  **isDistributed** "true" if the method must be scheduled in a
         forced round robin among the available resources (it is a
         String not a Java boolean).

-  **Parameter-level Metadata (@Parameter):** for each parameter and
   method, the user must define:

   -  **Direction:** *Direction.IN, Direction.INOUT, Direction.OUT or
      Direction.CONCURRENT*

   -  **Type:** COMPSs supports the following types for task parameters:

      -  **Basic types:** *Type.BOOLEAN, Type.CHAR, Type.BYTE,
         Type.SHORT, Type.INT, Type.LONG, Type.FLOAT, Type.DOUBLE*. They
         can only have **IN** direction, since primitive types in Java
         are always passed by value.

      -  **String:** *Type.STRING*. It can only have **IN** direction,
         since Java Strings are immutable.

      -  **File:** *Type.FILE*. It can have any direction (IN, OUT,
         INOUT or CONCURRENT). The real Java type associated with a FILE
         parameter is a String that contains the path to the file.
         However, if the user specifies a parameter as a FILE, COMPSs
         will treat it as such.

      -  **Object:** *Type.Object*. It can have any direction (IN, OUT,
         INOUT or CONCURRENT).

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

-  **Service-level Metadata:** for each selected service, the following
   metadata has to be defined:

   -  **@Service:** Mandatory. It specifies the service properties.

      -  **namespace** Mandatory. Service namespace

      -  **name** Mandatory. Service name.

      -  **port** Mandatory. Service port.

      -  **operation** Operation type.

      -  **priority** "true" if the service takes priority, "false"
         otherwise. This parameter is used by the COMPSs scheduler (it
         is a String not a Java boolean).

The Java annotated interface of the Simple app example (:numref:`simple_itf_java` SimpleItf.java)
includes the description of the *Increment()* method metadata. The
method interface contains a single input parameter, a string containing
a path to the file counterFile. In this example there are constraints on
the minimum number of processors and minimum memory size needed to run
the method.

.. code-block:: java
    :name: simple_itf_java
    :caption: Interface of the Simple application (SimpleItf.java)

    package simple;

    import  es.bsc.compss.types.annotations.Constraints;
    import  es.bsc.compss.types.annotations.task.Method;
    import  es.bsc.compss.types.annotations.Parameter;
    import  es.bsc.compss.types.annotations.parameter.Direction;
    import  es.bsc.compss.types.annotations.parameter.Type;

    public interface SimpleItf {

      @Constraints(computingUnits = "1", memorySize = "0.3")
      @Method(declaringClass = "simple.SimpleImpl")
      void increment(
          @Parameter(type = Type.FILE, direction = Direction.INOUT)
          String file
      );

    }

Alternative method implementations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since version 1.2, the COMPSs programming model allows developers to
define sets of alternative implementations of the same method in the
Java annotated interface. :numref:`alternative_implementations_java` depicts an example where
the developer sorts an integer array using two different methods: merge
sort and quick sort that are respectively hosted in the
*packagepath.Mergesort* and *packagepath.Quicksort* classes.

.. code-block:: java
    :name: alternative_implementations_java
    :caption: Alternative sorting method definition example

    @Method(declaringClass = "packagepath.Mergesort")
    @Method(declaringClass = "packagepath.Quicksort")
    void sort(
        @Parameter(type = Type.OBJECT, direction = Direction.INOUT)
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

    @Constraints(computingUnits = "1")
    @Method(declaringClass = "packagepath.Mergesort")
    @Method(declaringClass = "packagepath.Quicksort")
    void sort(
        @Parameter(type = Type.OBJECT, direction = Direction.INOUT)
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

    @Constraints(computingUnits = "1")
    @Method(declaringClass = "packagepath.Mergesort", constraints = @Constraints(memorySize = "2.0"))
    @Method(declaringClass = "packagepath.Quicksort", constraints = @Constraints(memorySize = "0.5"))
    void sort(
        @Parameter(type = Type.OBJECT, direction = Direction.INOUT)
        int[] array
    );

Java API calls
~~~~~~~~~~~~~~

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

When an object if used in a task, COMPSs runtime store the references of
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
            final int ITERATIONS = 10;
            for (int i = 0; i < ITERATIONS; ++i) {
                Dummy d = new Dummy(d);
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
            for (int i=0; i<1; i++) {
                TaskImpl.task(FILE_NAME, i);
            }
            /*Waits until all tasks have finished and
              synchronizes the file with its last version*/
            COMPSs.getFile(FILE_NAME);
    	}
    }

Application Compilation
-----------------------

A COMPSs Java application needs to be packaged in a *jar* file
containing the class files of the main code, of the methods
implementations and of the *Itf* annotation. Next we provide a set of
commands to compile the Java Simple application (detailed at
:ref:`Sections/07_Sample_Applications/01_Java:Java Sample applications`).

.. code-block:: console

    $ cd tutorial_apps/java/simple/src/main/java/simple/
    $~/tutorial_apps/java/simple/src/main/java/simple$ javac *.java
    $~/tutorial_apps/java/simple/src/main/java/simple$ cd ..
    $~/tutorial_apps/java/simple/src/main/java$ jar cf simple.jar simple/
    $~/tutorial_apps/java/simple/src/main/java$ mv ./simple.jar ../../../jar/

In order to properly compile the code, the CLASSPATH variable has to
contain the path of the *compss-engine.jar* package. The default COMPSs
installation automatically add this package to the CLASSPATH; please
check that your environment variable CLASSPATH contains the
*compss-engine.jar* location by running the following command:

.. code-block:: console

    $ echo $CLASSPATH | grep compss-engine

If the result of the previous command is empty it means that you are
missing the *compss-engine.jar* package in your classpath. We recommend
to automatically load the variable by editing the *.bashrc* file:

.. code-block:: console

    $ echo "# COMPSs variables for Java compilation" >> ~/.bashrc
    $ echo "export CLASSPATH=$CLASSPATH:/opt/COMPSs/Runtime/compss-engine.jar" >> ~/.bashrc

If you are using an IDE (such as Eclipse or NetBeans) we recommend you
to add the *compss-engine.jar* file as an external file to the project.
The *compss-engine.jar* file is available at your current COMPSs
installation under the following path: ``/opt/COMPSs/Runtime/compss-engine.jar``

*Please notice that if you have performed a custom installation, the
location of the package can be different.*

An Integrated Development Environment for Eclipse is also available to
simplify the development, compilation, deployment and execution COMPSs
applications. For further information about the *COMPSs IDE* please
refer to the *COMPSs IDE User Guide* available at http://compss.bsc.es .

Application Execution
---------------------

A Java COMPSs application is executed through the *runcompss* script. An
example of an invocation of the script is:

.. code-block:: console

    $ runcompss --classpath=/home/compss/tutorial_apps/java/simple/jar/simple.jar simple.Simple 1

A comprehensive description of the *runcompss* command is available in
the :ref:`Sections/03_User_Manual_App_Exec/01_Executing:Executing COMPSs applications` section.  

In addition to Java, COMPSs supports the execution of applications
written in other languages by means of bindings. A binding manages the
interaction of the no-Java application with the COMPSs Java runtime,
providing the necessary language translation.

The next sections describe the Python and C/C++ language bindings
offered by COMPSs.
