# multiprocessing - All start methods - Section introduction and initial examples

### All start methods

What follows applies to every start method.

Avoid shared state

>

So far as you can manage, try not to move large amounts of data between processes.

It is most likely best to stay with queues or pipes for communication between processes, rather than reaching for the lower-level synchronization primitives.

Picklability

>

Make sure the arguments to the methods of proxies are picklable.

Thread safety of proxies

>

Refrain from touching one proxy object across several threads unless a lock guards it.

(There is never a problem with different processes using the *same* proxy.)

Joining zombie processes

>

On POSIX, when a process finishes but has not been joined, it turns into a zombie. There should never be very many, because every time a new process starts (or `active_children()` is called) every finished process that has not yet been joined gets joined. Calling a finished process's `Process.is_alive` will also join the process. Regardless, explicitly joining every process you launch is most likely sound practice.

Better to inherit than pickle/unpickle

>

When the *spawn* or *forkserver* start methods are in use, many types from `multiprocessing` have to be picklable so that child processes can use them. That said, you should as a rule steer clear of sending shared objects to other processes over pipes or queues. Instead, set up the program so that a process requiring a shared resource built elsewhere picks it up by inheritance from an ancestor process.

Avoid terminating processes

>

Using the `Process.terminate` method to halt a process is apt to leave any shared resources (locks, semaphores, pipes and queues, for instance) the process is currently using broken or out of reach for other processes.

So it is probably best to consider using `Process.terminate` only on processes that never touch any shared resources.

Joining processes that use queues

>

Remember that, once a process has placed items in a queue, it puts off terminating until the “feeder” thread has fed every buffered item into the underlying pipe. (The child process can call the queue's `Queue.cancel_join_thread` method to sidestep this behaviour.)

This means that whenever you use a queue you have to make certain every item placed on the queue eventually gets removed before the process is joined. Otherwise you cannot be certain that processes which placed items on the queue will terminate. Bear in mind too that non-daemonic processes get joined automatically.

An example that will deadlock is the following:

```python
from multiprocessing import Process, Queue

def f(q):
    q.put('X' * 1000000)

if __name__ == '__main__':
    queue = Queue()
    p = Process(target=f, args=(queue,))
    p.start()
    p.join()                    # this deadlocks
    obj = queue.get()

```

One remedy is to flip the final two lines around (or just delete the `p.join()` line).

Explicitly pass resources to child processes

>

On POSIX with the *fork* start method, a child process is able to tap a shared resource built in a parent process by way of a global resource. The better route, though, is handing the object in as an argument to the child process's constructor.

Aside from making the code (potentially) work with Windows and the other start methods, this also makes sure that, as long as the child process stays alive, the object will not be garbage collected in the parent process. That might matter if some resource is freed when the object gets garbage collected in the parent process.

So for instance

[Subject index](INDEX.md) · [Previous](programming-guidelines.md) · [Continue](process-start-lock-example.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md)
