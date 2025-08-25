Alternative ways to define dynamic constraints
==============================================

Dynamic constraints can also be defined in various different ways depending on the preferences of the task.

Variable from the arguments
---------------------------

The constraint name needs to match a name of a parameter in the arguments of the function,
this can be useful if you can easily add a new parameter to the function, or if you already pass the desired constraint value to the function.

.. code-block:: python
    :name: dynamic_constraint_argument_task_python
    :caption: dynamic_constraint argument task example

    from pycompss.api.task import task
    from pycompss.api.constraint import constraint

    @constraint(computing_units="comp")
    @task()
    def func(a, b, c, comp):
        c += a + b
        ...

The way you pass the argument can change between function calls including its value.

.. code-block:: python
    :name: dynamic_constraint_argument_task_call_python
    :caption: dynamic_constraint argument task call example

    def main():
        {...}
        func(a, b, c, 2)
        comp = 4
        func(a, b, c, comp)
        func(a, b, c, comp=1)


Evaluation of a regular expression
----------------------------------

All the variable names used in the expression need to match the ones from the function definition.
This way there is no need to add an extra parameter to the function or create a new global variable,
but is only useful if you can get the constraint value you want from the parameters.

.. code-block:: python
    :name: dynamic_constraint_eval_task_python
    :caption: dynamic_constraint eval task example

    from pycompss.api.task import task
    from pycompss.api.constraint import constraint

    @constraint(computing_units="int((a * 2) / c)")
    @task()
    def func(a, b, c):
        c += a + b
        ...

.. code-block:: python
    :name: dynamic_constraint_eval_task_call_python
    :caption: dynamic_constraint eval task call example

    def main():
        {...}
        func(a, b, c)
        a = 2
        func(a, b, c)
        c = 4
        func(a, b, c)

.. IMPORTANT::

     When using evaluation of variables, it is very important the evaluation of the expression returns a usable value for the constraint,
     also be careful when using Future Objects because they cannot be evaluated.
