Task Selection
~~~~~~~~~~~~~~

As in the case of Java, a COMPSs Python application is a Python
sequential program that contains calls to tasks. In particular, the user
can select as a task:

-  Functions

-  Instance methods: methods invoked on objects.

-  Class methods: static methods belonging to a class.

The task definition in Python is done by means of Python decorators
instead of an annotated interface. In particular, the user needs to add
a ``@task`` decorator that describes the task before the
definition of the function/method.

As an example (:numref:`code_python`), let us assume that the application calls a function
*func*, which receives a file path (string parameter) and an integer
parameter. The code of *func* updates the file.

.. code-block:: python
    :name: code_python
    :caption: Python application example

    def func(file_path, value):
        # update the file 'file_path'

    def main():
        my_file = '/tmp/sample_file.txt'
        func(my_file, 1)

    if __name__ == '__main__':
        main()


In order to select ``func`` as a task, the corresponding ``@task``
decorator needs to be placed right before the definition of the
function, providing some metadata about the parameters of that function.
The ``@task`` decorator has to be imported from the *pycompss*
library (:numref:`task_import_python`).

.. code-block:: python
    :name: task_import_python
    :caption: Python task import

    from pycompss.api.task import task

    @task()
    def func():
         ...

.. TIP::

    The PyCOMPSs task api also provides the ``@task`` decorator in camelcase
    (``@Task``) with the same functionality.

    The rationale of providing both ``@task`` and ``@Task`` relies on following
    the PEP8 naming convention. Decorators are usually defined using lowercase,
    but since the task decorator is implemented following the class pattern,
    its name is also available as camelcase.


Function parameters
^^^^^^^^^^^^^^^^^^^

The *@task* decorator does not interfere with the function parameters,
Consequently, the user can define the function parameters as normal python
functions (:numref:`task_parameters_python`).

.. code-block:: python
    :name: task_parameters_python
    :caption: Task function parameters example

    @task()
    def func(param1, param2):
         ...

The use of *\*args* and *\*\*kwargs* as function parameters is
supported (:numref:`task_args_kwargs_python`).

.. code-block:: python
    :name: task_args_kwargs_python
    :caption: Python task *\*args* and *\*\*kwargs example*

    @task(returns=int)
    def argkwarg_func(*args, **kwargs):
        ...

And even with other parameters, such as usual parameters and *default
defined arguments*. :numref:`task_default_parameters_python` shows an example
of a task with two three parameters (whose one of them (*’s’*) has a default
value), *\*args* and *\*\*kwargs*.

.. code-block:: python
    :name: task_default_parameters_python
    :caption: Python task with default parameters example

    @task(returns=int)
    def multiarguments_func(v, w, s=2, *args, **kwargs):
        ...


Tasks within classes
^^^^^^^^^^^^^^^^^^^^

Functions within classes can also be declared as tasks as normal functions.
The main difference is the existence of the ``self`` parameter which enables
to modify the callee object.

For tasks corresponding to instance methods, by default the task is
assumed to modify the callee object (the object on which the method is
invoked). The programmer can tell otherwise by setting the
*target_direction* argument of the *@task* decorator to *IN*
(:numref:`task_instance_method_python`).

.. code-block:: python
    :name: task_instance_method_python
    :caption: Python instance method example

    class MyClass(object):
        ...
        @task(target_direction=IN)
        def instance_method(self):
            ... # self is NOT modified here

Class methods and static methods can also be declared as tasks. The only
requirement is to place the ``@classmethod`` or ``@staticmethod`` over
the *@task* decorator (:numref:`task_classmethod_instancemethod_python`).
Note that there is no need to use the *target_direction* flag within the
*@task* decorator.

.. code-block:: python
    :name: task_classmethod_instancemethod_python
    :caption: Python ``@classmethod`` and ``@staticmethod`` tasks example

    class MyClass(object):
        ...
        @classmethod
        @task()
        def class_method(cls, a, b, c):
            ...

        @staticmethod
        @task(returns=int)
        def static_method(a, b, c):
            ...

.. TIP::

   Tasks inheritance and overriding supported!!!


.. CAUTION::

   The objects used as task parameters **MUST BE** serializable:

      * Implement the ``__getstate__`` and ``__setstate__`` functions in their
        classes for those objects that are not automatically serializable.
      * The classes must not be declared in the same file that contains the
        main method (``if __name__=='__main__'``) (known pickle issue).

.. IMPORTANT::

   For instances of user-defined classes, the classes of these objects
   should have an empty constructor, otherwise the programmer will not be
   able to invoke task instance methods on those objects (:numref:`user_class_return_python`).

   .. code-block:: python
       :name: user_class_return_python
       :caption: Using user-defined classes as task returns

       # In file utils.py
       from pycompss.api.task import task
       class MyClass(object):
           def __init__(self): # empty constructor
               ...

           @task()
           def yet_another_task(self):
               # do something with the self attributes
               ...

           ...

       # In file main.py
       from pycompss.api.task import task
       from utils import MyClass

       @task(returns=MyClass)
       def ret_func():
           ...
           myc = MyClass()
           ...
           return myc

       def main():
           o = ret_func()
           # invoking a task instance method on a future object can only
           # be done when an empty constructor is defined in the object's
           # class
           o.yet_another_task()

       if __name__=='__main__':
           main()
