.. _python_sample_applications:

|:snake:| Python
################

The first two examples in this section are simple applications developed
in COMPSs to easily illustrate how to code, compile and run COMPSs
applications. These applications are executed locally and show different
ways to take advantage of all the COMPSs features.

The rest of the examples are more elaborated and consider the execution
in a cloud platform where the VMs mount a common storage on
**/sharedDisk** directory. This is useful in the case of applications
that require working with big files, allowing to transfer data only
once, at the beginning of the execution, and to enable the application
to access the data directly during the rest of the execution.


.. nbgallery::
    :name: python_sample_apps

    05_Sample_Applications/02_Python/01_Simple
    05_Sample_Applications/02_Python/02_Increment
    05_Sample_Applications/02_Python/03_KMeans
    05_Sample_Applications/02_Python/04_Matmul
    05_Sample_Applications/02_Python/05_Lysozyme_in_water
    05_Sample_Applications/02_Python/99_Persistent_Storage
