Wordcount
---------

The Wordcount application is a Python application that reads a set of
files and counts the amount of different words on them. In this example,
we provide the wordcount implementation using the DDS interface:


.. code-block:: python
    :name: code_wordcount_dds_pycompss
    :caption: Wordcount application using DDS interface (``wordcount_dds.py``)

    import sys
    import time
    from pycompss.dds import DDS


    def word_count():
        """Word count using DDS.

        :return: None
        """
        path_file = sys.argv[1]
        start = time.time()

        results = (
            DDS()
            .load_files_from_dir(path_file)
            .flat_map(lambda x: x[1].split())
            .map(lambda x: "".join(e for e in x if e.isalnum()))
            .count_by_value(as_dict=True)
        )

        print("Results: " + str(results))
        print("Elapsed Time: ", time.time() - start)


    if __name__ == "__main__":
        word_count()


The wordcount application can be executed by invoking the ``runcompss`` command
with the application file name and a path which contains a set of files.

The following lines provide an example of its execution before generating
a random dataset using the `lorem-text <https://pypi.org/project/lorem-text/>`_ package.

.. code-block:: console

    compss@bsc:~$ pip install lorem-text
    compss@bsc:~$ mkdir dataset
    compss@bsc:~$ for i in {1..10}; do lorem_text --words 100 > dataset/$i.txt; done
    compss@bsc:~$ runcompss --graph wordcount_dds.py $(pwd)/dataset/
    [ INFO ] Inferred PYTHON language
    [ INFO ] Using default location for project file: /opt/COMPSs//Runtime/configuration/xml/projects/default_project.xml
    [ INFO ] Using default location for resources file: /opt/COMPSs//Runtime/configuration/xml/resources/default_resources.xml
    [ INFO ] Using default execution type: compss

    ----------------- Executing wordcount_dds.py --------------------------

    WARNING: COMPSs Properties file is null. Setting default values
    [(620)    API]  -  Starting COMPSs Runtime v3.3 (build 20231107-1626.rfd920cb7d4a03b1e84725271049e91f5de261e8c)
    Results: {'ea': 3, 'est': 6, 'velit': 6, 'reiciendis': 7, 'consequatur': 6, 'reprehenderit': 6, 'magnam': 5, 'similique': 5, 'cumque': 6, 'facere': 5, 'dicta': 3, 'consectetur': 8, 'doloremque': 4, 'vitae': 4, 'perferendis': 6, 'tempora': 5, 'voluptatem': 2, 'possimus': 7, 'aliquid': 10, 'assumenda': 6, 'natus': 6, 'quas': 3, 'molestiae': 6, 'quam': 8, 'enim': 6, 'officiis': 6, 'rem': 4, 'quibusdam': 8, 'repellendus': 7, 'quod': 6, 'praesentium': 7, 'iusto': 5, 'at': 4, 'mollitia': 6, 'qui': 4, 'accusantium': 7, 'nesciunt': 6, 'ipsum': 5, 'excepturi': 6, 'minima': 7, 'eius': 7, 'veritatis': 5, 'pariatur': 6, 'beatae': 6, 'adipisci': 8, 'corporis': 6, 'quae': 8, 'sunt': 8, 'autem': 10, 'optio': 7, 'laboriosam': 10, 'temporibus': 6, 'deleniti': 8, 'nemo': 7, 'distinctio': 7, 'maxime': 6, 'consequuntur': 4, 'odit': 5, 'sit': 5, 'non': 4, 'saepe': 5, 'animi': 6, 'ratione': 5, 'inventore': 7, 'aliquam': 6, 'harum': 6, 'nam': 4, 'in': 5, 'veniam': 9, 'eligendi': 6, 'commodi': 4, 'eum': 5, 'quo': 6, 'quaerat': 8, 'nihil': 6, 'dolores': 4, 'impedit': 5, 'voluptatibus': 5, 'libero': 6, 'quos': 7, 'nobis': 5, 'quidem': 4, 'magni': 6, 'voluptates': 6, 'neque': 4, 'ducimus': 8, 'ex': 6, 'doloribus': 4, 'illo': 6, 'dolor': 9, 'ut': 7, 'totam': 5, 'expedita': 4, 'aperiam': 8, 'provident': 6, 'odio': 10, 'earum': 8, 'nisi': 7, 'cupiditate': 5, 'tempore': 7, 'atque': 4, 'ipsa': 8, 'dolorum': 7, 'aut': 4, 'blanditiis': 4, 'corrupti': 7, 'et': 5, 'soluta': 6, 'tenetur': 5, 'obcaecati': 7, 'placeat': 6, 'sint': 7, 'eveniet': 4, 'accusamus': 6, 'hic': 5, 'illum': 3, 'itaque': 8, 'voluptas': 7, 'laudantium': 5, 'dolorem': 4, 'necessitatibus': 5, 'molestias': 6, 'porro': 4, 'omnis': 5, 'quis': 5, 'id': 6, 'vero': 5, 'sequi': 3, 'recusandae': 7, 'amet': 6, 'numquam': 5, 'iste': 6, 'sed': 8, 'dignissimos': 8, 'facilis': 7, 'a': 5, 'voluptate': 7, 'quia': 6, 'sapiente': 7, 'officia': 6, 'culpa': 7, 'error': 4, 'fugit': 5, 'repellat': 6, 'esse': 5, 'quisquam': 4, 'asperiores': 6, 'repudiandae': 4, 'deserunt': 4, 'dolore': 4, 'quasi': 5, 'minus': 4, 'ipsam': 4, 'architecto': 6, 'nulla': 7, 'fuga': 5, 'suscipit': 6, 'ullam': 5, 'ad': 5, 'nostrum': 3, 'labore': 4, 'aspernatur': 5, 'perspiciatis': 3, 'incidunt': 5, 'modi': 2, 'cum': 5, 'unde': 5, 'ab': 5, 'delectus': 4, 'alias': 1, 'laborum': 5, 'rerum': 5, 'eaque': 4, 'vel': 2, 'maiores': 4, 'explicabo': 2, 'eos': 1, 'debitis': 1, 'exercitationem': 4, 'fugiat': 2, 'iure': 1, 'voluptatum': 2}
    Elapsed Time:  3.730666399002075
    [(7001)    API]  -  Execution Finished

    ------------------------------------------------------------



:numref:`wordcount_dds_python` depicts the generated task dependency graph. The dataset
reading can be identified in the 10 blue tasks, while the white tasks conform a
reduction that accumulates the amount of word appearances.

.. figure:: ./Figures/wordcount_dds_graph.png
   :name: wordcount_dds_python
   :alt: Python wordcount using DDS interface tasks graph
   :align: center
   :width: 75.0%

   Python wordcount using DDS interface tasks graph
