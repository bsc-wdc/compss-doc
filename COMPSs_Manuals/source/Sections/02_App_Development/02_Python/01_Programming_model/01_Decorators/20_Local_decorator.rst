@local
======

The *@local* decorator is used to declare that a function requires to
synchronize any of its parameters automatically.

Besides the synchronization API functions, the programmer has also a
decorator for automatic function parameters synchronization at his
disposal. The *@local* decorator can be placed over functions
that are not decorated as tasks, but that may receive results from
tasks (:numref:`local_python_deco`). In this case, the *@local* decorator synchronizes the
necessary parameters in order to continue with the function execution
without the need of using explicitly the *compss_wait_on* call for
each parameter.

.. code-block:: python
    :name: local_python_deco
    :caption: @local decorator example

    from pycompss.api.task import task
    from pycompss.api.api import compss_wait_on
    from pycompss.api.parameter import INOUT
    from pycompss.api.local import local

    @task(v=INOUT)
    def append_three_ones(v):
        v += [1, 1, 1]

    @local
    def scale_vector(v, k):
        return [k*x for x in v]

    if __name__=='__main__':
        v = [1,2,3]
        append_three_ones(v)
        # v is automatically synchronized when calling the scale_vector function.
        w = scale_vector(v, 2)




