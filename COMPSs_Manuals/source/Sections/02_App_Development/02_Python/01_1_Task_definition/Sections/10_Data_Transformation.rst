.. spelling:word-list::

    dt

Data Transformation
~~~~~~~~~~~~~~~~~~~

The *@data_transformation* (or just *@dt*) decorator is used for the execution of a data transformation function that should be applied on a given
```PyCOMPSs task``` parameter. It means, by specifying the parameter name and a python function, users can assure that the parameter will go through
transformation process by the given function. Then the result of the data transformation function will be used in the task instead of the initial
value of the parameter.


Data transformation decorator has a simple order for the definition. The first argument of the decorator is a string name of the parameter we want to
transform. The second argument is the data transformation function (NOT as a string, but actual reference) that expects at least one input which will
the transformation will be applied to. If the transformation function needs more parameters, they can be added to the *@dt* definition as ```kwargs```.

.. code-block:: python
    :name: dt_syntax
    :caption: Arguments list of the data transformation decorator.

    @dt("<parameter_name>", "<dt_function>", "<kwargs_of_dt_function>")
    @task()
    def task_func(...):
        ...


.. IMPORTANT::

    Please note that data transformation definitions should be on top of the *@task* (or *@software*) decorator.


Adding data transformation on top of the ```@software``` or ```@task``` decorator allows the PyCOMPSs Runtime generate an intermediate task. This task method applies the given DT
to the given input and the output is sent to the *original* task as the input. Following code snippet is an example of basic usage of the *@dt* decorator:


.. code-block:: python
    :name: dt_basic
    :caption: Basic Data Transformation code example.

    import numpy as np
    from pycompss.api.data_transformation import dt
    from pycompss.api.software import software
    from pycompss.api.api import compss_wait_on


    @software(config_file="simulation.json")
    def simulation():
        ...
        return a

    def reshape(A, new_x, new_y):
        return A.reshape((new_x, new_y))

    @dt("input_data", reshape, new_x=10, new_y=100)
    @software("data_analysis.json")
    def data_analysis(input_data):
        ...
        return result

    def main():
        A = simulation()
        result = data_analysis(A)
        result = compss_wait_on(result)
        print(result)


As we can see in the example, the result of "some_task" function is assigned to the parameter A. In the next line when "dt_example" is called, before the task execution,
parameter A will go through the "dt_function" where "new_x" and "new_y" will be 10 and 100 respectively. Once the execution of the Data Transformation task is finished, the result
will be passed to the "dt_example" task as input.


PyCOMPSs also supports inter-types data transformations which allows the conversion of the input data to another object type. For example, if the user wants to use
a object's serialized file as an input for a task, but the task function expects the object itself, then ```@dt``` can take care of it. So far PyCOMPSs supports this kind
of data transformations only for the ```FILE```, ```OBJECT``` and ```COLLECTION``` types.

For the cases where type conversions happen, there are some mandatory and optional parameters:

    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | Parameter              | Description                                                                                                                             |
    +========================+=========================================================================================================================================+
    | **target**             | (Mandatory) Name of the input parameter that DT will be applied to.                                                                     |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **function**           | (Mandatory) The data transformation function.                                                                                           |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **type**               | (Mandatory) Type of the DT (e.g. FILE_TO_OBJECT)                                                                                        |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **destination**        | If the output of the DT is a file, then output file name can be specified as "destination".                                             |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **size**               | (Mandatory only if the output of the DT is a COLLECTION) Size of the output COLLECTION.                                                 |
    +------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+


In the example below we can see a code snippet where the Data Transformation task deserializes a file and assigns it to the input parameter. That's why it's *type* is
```FILE_TO_OBJECT```:


.. code-block:: python
    :name: dt_fto
    :caption: Data Transformation with type conversion.

    from pycompss.api.data_transformation import *
    from pycompss.api.task import task
    from pycompss.api.parameter import FILE_OUT
    from pycompss.api.api import compss_wait_on

    @task(result_file=FILE_OUT)
    def generate(result_file):
        ...

    def deserialize(some_file):
        # deserialize the file
        ...
        return deserialized_object

    @dt(target="input", function=deserialize, type=FILE_TO_OBJECT)
    @software("example.json")
    def simulation(input):
        # 'input' is deserialized object from its initial file path
        ...

    def main(self):
        some_file = "src/some_file"
        generate(some_file)
        result = simulation(some_file)
        result = compss_wait_on(result)


If the user wants to use a workflow as a data transformation function and thus avoid the intermediate task creation, PyCOMPSs provides the ```is_workflow```
argument to do so (by default *False*). This gives the flexibility of importing workflow from different libraries.


It is possible to define multiple data transformations for the same parameter, as well as for the multiple parameters of the same task. In both
cases each data transformation with "is_workflow=False" will take place in a different task (in the order of the definition from top to bottom):


.. code-block:: python
    :name: dt_multiple
    :caption: Multiple data transformations on top of a @software function.

    import dislib as ds
    from pycompss.api.data_transformation import *
    from pycompss.api.task import task
    from pycompss.api.api import compss_wait_on

    def load_w_dislib(file_path, blocK_size=10):
        obj = ds.load_txt_file(file_path, block_size)
        ...
        return obj

    def extract_columns(input):
        # modifies input
        ...
        return input

    def scale_by_x(input, rate=100):
        # modifies input
        ...
        return input

    @dt(target="A", function=load_w_dislib, type=FILE_TO_OBJECT, is_workflow=True)
    @dt("A", extract_columns, is_workflow=False)
    @dt(target="B", function=load_w_dislib, type=FILE_TO_OBJECT, is_workflow=True)
    @dt("B", scale_by_x, rate=5)
    @software("workflow.json")
    def run_simulation(A, B):
        # A and B are both loaded from text files using "dislib" and modified
        ...

    def main():
        first_file = "src/file_A"
        second_file = "src/file_B"
        run_simulation(first_file, second_file)
        ...


PyCOMPSs API also provides Data Transformation Object class which gives the flexibility of the data transformation definitions. Any task function can be
decorated with an empty **@dt** and simply by passing *DTO*\(s) as a task parameter the user can achieve the same behavior. Same as the decorator itself, DTO
accepts the arguments in the same order (*"<parameter_name>", "<dt_function>", "<kwargs_of_dt_function>"*). A list of DTO objects is also accepted for the same or
various parameters:


.. code-block:: python
    :name: dt_dto
    :caption: Data Transformation Object example.

    import dislib as ds

    from pycompss.api.data_transformation import dto
    from pycompss.api.data_transformation import dt
    from pycompss.api.task import task
    from pycompss.api.api import compss_wait_on


    @dt()
    @task(returns=obj)
    def run_simulation(A, B):
        ...

    def scale(A):
        # modifies A
        ...
        return A

    def main():
        # initialize inputs
        A = ds.load_txt_file(...)
        B = ds.load_txt_file(...)

        # create Data Transformation Objects
        dt_1 = dto("A", scale)
        dt_2 = dto("B", scale, is_workflow=False)

        # send DT Objects to the task function as input
        result = run_simulation(A, B, dt=[dt_1, dt_2]))
        result = cwo(result)
