First steps
===========

COMPSs relies on a Storage API to enable the interation with persistent storage
frameworks (:numref:`storage_architecture`), which is composed by two main
modules: *Storage Object Interface* (SOI) and *Storage Runtime Interface* (SRI)

.. figure:: ./Figures/1_storage.png
   :name: storage_architecture
   :alt: COMPSs with persistent storage architecture
   :align: center
   :width: 50.0%

   COMPSs with persistent storage architecture

Any COMPSs application aimed at using a persistent storage framework has to
include calls to:

    * The SOI in order to define the data model (see :ref:`Sections/06_Persistent_Storage/01_Storage_integration/01_Data_model:Defining the data model`),
      and relies on COMPSs, which interacts with the persistent storage framework through the SRI.
    * The SRI in order to interact directly with the storage backend (e.g. retrieve data, etc.)
      (see :ref:`Sections/06_Persistent_Storage/01_Storage_integration/02_Interact_with_storage:Interacting with the persistent storage`).

In addition, it must be taken into account that the execution of an application
using a persistent storage framework requires some specific flags in
``runcompss`` and ``enqueue_compss``
(see :ref:`Sections/06_Persistent_Storage/01_Storage_integration/03_Running_with_storage:Running with persistent storage`).

Currently, there exists storage interfaces for dataClay_, Hecuba_ and Redis_.
They are thoroughly described from the developer and user point of view in Sections:

    * :ref:`Sections/06_Persistent_Storage/02_COMPSs_dataClay:COMPSs + dataClay`
    * :ref:`Sections/06_Persistent_Storage/03_COMPSs_Hecuba:COMPSs + Hecuba`
    * :ref:`Sections/06_Persistent_Storage/04_COMPSs_Redis:COMPSs + Redis`

The interface is open to any other storage framework by implementing the
required functionalities described in
:ref:`Sections/06_Persistent_Storage/05_Own_interface:Implement your own Storage interface for COMPSs`.


.. toctree::
    :maxdepth: 2
    :caption: Table of Contents
    :hidden:

    01_Storage_integration/01_Data_model
    01_Storage_integration/02_Interact_with_storage
    01_Storage_integration/03_Running_with_storage


.. _dataClay: https://www.bsc.es/research-and-development/software-and-apps/software-list/dataclay

.. _Hecuba: https://www.bsc.es/research-and-development/software-and-apps/software-list/hecuba

.. _Redis: https://redis.io/
