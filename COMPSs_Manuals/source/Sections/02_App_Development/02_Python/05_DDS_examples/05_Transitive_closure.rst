Transitive closure
------------------

The Transitive Closure application is a Python application that calculates
the reachability matrix of a directed graph.

Given a directed graph, the transitive closure application finds out if a
vertex *j* is reachable from another vertex *i* for all vertex pairs *(i, j)*
in the given graph.
Reachable means that there is a path from vertex *i* to *j*.
The reachability matrix is called the transitive closure of a graph.

In this example, we provide the transitive closure implementation using the DDS interface:


.. code-block:: python
    :name: code_transitive_closure_dds_pycompss
    :caption: Transitive closure application using DDS interface (``transitive_closure_dds.py``)

    import sys
    import random
    from pycompss.dds import DDS


    def _generate_graph():
        """Generate graph.

        :returns: Set of edges.
        """
        num_edges = 10
        num_vertices = 5
        rand = random.Random(42)

        edges = set()
        while len(edges) < num_edges:
            src = rand.randrange(0, num_vertices)
            dst = rand.randrange(0, num_vertices)
            if src != dst:
                edges.add((src, dst))
        return edges


    def transitive_closure(partitions=2):
        """Transitive closure.

        :param partitions: Number of partitions.
        :results: Transitive closure result.
        """
        edges = _generate_graph()
        od = DDS().load(edges, partitions).collect(future_objects=True)

        # Because join() joins on keys, the edges are stored in reversed order.
        edges = DDS().load(od, -1).map(lambda x_y: (x_y[1], x_y[0]))

        next_count = DDS().load(od, -1).count()

        while True:
            old_count = next_count
            # Perform the join, obtaining an RDD of (y, (z, x)) pairs,
            # then project the result to obtain the new (x, z) paths.
            new_edges = (
                DDS().load(od, -1).join(edges).map(lambda __a_b: (__a_b[1][1], __a_b[1][0]))
            )
            od = DDS().load(od, -1).union(new_edges).distinct().collect(future_objects=True)

            next_count = DDS().load(od, -1).count()

            if next_count == old_count:
                break

        print(f"TC has {next_count} edges")


    if __name__ == "__main__":
        transitive_closure()


The transitive closure application can be executed by invoking the ``runcompss`` command
without parameters.
The following line provide an example of its execution.

.. code-block:: console

    compss@bsc:~$ runcompss --graph transitive_closure_dds.py
    [ INFO ] Inferred PYTHON language
    [ INFO ] Using default location for project file: /opt/COMPSs//Runtime/configuration/xml/projects/default_project.xml
    [ INFO ] Using default location for resources file: /opt/COMPSs//Runtime/configuration/xml/resources/default_resources.xml
    [ INFO ] Using default execution type: compss

    ----------------- Executing transitive_closure.py --------------------------

    WARNING: COMPSs Properties file is null. Setting default values
    [(661)    API]  -  Starting COMPSs Runtime v3.2.rc2308 (build 20230810-0858.rababfc59af07237e625a2cb93b033ae427343b5f)
    TC has 20 edges
    [(12610)    API]  -  Execution Finished

    ------------------------------------------------------------



:numref:`transitive_closure_dds_python` depicts the generated task dependency graph.

.. figure:: ./Figures/transitive_closure_dds_graph.png
   :name: transitive_closure_dds_python
   :alt: Python transitive closure using DDS interface tasks graph
   :align: center
   :width: 100.0%

   Python transitive closure using DDS interface tasks graph
