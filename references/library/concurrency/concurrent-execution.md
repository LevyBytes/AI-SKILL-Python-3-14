# Concurrent Execution

- [`concurrent.interpreters` - Multiple interpreters in the same process](https://docs.python.org/3.14/library/concurrent.interpreters.html)
  - [Key details](https://docs.python.org/3.14/library/concurrent.interpreters.html#key-details)
  - [Introduction](https://docs.python.org/3.14/library/concurrent.interpreters.html#introduction)
    - [Multiple Interpreters and Isolation](https://docs.python.org/3.14/library/concurrent.interpreters.html#multiple-interpreters-and-isolation)
    - [Running in an Interpreter](https://docs.python.org/3.14/library/concurrent.interpreters.html#running-in-an-interpreter)
    - [Concurrency and Parallelism](https://docs.python.org/3.14/library/concurrent.interpreters.html#concurrency-and-parallelism)
    - [Communication Between Interpreters](https://docs.python.org/3.14/library/concurrent.interpreters.html#communication-between-interpreters)
    - [“Sharing” Objects](https://docs.python.org/3.14/library/concurrent.interpreters.html#sharing-objects)

  - [Reference](https://docs.python.org/3.14/library/concurrent.interpreters.html#reference)
    - [Interpreter objects](https://docs.python.org/3.14/library/concurrent.interpreters.html#interpreter-objects)
    - [Exceptions](https://docs.python.org/3.14/library/concurrent.interpreters.html#exceptions)
    - [Communicating Between Interpreters](https://docs.python.org/3.14/library/concurrent.interpreters.html#communicating-between-interpreters)

  - [Basic usage](https://docs.python.org/3.14/library/concurrent.interpreters.html#basic-usage)

- [`subprocess` - Subprocess management](https://docs.python.org/3.14/library/subprocess.html)
  - [Using the `subprocess` Module](https://docs.python.org/3.14/library/subprocess.html#using-the-subprocess-module)
    - [Frequently Used Arguments](https://docs.python.org/3.14/library/subprocess.html#frequently-used-arguments)
    - [Popen Constructor](https://docs.python.org/3.14/library/subprocess.html#popen-constructor)
    - [Exceptions](https://docs.python.org/3.14/library/subprocess.html#exceptions)

  - [Security Considerations](https://docs.python.org/3.14/library/subprocess.html#security-considerations)
  - [Popen Objects](https://docs.python.org/3.14/library/subprocess.html#popen-objects)
  - [Windows Popen Helpers](https://docs.python.org/3.14/library/subprocess.html#windows-popen-helpers)
    - [Windows Constants](https://docs.python.org/3.14/library/subprocess.html#windows-constants)

  - [Older high-level API](https://docs.python.org/3.14/library/subprocess.html#older-high-level-api)
  - [Replacing Older Functions with the `subprocess` Module](https://docs.python.org/3.14/library/subprocess.html#replacing-older-functions-with-the-subprocess-module)
    - [Replacing **/bin/sh** shell command substitution](https://docs.python.org/3.14/library/subprocess.html#replacing-bin-sh-shell-command-substitution)
    - [Replacing shell pipeline](https://docs.python.org/3.14/library/subprocess.html#replacing-shell-pipeline)
    - [Replacing `os.system()`](https://docs.python.org/3.14/library/subprocess.html#replacing-os-system)
    - [Replacing the `os.spawn` family](https://docs.python.org/3.14/library/subprocess.html#replacing-the-os-spawn-family)
    - [Replacing `os.popen()`](https://docs.python.org/3.14/library/subprocess.html#replacing-os-popen)

  - [Legacy Shell Invocation Functions](https://docs.python.org/3.14/library/subprocess.html#legacy-shell-invocation-functions)
  - [Notes](https://docs.python.org/3.14/library/subprocess.html#notes)
    - [Timeout Behavior](https://docs.python.org/3.14/library/subprocess.html#timeout-behavior)
    - [Converting an argument sequence to a string on Windows](https://docs.python.org/3.14/library/subprocess.html#converting-an-argument-sequence-to-a-string-on-windows)
    - [Disable use of `posix_spawn()`](https://docs.python.org/3.14/library/subprocess.html#disable-use-of-posix-spawn)

- [`sched` - Event scheduler](https://docs.python.org/3.14/library/sched.html)
  - [Scheduler Objects](https://docs.python.org/3.14/library/sched.html#scheduler-objects)

- [`queue` - A synchronized queue class](https://docs.python.org/3.14/library/queue.html)
  - [Queue Objects](https://docs.python.org/3.14/library/queue.html#queue-objects)
    - [Waiting for task completion](https://docs.python.org/3.14/library/queue.html#waiting-for-task-completion)
    - [Terminating queues](https://docs.python.org/3.14/library/queue.html#terminating-queues)

  - [SimpleQueue Objects](https://docs.python.org/3.14/library/queue.html#simplequeue-objects)

- [`contextvars` - Context Variables](https://docs.python.org/3.14/library/contextvars.html)
  - [Context Variables](https://docs.python.org/3.14/library/contextvars.html#context-variables)
  - [Manual Context Management](https://docs.python.org/3.14/library/contextvars.html#manual-context-management)
  - [asyncio support](https://docs.python.org/3.14/library/contextvars.html#asyncio-support)

Listed next are support modules backing some of the services above:

- [`_thread` - Low-level threading API](https://docs.python.org/3.14/library/_thread.html)

[Subject index](INDEX.md) · [Previous](concurrent-execution-overview.md) · [Owning module, declaration or section: Concurrent Execution](concurrent-execution-overview.md)
