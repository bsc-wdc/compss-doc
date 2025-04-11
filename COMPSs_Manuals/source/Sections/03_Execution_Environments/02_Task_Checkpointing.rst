Checkpointing
=============

COMPSs and PyCOMPSs allow for task-level checkpointing. This feature allows the user to combine different checkpointing mechanisms to save the progress of an application execution (i.e., completed tasks and their output values) to recover it in the case of a failure. This section provides information on how to use the checkpointing recovery system. 

Application developers can request the COMPSs runtime to checkpoint the application progress with the snapshot method of the API. When this method is invoked, the final version of each data value produced by any task of the application will be checkpointed. Upcoming executions will be able to resume the execution from that point with no additional development effort.

Java example:
:: 

    import es.bsc.compss.api.COMPSs;

    COMPSs.snapshot();

Python example:
:: 

    from pycompss.api.api import compss_snapshot

    compss_snapshot()
    

In addition, the COMPSs runtime system provides three mechanisms to perform an automatic checkpointing of the application:
* Periodic checkpointing: periodically saves the application progress in configurable intervals of ``n`` hours, minutes, or seconds.
* Finished tasks: triggers the checkpointing of the application progress upon the completion on ``n`` non-checkpointed tasks.
* Tasks groups: this mechanism allows the definition of custom policies to checkpoint the application progress. A customizable policy assigns each task to a checkpointing group at task instantiation time. When all the tasks within the group have been instantiated -- the policy closes the group --, the checkpoint manager determines the final version of each data produced by the tasks within the group. As tasks producing these values complete their computation, checkpoint manager requests a copy to checkpoint that value.

To develop checkpointing policies, checkpointing policy developer need to create a Java class extending the CheckpointManagerImpl class (``es.bsc.compss.checkpoint.CheckpointManagerImpl``) and implement the ``assignTaskToGroup`` method. The ``assignTaskToGroup`` method is invoked every time that the runtime instantiates a class and its purpose is to assign a task group to that task. To that end the policy can use any information related to the task; e.g., id of the task, method to execute, accessed data versions on its parameters, etc. Once the group is determined, the policy has to invoke the ``addTaskToGroup`` method to let the checkpoint manager to which group the task belongs. In addition, if the policy determines that all the tasks within the group have been instantiated, it needs to close the group using the ``closeGroup`` method.

The following snippet shows an example of a checkpoint policy implementation creating groups of N tasks subsequently instantiated.

Checkpoint policy implementation
:: 

    public class CheckpointPolicyInstantiatedGroup extends CheckpointManagerImpl {

        private int currentGroup = 0; 
        private int groupSize = 3;
        public CheckpointPolicyInstantiatedGroup(HashMap<String, String> config, AccessProcessor ap) {
            super(config, 0, 0, ap);
            this.groupsize = config.get("instantiated.group");
        }

        @Override
        protected void assignTaskToGroup(Task t) {
            // Assign the task to the decided group
            CheckpointGroupImpl group = this.addTaskToGroup(t, String.valueOf(countingGroup));
            // If the group reaches its size of closure it closes (in this case is 1)
            if (group.getSize() == groupSize) {
                this.closeGroup(String.valueOf(countingGroup));
                countingGroup += 1;
            }

    }



COMPSs release contains three pre-defined policies, each leveraging on only one of these mechanisms:

.. table:: Checkpointing
    :name: checkpointing description
    
    +-----------------------------------+------------------------------------------------------------------------------------+-------------------------+------------------------------------------+
    | **Policy name**                   | **Class name**                                                                     | **Params**              | **Description**                          |
    +===================================+====================================================================================+=========================+==========================================+
    | Periodic Time (PT)                | es.bsc.compss.checkpoint.policies.CheckpointPolicyPeriodicTime                     | period.time             | Checkpoints every n time                 |
    +-----------------------------------+------------------------------------------------------------------------------------+-------------------------+------------------------------------------+
    | Finished Tasks (FT)               | es.bsc.compss.checkpoint.policies.CheckpointPolicyFinishedTasks                    | finished.tasks          | Checkpoints every n finished tasks       |
    +-----------------------------------+------------------------------------------------------------------------------------+-------------------------+------------------------------------------+
    | Instantiated Tasks Group (ITG)    | es.bsc.compss.checkpoint.policies.CheckpointPolicyInstantiatedGroup                | instantiated.group      | Checkpoints every n instantiated tasks   |
    +-----------------------------------+------------------------------------------------------------------------------------+-------------------------+------------------------------------------+

In order to use checkpointing it is needed to specify three flags in the ``enqueue_compss`` and ``runcompss``. These are:
* ``--checkpoint``: This parameter lets you choose the checkpointing policy, and assign one of the class names.
* ``--checkpoint_params``: This parameter lets you choose the checkpointing span, depending on the policy the user has to choose the corresponding param from the table (in the time case the user has to define the time in either s (seconds), m (minutes) or h (hours), and other options that will be explained later on.
* ``--checkpoint_folder``: This parameter defines the folder where the checkpoints will be saved.

As an additional feature the user can avoid checkpointing a specific task, that may have a big overhead on the filesystem by passing the list of signature names in the ``checkpoint_params`` flag using the following parameter ``avoid.checkpoint`` 

An example of usage would be the following:

:: 

    --checkpoint_params=period.time:s,avoid.checkpoint:[checkpoint_file_test.increment] \
    --checkpoint=es.bsc.compss.checkpoint.policies.CheckpointPolicyPeriodicTime \
    --checkpoint_folder=/tmp/checkpointing/ \
