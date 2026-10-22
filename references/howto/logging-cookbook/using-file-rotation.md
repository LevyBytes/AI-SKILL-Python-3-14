# Using file rotation

### Using file rotation

There are times when you'd like a log file to expand up to some threshold size, then start a new file and continue logging there. You might also wish to retain a fixed count of such files, and once that count is reached, cycle the files so that both their number and their size stay capped. To cover this pattern of use, the logging package supplies a [`RotatingFileHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.RotatingFileHandler):

```python
import glob
import logging
import logging.handlers

LOG_FILENAME = 'logging_rotatingfile_example.out'

# Set up a specific logger with our desired output level
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(
              LOG_FILENAME, maxBytes=20, backupCount=5)

my_logger.addHandler(handler)

# Log some messages
for i in range(20):
    my_logger.debug('i = %d' % i)

# See what files are created
logfiles = glob.glob('%s*' % LOG_FILENAME)

for filename in logfiles:
    print(filename)

```

You should end up with 6 distinct files, each holding a slice of the application's log history:

```none
logging_rotatingfile_example.out
logging_rotatingfile_example.out.1
logging_rotatingfile_example.out.2
logging_rotatingfile_example.out.3
logging_rotatingfile_example.out.4
logging_rotatingfile_example.out.5

```

The newest file remains `logging_rotatingfile_example.out` at all times, and whenever it hits the size cap it gets renamed with a `.1` suffix tacked on. Every backup file already present shifts its suffix upward by one (`.1` becomes `.2`, etc.) while the `.6` file gets deleted.

Plainly, this example sets the log length far too low to make a dramatic point. In real use you'd pick a fitting value for *maxBytes*.

[Subject index](INDEX.md) · [Previous source context](deploying-web-applications-using-gunicorn-and-uwsgi.md) · [Following source context](formatter-style-and-logging-call-interpolation-contracts.md)
