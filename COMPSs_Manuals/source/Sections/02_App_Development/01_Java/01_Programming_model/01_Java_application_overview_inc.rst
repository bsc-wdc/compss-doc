A COMPSs application is composed of three parts:

-  **Main application code:** the code that is executed sequentially and
   contains the calls to the user-selected methods that will be executed
   by the COMPSs runtime as asynchronous parallel tasks.

-  **Remote methods code:** the implementation of the tasks.

-  **Task definition interface:** It is a Java annotated interface which
   declares the methods to be run as remote tasks along with metadata
   information needed by the runtime to properly schedule the tasks.

The main application file name has to be the same of the main class and
starts with capital letter, in this case it is **Simple.java**. The Java
annotated interface filename is *application name + Itf.java*, in this
case it is **SimpleItf.java**. And the code that implements the remote
tasks is defined in the *application name + Impl.java* file, in this
case it is **SimpleImpl.java**.

All code examples are in the ``/home/compss/tutorial_apps/java/`` folder
of the development environment.

.. rubric:: Main application code

In COMPSs, the user's application code is kept unchanged, no API calls
need to be included in the main application code in order to run the
selected tasks on the nodes.

The COMPSs runtime is in charge of replacing the invocations to the
user-selected methods with the creation of remote tasks also taking care
of the access to files where required. Let's consider the Simple
application example that takes an integer as input parameter and
increases it by one unit.

The main application code of Simple application is shown in the following
code block. It is executed sequentially until the call to the **increment()**
method. COMPSs, as mentioned above, replaces the call to this method with
the generation of a remote task that will be executed on an available node.

.. code-block:: java
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

.. rubric:: Remote methods code

The following code contains the implementation of the remote method of
the *Simple* application that will be executed remotely by COMPSs.

.. code-block:: java
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

.. rubric:: Task definition interface

This Java interface is used to declare the methods to be executed
remotely along with Java annotations that specify the necessary metadata
about the tasks. The metadata can be of three different types:

#. For each parameter of a method, the data type (currently *File* type,
   primitive types and the *String* type are supported) and its
   directions (IN, OUT, INOUT, COMMUTATIVE or CONCURRENT).

#. The Java class that contains the code of the method.

#. The constraints that a given resource must fulfill to execute the
   method, such as the number of processors or main memory size.

The task description interface of the Simple app example is shown in the
following figure. It includes the description of the *Increment()* method
metadata. The method interface contains a single input parameter, a string
containing a path to the file counterFile. In this example there are
constraints on the minimum number of processors and minimum memory size
needed to run the method.

   .. code-block:: java
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
