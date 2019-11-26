PAPI: Hardware Counters
=======================

The applications instrumentation supports hardware counters through the
performance API (PAPI). In order to use it, PAPI needs to be present on
the machine before installing COMPSs.

During COMPSs installation it is possible to check if PAPI has been
detected in the Extrae config report:

.. code-block:: console

    Package configuration for Extrae VERSION based on extrae/trunk rev. XXXX:
    -----------------------
    Installation prefix: /opt/COMPSs/Dependencies/extrae
    Cross compilation: no
    ...
    ...
    ...

    Performance counters: yes
      Performance API: PAPI
      PAPI home: /usr
      Sampling support: yes

.. caution::
   PAPI detection is only performed in the machine where COMPSs is
   installed. User is responsible of providing a valid PAPI installation to
   the worker machines to be used (if they are different from the master),
   otherwise workers will crash because of the missing *libpapi.so*.

PAPI installation and requirements depend on the OS. On Ubuntu 14.04 it
is available under textitpapi-tools package; on OpenSuse textitpapi and
textitpapi-dev. For more information check
https://icl.cs.utk.edu/projects/papi/wiki/Installing_PAPI.

Extrae only supports 8 active hardware counters at the same time. Both
basic and advanced mode have the same default counters list:

PAPI_TOT_INS
    Instructions completed

PAPI_TOT_CYC
    Total cycles

PAPI_LD_INS
    Load instructions

PAPI_SR_INS
    Store instructions

PAPI_BR_UCN
    Unconditional branch instructions

PAPI_BR_CN
    Conditional branch instructions

PAPI_VEC_SP
    Single precision vector/SIMD instructions

RESOURCE_STALLS
    Cycles Allocation is stalled due to Resource Related reason

The XML config file contains a secondary set of counters. In order to
activate it just change the *starting-set-distribution* from 2 to 1
under the *cpu* tag. The second set provides the following information:

PAPI_TOT_INS
    Instructions completed

PAPI_TOT_CYC
    Total cycles

PAPI_L1_DCM
    Level 1 data cache misses

PAPI_L2_DCM
    Level 2 data cache misses

PAPI_L3_TCM
    Level 3 cache misses

PAPI_FP_INS
    Floating point instructions

To further customize the tracked counters, modify the XML to suit your
needs. To find the available PAPI counters on a given computer issue the
command *papi_avail -a*. For more information about Extrae’s XML
configuration refer to
https://www.bsc.es/computer-sciences/performance-tools/trace-generation/extrae/extrae-user-guide.


.. figure:: /Logos/bsc_logo.jpg
   :width: 40.0%
   :align: center
