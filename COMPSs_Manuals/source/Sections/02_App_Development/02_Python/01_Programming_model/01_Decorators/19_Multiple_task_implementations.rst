@implements
===========

As in Java COMPSs applications, it is possible to define multiple
implementations for each task. In particular, a programmer can define a
task for a particular purpose, and multiple implementations for that
task with the same objective, but with different constraints (e.g.
specific libraries, hardware, etc). To this end, the *@implement* (or @Implement)
decorator followed with the specific implementations constraints (with
the *@constraint* decorator, see Section [subsubsec:constraints]) needs
to be placed ON TOP of the @task decorator. Although the user only
calls the task that is not decorated with the *@implement* decorator,
when the application is executed in a heterogeneous distributed
environment, the runtime will take into account the constraints on each
implementation and will try to invoke the implementation that fulfills
the constraints within each resource, keeping this management invisible
to the user (:numref:`implements_python`).

Definition
----------

.. code-block:: python
    :name: implements_python
    :caption: Multiple task implementations example

    from pycompss.api.implement import implement

    @implement(source_class="sourcemodule", method="main_func")
    @constraint(app_software="numpy")
    @task(returns=list)
    def myfunctionWithNumpy(list1, list2):
        # Operate with the lists using numpy
        return resultList

    @task(returns=list)
    def main_func(list1, list2):
        # Operate with the lists using built-int functions
        return resultList

Please, note that if the implementation is used to define a binary,
OmpSs, MPI, COMPSs, multinode or reduction task invocation (see
:ref:`Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/XX_Other_task_types:Other task types`),
the @implement decorator must be always on top of the decorators stack,
followed by the @constraint decorator, then the
@binary/\ @ompss/\ @mpi/\ @compss/\ @multinode
decorator, and finally, the @task decorator in the lowest
level.
