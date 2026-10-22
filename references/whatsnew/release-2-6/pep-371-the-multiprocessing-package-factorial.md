# Python 2.6 changes: Multiprocessing factorial example output

```python
import time
from multiprocessing import Pool, Manager

def factorial(N, dictionary):
    "Compute a factorial."
    # Calculate the result
    fact = 1L
    for i in range(1, N+1):
        fact = fact * i

    # Store result in dictionary
    dictionary[N] = fact

if __name__ == '__main__':
    p = Pool(5)
    mgr = Manager()
    d = mgr.dict()         # Create shared dictionary

    # Run tasks using the pool
    for N in range(1, 1000, 10):
        p.apply_async(factorial, (N, d))

    # Mark pool as closed -- no more tasks can be added.
    p.close()

    # Wait for tasks to exit
    p.join()

    # Output results
    for k, v in sorted(d.items()):
        print k, v

```

Running it yields this output:

```python
1 1
11 39916800
21 51090942171709440000
31 8222838654177922817725562880000000
41 33452526613163807108170062053440751665152000000000
51 15511187532873822802242430164693032110632597200169861120000...

```

See also

The documentation for the [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) module.

[**PEP 371**](https://peps.python.org/pep-0371/) - Addition of the multiprocessing package

The PEP was authored by Jesse Noller together with Richard Oudkerk; the implementation came from Richard Oudkerk and Jesse Noller.

[Subject index](INDEX.md) · [Previous source section](pep-371-the-multiprocessing-package-factorial-and-factorial.md) · [Next source section](pep-3101-advanced-string-formatting-to.md) · [Release/subject declaration](python-3-0.md) · [Release/subject declaration](multiprocessing-package-introduction.md) · [Preceding release/subject continuation](multiprocessing-package-introduction.md)
