# 4.4.1. General Computing Model

### 4.4. Runtime Components

### 4.4.1. General Computing Model

Python's execution model is not something that runs in isolation. It executes atop a host machine and by way of that host's runtime environment — including its operating system (OS), where one exists. As a program runs, the conceptual layers describing how it runs on the host take roughly this shape:

>   **host machine**  **process** (global resources)  **thread** (runs machine code)

A process stands for a program running on the host. Picture each process as being the data part of its program. Picture the threads of the process as the execution part of the program. Grasping this distinction will matter for understanding the conceptual Python runtime.

The process, in its role as the data part, is the execution context within which the program runs. By and large it amounts to the collection of resources the host assigns to the program — memory, signals, file handles, sockets, and environment variables among them.

One process is isolated and independent from another. (The same goes for one host versus another.) The host both governs the process' access to its assigned resources and coordinates among processes.

A thread stands for the genuine execution of the program's machine code, running with respect to the resources assigned to the program's process. When and how that execution happens is entirely the host's call.

As Python sees it, a program always begins with exactly one thread. The program may, however, expand to run across several threads at once. Multiple threads per process is something most hosts support, though not all. Threads within a process, unlike processes, are neither isolated nor independent from one another. To be precise, every thread in a process shares all of the process' resources.

The crux of threads is that each one genuinely does *run* on its own, alongside the others at the same moment. That "same moment" may be merely conceptual ("concurrently") or actual ("in parallel"). Whichever it is, the threads run, in effect, at a rate that is not synchronized.

Note

That unsynchronized rate means there is no guarantee that any of the process' memory stays consistent for the code running in a given thread. Multi-threaded programs must therefore be careful to coordinate access to resources meant to be shared. They must likewise be utterly scrupulous about never touching any *other* resources from multiple threads; otherwise two threads running concurrently could inadvertently trip over each other's use of some shared data. The whole of this holds for both Python programs and the Python runtime.

What this sweeping, unstructured demand costs you is the price paid for the sort of raw concurrency threads deliver. Skipping the required discipline generally lands you with non-deterministic bugs and corrupted data.

[Subject index](INDEX.md) · [Owning language section](structure-of-a-program.md) · [Previous source section](exceptions.md) · [Following source section](python-runtime-model.md)
