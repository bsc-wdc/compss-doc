Integration with EDDL
---------------------

PyCOMPSs can also be used with the EDDL Python wrapper, known as `pyeddl <https://github.com/deephealthproject/pyeddl>`_
in order to enable the usage of PyEDDL Net objects within PyCOMPSs workflows in distributed environments.


Usage
~~~~~

PyCOMPSs has been enhanced to manage transparently PyEDDL Net objects.
This means that you can use PyEDDL Net objects for task parameters as any usual parameter.

Underneath, PyCOMPSs detects the PyEDDL Net object and uses the specific PyEDDL serializer
(``serialize_net_to_onnx_string``) and deserializer (``import_net_from_onnx_file``)
in order to transfer the object among nodes of the distributed environment.

.. IMPORTANT::

    EDDL and PyEDDL **MUST** be installed and available in the environment.


Sample Application
~~~~~~~~~~~~~~~~~~

The following code (:numref:`code_pyeddl_pycompss`) shows how to use PyEDDL Net object
within a PyCOMPSs application:

.. code-block:: python
    :name: code_pyeddl_pycompss
    :caption: PyCOMPSs application with PyEDDL Net object example (``pyeddl_pycompss.py``)

    MISSING CODE HERE


Execution
~~~~~~~~~

An application parallelized with PyCOMPSs using PyEDDL Net objects **MUST** be executed as
any COMPSs application (for full description about the execution environments
and options please check the
:ref:`Sections/03_Execution:|:rocket:| Execution` Section.).

For example, we can run :numref:`code_pyeddl_pycompss` locally (using the
PyCOMPSs CLI) with the following script:


.. code-block:: bash

   $ pycompss run pyeddl_pycompss.py

The execution output is:

.. code-block:: console

    MISSING OUTPUT HERE
