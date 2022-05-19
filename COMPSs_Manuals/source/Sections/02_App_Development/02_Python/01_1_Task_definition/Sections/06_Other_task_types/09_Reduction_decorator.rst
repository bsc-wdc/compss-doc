Reduction decorator
^^^^^^^^^^^^^^^^^^^

The *@reduction* (or @Reduction) decorator shall be used to define that a task
is going to be subdivided into smaller tasks that take as input
a subset of the input data. (:numref:`reduction_task_python`).

.. code-block:: python
    :name: reduction_task_python
    :caption: Reduction task example

    from pycompss.api.reduction import reduction

    @reduction(chunk_size="2")
    @task()
    def myreduction():
        pass

The only supported parameter is *chunk_size*, used to define the
size of the data that the generated tasks will get as input parameter.
The data given as input to the main reduction task is subdivided into chunks
of the set size.
