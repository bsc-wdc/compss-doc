Task Return
~~~~~~~~~~~

If the function or method returns a value, the programmer can use the
*returns* argument within the *@task* decorator. In this
argument, the programmer can specify the type of that value
(:numref:`task_returns_python`).

.. code-block:: python
    :name: task_returns_python
    :caption: Python task returns example

    @task(returns=int)
    def ret_func():
         return 1

Moreover, if the function or method returns more than one value, the
programmer can specify how many and their type in the *returns*
argument. :numref:`task_multireturn_python` shows how to specify that two
values (an integer and a list) are returned.

.. code-block:: python
    :name: task_multireturn_python
    :caption: Python task with multireturn example

    @task(returns=(int, list))
    def ret_func():
         return 1, [2, 3]

Alternatively, the user can specify the number of return statements as
an integer value (:numref:`task_returns_integer_python`).
This way of specifying the amount of return eases the
*returns* definition since the user does not need to specify explicitly
the type of the return arguments. However, it must be considered that
the type of the object returned when the task is invoked will be a
future object. This consideration may lead to an error if the user
expects to invoke a task defined within an object returned by a previous
task. In this scenario, the solution is to specify explicitly the return
type.

.. code-block:: python
    :name: task_returns_integer_python
    :caption: Python task returns with integer example

    @task(returns=1)
    def ret_func():
         return "my_string"

    @task(returns=2)
    def ret_func():
         return 1, [2, 3]

.. IMPORTANT::

   If the programmer selects as a task a function or method that returns a
   value, that value is not generated until the task executes (:numref:`task_return_value_python`).

   .. code-block:: python
       :name: task_return_value_python
       :caption: Task return value generation

       @task(return=MyClass)
       def ret_func():
           return MyClass(...)

       ...

       if __name__=='__main__':
           o = ret_func()  # o is a future object

   The object returned can be involved in a subsequent task call, and the
   COMPSs runtime will automatically find the corresponding data
   dependency. In the following example, the object *o* is passed as a
   parameter and callee of two subsequent (asynchronous) tasks,
   respectively (:numref:`task_return_value_usage_python`).

   .. code-block:: python
       :name: task_return_value_usage_python
       :caption: Task return value subsequent usage

       if __name__=='__main__':
           # o is a future object
           o = ret_func()

           ...

           another_task(o)

           ...

           o.yet_another_task()

.. TIP::

    PyCOMPSs is able to infer if the task returns something and its amount in
    most cases. Consequently, the user can specify the task without *returns*
    argument. But this is discouraged since it requires code analysis,
    including an overhead that can be avoided by using the *returns* argument.

.. TIP::

    PyCOMPSs is compatible with Python 3 type hinting. So, if type hinting
    is present in the code, PyCOMPSs is able to detect the return type and
    use it (there is no need to use the *returns*):

    .. code-block:: python
        :name: task_returns_type_hinting_python
        :caption: Python task returns with type hinting

        @task()
        def ret_func() -> str:
             return "my_string"

        @task()
        def ret_func() -> (int, list):
             return 1, [2, 3]
