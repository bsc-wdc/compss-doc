Simple
------

The Simple application is a Python application that increases a counter
by means of a task. The counter is stored inside a file that is
transferred to the worker when the task is executed. Next, we provide the
main code and the task declaration:

.. code-block:: python

    from pycompss.api.task import task
    from pycompss.api.parameter import FILE_INOUT


    @task(filePath=FILE_INOUT)
    def increment(filePath):
        # Read value
        fis = open(filePath, "r")
        value = fis.read()
        fis.close()

        # Write value
        fos = open(filePath, "w")
        fos.write(str(int(value) + 1))
        fos.close()


    def main_program():
        from pycompss.api.api import compss_open

        # Check and get parameters
        if len(sys.argv) != 2:
            exit(-1)
        initialValue = sys.argv[1]

        fileName = "counter"

        # Write value
        fos = open(fileName, "w")
        fos.write(initialValue)
        fos.close()
        print("Initial counter value is %s" % str(initialValue))

        # Execute increment
        increment(fileName)

        # Write new value
        fis = compss_open(fileName, "r+")
        finalValue = fis.read()
        fis.close()
        print("Final counter value is %s" % str(finalValue))


    if __name__ == "__main__":
        main_program()


The simple application can be executed by invoking the ``runcompss`` command
with the application file name and the initial counter value.

The following lines provide an example of its execution.

.. code-block:: console

    compss@bsc:~$ runcompss simple.py 1
    [ INFO ] Inferred PYTHON language
    [ INFO ] Using default location for project file: /opt/COMPSs//Runtime/configuration/xml/projects/default_project.xml
    [ INFO ] Using default location for resources file: /opt/COMPSs//Runtime/configuration/xml/resources/default_resources.xml
    [ INFO ] Using default execution type: compss

    ----------------- Executing simple.py --------------------------

    WARNING: COMPSs Properties file is null. Setting default values
    [(983)    API]  -  Starting COMPSs Runtime v3.3 (build 20231107-1626.rfd920cb7d4a03b1e84725271049e91f5de261e8c)
    Initial counter value is 1
    Final counter value is 2
    [(9286)    API]  -  Execution Finished

    ------------------------------------------------------------
