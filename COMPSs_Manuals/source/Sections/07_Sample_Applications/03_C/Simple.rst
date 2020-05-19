Simple
------

The Simple application is a C application that increases a counter by
means of a task. The counter is stored inside a file that is transfered
to the worker when the task is executed. Thus, the tasks inferface is
defined as follows:

.. code-block:: C

      // simple.idl
      interface simple {
    	  void increment(inout File filename);
      };

Next we also provide the invocation of the task from the main code and
the increment’s method code.

.. code-block:: C

      // simple.cc

      int main(int argc, char *argv[]) {
          // Check and get parameters
          if (argc != 2) {
    	  usage();
    	  return -1;
          }
          string initialValue = argv[1];
          file fileName = strdup(FILE_NAME);

          // Init compss
          compss_on();

          // Write file
          ofstream fos (fileName);
          if (fos.is_open()) {
    	  fos << initialValue << endl;
    	  fos.close();
          } else {
    	  cerr << "[ERROR] Unable to open file" << endl;
    	  return -1;
          }
          cout << "Initial counter value is " << initialValue << endl;

          // Execute increment
          increment(&fileName);

          // Read new value
          string finalValue;
          ifstream fis;
          compss_ifstream(fileName, fis);
          if (fis.is_open()) {
    	  if (getline(fis, finalValue)) {
    	      cout << "Final counter value is " << finalValue << endl;
    	      fis.close();
    	  } else {
    	      cerr << "[ERROR] Unable to read final value" << endl;
    	      fis.close();
    	      return -1;
    	  }
          } else {
    	  cerr << "[ERROR] Unable to open file" << endl;
    	  return -1;
          }

          // Close COMPSs and end
          compss_off();
          return 0;
      }

.. code-block:: C

      //simple-functions.cc

      void increment(file *fileName) {
          cout << "INIT TASK" << endl;
          cout << "Param: " << *fileName << endl;
          // Read value
          char initialValue;
          ifstream fis (*fileName);
          if (fis.is_open()) {
    	  if (fis >> initialValue) {
    	      fis.close();
    	  } else {
    	      cerr << "[ERROR] Unable to read final value" << endl;
    	      fis.close();
    	  }
    	  fis.close();
          } else {
    	  cerr << "[ERROR] Unable to open file" << endl;
          }

          // Increment
          cout << "INIT VALUE: " << initialValue << endl;
          int finalValue = ((int)(initialValue) - (int)('0')) + 1;
          cout << "FINAL VALUE: " << finalValue << endl;

          // Write new value
          ofstream fos (*fileName);
          if (fos.is_open()) {
    	  fos << finalValue << endl;
    	  fos.close();
          } else {
    	  cerr << "[ERROR] Unable to open file" << endl;
          }
          cout << "END TASK" << endl;
      }

Finally, to compile and execute this application users must run the
following commands:

.. code-block:: console

    compss@bsc:~$ cd ~/tutorial_apps/c/simple/
    compss@bsc:~/tutorial_apps/c/simple$ compss_build_app simple
    compss@bsc:~/tutorial_apps/c/simple$ runcompss --lang=c --project=./xml/project.xml --resources=./xml/resources.xml ~/tutorial_apps/c/simple/master/simple 1
    [  INFO] Using default execution type: compss

    ----------------- Executing simple --------------------------

    JVM_OPTIONS_FILE: /tmp/tmp.n2eZjgmDGo
    COMPSS_HOME: /opt/COMPSs
    Args: 1

    WARNING: COMPSs Properties file is null. Setting default values
    [(617)    API]  -  Starting COMPSs Runtime v<version>
    Initial counter value is 1
    [   BINDING]  -  @GS_register  -  Ref: 0x7fffa35d0f48
    [   BINDING]  -  @GS_register  -  ENTRY ADDED
    [   BINDING]  -  @GS_register  -  Entry.type: 9
    [   BINDING]  -  @GS_register  -  Entry.classname: File
    [   BINDING]  -  @GS_register  -  Entry.filename: counter
    [   BINDING]  -  @GS_register  -  setting filename: counter
    [   BINDING]  -  @GS_register  -  Filename: counter
    [   BINDING]  -  @GS_register  - Result is 0
    [   BINDING]  -  @compss_wait_on  -  Entry.type: 9
    [   BINDING]  -  @compss_wait_on  -  Entry.classname: File
    [   BINDING]  -  @compss_wait_on  -  Entry.filename: counter
    [   BINDING]  -  @compss_wait_on  -  Runtime filename: /home/compss/.COMPSs/simple_01/tmpFiles/d1v2_1479141705574.IT
    [   BINDING]  -  @compss_wait_on  -  File renaming: /home/compss/.COMPSs/simple_01/tmpFiles/d1v2_1479141705574.IT to counter
    Final counter value is 2
    [(3755)    API]  -  Execution Finished

    ------------------------------------------------------------
