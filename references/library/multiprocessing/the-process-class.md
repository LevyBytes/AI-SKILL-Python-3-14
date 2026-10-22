# multiprocessing — The `Process` class

### The `Process` class

Under `multiprocessing`, you spawn a process by constructing a `Process` object and then invoking its `start()` method. As for its interface, `Process` tracks that of [`threading.Thread`](https://docs.python.org/3.14/library/threading.html#threading.Thread). Below is a bare-bones multiprocess program:

```python
from multiprocessing import Process

def f(name):
    print('hello', name)

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()

```

The expanded example below surfaces the specific process IDs at play:

```python
from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()

```

To learn why the `if __name__ == '__main__'` portion is required, consult Programming guidelines.

In general the arguments handed to `Process` have to be picklable so they can travel to the child process. Were you to type the example above straight into a REPL, the child process might raise an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) while attempting to find the *f* function inside the `__main__` module.

[Subject index](INDEX.md) · [Previous](introduction.md) · [Continue](contexts-and-start-methods.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md)
