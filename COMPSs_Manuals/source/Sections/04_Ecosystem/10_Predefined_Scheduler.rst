Predefined Scheduler Guide
##########################

How it works 
************
The Predefined Scheduler reads a JSON configuration file that defines:
    * 1. **Task execution order** - Which tasks to execute
    * 2. **Implementation selection** - Which implementation to use for tasks with multiple options
    * 3. **Task dependencies** - Which tasks must complete before others can start
    * 4. **Resource assignments** - Which worker should execute each task
The scheduler then enforces this plan during execution, ensuring tasks are scheduled exactly as specified.

Configuration Format
********************

Basic Structure
===============

The configuration is a JSON file containing an array of task definitions:

.. code-block:: json
    :name: predefined_json_structure
    :caption: Predefined JSON structure.
    
    [
        {
            "taskId": 1,
            "implementationId": 0,
            "predecesors": [],
            "resource": "COMPSsWorker01"
        },
        {
            "taskId": 2,
            "implementationId": 0,
            "predecesors": [1],
            "resource": "COMPSsWorker01"
        }
    ]

Field Descriptions
==================

**taskId** (required)
    * Type: Integer
    * Description: Unique identifier for the task
    * Example: 1, 2, 3, etc.
    * Note: Task IDs are assigned by COMPSs in the order tasks are created
**implementationId** (required)
    * Type: Integer
    * Description: Specifies which implementation to use for this task
    * Default: 0 (first implementation)
    * Use Case: For tasks with multiple implementations (e.g., CPU vs GPU),this selects which one to execute
**predecessors** (required)
    * Type: Array of integers
    * Description: List of task IDs that must complete before this task can start
    * Example: [] (no dependencies), [1], [1, 2, 3]
    * Note: Empty array means the task can start immediately
**resource** (required for single-node tasks)
    * Type: String
    * Description: Name of the worker that should execute this task
    * Example: "COMPSsWorker01"
    * Note: Must match worker names defined in project.xml and resources.xml
**resources** (required for multi-node tasks)
    * Type: Array of strings
    * Description: List of workers for multi-node tasks
    * Example: ["COMPSsWorker01", "COMPSsWorker02", "COMPSsWorker03"]
    * Note: Use this instead of resource for tasks that require multiple nodes

Usage
*****

**Step 1: Create Configuration File**
Create a JSON file (e.g., schedule_config.json) with your task scheduling plan:

.. code-block:: json
    
    [
        {
            "taskId": 1,
            "implementationId": 0,
            "predecesors": [],
            "resource": "COMPSsWorker01"
        },
        {
            "taskId": 2,
            "implementationId": 0,
            "predecesors": [1],
            "resource": "COMPSsWorker02"
        },
        {
            "taskId": 3,
            "implementationId": 0,
            "predecesors": [1,2],
            "resource": "COMPSsWorker01"
        }
    ]

**Step 2: Run COMPSs with Predefined Scheduler**
Use the ``--scheduler`` and ``--scheduler_config_file`` flags:

.. code-block:: console

    $ runcompss --scheduler=es.bsc.compss.scheduler.predefined.PredefinedTS --scheduler_config_file=/path/to/schedule_config.json --project=/path/to/project.xml --resources=/path/to/resources.xml app.py

**Step 3: Verify execution**
Check the traces to see your scheduling.

Complete Example
****************

Application Code (example.py)
=============================

.. code-block:: python
    :name: python_app_example
    :caption: Python application example.

    from pycompss.api.task import task
    from pycompss.api.api import compss_wait_on

    @task(returns=int)
    def compute(value):
        return value * 2

    def main():
        # Create 5 tasks
        results = []
        for i in range(1, 6):
            result = compute(i)
            results.append(result)
        
        # Wait for results
        for i, result in enumerate(results):
            final = compss_wait_on(result)
            print(f"Task {i+1} result: {final}")

    if __name__ == "__main__":
        main()


Configuration File (config.json)
================================

.. code-block:: json

    [
    {
        "taskId": 1,
        "implementationId": 0,
        "predecessors": [],
        "resource": "COMPSsWorker01"
    },
    {
        "taskId": 2,
        "implementationId": 0,
        "predecessors": [1],
        "resource": "COMPSsWorker01"
    },
    {
        "taskId": 3,
        "implementationId": 0,
        "predecessors": [],
        "resource": "COMPSsWorker02"
    },
    {
        "taskId": 4,
        "implementationId": 0,
        "predecessors": [2, 3],
        "resource": "COMPSsWorker01"
    },
    {
        "taskId": 5,
        "implementationId": 0,
        "predecessors": [4],
        "resource": "COMPSsWorker02"
    }
    ]


Execution
=========

.. code-block:: console

    $ runcompss --scheduler=es.bsc.compss.scheduler.predefined.PredefinedTS --scheduler_config_file=config.json example.py



Advanced Features
*****************

Multi-Node Tasks
================

For tasks that require multiple nodes (e.g., MPI tasks), use the **resources** field:

.. code-block:: json

    {
    "taskId": 1,
    "implementationId": 0,
    "predecessors": [],
    "resources": [
        "COMPSsWorker01",
        "COMPSsWorker02",
        "COMPSsWorker03"
    ]
    }


Multiple Implementations
========================

If a task has multiple implementations (e.g., CPU and GPU versions), specify which one to use:

.. code-block:: json

    {
    "taskId": 1,
    "implementationId": 0,  // Use CPU implementation
    "predecessors": [],
    "resource": "COMPSsWorker01"
    },
    {
    "taskId": 2,
    "implementationId": 1,  // Use GPU implementation
    "predecessors": [1],
    "resource": "COMPSsWorker02"
    }


Generating Configuration from Logs
**********************************

You can generate a configuration file from a previous execution's `runtime.log`:

.. code-block:: console

    $ python3 generate_config.py runtime.log > config.json

This extracts the actual task scheduling that occurred and creates a configuration file that can be used to reproduce that exact execution.

You can find script examples on how to reproduce executions at the test suite:

``tests/sources/local/python/4_scheduler_predefined/scripts/``


Resource Name Mapping (SLURM)
*****************************

When running on SLURM clusters, the Predefined Scheduler automatically maps logical resource names to actual SLURM nodes.

How It Works
============

1. You specify logical names in your config:

.. code-block:: json
    
    {
        "taskId": 1,
        "resource": "COMPSsWorker01"
    }
   

2. The scheduler reads `SLURM_NODELIST` and maps:

.. code-block:: console

   COMPSsWorker01 → gs10r3b01-ib0
   COMPSsWorker02 → gs10r3b03-ib0
   COMPSsWorker03 → gs10r3b68-ib0


3. The mapping is **cyclic** if you have more logical workers than physical nodes

Example
=======

If `SLURM_NODELIST=node[01-03]` and your config has 5 workers:

.. code-block:: console

    COMPSsWorker01 → node01-ib0
    COMPSsWorker02 → node02-ib0
    COMPSsWorker03 → node03-ib0
    COMPSsWorker04 → node01-ib0  (cycles back)
    COMPSsWorker05 → node02-ib0
    

Limitations
===========

1. **Task ID Assignment**: Task IDs must match the order COMPSs assigns them (based on task creation order in your application)

2. **Dynamic Tasks**: Not suitable for applications with dynamic task creation patterns

3. **Resource Availability**: Assumes all specified resources are available at execution time

4. **No Runtime Adaptation**: The schedule is fixed and won't adapt to runtime conditions


Troubleshooting
***************

Configuration Not Loaded
========================

**Symptom**: Scheduler doesn't use your configuration

**Solutions**:
- Check file path is absolute or relative to execution directory
- Verify JSON syntax: `python3 -m json.tool config.json`
- Check `runtime.log` for error messages

Tasks Not Scheduled as Expected
===============================

**Symptom**: Tasks execute in different order or on different resources

**Solutions**:
- Verify task IDs match actual task creation order
- Check that resource names match exactly (case-sensitive)
- Ensure all dependencies are satisfied

Resource Not Found
==================

**Symptom**: Error about unknown resource

**Solutions**:
- Verify resource names in `project.xml` and `resources.xml`
- Check for typos in resource names
- Ensure workers are actually available

Invalid JSON
============

**Symptom**: Parser error when loading configuration

**Solutions**:
- Validate JSON: `python3 -m json.tool config.json`
- Check for:
  - Missing commas
  - Trailing commas (not allowed in JSON)
  - Unquoted strings
  - Mismatched brackets

FAQ
***

**Q**: Can I use this with any COMPSs application?
==================================================

**A**: Yes, but it works best with applications that have predictable task creation patterns.

**Q**: How do I know what task IDs will be assigned?
====================================================

**A**: Task IDs are assigned sequentially in the order tasks are created. You can run your application once with a default scheduler and extract the task IDs from the logs.

**Q**: Can I mix predefined scheduling with dynamic scheduling?
===============================================================

**A**: No, the Predefined Scheduler controls all task scheduling decisions.

**Q**: What happens if a task fails?
====================================

**A**: Standard COMPSs error handling applies. Failed tasks can be retried according to your COMPSs configuration.

**Q**: Can I update the configuration during execution?
=======================================================

**A**: No, the configuration is loaded once at startup and cannot be modified during execution.

**Q**: Does this work with all task types?
==========================================

**A**: It supports regular tasks, multi-node tasks, and tasks with multiple implementations, but does **NOT** support reduce tasks.

Performance Considerations
**************************

When to Use Predefined Scheduler
================================

**Good for**:
    * Reproducible experiments
    * Known optimal schedules
    * Testing specific scenarios
    * Trace replay

**Not ideal for**:
    * Highly dynamic workloads
    * Unknown task patterns
    * Adaptive scheduling needs
    * Load balancing across heterogeneous resources

Overhead
========

The Predefined Scheduler has minimal overhead:
- Configuration is loaded once at startup
- Scheduling decisions are O(1) lookups
- No runtime optimization computations

