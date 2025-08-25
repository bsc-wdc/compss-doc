Defining the data model
=======================

The data model consists of a set of related classes programmed in one of the
supported languages aimed are representing the objects used in the application
(e.g. in a wordcount application, the data model would be text).

In order to define that the application objects are going to be stored in the
underlying persistent storage backend, the data model must be enriched with
the *Storage Object Interface* (SOI).

The SOI provides a set of functionalities that all objects stored in the
persistent storage backend will need. Consequently, the user must inherit
the SOI on its data model classes, and give some insights of the class
attributes.

The following subsections detail how to enrich the data model in Java and
Python applications.

Java
----

To define that a class objects are going to be stored in the persistent storage
backend, the class must extend the ``StorageObject`` class (as well as
implement the ``Serializable`` interface). This class is provided by the
persistent storage backend.


.. code-block:: java

    import storage.StorageObject;
    import java.io.Serializable;

    class MyClass extends StorageObject implements Serializable {

        private double[] vector;

        /**
        * Write here your class-specific
        * constructors, attributes and methods.
        */
    }


The ``StorageObject`` object enriches the class with some methods that allow the
user to interact with the persistent storage backend. These methods can be
found in :numref:`storage_obj_methods_java`.


.. table:: Available methods from StorageObject
    :name: storage_obj_methods_java

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

These functions can be used from the application in order to persist an object
(pushing the object into the persistent storage) with ``make_persistent``,
remove it from the persistent storage with ``delete_persistent`` or
getting the object identifier with ``getID`` for the later interaction with
the storage backend.

.. code-block:: java

    import MyPackage.MyClass;

    class Test{
        // ...
        public static void main(String args[]){
            // ...
            MyClass my_obj = new MyClass();
            my_obj.matrix = new double[10];
            my_obj.makePersistent();         // make persistent without parameter
            String obj_id = my_obj.getID();  // get the idenfier provided by the storage framework
            // ...
            my_obj.deletePersistent();
            // ...
            MyClass my_obj2 = new MyClass();
            my_obj2.matrix = new double[20];
            my_obj2.makePersistent("obj2");  // make persistent providing identifier
            // ...
            my_obj2.delete_persistent();
            // ...
        }
    }


Python
------

To define that a class objects are going to be stored in the persistent storage
backend, the class must inherit the ``StorageObject`` class. This class
is provided by the persistent storage backend.

.. code-block:: python

    from storage.api import StorageObject

    class MyClass(StorageObject):
         ...

In addition, the user has to give details about the class attributes using
the class documentation.
For example, if the user wants to define a class containing a numpy ndarray as
attribute, the user has to specify this attribute starting with ``@ClassField``
followed by the attribute name and type:

.. code-block:: python

    from storage.api import StorageObject

    class MyClass(StorageObject):
        """
        @ClassField matrix numpy.ndarray
        """
        pass

.. IMPORTANT::

    Methods inside the class are not supported by all storage backends.
    dataClay is currently the only backend that provides support for them
    (see :ref:`Sections/04_Tools/08_Persistent_Storage/02_COMPSs_dataClay:Enabling COMPSs applications with dataClay`).

Then, the user can use the instantiated object normally:

.. code-block:: python

    from MyFile import MyClass
    import numpy as np

    my_obj = MyClass()
    my_obj.matrix = np.random.rand(10, 2)
    ...

The following code snippet gives some examples of several types of attributes:


.. code-block:: python

    from storage.api import StorageObject

    class MyClass(StorageObject):
        """
        # Elemmental types
        @ClassField field1 int
        @ClassField field2 str
        @ClassField field3 np.ndarray

        # Structured types
        @ClassField field4 list <int>
        @ClassField field5 set <list<float>>

        # Another class instance as attribute
        @ClassField field6 AnotherClassName

        # Complex dictionaries:
        @ClassField field7 dict <<int,str>, dict<<int>, list<str>>>
        @ClassField field8 dict <<int>, AnotherClassName>

        # Dictionary with structured value:
        @ClassField field9 dict <<k1: int, k2: int>, tuple<v1: int, v2: float, v3: text>>
        # Plain definition of the same dictionary:
        @ClassField field10 dict <<int,int>, str>
        """
        pass

Finally, the ``StorageObject`` class includes some functions in the class that
will be available from the instantiated objects
(:numref:`storage_obj_methods_python`).

.. table:: Available methods from StorageObject in Python
    :name: storage_obj_methods_python

    +---------------------------+---------+---------------------------------------------------------------------------------------------+
    | Name                      | Returns | Comments                                                                                    |
    +===========================+=========+=============================================================================================+
    | make_persistent(String id)| Nothing | | Inserts the object in the database with the id.                                           |
    |                           |         | | If id is null, a random UUID will be computed instead.                                    |
    +---------------------------+---------+---------------------------------------------------------------------------------------------+
    | delete_persistent()       | Nothing | | Removes the object from the storage.                                                      |
    |                           |         | | It does nothing if it was not already there.                                              |
    +---------------------------+---------+---------------------------------------------------------------------------------------------+
    | getID()                   | String  | | Returns the current object identifier if the object is not persistent (``None`` instead). |
    +---------------------------+---------+---------------------------------------------------------------------------------------------+


These functions can be used from the application in order to persist an object
(pushing the object into the persistent storage) with ``make_persistent``,
remove it from the persistent storage with ``delete_persistent`` or
getting the object identifier with ``getID`` for the later interaction with
the storage backend.

.. code-block:: python

    import numpy as np

    my_obj = MyClass()
    my_obj.matrix = np.random.rand(10, 2)
    my_obj.make_persistent()  # make persistent without parameter
    obj_id = my_obj.getID()   # get the idenfier provided by the storage framework
    ...
    my_obj.delete_persistent()
    ...
    my_obj2 = MyClass()
    my_obj2.matrix = np.random.rand(10, 3)
    my_obj2.make_persistent('obj2')  # make persistent providing identifier
    ...
    my_obj2.delete_persistent()
    ...


C/C++
-----

.. ADMONITION:: Unsupported
    :class: warning

    Persistent storage is not supported with C/C++ COMPSs applications.
