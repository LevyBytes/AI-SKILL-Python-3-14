# Using a rotator and namer to customize log rotation processing

### Using a rotator and namer to customize log rotation processing

The runnable script below demonstrates one way to define a namer and rotator, showing gzip compression applied to the log file:

```python
import gzip
import logging
import logging.handlers
import os
import shutil

def namer(name):
    return name + ".gz"

def rotator(source, dest):
    with open(source, 'rb') as f_in:
        with gzip.open(dest, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    os.remove(source)

rh = logging.handlers.RotatingFileHandler('rotated.log', maxBytes=128, backupCount=5)
rh.rotator = rotator
rh.namer = namer

root = logging.getLogger()
root.setLevel(logging.INFO)
root.addHandler(rh)
f = logging.Formatter('%(asctime)s %(message)s')
rh.setFormatter(f)
for i in range(1000):
    root.info(f'Message no. {i + 1}')

```

Once this has run, six new files turn up, five of them compressed:

```shell
$ ls rotated.log*
rotated.log       rotated.log.2.gz  rotated.log.4.gz
rotated.log.1.gz  rotated.log.3.gz  rotated.log.5.gz
$ zcat rotated.log.1.gz
2023-01-20 02:28:17,767 Message no. 996
2023-01-20 02:28:17,767 Message no. 997
2023-01-20 02:28:17,767 Message no. 998

```

[Subject index](INDEX.md) · [Previous source context](an-example-dictionary-based-configuration.md) · [Following source context](imports-dispatch-handler-and-whole-listener-process.md)
