# Logging to multiple destinations

### Logging to multiple destinations

Suppose you wish to send log output to both the console and a file, using distinct message formats and applying under distinct conditions. Imagine routing messages at DEBUG and above into the file, while only INFO and above reach the console. Assume too that the file ought to carry timestamps although the console lines should omit them. The following shows one way to pull this off:

```python
import logging

# set up logging to file - see previous section for more details
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='/tmp/myapp.log',
                    filemode='w')
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger().addHandler(console)

# Now, we can log to the root logger, or any other logger. First the root...
logging.info('Jackdaws love my big sphinx of quartz.')

# Now, define a couple of other loggers which might represent areas in your
# application:

logger1 = logging.getLogger('myapp.area1')
logger2 = logging.getLogger('myapp.area2')

logger1.debug('Quick zephyrs blow, vexing daft Jim.')
logger1.info('How quickly daft jumping zebras vex.')
logger2.warning('Jail zesty vixen who grabbed pay from quack.')
logger2.error('The five boxing wizards jump quickly.')

```

After you run this, the console output reads:

```none
root        : INFO     Jackdaws love my big sphinx of quartz.
myapp.area1 : INFO     How quickly daft jumping zebras vex.
myapp.area2 : WARNING  Jail zesty vixen who grabbed pay from quack.
myapp.area2 : ERROR    The five boxing wizards jump quickly.

```

while the file ends up holding roughly this:

```none
10-22 22:19 root         INFO     Jackdaws love my big sphinx of quartz.
10-22 22:19 myapp.area1  DEBUG    Quick zephyrs blow, vexing daft Jim.
10-22 22:19 myapp.area1  INFO     How quickly daft jumping zebras vex.
10-22 22:19 myapp.area2  WARNING  Jail zesty vixen who grabbed pay from quack.
10-22 22:19 myapp.area2  ERROR    The five boxing wizards jump quickly.

```

Notice the DEBUG line appears solely in the file. Every other message lands in both places.

Console and file handlers feature in this example, yet you are free to combine whatever count and assortment of handlers suits you.

Keep in mind that picking the log filename `/tmp/myapp.log` above assumes the conventional POSIX spot for transient files. Under Windows you will likely want a different folder for the log - simply confirm the folder exists and that your account can both create and write files within it.

[Subject index](INDEX.md) · [Previous source context](multiple-handlers-and-formatters.md) · [Following source context](route-logging-severities-to-stdout-stderr-and-file.md)
