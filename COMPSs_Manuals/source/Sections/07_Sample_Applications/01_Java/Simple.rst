Simple
------

The Simple application is a Java application that increases a counter by
means of a task. The counter is stored inside a file that is transferred
to the worker when the task is executed. Thus, the tasks interface is
defined as follows:

.. code-block:: java

    	// simple.SimpleItf

    	@Method(declaringClass = "simple.SimpleImpl")
    	void increment(
    		@Parameter(type = Type.FILE, direction = Direction.INOUT) String file
    	);

Next we also provide the invocation of the task from the main code and
the increment's method code.

.. code-block:: java

    	// simple.Simple

    	public static void main(String[] args) throws Exception {
    		// Check and get parameters
    		if (args.length != 1) {
    			usage();
    			throw new Exception("[ERROR] Incorrect number of parameters");
    		}
    		int initialValue = Integer.parseInt(args[0]);

    		// Write value
    		FileOutputStream fos = new FileOutputStream(fileName);
    		fos.write(initialValue);
    		fos.close();
    		System.out.println("Initial counter value is " + initialValue);

    		//Execute increment
    		SimpleImpl.increment(fileName);

    		// Write new value
    		FileInputStream fis = new FileInputStream(fileName);
    		int finalValue = fis.read();
    		fis.close();
    		System.out.println("Final counter value is " + finalValue);
    	}

.. code-block:: java

    	// simple.SimpleImpl

    	public static void increment(String counterFile) throws FileNotFoundException, IOException {
    		// Read value
    		FileInputStream fis = new FileInputStream(counterFile);
    		int count = fis.read();
    		fis.close();

    		// Write new value
    		FileOutputStream fos = new FileOutputStream(counterFile);
    		fos.write(++count);
    		fos.close();
    	}

Finally, to compile and execute this application users must run the
following commands:

.. code-block:: console

    compss@bsc:~$ cd ~/tutorial_apps/java/simple/src/main/java/simple/
    compss@bsc:~/tutorial_apps/java/simple/src/main/java/simple$ javac *.java
    compss@bsc:~/tutorial_apps/java/simple/src/main/java/simple$ cd ..
    compss@bsc:~/tutorial_apps/java/simple/src/main/java$ jar cf simple.jar simple
    compss@bsc:~/tutorial_apps/java/simple/src/main/java$ mv simple.jar ~/tutorial_apps/java/simple/jar/

    compss@bsc:~$ cd ~/tutorial_apps/java/simple/jar
    compss@bsc:~/tutorial_apps/java/simple/jar$ runcompss simple.Simple 1
    compss@bsc:~/tutorial_apps/java/simple/jar$ runcompss simple.Simple 1
    [  INFO] Using default execution type: compss
    [  INFO] Using default location for project file: /opt/COMPSs/Runtime/configuration/xml/projects/default_project.xml
    [  INFO] Using default location for resources file: /opt/COMPSs/Runtime/configuration/xml/resources/default_resources.xml

    ----------------- Executing simple.Simple --------------------------

    WARNING: COMPSs Properties file is null. Setting default values
    [(772)    API]  -  Starting COMPSs Runtime v<version>
    Initial counter value is 1
    Final counter value is 2
    [(3813)    API]  -  Execution Finished

    ------------------------------------------------------------
