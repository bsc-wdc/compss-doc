@reduction
==========

The *@reduction* (or @Reduction) decorator shall be used to define that a task
is going to be subdivided into smaller tasks that take as input
a subset of the input data (one ``COLLECTION``).

Definition
----------

The only supported parameter is *chunk_size*, used to define the
size of the data that the generated tasks will get as input parameter.
The data given as input to the main reduction task is subdivided into chunks
of the set size.

:numref:`reduction_task_python` shows how to declare a reduction task.
In detail, this application calls 10 times to ``calculate_area`` and appends
the results into ``areas`` list. Then, invokes the ``sum_reduction`` task (that
is declared as a reduction task) with the ``areas`` list and has ``chunk_size=2``.
Although it is invoked once, the COMPSs runtime splits the input data (``areas``)
into chunks of 2 elements, and applies the ``sum_reduction`` function to them
until the final result is achieved.
Then, the ``compss_wait_on`` retrieves the final result and it is printed.

.. code-block:: python
    :name: reduction_task_python
    :caption: Reduction task example

    from pycompss.api.reduction import reduction
    from pycompss.api.task import task
    from pycompss.api.parameter import COLLECTION_IN
    from pycompss.api.api import compss_wait_on


    @task(returns=int)
    def calculate_area(height, width):
        return height * width


    @reduction(chunk_size="2")
    @task(returns=int, areas=COLLECTION_IN)
    def sum_reduction(areas):
        total_area = 0
        for area in areas:
            total_area += area
        return total_area


    def main():
        areas = []
        for i in range(10):
            areas.append(calculate_area(i, i))
        result = sum_reduction(areas)
        result = compss_wait_on(result)
        print("Result: %d" % result)


    if __name__ == "__main__":
        main()


.. CAUTION::

    The task decorated with ``@reduction`` can have multiple parameters, but
    **ONLY ONE** ``COLLECTION_IN`` **parameter**, which will be split into
    chunks to perform the reduction.
