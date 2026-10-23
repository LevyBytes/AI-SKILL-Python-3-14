# pathlib - Basic use

### Basic use

Importing the main class:

```python
>>> from pathlib import Path

```

Listing subdirectories:

```python
>>> p = Path('.')
>>> [x for x in p.iterdir() if x.is_dir()]
[PosixPath('.hg'), PosixPath('docs'), PosixPath('dist'),
 PosixPath('__pycache__'), PosixPath('build')]

```

Listing Python source files in this directory tree:

```python
>>> list(p.glob('**/*.py'))
[PosixPath('test_pathlib.py'), PosixPath('setup.py'),
 PosixPath('pathlib.py'), PosixPath('docs/conf.py'),
 PosixPath('build/lib/pathlib.py')]

```

Navigating inside a directory tree:

```python
>>> p = Path('/etc')
>>> q = p / 'init.d' / 'reboot'
>>> q
PosixPath('/etc/init.d/reboot')
>>> q.resolve()
PosixPath('/etc/rc.d/init.d/halt')

```

Querying path properties:

```python
>>> q.exists()
True
>>> q.is_dir()
False

```

Opening a file:

```python
>>> with q.open() as f: f.readline()
...
'#!/bin/bash\n'

```

[Subject index](INDEX.md) · [Previous](pathlib-object-oriented-filesystem-paths.md) · [Continue](pathlib-unsupportedoperation.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md)
