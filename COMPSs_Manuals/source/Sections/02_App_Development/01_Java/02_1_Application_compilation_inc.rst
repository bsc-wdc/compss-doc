A COMPSs Java application needs to be packaged in a *jar* file
containing the class files of the main code, of the methods
implementations and of the *Itf* annotation. This jar package can be
generated using the commands available in the Java SDK or creating your
application as a Apache Maven project.

To integrate COMPSs in the maven compile process you just need to add the
*compss-api* artifact as dependency in the application project.

.. code-block:: xml

    <dependencies>
        <dependency>
            <groupId>es.bsc.compss</groupId>
            <artifactId>compss-api</artifactId>
            <version>${compss.version}</version>
        </dependency>
    </dependencies>

To build the jar in the maven case use the following command

.. code-block:: console

    $ mvn package


Next we provide a set of commands to compile the Java Simple application (detailed at
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
