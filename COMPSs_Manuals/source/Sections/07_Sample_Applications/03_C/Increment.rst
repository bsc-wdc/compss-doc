Increment
---------

The Increment application is a C application that increases N times
three different counters. Each increase step is developed by a separated
task. The purpose of this application is to show parallelism between the
three counters.

Next we provide the main code of this application. The code inside the
*increment* task is the same than the previous example.

.. code-block:: C

      // increment.cc

      int main(int argc, char *argv[]) {
          // Check and get parameters
          if (argc != 5) {
    	  usage();
    	  return -1;
          }
          int N = atoi( argv[1] );
          string counter1 = argv[2];
          string counter2 = argv[3];
          string counter3 = argv[4];

          // Init COMPSs
          compss_on();

          // Initialize counter files
          file fileName1 = strdup(FILE_NAME1);
          file fileName2 = strdup(FILE_NAME2);
          file fileName3 = strdup(FILE_NAME3);
          initializeCounters(counter1, counter2, counter3, fileName1, fileName2, fileName3);

          // Print initial counters state
          cout << "Initial counter values: " << endl;
          printCounterValues(fileName1, fileName2, fileName3);

          // Execute increment tasks
          for (int i = 0; i < N; ++i) {
    	  increment(&fileName1);
    	  increment(&fileName2);
    	  increment(&fileName3);
          }

          // Print final state
          cout << "Final counter values: " << endl;
          printCounterValues(fileName1, fileName2, fileName3);

          // Stop COMPSs
          compss_off();

          return 0;
      }

As shown in the main code, this application has 4 parameters that stand
for:

#. **N:** Number of times to increase a counter

#. **counter1:** Initial value for counter 1

#. **counter2:** Initial value for counter 2

#. **counter3:** Initial value for counter 3

Next we will compile and run the Increment application with the *-g*
option to be able to generate the final graph at the end of the
execution.

.. code-block:: console

    compss@bsc:~$ cd ~/tutorial_apps/c/increment/
    compss@bsc:~/tutorial_apps/c/increment$ compss_build_app increment
    compss@bsc:~/tutorial_apps/c/increment$ runcompss --lang=c -g --project=./xml/project.xml --resources=./xml/resources.xml ~/tutorial_apps/c/increment/master/increment 10 1 2 3
    [  INFO] Using default execution type: compss

    ----------------- Executing increment --------------------------

    JVM_OPTIONS_FILE: /tmp/tmp.mgCheFd3kL
    COMPSS_HOME: /opt/COMPSs
    Args: 10 1 2 3

    WARNING: COMPSs Properties file is null. Setting default values
    [(655)    API]  -  Starting COMPSs Runtime v<version>
    Initial counter values:
    - Counter1 value is 1
    - Counter2 value is 2
    - Counter3 value is 3
    [   BINDING]  -  @GS_register  -  Ref: 0x7ffea17719f0
    [   BINDING]  -  @GS_register  -  ENTRY ADDED
    [   BINDING]  -  @GS_register  -  Entry.type: 9
    [   BINDING]  -  @GS_register  -  Entry.classname: File
    [   BINDING]  -  @GS_register  -  Entry.filename: file1.txt
    [   BINDING]  -  @GS_register  -  setting filename: file1.txt
    [   BINDING]  -  @GS_register  -  Filename: file1.txt
    [   BINDING]  -  @GS_register  - Result is 0
    [   BINDING]  -  @GS_register  -  Ref: 0x7ffea17719f8
    [   BINDING]  -  @GS_register  -  ENTRY ADDED
    [   BINDING]  -  @GS_register  -  Entry.type: 9
    [   BINDING]  -  @GS_register  -  Entry.classname: File
    [   BINDING]  -  @GS_register  -  Entry.filename: file2.txt
    [   BINDING]  -  @GS_register  -  setting filename: file2.txt
    [   BINDING]  -  @GS_register  -  Filename: file2.txt
    [   BINDING]  -  @GS_register  - Result is 0
    [   BINDING]  -  @GS_register  -  Ref: 0x7ffea1771a00
    [   BINDING]  -  @GS_register  -  ENTRY ADDED
    [   BINDING]  -  @GS_register  -  Entry.type: 9
    [   BINDING]  -  @GS_register  -  Entry.classname: File
    [   BINDING]  -  @GS_register  -  Entry.filename: file3.txt
    [   BINDING]  -  @GS_register  -  setting filename: file3.txt
    [   BINDING]  -  @GS_register  -  Filename: file3.txt
    [   BINDING]  -  @GS_register  - Result is 0
    [   BINDING]  -  @GS_register  -  Ref: 0x7ffea17719f0
    [   BINDING]  -  @GS_register  -  ENTRY FOUND
    [   BINDING]  -  @GS_register  -  Entry.type: 9
    [   BINDING]  -  @GS_register  -  Entry.classname: File
    [   BINDING]  -  @GS_register  -  Entry.filename: file1.txt
    [   BINDING]  -  @GS_register  -  setting filename: file1.txt
    [   BINDING]  -  @GS_register  -  Filename: file1.txt
    [   BINDING]  -  @GS_register  - Result is 0
    [   BINDING]  -  @GS_register  -  Ref: 0x7ffea17719f8
    [   BINDING]  -  @GS_register  -  ENTRY FOUND
    [   BINDING]  -  @GS_register  -  Entry.type: 9
    [   BINDING]  -  @GS_register  -  Entry.classname: File
    [   BINDING]  -  @GS_register  -  Entry.filename: file2.txt
    [   BINDING]  -  @GS_register  -  setting filename: file2.txt
    [   BINDING]  -  @GS_register  -  Filename: file2.txt
    [   BINDING]  -  @GS_register  - Result is 0
    [   BINDING]  -  @GS_register  -  Ref: 0x7ffea1771a00
    [   BINDING]  -  @GS_register  -  ENTRY FOUND
    [   BINDING]  -  @GS_register  -  Entry.type: 9
    [   BINDING]  -  @GS_register  -  Entry.classname: File
    [   BINDING]  -  @GS_register  -  Entry.filename: file3.txt
    [   BINDING]  -  @GS_register  -  setting filename: file3.txt
    [   BINDING]  -  @GS_register  -  Filename: file3.txt
    [   BINDING]  -  @GS_register  - Result is 0
    [   BINDING]  -  @GS_register  -  Ref: 0x7ffea17719f0
    [   BINDING]  -  @GS_register  -  ENTRY FOUND
    [   BINDING]  -  @GS_register  -  Entry.type: 9
    [   BINDING]  -  @GS_register  -  Entry.classname: File
    [   BINDING]  -  @GS_register  -  Entry.filename: file1.txt
    [   BINDING]  -  @GS_register  -  setting filename: file1.txt
    [   BINDING]  -  @GS_register  -  Filename: file1.txt
    [   BINDING]  -  @GS_register  - Result is 0
    [   BINDING]  -  @GS_register  -  Ref: 0x7ffea17719f8
    [   BINDING]  -  @GS_register  -  ENTRY FOUND
    [   BINDING]  -  @GS_register  -  Entry.type: 9
    [   BINDING]  -  @GS_register  -  Entry.classname: File
    [   BINDING]  -  @GS_register  -  Entry.filename: file2.txt
    [   BINDING]  -  @GS_register  -  setting filename: file2.txt
    [   BINDING]  -  @GS_register  -  Filename: file2.txt
    [   BINDING]  -  @GS_register  - Result is 0
    [   BINDING]  -  @GS_register  -  Ref: 0x7ffea1771a00
    [   BINDING]  -  @GS_register  -  ENTRY FOUND
    [   BINDING]  -  @GS_register  -  Entry.type: 9
    [   BINDING]  -  @GS_register  -  Entry.classname: File
    [   BINDING]  -  @GS_register  -  Entry.filename: file3.txt
    [   BINDING]  -  @GS_register  -  setting filename: file3.txt
    [   BINDING]  -  @GS_register  -  Filename: file3.txt
    [   BINDING]  -  @GS_register  - Result is 0
    [   BINDING]  -  @GS_register  -  Ref: 0x7ffea17719f0
    [   BINDING]  -  @GS_register  -  ENTRY FOUND
    [   BINDING]  -  @GS_register  -  Entry.type: 9
    [   BINDING]  -  @GS_register  -  Entry.classname: File
    [   BINDING]  -  @GS_register  -  Entry.filename: file1.txt
    [   BINDING]  -  @GS_register  -  setting filename: file1.txt
    [   BINDING]  -  @GS_register  -  Filename: file1.txt
    [   BINDING]  -  @GS_register  - Result is 0
    [   BINDING]  -  @GS_register  -  Ref: 0x7ffea17719f8
    [   BINDING]  -  @GS_register  -  ENTRY FOUND
    [   BINDING]  -  @GS_register  -  Entry.type: 9
    [   BINDING]  -  @GS_register  -  Entry.classname: File
    [   BINDING]  -  @GS_register  -  Entry.filename: file2.txt
    [   BINDING]  -  @GS_register  -  setting filename: file2.txt
    [   BINDING]  -  @GS_register  -  Filename: file2.txt
    [   BINDING]  -  @GS_register  - Result is 0
    [   BINDING]  -  @GS_register  -  Ref: 0x7ffea1771a00
    [   BINDING]  -  @GS_register  -  ENTRY FOUND
    [   BINDING]  -  @GS_register  -  Entry.type: 9
    [   BINDING]  -  @GS_register  -  Entry.classname: File
    [   BINDING]  -  @GS_register  -  Entry.filename: file3.txt
    [   BINDING]  -  @GS_register  -  setting filename: file3.txt
    [   BINDING]  -  @GS_register  -  Filename: file3.txt
    [   BINDING]  -  @GS_register  - Result is 0
    [   BINDING]  -  @GS_register  -  Ref: 0x7ffea17719f0
    [   BINDING]  -  @GS_register  -  ENTRY FOUND
    [   BINDING]  -  @GS_register  -  Entry.type: 9
    [   BINDING]  -  @GS_register  -  Entry.classname: File
    [   BINDING]  -  @GS_register  -  Entry.filename: file1.txt
    [   BINDING]  -  @GS_register  -  setting filename: file1.txt
    [   BINDING]  -  @GS_register  -  Filename: file1.txt
    [   BINDING]  -  @GS_register  - Result is 0
    [   BINDING]  -  @GS_register  -  Ref: 0x7ffea17719f8
    [   BINDING]  -  @GS_register  -  ENTRY FOUND
    [   BINDING]  -  @GS_register  -  Entry.type: 9
    [   BINDING]  -  @GS_register  -  Entry.classname: File
    [   BINDING]  -  @GS_register  -  Entry.filename: file2.txt
    [   BINDING]  -  @GS_register  -  setting filename: file2.txt
    [   BINDING]  -  @GS_register  -  Filename: file2.txt
    [   BINDING]  -  @GS_register  - Result is 0
    [   BINDING]  -  @GS_register  -  Ref: 0x7ffea1771a00
    [   BINDING]  -  @GS_register  -  ENTRY FOUND
    [   BINDING]  -  @GS_register  -  Entry.type: 9
    [   BINDING]  -  @GS_register  -  Entry.classname: File
    [   BINDING]  -  @GS_register  -  Entry.filename: file3.txt
    [   BINDING]  -  @GS_register  -  setting filename: file3.txt
    [   BINDING]  -  @GS_register  -  Filename: file3.txt
    [   BINDING]  -  @GS_register  - Result is 0
    [   BINDING]  -  @GS_register  -  Ref: 0x7ffea17719f0
    [   BINDING]  -  @GS_register  -  ENTRY FOUND
    [   BINDING]  -  @GS_register  -  Entry.type: 9
    [   BINDING]  -  @GS_register  -  Entry.classname: File
    [   BINDING]  -  @GS_register  -  Entry.filename: file1.txt
    [   BINDING]  -  @GS_register  -  setting filename: file1.txt
    [   BINDING]  -  @GS_register  -  Filename: file1.txt
    [   BINDING]  -  @GS_register  - Result is 0
    [   BINDING]  -  @GS_register  -  Ref: 0x7ffea17719f8
    [   BINDING]  -  @GS_register  -  ENTRY FOUND
    [   BINDING]  -  @GS_register  -  Entry.type: 9
    [   BINDING]  -  @GS_register  -  Entry.classname: File
    [   BINDING]  -  @GS_register  -  Entry.filename: file2.txt
    [   BINDING]  -  @GS_register  -  setting filename: file2.txt
    [   BINDING]  -  @GS_register  -  Filename: file2.txt
    [   BINDING]  -  @GS_register  - Result is 0
    [   BINDING]  -  @GS_register  -  Ref: 0x7ffea1771a00
    [   BINDING]  -  @GS_register  -  ENTRY FOUND
    [   BINDING]  -  @GS_register  -  Entry.type: 9
    [   BINDING]  -  @GS_register  -  Entry.classname: File
    [   BINDING]  -  @GS_register  -  Entry.filename: file3.txt
    [   BINDING]  -  @GS_register  -  setting filename: file3.txt
    [   BINDING]  -  @GS_register  -  Filename: file3.txt
    [   BINDING]  -  @GS_register  - Result is 0
    [   BINDING]  -  @GS_register  -  Ref: 0x7ffea17719f0
    [   BINDING]  -  @GS_register  -  ENTRY FOUND
    [   BINDING]  -  @GS_register  -  Entry.type: 9
    [   BINDING]  -  @GS_register  -  Entry.classname: File
    [   BINDING]  -  @GS_register  -  Entry.filename: file1.txt
    [   BINDING]  -  @GS_register  -  setting filename: file1.txt
    [   BINDING]  -  @GS_register  -  Filename: file1.txt
    [   BINDING]  -  @GS_register  - Result is 0
    [   BINDING]  -  @GS_register  -  Ref: 0x7ffea17719f8
    [   BINDING]  -  @GS_register  -  ENTRY FOUND
    [   BINDING]  -  @GS_register  -  Entry.type: 9
    [   BINDING]  -  @GS_register  -  Entry.classname: File
    [   BINDING]  -  @GS_register  -  Entry.filename: file2.txt
    [   BINDING]  -  @GS_register  -  setting filename: file2.txt
    [   BINDING]  -  @GS_register  -  Filename: file2.txt
    [   BINDING]  -  @GS_register  - Result is 0
    [   BINDING]  -  @GS_register  -  Ref: 0x7ffea1771a00
    [   BINDING]  -  @GS_register  -  ENTRY FOUND
    [   BINDING]  -  @GS_register  -  Entry.type: 9
    [   BINDING]  -  @GS_register  -  Entry.classname: File
    [   BINDING]  -  @GS_register  -  Entry.filename: file3.txt
    [   BINDING]  -  @GS_register  -  setting filename: file3.txt
    [   BINDING]  -  @GS_register  -  Filename: file3.txt
    [   BINDING]  -  @GS_register  - Result is 0
    [   BINDING]  -  @GS_register  -  Ref: 0x7ffea17719f0
    [   BINDING]  -  @GS_register  -  ENTRY FOUND
    [   BINDING]  -  @GS_register  -  Entry.type: 9
    [   BINDING]  -  @GS_register  -  Entry.classname: File
    [   BINDING]  -  @GS_register  -  Entry.filename: file1.txt
    [   BINDING]  -  @GS_register  -  setting filename: file1.txt
    [   BINDING]  -  @GS_register  -  Filename: file1.txt
    [   BINDING]  -  @GS_register  - Result is 0
    [   BINDING]  -  @GS_register  -  Ref: 0x7ffea17719f8
    [   BINDING]  -  @GS_register  -  ENTRY FOUND
    [   BINDING]  -  @GS_register  -  Entry.type: 9
    [   BINDING]  -  @GS_register  -  Entry.classname: File
    [   BINDING]  -  @GS_register  -  Entry.filename: file2.txt
    [   BINDING]  -  @GS_register  -  setting filename: file2.txt
    [   BINDING]  -  @GS_register  -  Filename: file2.txt
    [   BINDING]  -  @GS_register  - Result is 0
    [   BINDING]  -  @GS_register  -  Ref: 0x7ffea1771a00
    [   BINDING]  -  @GS_register  -  ENTRY FOUND
    [   BINDING]  -  @GS_register  -  Entry.type: 9
    [   BINDING]  -  @GS_register  -  Entry.classname: File
    [   BINDING]  -  @GS_register  -  Entry.filename: file3.txt
    [   BINDING]  -  @GS_register  -  setting filename: file3.txt
    [   BINDING]  -  @GS_register  -  Filename: file3.txt
    [   BINDING]  -  @GS_register  - Result is 0
    [   BINDING]  -  @GS_register  -  Ref: 0x7ffea17719f0
    [   BINDING]  -  @GS_register  -  ENTRY FOUND
    [   BINDING]  -  @GS_register  -  Entry.type: 9
    [   BINDING]  -  @GS_register  -  Entry.classname: File
    [   BINDING]  -  @GS_register  -  Entry.filename: file1.txt
    [   BINDING]  -  @GS_register  -  setting filename: file1.txt
    [   BINDING]  -  @GS_register  -  Filename: file1.txt
    [   BINDING]  -  @GS_register  - Result is 0
    [   BINDING]  -  @GS_register  -  Ref: 0x7ffea17719f8
    [   BINDING]  -  @GS_register  -  ENTRY FOUND
    [   BINDING]  -  @GS_register  -  Entry.type: 9
    [   BINDING]  -  @GS_register  -  Entry.classname: File
    [   BINDING]  -  @GS_register  -  Entry.filename: file2.txt
    [   BINDING]  -  @GS_register  -  setting filename: file2.txt
    [   BINDING]  -  @GS_register  -  Filename: file2.txt
    [   BINDING]  -  @GS_register  - Result is 0
    [   BINDING]  -  @GS_register  -  Ref: 0x7ffea1771a00
    [   BINDING]  -  @GS_register  -  ENTRY FOUND
    [   BINDING]  -  @GS_register  -  Entry.type: 9
    [   BINDING]  -  @GS_register  -  Entry.classname: File
    [   BINDING]  -  @GS_register  -  Entry.filename: file3.txt
    [   BINDING]  -  @GS_register  -  setting filename: file3.txt
    [   BINDING]  -  @GS_register  -  Filename: file3.txt
    [   BINDING]  -  @GS_register  - Result is 0
    [   BINDING]  -  @GS_register  -  Ref: 0x7ffea17719f0
    [   BINDING]  -  @GS_register  -  ENTRY FOUND
    [   BINDING]  -  @GS_register  -  Entry.type: 9
    [   BINDING]  -  @GS_register  -  Entry.classname: File
    [   BINDING]  -  @GS_register  -  Entry.filename: file1.txt
    [   BINDING]  -  @GS_register  -  setting filename: file1.txt
    [   BINDING]  -  @GS_register  -  Filename: file1.txt
    [   BINDING]  -  @GS_register  - Result is 0
    [   BINDING]  -  @GS_register  -  Ref: 0x7ffea17719f8
    [   BINDING]  -  @GS_register  -  ENTRY FOUND
    [   BINDING]  -  @GS_register  -  Entry.type: 9
    [   BINDING]  -  @GS_register  -  Entry.classname: File
    [   BINDING]  -  @GS_register  -  Entry.filename: file2.txt
    [   BINDING]  -  @GS_register  -  setting filename: file2.txt
    [   BINDING]  -  @GS_register  -  Filename: file2.txt
    [   BINDING]  -  @GS_register  - Result is 0
    [   BINDING]  -  @GS_register  -  Ref: 0x7ffea1771a00
    [   BINDING]  -  @GS_register  -  ENTRY FOUND
    [   BINDING]  -  @GS_register  -  Entry.type: 9
    [   BINDING]  -  @GS_register  -  Entry.classname: File
    [   BINDING]  -  @GS_register  -  Entry.filename: file3.txt
    [   BINDING]  -  @GS_register  -  setting filename: file3.txt
    [   BINDING]  -  @GS_register  -  Filename: file3.txt
    [   BINDING]  -  @GS_register  - Result is 0
    [   BINDING]  -  @compss_wait_on  -  Entry.type: 9
    [   BINDING]  -  @compss_wait_on  -  Entry.classname: File
    [   BINDING]  -  @compss_wait_on  -  Entry.filename: file1.txt
    [   BINDING]  -  @compss_wait_on  -  Runtime filename: /home/compss/.COMPSs/increment_01/tmpFiles/d1v11_1479142004112.IT
    [   BINDING]  -  @compss_wait_on  -  File renaming: /home/compss/.COMPSs/increment_01/tmpFiles/d1v11_1479142004112.IT to file1.txt
    [   BINDING]  -  @compss_wait_on  -  Entry.type: 9
    [   BINDING]  -  @compss_wait_on  -  Entry.classname: File
    [   BINDING]  -  @compss_wait_on  -  Entry.filename: file2.txt
    [   BINDING]  -  @compss_wait_on  -  Runtime filename: /home/compss/.COMPSs/increment_01/tmpFiles/d2v11_1479142004112.IT
    [   BINDING]  -  @compss_wait_on  -  File renaming: /home/compss/.COMPSs/increment_01/tmpFiles/d2v11_1479142004112.IT to file2.txt
    [   BINDING]  -  @compss_wait_on  -  Entry.type: 9
    [   BINDING]  -  @compss_wait_on  -  Entry.classname: File
    [   BINDING]  -  @compss_wait_on  -  Entry.filename: file3.txt
    [   BINDING]  -  @compss_wait_on  -  Runtime filename: /home/compss/.COMPSs/increment_01/tmpFiles/d3v11_1479142004112.IT
    [   BINDING]  -  @compss_wait_on  -  File renaming: /home/compss/.COMPSs/increment_01/tmpFiles/d3v11_1479142004112.IT to file3.txt
    Final counter values:
    - Counter1 value is 2
    - Counter2 value is 3
    - Counter3 value is 4
    [(4288)    API]  -  Execution Finished

    ------------------------------------------------------------

By running the *compss_gengraph* command users can obtain the task
graph of the above execution. Next we provide the set of commands to
obtain the graph show in :numref:`increment_c`.

.. code-block:: console

    compss@bsc:~$ cd ~/.COMPSs/increment_01/monitor/
    compss@bsc:~/.COMPSs/increment_01/monitor$ compss_gengraph complete_graph.dot
    compss@bsc:~/.COMPSs/increment_01/monitor$ evince complete_graph.pdf

.. figure:: ./Figures/increment_graph.jpeg
   :name: increment_c
   :alt: C increment tasks graph
   :align: center
   :width: 25.0%

   C increment tasks graph
