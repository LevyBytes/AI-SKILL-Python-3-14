# multiprocessing - Using a pool of workers

### Using a pool of workers

The `Pool` class stands for a pool of worker processes. It offers methods that let tasks be handed off to the worker processes in several different ways.

For example:

The complete program is in the [upstream source](https://docs.python.org/3.14/library/multiprocessing.html#using-a-pool-of-workers).

Bear in mind that a pool's methods should only ever be invoked by the process that created the pool.

Note

For this package to work, the children must be able to import the `__main__` module. While Programming guidelines covers this point, it is worth flagging here too. The practical consequence is that certain examples, like the `multiprocessing.pool.Pool` examples, will fail inside the interactive interpreter. For example:

```python
>>> from multiprocessing import Pool
>>> p = Pool(5)
>>> def f(x):
...     return x*x
...
>>> with p:
...     p.map(f, [1,2,3])
Process PoolWorker-1:
Process PoolWorker-2:
Process PoolWorker-3:
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
AttributeError: Can't get attribute 'f' on <module '__main__' (<class '_frozen_importlib.BuiltinImporter'>)>
AttributeError: Can't get attribute 'f' on <module '__main__' (<class '_frozen_importlib.BuiltinImporter'>)>
AttributeError: Can't get attribute 'f' on <module '__main__' (<class '_frozen_importlib.BuiltinImporter'>)>

```

(Should you actually try this, it will print three complete tracebacks interleaved in a roughly random order, after which you may need to find a way to stop the parent process.)

[Subject index](INDEX.md) · [Previous](sharing-state-between-processes.md) · [Continue](reference.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md)
