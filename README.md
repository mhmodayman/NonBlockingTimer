# NonBlockingTimer
One shot and periodic timers

It supports creating multiple timers
--> each will preserve its _tstate_lock, and ident during the execution (No memory leakage at all)
