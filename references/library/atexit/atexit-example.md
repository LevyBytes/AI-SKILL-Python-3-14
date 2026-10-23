# atexit`atexit` Example

### `atexit` Example

The short example below shows a module seeding a counter from a file at import time and then writing the counter's new value back automatically as the program ends, all without depending on the application to call into this module explicitly at termination.

```python
try:
    with open('counterfile') as infile:
        _count = int(infile.read())
except FileNotFoundError:
    _count = 0

def incrcounter(n):
    global _count
    _count = _count + n

def savecounter():
    with open('counterfile', 'w') as outfile:
        outfile.write('%d' % _count)

import atexit

atexit.register(savecounter)

```

You may likewise feed positional and keyword arguments into `register()`, and they get forwarded to the registered function at call time:

```python
def goodbye(name, adjective):
    print('Goodbye %s, it was %s to meet you.' % (name, adjective))

import atexit

atexit.register(goodbye, 'Donny', 'nice')
# or:
atexit.register(goodbye, adjective='nice', name='Donny')

```

Applied as a [decorator](https://docs.python.org/3.14/glossary.html#term-decorator):

```python
import atexit

@atexit.register
def goodbye():
    print('You are now leaving the Python sector.')

```

Only functions invocable with no arguments will work this way.

[Subject index](INDEX.md) · [Previous](atexit-register-to-atexit-unregister.md) · [Continue](../audioop/audioop-manipulate-raw-audio-data.md) · [Owning module, declaration or section: atexit](atexit-register-to-atexit-unregister.md)
