@container
==========

The ``@container`` (or ``@Container``) decorator shall be used to define that a
task is going to be executed within a container (:numref:`container_task_python`).

Definition
----------

.. code-block:: python
    :name: container_task_python
    :caption: Container task example

    from pycompss.api.container import container
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


The ``container_fun`` task will be executed within the container defined in the
``@container`` decorator using the **DOCKER** engine with the **compss/compss** ``image``.
This task is pure python and you can import and use any library available in
the container. In addition, to these ``@container`` parameters, it is possible
to use the ``options`` parameter with a string containing the desired container
specific flags.

This feature allows to use specific containers for tasks where the library
dependencies are met.

.. TIP::

    In addition to **Docker** container support, **Singularity** and **uDocker** are also
    supported.

    **Singularity container** can be selected by setting the engine to ``"SINGULARITY"``:

    .. code-block::

        @container(engine="SINGULARITY",
                   image="compss")

    Whilst **uDocker container** can be selected by setting the engine to ``"UDOCKER"``:

    .. code-block::

        @container(engine="UDOCKER",
                   image="compss")


.. TIP::

    It is possible to define options for the container engine selected by using
    the ``options`` parameter within the ``@container`` decorator.
    The available options depend on the the container engine selected, and can
    be found on its specific documentation

    For example, it can be used to define a specific mount point using uDocker
    as follows:

    .. code-block::

        @container(engine="UDOCKER",
                   image="compss",
                   options="-v /home/user/mount_directory:/home/user/mount_directory")


In addition, the ``@container`` decorator can be placed on top of the
``@binary``, ``@ompss`` or ``@mpi`` decorators. :numref:`container_task_python_binary`
shows how to execute the same example described in the
:ref:`Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/04_Binary_decorator:@binary`
section, but within the ``compss/compss`` container using Docker.
This will execute the binary/ompss/mpi binary within the container.


.. code-block:: python
    :name: container_task_python_binary
    :caption: Container binary task example

    from pycompss.api.container import container
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


Summary
-------

Next table summarizes the parameters of this decorator. Please note that ``working_dir`` and ``args`` are the only decorator properties that can contain task parameters
defined in curly braces.

+------------------------+------------------------------------------------------------------+
| Parameter              | Description                                                      |
+========================+==================================================================+
| **engine**             |  Container engine to use (e.g. DOCKER or SINGULARITY).           |
+------------------------+------------------------------------------------------------------+
| **image**              |  Container image to be deployed and used for the task execution. |
+------------------------+------------------------------------------------------------------+
