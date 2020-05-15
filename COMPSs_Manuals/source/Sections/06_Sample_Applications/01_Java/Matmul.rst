Matrix multiplication
---------------------

The Matrix Multiplication (Matmul) is a pure Java application that
multiplies two matrices in a direct way. The application creates 2
matrices of N x N size initialized with values, and multiply the
matrices by blocks.

This application provides three different implementations that only
differ on the way of storing the matrix:

#. **matmul.objects.Matmul** Matrix stored by means of objects

#. **matmul.files.Matmul** Matrix stored in files

#. **matmul.arrays.Matmul** Matrix represented by an array

.. figure:: ./Figures/matrix.jpeg
   :name: matmul
   :alt: Matrix multiplication
   :align: center
   :width: 70.0%

   Matrix multiplication

In all the implementations the multiplication is implemented in the
multiplyAccumulative method that is thus selected as the task to be
executed remotely. As example, we we provide next the task
implementation and the tasks interface for the objects implementation.

.. code-block:: java

    	// matmul.objects.Block

    	public void multiplyAccumulative(Block a, Block b) {
    		for (int i = 0; i < M; i++) {
    			for (int j = 0; j < M; j++) {
    				for (int k = 0; k < M; k++) {
    					data[i][j] += a.data[i][k]*b.data[k][j];
    				}
    			}
    		}
    	}

.. code-block:: java

    	// matmul.objects.MatmulItf

    	@Method(declaringClass = "matmul.objects.Block")
    	void multiplyAccumulative(
    		@Parameter Block a,
    		@Parameter Block b
    	);

In order to run the application the matrix dimension (number of blocks)
and the dimension of each block have to be supplied. Consequently, any
of the implementations must be executed by running the following
command.

.. code-block:: console

    compss@bsc:~$ runcompss matmul.<IMPLEMENTATION_TYPE>.Matmul <matrix_dim> <block_dim>

Finally, we provide an example of execution for each implementation.

.. code-block:: console

    compss@bsc:~$ cd ~/tutorial_apps/java/matmul/jar/
    compss@bsc:~/tutorial_apps/java/matmul/jar$ runcompss matmul.objects.Matmul 8 4
    [  INFO] Using default execution type: compss
    [  INFO] Using default location for project file: /opt/COMPSs/Runtime/configuration/xml/projects/default_project.xml
    [  INFO] Using default location for resources file: /opt/COMPSs/Runtime/configuration/xml/resources/default_resources.xml

    ----------------- Executing matmul.objects.Matmul --------------------------

    WARNING: COMPSs Properties file is null. Setting default values
    [(887)    API]  -  Starting COMPSs Runtime v<version>
    [LOG] MSIZE parameter value = 8
    [LOG] BSIZE parameter value = 4
    [LOG] Allocating A/B/C matrix space
    [LOG] Computing Result
    [LOG] Main program finished.
    [(7415)    API]  -  Execution Finished

    ------------------------------------------------------------

.. code-block:: console

    compss@bsc:~$ cd ~/tutorial_apps/java/matmul/jar/
    compss@bsc:~/tutorial_apps/java/matmul/jar$ runcompss matmul.files.Matmul 8 4
    [  INFO] Using default execution type: compss
    [  INFO] Using default location for project file: /opt/COMPSs/Runtime/configuration/xml/projects/default_project.xml
    [  INFO] Using default location for resources file: /opt/COMPSs/Runtime/configuration/xml/resources/default_resources.xml

    ----------------- Executing matmul.files.Matmul --------------------------

    WARNING: COMPSs Properties file is null. Setting default values
    [(907)    API]  -  Starting COMPSs Runtime v<version>
    [LOG] MSIZE parameter value = 8
    [LOG] BSIZE parameter value = 4
    [LOG] Computing result
    [LOG] Main program finished.
    [(9925)    API]  -  Execution Finished

    ------------------------------------------------------------

.. code-block:: console

    compss@bsc:~$ cd ~/tutorial_apps/java/matmul/jar/
    compss@bsc:~/tutorial_apps/java/matmul/jar$ runcompss matmul.arrays.Matmul 8 4
    [  INFO] Using default execution type: compss
    [  INFO] Using default location for project file: /opt/COMPSs/Runtime/configuration/xml/projects/default_project.xml
    [  INFO] Using default location for resources file: /opt/COMPSs/Runtime/configuration/xml/resources/default_resources.xml

    ----------------- Executing matmul.arrays.Matmul --------------------------

    WARNING: COMPSs Properties file is null. Setting default values
    [(1062)    API]  -  Starting COMPSs Runtime v<version>
    [LOG] MSIZE parameter value = 8
    [LOG] BSIZE parameter value = 4
    [LOG] Allocating C matrix space
    [LOG] Computing Result
    [LOG] Main program finished.
    [(7811)    API]  -  Execution Finished

    ------------------------------------------------------------
