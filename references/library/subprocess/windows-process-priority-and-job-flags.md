# subprocess: `subprocess.REALTIME_PRIORITY_CLASS`, `subprocess.CREATE_NO_WINDOW`, `subprocess.DETACHED_PROCESS`, `subprocess.CREATE_DEFAULT_ERROR_MODE`, `subprocess.CREATE_BREAKAWAY_FROM_JOB`

subprocess.REALTIME_PRIORITY_CLASS

A `Popen` `creationflags` parameter signaling that the new process should run at realtime priority. Reaching for REALTIME_PRIORITY_CLASS is almost never warranted, since it disrupts system threads handling mouse input, keyboard input, and background disk flushing. Such a class suits applications that "talk" straight to hardware or that carry out short tasks meant to face minimal interruption.

Added in version 3.7.

 subprocess.CREATE_NO_WINDOW

A `Popen` `creationflags` parameter signaling that the new process should open no window.

Added in version 3.7.

 subprocess.DETACHED_PROCESS

A `Popen` `creationflags` parameter signaling that the new process should not inherit the console of its parent. Pairing this value with CREATE_NEW_CONSOLE is not allowed.

Added in version 3.7.

 subprocess.CREATE_DEFAULT_ERROR_MODE

A `Popen` `creationflags` parameter signaling that the new process should skip inheriting the calling process's error mode. The new process instead receives the default error mode. Multithreaded shell applications running with hard errors disabled find this feature especially handy.

Added in version 3.7.

 subprocess.CREATE_BREAKAWAY_FROM_JOB

A `Popen` `creationflags` parameter signaling that the new process should stay unconnected to the job.

Added in version 3.7.

[Subject index](INDEX.md) · [Previous](windows-standard-handles-and-process-flags.md) · [Continue](subprocess-call-to-subprocess-check-call.md) · [Owning module, declaration or section: subprocess](subprocess-subprocess-management.md) · [Owning module, declaration or section: Windows Constants](windows-standard-handles-and-process-flags.md)
