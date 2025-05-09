Hello World
-----------

The Hello World is a Java application that creates a task and prints a
Hello World! message. Its purpose is to clarify that the COMPSs tasks
output is redirected to the job files and it is **not** available at the
standard output.

Next we provide the important parts of the application's code.

.. code-block:: java

    	// hello.Hello

    	public static void main(String[] args) throws Exception {
    		// Check and get parameters
    		if (args.length != 0) {
    			usage();
    			throw new Exception("[ERROR] Incorrect number of parameters");
    		}

    		// Hello World from main application
    		System.out.println("Hello World! (from main application)");

    		// Hello World from a task
    		HelloImpl.sayHello();
    	}

As shown in the main code, this application has no input arguments.

.. code-block:: java

    	// hello.HelloImpl

    	public static void sayHello() {
    		System.out.println("Hello World! (from a task)");
    	}

Remember that, to run with COMPSs, java applications must provide an
interface. For simplicity, in this example, the content of the interface
only declares the task which has no parameters:

.. code-block:: java

    	// hello.HelloItf

    	@Method(declaringClass = "hello.HelloImpl")
    	  void sayHello(
    	);

Notice that there is a first Hello World message printed from the main
code and, a second one, printed inside a task. When executing
sequentially this application users will be able to see both messages at
the standard output. However, when executing this application with
COMPSs, users will only see the message from the main code at the
standard output. The message printed from the task will be stored inside
the job log files.

Let's try it. First we proceed to compile the code by running the
following instructions:

.. code-block:: console

    compss@bsc:~$ cd ~/tutorial_apps/java/hello/src/main/java/hello/
    compss@bsc:~/tutorial_apps/java/hello/src/main/java/hello$ javac *.java
    compss@bsc:~/tutorial_apps/java/hello/src/main/java/hello$ cd ..
    compss@bsc:~/tutorial_apps/java/hello/src/main/java$ jar cf hello.jar hello
    compss@bsc:~/tutorial_apps/java/hello/src/main/java$ mv hello.jar ~/tutorial_apps/java/hello/jar/

Alternatively, this example application is prepared to be compiled with
*maven*:

.. code-block:: console

    compss@bsc:~$ cd ~/tutorial_apps/java/hello/
    compss@bsc:~/tutorial_apps/java/hello$ mvn clean package

Once done, we can sequentially execute the application by directly
invoking the *jar* file.

.. code-block:: console

    compss@bsc:~$ cd ~/tutorial_apps/java/hello/jar/
    compss@bsc:~/tutorial_apps/java/hello/jar$ java -cp hello.jar hello.Hello
    Hello World! (from main application)
    Hello World! (from a task)

And we can also execute the application with COMPSs:

.. code-block:: console

    compss@bsc:~$ cd ~/tutorial_apps/java/hello/jar/
    compss@bsc:~/tutorial_apps/java/hello/jar$ runcompss -d hello.Hello
    [  INFO] Using default execution type: compss
    [  INFO] Using default location for project file: /opt/COMPSs/Runtime/configuration/xml/projects/default_project.xml
    [  INFO] Using default location for resources file: /opt/COMPSs/Runtime/configuration/xml/resources/default_resources.xml

    ----------------- Executing hello.Hello --------------------------

    WARNING: COMPSs Properties file is null. Setting default values
    [(928)    API]  -  Deploying COMPSs Runtime v<version>
    [(931)    API]  -  Starting COMPSs Runtime v<version>
    [(931)    API]  -  Initializing components
    [(1472)    API]  -  Ready to process tasks
    Hello World! (from main application)
    [(1474)    API]  -  Creating task from method sayHello in hello.HelloImpl
    [(1474)    API]  -  There is 0 parameter
    [(1477)    API]  -  No more tasks for app 1
    [(4029)    API]  -  Getting Result Files 1
    [(4030)    API]  -  Stop IT reached
    [(4030)    API]  -  Stopping AP...
    [(4031)    API]  -  Stopping TD...
    [(4161)    API]  -  Stopping Comm...
    [(4163)    API]  -  Runtime stopped
    [(4166)    API]  -  Execution Finished

    ------------------------------------------------------------

Notice that the COMPSs execution is using the *-d* option to allow the
job logging. Thus, we can check out the application jobs folder to look
for the task output.

.. code-block:: console

    compss@bsc:~$ cd ~/.COMPSs/hello.Hello_01/jobs/
    compss@bsc:~/.COMPSs/hello.Hello_01/jobs$ ls -1
    job1_NEW.err
    job1_NEW.out
    compss@bsc:~/.COMPSs/hello.Hello_01/jobs$ cat job1_NEW.out
    [JAVA EXECUTOR] executeTask - Begin task execution
    WORKER - Parameters of execution:
      * Method type: METHOD
      * Method definition: [DECLARING CLASS=hello.HelloImpl, METHOD NAME=sayHello]
      * Parameter types:
      * Parameter values:
    Hello World! (from a task)
    [JAVA EXECUTOR] executeTask - End task execution
