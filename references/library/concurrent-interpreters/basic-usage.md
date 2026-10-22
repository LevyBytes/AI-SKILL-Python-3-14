# concurrent.interpreters — Basic usage

### Basic usage

Building an interpreter and running code within it:

```python
from concurrent import interpreters

interp = interpreters.create()

# Run in the current OS thread.

interp.exec('print("spam!")')

interp.exec("""if True:
    print('spam!')
    """)

from textwrap import dedent
interp.exec(dedent("""
    print('spam!')
    """))

def run(arg):
    return arg

res = interp.call(run, 'spam!')
print(res)

def run():
    print('spam!')

interp.call(run)

# Run in new OS thread.

t = interp.call_in_thread(run)
t.join()

```

[Subject index](INDEX.md) · [Previous](interpreter-queues-and-capacity-errors.md) · [Owning module, declaration or section: concurrent.interpreters](multiple-interpreters-overview.md)
