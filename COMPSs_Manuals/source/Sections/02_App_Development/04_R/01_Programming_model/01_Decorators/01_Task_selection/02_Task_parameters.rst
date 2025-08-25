Task Parameters
===============

The metadata corresponding to a parameter is specified as an argument of
the ``task`` decorator, whose name is the formal parameter's name and whose
value defines the type and direction of the parameter. The parameter types and
directions can be:

Types
   * *Primitive types* (integer, long, float, boolean, strings)
   * *Objects* (instances of user-defined classes, dictionaries, lists, tuples, complex numbers)

Direction
   * Read-only (``IN``)
   * Read-write (``INOUT``)
   * Write-only (``OUT``)

The direction is only mandatory for ``INOUT`` and ``OUT`` parameters.

.. NOTE::

  Please note that in the following cases there is no need
  to include an argument in the *task* decorator for a given
  task parameter:

  -  Parameters of primitive types (integer, long, float, boolean) and
     strings: the type of these parameters can be automatically inferred
     by COMPSs, and their direction is always ``IN``.

  -  Read-only object parameters: the type of the parameter is
     automatically inferred, and the direction defaults to ``IN``.


Objects
-------

The default type for a parameter is object. Consequently, there is no need
to use a specific keyword. However, it is necessary to indicate its direction
(unless for input parameters):

.. LIST-TABLE::
    :header-rows: 1

    * - PARAMETER
      - DESCRIPTION
    * - ``IN``
      - The parameter is read-only.
    * - ``INOUT``
      - The parameter is read-write.
    * - ``OUT``
      - The parameter is write-only.
