Defining the data model
-----------------------

The data model consists of a set of related classes programmed in one of the
supported languages aimed are representing the objects used in the application
(e.g. in a wordcount application, the data model would be text).

In order to define that the application objects are going to be stored in the
underlying persistent storage backend, the data model must be enriched with
the Storage Object Interface (SOI).

The SOI provides a set of functionalities that all objects stored in the
persistent storage backend will need. Consequently, the user must inherit
the SOI on its data model classes, and give some insights of the class
attributes.

The following subsections detail how to enrich the data model in Java and
Python applications.

Java
~~~~

TODO: Add Java data model specification.

Python
~~~~~~

To define that a class objects are going to be stored in the persistent storage
backend, the class must inherit the ``StorageObject`` class. This class
is provided by the persistent storage backend.

.. code-block:: python

    from storage.api import StorageObject

    class MyClass(StorageObject):
         ...

The StorageObject class includes some functions in the class that will be
available from the instantiated objects (:numref:`storage_obj_methods_python`).

.. table:: Available methods from StorageObject in Python
    :name: storage_obj_methods_python
    :widths: auto

    +---------------------------+---------+-----------------------------------------------------------------------------------------+
    | Name                      | Returns | Comments                                                                                |
    +===========================+=========+=========================================================================================+
    | makePersistent(String id) | Nothing | | Inserts the object in the database with the id.                                       |
    |                           |         | | If id is null, a random UUID will be computed instead.                                |
    +---------------------------+---------+-----------------------------------------------------------------------------------------+
    | deletePersistent()        | Nothing | | Removes the object from the storage.                                                  |
    |                           |         | | It does nothing if it was not already there.                                          |
    +---------------------------+---------+-----------------------------------------------------------------------------------------+
    | getID()                   | String  | | Returns the current object identifier if the object is not persistent (null instead). |
    +---------------------------+---------+-----------------------------------------------------------------------------------------+




In addition, the user has to give details about the function attributes using
the class documentation. The following code snippet gives some examples of
several types of attributes:


.. code-block:: python

    from storage.api import StorageObject

    class MyClass(StorageObject):
        """
        # Dictionary with structured value:
        @TypeSpecification field1 dict <<k1: int, k2: int>, tuple<v1: int, v2: float, v3: text>>

        # Plain definition of the same dictionary:
        @TypeSpecification field2 dict <<int,int>, str>

        # Another class instance as attribute
        @TypeSpecification field3 AnotherClassName

        # Complex dictionaries:
        @TypeSpecification field4 dict <<int,str>, dict<<int>, list<str>>>
        @TypeSpecification field5 dict <<int>, AnotherClassName>

        # Structured types
        @TypeSpecification field6 list <int>
        @TypeSpecification field7 set <list<float>>
        # Elemmental types
        @TypeSpecification field8 int
        @TypeSpecification field9 str
        """
        pass



C/C++
~~~~~

Persistent storage is not supported with C/C++ COMPSs applications.
