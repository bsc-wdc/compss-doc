===================
Workflow Provenance
===================

The COMPSs runtime includes the capacity of recording details of the
application's execution as metadata, also known as *Workflow Provenance*. With workflow provenance, you are able to share
not only your workflow application (i.e. the source code) but also your workflow run (i.e. the datasets used as inputs, the outputs generated as
results, and details on the environment where the application was run). This is supported for both Python
and Java COMPSs applications. More technical details on how Provenance is generated in COMPSs using a lightweight approach
that does not introduce overhead to the workflow execution can be found in the paper:

- `Automatic, Efficient and Scalable Provenance Registration for FAIR HPC Workflows <http://dx.doi.org/10.1109/WORKS56498.2022.00006>`_ (`Slides <https://zenodo.org/record/7701868>`_)

Provenance information can be useful for a number of things, including **Governance, Reproducibility, Replicability, Traceability,
or Knowledge Extraction**, among others.
In our case, we have initially targeted workflow provenance recording to enable users to **publish research results** obtained with COMPSs as
artifacts that can be cited in scientific publications with their corresponding DOI as a persistent identifier.
See Section :ref:`Sections/05_Tools/04_Workflow_Provenance/06_WorkflowHub:Publish and cite your results with WorkflowHub` to learn
precisely how to do that. We see a growing number of scientific conferences requesting these reproducible artifacts, such as:

- `The Reproducibility Initiative at the International Conference for High Performance Computing, Networking, Storage, and Analysis (SC) <https://sc24.supercomputing.org/program/papers/reproducibility-initiative/>`_
- `Reproducibility at the International Conference on Parallel Processing (ICPP) <https://icpp2024.org/index.php?option=com_content&view=article&id=4&Itemid=108>`_
- `Call for Artifacts at the International European Conference on Parallel and Distributed Computing (EuroPar) <https://2024.euro-par.org/calls/artifacts/>`_
- `The ACM Special Interest Group on Management of Data (SIGMOD) Reproducibility Award <https://reproducibility.sigmod.org/reports.html>`_
- `Call for Artifacts at USENIX Conference on File and Storage Technologies (FAST) <https://www.usenix.org/conference/fast24/call-for-artifacts>`_
- And many more...

.. TIP::
    A step-by-step guide on how to share your COMPSs execution results in scientific papers can be found
    `here <https://zenodo.org/records/10046567>`_.

When the provenance option is activated, the runtime records every access
to a file or directory specified in the application, as well as its direction (IN,
OUT, INOUT). In addition to this, other information such as the parameters passed as inputs in the command line
that submitted the application, its source files, workflow diagram and task profiling statistics, authors and
their institutions, ... are also stored.
All this information is later used to record the workflow provenance
of your application using the `RO-Crate specification <https://www.researchobject.org/ro-crate/>`_, and with the assistance of
the `ro-crate-py library <https://github.com/ResearchObject/ro-crate-py>`_. RO-Crate is based on
JSON-LD (JavaScript Object Notation for Linked Data), is
much simpler than other standards and tools created to record Provenance, and
that is why it has been adopted in a number of `communities <https://www.researchobject.org/ro-crate/use_cases>`_.
Using RO-Crate to register the execution's information ensures
not only to register correctly the Provenance of a COMPSs application run, but
also compatibility with some existing portals that already embrace
RO-Crate as their core format for representing metadata, such as `WorkflowHub <https://workflowhub.eu/>`_. Our RO-Crate
format is compliant with the `Workflow RO-Crate Profile v1.0 <https://w3id.org/workflowhub/workflow-ro-crate/1.0>`_ and the
`Workflow Run Crate Profile v0.5 <https://w3id.org/ro/wfrun/workflow/0.5>`_.

.. toctree::
    :maxdepth: 2
    :caption: Table of Contents

    04_Workflow_Provenance/01_Dependencies
    04_Workflow_Provenance/02_YAML
    04_Workflow_Provenance/03_Activation
    04_Workflow_Provenance/04_Result
    04_Workflow_Provenance/05_Debug
    04_Workflow_Provenance/06_WorkflowHub
    04_Workflow_Provenance/07_Examples

