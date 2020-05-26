Interacting with the persistent storage
---------------------------------------

The **Storage Runtime Interface** (SRI) provides some functions to interact
with the storage backend. All of them are aimed at enabling the COMPSs
runtime to deal with persistent data across the infrastructure.

However, the function to retrieve an object from the storage backend from its
identifier can be useful for the user.
Consequently, users can import the SRI and use the ``getByID`` function
when needed necessary. This function requires a String parameter with
the object identifier, and returns the object associated with that identifier
(``null`` or ``None`` otherwise).

The following subsections detail how to call the ``getByID`` function in Java
and Python applications.

Java
~~~~

Import the ``getByID`` function from the storage api and use it:

.. code-block:: java

    import storage.StorageItf;
    import MyPackage.MyClass;

    class Test{
        // ...
        public static void main(String args[]){
            // ...
            obj = StorageItf.getByID("my_obj");
            // ...
        }
    }


Python
~~~~~~

Import the ``getByID`` function from the storage api and use it:

.. code-block:: python

    from storage.api import getByID

    ..
    obj = getByID('my_obj')
    ...


C/C++
~~~~~

.. ADMONITION:: Unsupported
    :class: warning

    Persistent storage is not supported with C/C++ COMPSs applications.
