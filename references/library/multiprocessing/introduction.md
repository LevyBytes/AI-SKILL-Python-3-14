# multiprocessing — Introduction

### Introduction

`multiprocessing` is a package whose support for launching processes mirrors the API of the [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module. By relying on subprocesses rather than threads, the `multiprocessing` package provides concurrency both locally and remotely, neatly working around the [Global Interpreter Lock](https://docs.python.org/3.14/glossary.html#term-global-interpreter-lock). Because of that, the `multiprocessing` module lets a developer take full advantage of every processor on a given machine. It runs on both POSIX and Windows.

Through its `Pool` object, the `multiprocessing` module gives you a handy way to run one function over many input values in parallel, spreading those inputs across processes (data parallelism). The example that follows illustrates the usual approach of placing such functions inside a module, allowing child processes to import that module without trouble. This basic example of data parallelism using `Pool`,

```python
from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))

```

will print to standard output

```python
[1, 4, 9]

```

Beyond that, the `multiprocessing` module brings in APIs without counterparts in the [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module, such as being able to `terminate`, `interrupt` or `kill` a process that is running.

See also

[`concurrent.futures.ProcessPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor) provides a higher level way to hand tasks to a background process while the caller keeps running. Relative to working with the `Pool` interface directly, the [`concurrent.futures`](https://docs.python.org/3.14/library/concurrent.futures.html#module-concurrent.futures) API makes it easier to keep submitting work to the underlying process pool distinct from waiting on the outcomes.

[Subject index](INDEX.md) · [Previous](multiprocessing-process-based-parallelism.md) · [Continue](the-process-class.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md)
