Publish at Zenodo
=================


Similarly as with WorkflowHub, once the provenance metadata for your COMPSs application has been generated, you have the possibility of publishing
your results (i.e. both the workflow and the workflow run) in `Zenodo <https://zenodo.org>`_, the Open Science portal.
Zenodo helps researchers receive credit by making the research results citable and through OpenAIRE integrates them into existing reporting
lines to funding agencies like the European Commission. Citation information is also passed to DataCite and onto the scholarly aggregators.


Software requirements
---------------------

To upload COMPSs RO-Crates to Zenodo, the `rocrate-inveniordm package <https://github.com/ResearchObject/ro-crate-inveniordm>`_ must be used,
thus, it must be installed in advance. Depending on the target system, different
options are available using ``pip``:

If the installation is in a laptop or machine you manage, you can use the command:

.. code-block:: console

    $ pip install rocrate-inveniordm

If you do not manage the target machine, you can install the library in your own user space using:

.. code-block:: console

    $ pip install rocrate-inveniordm --user

This would typically install the library in ``~/.local/``. Another option is to specify the target directory with:

.. code-block:: console

    $ pip install -t install_path rocrate-inveniordm


.. WARNING::

    The ro-crate-inveniordm package compatible with COMPSs has not been merged yet to the main branch, and can be found 
    for now at https://github.com/rsirvent/ro-crate-inveniordm


Configure rocrate-inveniordm
----------------------------

Follow the steps specified at the `rocrate-inveniordm README <https://github.com/ResearchObject/ro-crate-inveniordm/blob/main/README.md>`_:

- Configure your Zenodo access token at the Zenodo portal (``Profile`` -> ``Applications`` -> ``Personal access tokens`` -> ``New token``)

- Setup environment variables ``INVENIORDM_BASE_URL`` (the Zenodo url), ``INVENIORDM_API_KEY`` (the API token created before).

.. code-block:: console

    $ export INVENIORDM_BASE_URL="https://zenodo.org/"
    $ export INVENIORDM_API_KEY="your_api_key"


Publication steps
-----------------

The steps to achieve the publication of a COMPSs execution are:

- Submit the crate describing your run using the ``rocrate_inveniordm`` CLI (note the underscore):

.. code-block:: console

    $ rocrate_inveniordm -z COMPSs_RO-Crate_20250526_113729/
    ...
    Preparing to upload 1 files...
    Uploading 1 files...
    COMPSs_RO-Crate_20250526_113729.zip
    All 1 files uploaded.
    Successfully created record 15517563

The ``-z`` flag will automatically zip the content of the folder, and upload it to your ``Dashboard`` in Zenodo.

.. WARNING::

    It is STRONGLY recommended to always use the ``-z`` flag. Although the content could be uploaded without being zipped,
    Zenodo flattens the structure of the directory content in the upload, which may be dangerous for an RO-Crate package.


- Go to your ``Dashboard`` in Zenodo, review the record that has been just uploaded:

.. figure:: ./Figures/ZenodoRecord.png
   :name: Zenodo record created with the upload
   :alt: Zenodo record
   :align: center
   :width: 90.0%

   Zenodo record created with the upload

- Select if you need a DOI to be generated, to later reference your experiment.

- Check that the metadata has been correctly imported:

  - Resource type: Workflow.
  - The Title, Publication date, Creators (all names, institutions and ORCIDs), Description, License and Publisher.
  - Click ``Preview`` to see how the final record will look like.
  - Click ``Save draft`` if you want to continue editing later.
  - Click ``Publish`` to make your record publicly available.

The final record would look something like this example we provide:

.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.15517084.svg
   :target: https://doi.org/10.5281/zenodo.15517084
   :align: left
   :width: 20.0%


.. figure:: ./Figures/ZenodoPublished.png
   :name: Zenodo published record
   :alt: Zenodo published
   :align: center
   :width: 90.0%

   Zenodo published record


.. TIP::

    For better compatibility with Zenodo, use the SPDX full URL when specifying the license metadata of your COMPSs experiment.
    See the full list of licenses at: https://spdx.org/licenses/ Details on how to define the license for your COMPSs run
    can be found at Section :ref:`yaml-config`.
