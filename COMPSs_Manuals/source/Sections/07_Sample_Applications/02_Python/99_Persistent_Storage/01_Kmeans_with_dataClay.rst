Kmeans with dataClay
--------------------

KMeans is machine-learning algorithm (NP-hard), popularly employed for cluster
analysis in data mining, and interesting for benchmarking and performance evaluation.

The objective of the Kmeans algorithm to group a set of multidimensional points
into a predefined number of clusters, in which each point belongs to the closest
cluster (with the nearest mean distance), in an iterative process.

In this application we make use of the persistent storage API.
In particular, the dataset fragments are considered ``StorageObject``,
delegating its content into the persistent framework.
Since the data model (object declared as storage object) includes functions,
it can run efficiently with dataClay.

First, lets see the data model (``storage_model/fragment.py``)


.. code-block:: python

        from storage.api import StorageObject

        try:
            from pycompss.api.task import task
            from pycompss.api.parameter import IN
        except ImportError:
            # Required since the pycompss module is not ready during the registry
            from dataclay.contrib.dummy_pycompss import task, IN

        from dataclay import dclayMethod

        import numpy as np
        from sklearn.metrics import pairwise_distances


        class Fragment(StorageObject):
            """
            @ClassField points numpy.ndarray

            @dclayImport numpy as np
            @dclayImportFrom sklearn.metrics import pairwise_distances
            """
            @dclayMethod()
            def __init__(self):
                super(Fragment, self).__init__()
                self.points = None

            @dclayMethod(num_points='int', dim='int', mode='str', seed='int')
            def generate_points(self, num_points, dim, mode, seed):
                """
                Generate a random fragment of the specified number of points using the
                specified mode and the specified seed. Note that the generation is
                distributed (the master will never see the actual points).
                :param num_points: Number of points
                :param dim: Number of dimensions
                :param mode: Dataset generation mode
                :param seed: Random seed
                :return: Dataset fragment
                """
                # Random generation distributions
                rand = {
                    'normal': lambda k: np.random.normal(0, 1, k),
                    'uniform': lambda k: np.random.random(k),
                }
                r = rand[mode]
                np.random.seed(seed)
                mat = np.asarray(
                    [r(dim) for __ in range(num_points)]
                )
                # Normalize all points between 0 and 1
                mat -= np.min(mat)
                mx = np.max(mat)
                if mx > 0.0:
                    mat /= mx

                self.points = mat

            @task(returns=np.ndarray, target_direction=IN)
            @dclayMethod(centres='numpy.ndarray', return_='anything')
            def partial_sum(self, centres):
                partials = np.zeros((centres.shape[0], 2), dtype=object)
                arr = self.points
                close_centres = pairwise_distances(arr, centres).argmin(axis=1)
                for center_idx, _ in enumerate(centres):
                    indices = np.argwhere(close_centres == center_idx).flatten()
                    partials[center_idx][0] = np.sum(arr[indices], axis=0)
                    partials[center_idx][1] = indices.shape[0]
                return partials


Now we can focus in the main kmeans application (``kmeans.py``):

.. code-block:: python

    import time
    import numpy as np

    from pycompss.api.task import task
    from pycompss.api.api import compss_wait_on
    from pycompss.api.api import compss_barrier

    from storage_model.fragment import Fragment

    from sklearn.metrics.pairwise import paired_distances


    @task(returns=dict)
    def merge(*data):
        accum = data[0].copy()
        for d in data[1:]:
            accum += d
        return accum


    def converged(old_centres, centres, epsilon, iteration, max_iter):
        if old_centres is None:
            return False
        dist = np.sum(paired_distances(centres, old_centres))
        return dist < epsilon ** 2 or iteration >= max_iter


    def recompute_centres(partials, old_centres, arity):
        centres = old_centres.copy()
        while len(partials) > 1:
            partials_subset = partials[:arity]
            partials = partials[arity:]
            partials.append(merge(*partials_subset))
        partials = compss_wait_on(partials)
        for idx, sum_ in enumerate(partials[0]):
            if sum_[1] != 0:
                centres[idx] = sum_[0] / sum_[1]
        return centres


    def kmeans_frag(fragments, dimensions, num_centres=10, iterations=20,
                    seed=0., epsilon=1e-9, arity=50):
        """
        A fragment-based K-Means algorithm.
        Given a set of fragments (which can be either PSCOs or future objects that
        point to PSCOs), the desired number of clusters and the maximum number of
        iterations, compute the optimal centres and the index of the centre
        for each point.
        PSCO.mat must be a NxD float np.ndarray, where D = dimensions
        :param fragments: Number of fragments
        :param dimensions: Number of dimensions
        :param num_centres: Number of centres
        :param iterations: Maximum number of iterations
        :param seed: Random seed
        :param epsilon: Epsilon (convergence distance)
        :param arity: Arity
        :return: Final centres and labels
        """
        # Set the random seed
        np.random.seed(seed)
        # Centres is usually a very small matrix, so it is affordable to have it in
        # the master.
        centres = np.asarray(
            [np.random.random(dimensions) for _ in range(num_centres)]
        )
        # Note: this implementation treats the centres as files, never as PSCOs.
        old_centres = None
        iteration = 0
        while not converged(old_centres, centres, epsilon, iteration, iterations):
            print("Doing iteration #%d/%d" % (iteration + 1, iterations))
            old_centres = centres.copy()
            partials = []
            for frag in fragments:
                partial = frag.partial_sum(old_centres)
                partials.append(partial)
            centres = recompute_centres(partials, old_centres, arity)
            iteration += 1
        return centres


    def parse_arguments():
        """
        Parse command line arguments. Make the program generate
        a help message in case of wrong usage.
        :return: Parsed arguments
        """
        import argparse
        parser = argparse.ArgumentParser(description='KMeans Clustering.')
        parser.add_argument('-s', '--seed', type=int, default=0,
                            help='Pseudo-random seed. Default = 0')
        parser.add_argument('-n', '--numpoints', type=int, default=100,
                            help='Number of points. Default = 100')
        parser.add_argument('-d', '--dimensions', type=int, default=2,
                            help='Number of dimensions. Default = 2')
        parser.add_argument('-c', '--num_centres', type=int, default=5,
                            help='Number of centres. Default = 2')
        parser.add_argument('-f', '--fragments', type=int, default=10,
                            help='Number of fragments.' +
                                 ' Default = 10. Condition: fragments < points')
        parser.add_argument('-m', '--mode', type=str, default='uniform',
                            choices=['uniform', 'normal'],
                            help='Distribution of points. Default = uniform')
        parser.add_argument('-i', '--iterations', type=int, default=20,
                            help='Maximum number of iterations')
        parser.add_argument('-e', '--epsilon', type=float, default=1e-9,
                            help='Epsilon. Kmeans will stop when:' +
                                 ' |old - new| < epsilon.')
        parser.add_argument('-a', '--arity', type=int, default=50,
                            help='Arity of the reduction carried out during \
                            the computation of the new centroids')
        return parser.parse_args()


    from storage_model.fragment import Fragment  # this will have to be removed

    @task(returns=Fragment)
    def generate_fragment(points, dim, mode, seed):
        """
        Generate a random fragment of the specified number of points using the
        specified mode and the specified seed. Note that the generation is
        distributed (the master will never see the actual points).
        :param points: Number of points
        :param dim: Number of dimensions
        :param mode: Dataset generation mode
        :param seed: Random seed
        :return: Dataset fragment
        """
        fragment = Fragment()
        # Make persistent before since it is populated in the task
        fragment.make_persistent()
        fragment.generate_points(points, dim, mode, seed)

    def main(seed, numpoints, dimensions, num_centres, fragments, mode, iterations,
             epsilon, arity):
        """
        This will be executed if called as main script. Look at the kmeans_frag
        for the KMeans function.
        This code is used for experimental purposes.
        I.e it generates random data from some parameters that determine the size,
        dimensionality and etc and returns the elapsed time.
        :param seed: Random seed
        :param numpoints: Number of points
        :param dimensions: Number of dimensions
        :param num_centres: Number of centres
        :param fragments: Number of fragments
        :param mode: Dataset generation mode
        :param iterations: Number of iterations
        :param epsilon: Epsilon (convergence distance)
        :param arity: Arity
        :return: None
        """
        start_time = time.time()

        # Generate the data
        fragment_list = []
        # Prevent infinite loops in case of not-so-smart users
        points_per_fragment = max(1, numpoints // fragments)

        for l in range(0, numpoints, points_per_fragment):
            # Note that the seed is different for each fragment.
            # This is done to avoid having repeated data.
            r = min(numpoints, l + points_per_fragment)

            fragment_list.append(
                generate_fragment(r - l, dimensions, mode, seed + l)
            )

        compss_barrier()
        print("Generation/Load done")
        initialization_time = time.time()
        print("Starting kmeans")

        # Run kmeans
        centres = kmeans_frag(fragments=fragment_list,
                              dimensions=dimensions,
                              num_centres=num_centres,
                              iterations=iterations,
                              seed=seed,
                              epsilon=epsilon,
                              arity=arity)
        compss_barrier()
        print("Ending kmeans")
        kmeans_time = time.time()

        print("-----------------------------------------")
        print("-------------- RESULTS ------------------")
        print("-----------------------------------------")
        print("Initialization time: %f" % (initialization_time - start_time))
        print("Kmeans time: %f" % (kmeans_time - initialization_time))
        print("Total time: %f" % (kmeans_time - start_time))
        print("-----------------------------------------")
        centres = compss_wait_on(centres)
        print("CENTRES:")
        print(centres)
        print("-----------------------------------------")


    if __name__ == "__main__":
        options = parse_arguments()
        main(**vars(options))

.. TIP::

    This code can work with Hecuba and Redis if the functions declared in
    the data model are declared outside the data model, and the kmeans
    application uses the ``points`` attribute explicitly.


Since this code is going to be executed with dataClay, it is be necessary to
declare the ``client.properties``, ``session.properties`` and
``storage_props.cfg`` files into the ``dataClay_confs`` with the following
contents as example (more configuration options can be found in the
dataClay manual):

client.properties
    .. code-block:: bash

        HOST=127.0.0.1
        TCPPORT=11034

session.properties
    .. code-block:: bash

        Account=bsc_user
        Password=bsc_user
        StubsClasspath=./stubs
        DataSets=hpc_dataset
        DataSetForStore=hpc_dataset
        DataClayClientConfig=./client.properties

storage_props.cfg
    .. code-block:: bash

        BACKENDS_PER_NODE=48


An example of the submission script that can be used in MareNostrum IV to
launch this kmeans with PyCOMPSs and dataClay is:

.. code-block:: bash

    #!/bin/bash -e

    module load gcc/8.1.0
    export COMPSS_PYTHON_VERSION=3-ML
    module load COMPSs/2.8
    module load mkl/2018.1
    module load impi/2018.1
    module load opencv/4.1.2
    module load DATACLAY/2.4.dev

    # Retrieve script arguments
    job_dependency=${1:-None}
    num_nodes=${2:-2}
    execution_time=${3:-5}
    tracing=${4:-false}
    exec_file=${5:-$(pwd)/kmeans.py}

    # Freeze storage_props into a temporal
    # (allow submission of multiple executions with varying parameters)
    STORAGE_PROPS=`mktemp -p ~`
    cp $(pwd)/dataClay_confs/storage_props.cfg "${STORAGE_PROPS}"

    if [[ ! ${tracing} == "false" ]]
    then
      extra_tracing_flags="\
        --jvm_workers_opts=\"-javaagent:/apps/DATACLAY/dependencies/aspectjweaver.jar\" \
        --jvm_master_opts=\"-javaagent:/apps/DATACLAY/dependencies/aspectjweaver.jar\" \
      "
      echo "Adding DATACLAYSRV_START_CMD to storage properties file"
      echo "\${STORAGE_PROPS}=${STORAGE_PROPS}"
      echo "" >> ${STORAGE_PROPS}
      echo "DATACLAYSRV_START_CMD=\"--tracing\"" >> ${STORAGE_PROPS}
    fi

    # Define script variables
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    WORK_DIR=${SCRIPT_DIR}/
    APP_CLASSPATH=${SCRIPT_DIR}/
    APP_PYTHONPATH=${SCRIPT_DIR}/

    # Define application variables
    graph=$tracing
    log_level="off"
    qos_flag="--qos=debug"
    workers_flag=""
    constraints="highmem"

    CPUS_PER_NODE=48
    WORKER_IN_MASTER=0

    shift 5

    # Those are evaluated at submit time, not at start time...
    COMPSS_VERSION=`module load whatis COMPSs 2>&1 >/dev/null | awk '{print $1 ; exit}'`
    DATACLAY_VERSION=`module load whatis DATACLAY 2>&1 >/dev/null | awk '{print $1 ; exit}'`

    # Enqueue job
    enqueue_compss \
      --job_name=kmeansOO_PyCOMPSs_dataClay \
      --job_dependency="${job_dependency}" \
      --exec_time="${execution_time}" \
      --num_nodes="${num_nodes}" \
      \
      --cpus_per_node="${CPUS_PER_NODE}" \
      --worker_in_master_cpus="${WORKER_IN_MASTER}" \
      --scheduler=es.bsc.compss.scheduler.loadbalancing.LoadBalancingScheduler \
      \
      "${workers_flag}" \
      \
      --worker_working_dir=/gpfs/scratch/user/ \
      \
      --constraints=${constraints} \
      --tracing="${tracing}" \
      --graph="${graph}" \
      --summary \
      --log_level="${log_level}" \
      "${qos_flag}" \
      \
      --classpath=${DATACLAY_JAR} \
      --pythonpath=${APP_PYTHONPATH}:${PYCLAY_PATH}:${PYTHONPATH} \
      --storage_props=${STORAGE_PROPS} \
      --storage_home=$COMPSS_STORAGE_HOME \
      --prolog="$DATACLAY_HOME/bin/dataclayprepare,$(pwd)/storage_model/,$(pwd)/,storage_model,python" \
      \
      ${extra_tracing_flags} \
      \
      --lang=python \
      \
      "$exec_file" $@ --use_storage
