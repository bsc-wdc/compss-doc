Container decorator
^^^^^^^^^^^^^^^^^^^

The ``@container`` (or ``@Container``) decorator shall be used to define that a
task is going to be executed within a container (:numref:`container_task_python`).

.. code-block:: python
    :name: container_task_python
    :caption: Container task example

    from pycompss.api.compss import container
    from pycompss.api.task import task
    from pycompss.api.parameter import *
    from pycompss.api.api import compss_wait_on

    @container(engine="DOCKER",
               image="compss/compss")
    @task(returns=1, num=IN, in_str=IN, fin=FILE_IN)
    def container_fun(num, in_str, fin):
        # Sample task body:
        with open(fin, "r") as fd:
            num_lines = len(fd.readlines())
        str_len = len(in_str)
        result = num * str_len * num_lines

        # You can import and use libraries available in the container

        return result

    if __name__=='__main__':
        result = container_fun(5, "hello", "dataset.txt")
        result = compss_wait_on(result)
        print("result: %s" % result)


The *container_fun* task will be executed within the container defined in the
*@container* decorator using the *docker* engine with the compss/compss *image*.
This task is pure python and you can import and use any library available in
the container

This feature allows to use specific containers for tasks where the library
dependencies are met.

.. TIP::

    Singularity is also supported, and can be selected by setting the engine to
    SINGULARITY:

    .. code-block::

        @container(engine=SINGULARITY)


In addition, the *@container* decorator can be placed on top of the
*@binary*, *@ompss* or *@mpi* decorators. :numref:`container_task_python_binary`
shows how to execute the same example described in the
:ref:`sections/02_app_development/02_python/01_1_task_definition/sections/06_Other_task_types:Binary decorator`
section, but within the ``compss/compss`` container using docker.
This will execute the binary/ompss/mpi binary within the container.


.. code-block:: python
    :name: container_task_python_binary
    :caption: Container binary task example

    from pycompss.api.compss import container
    from pycompss.api.task import task
    from pycompss.api.binary import binary
    from pycompss.api.parameter import *

    @container(engine="DOCKER",
               image="compss/compss")
    @binary(binary="grep", working_dir=".")
    @task(infile={Type:FILE_IN_STDIN}, result={Type:FILE_OUT_STDOUT})
    def grepper():
         pass

    if __name__=='__main__':
        infile = "infile.txt"
        outfile = "outfile.txt"
        grepper("Hi", infile, outfile)
