# Start, stop and restart modules

The `start`, `stop` and `restart` commands then live in their own modules; starting looks like this:

```python
# start.py
import logging

logger = logging.getLogger(__name__)

def command(options):
    logger.debug('About to start %s', options.name)
    # actually do the command processing here ...
    logger.info('Started the \'%s\' service.', options.name)

```

stopping is done this way:

```python
# stop.py
import logging

logger = logging.getLogger(__name__)

def command(options):
    n = len(options.names)
    if n == 1:
        plural = ''
        services = '\'%s\'' % options.names[0]
    else:
        plural = 's'
        services = ', '.join('\'%s\'' % name for name in options.names)
        i = services.rfind(', ')
        services = services[:i] + ' and ' + services[i + 2:]
    logger.debug('About to stop %s', services)
    # actually do the command processing here ...
    logger.info('Stopped the %s service%s.', services, plural)

```

and restarting follows the same pattern:

```python
# restart.py
import logging

logger = logging.getLogger(__name__)

def command(options):
    n = len(options.names)
    if n == 1:
        plural = ''
        services = '\'%s\'' % options.names[0]
    else:
        plural = 's'
        services = ', '.join('\'%s\'' % name for name in options.names)
        i = services.rfind(', ')
        services = services[:i] + ' and ' + services[i + 2:]
    logger.debug('About to restart %s', services)
    # actually do the command processing here ...
    logger.info('Restarted the %s service%s.', services, plural)

```

[Subject index](INDEX.md) · [CLI logging dispatcher and common log-level setup](cli-logging-dispatcher-and-common-log-level-setup.md) · [CLI logging output at default, DEBUG and WARNING levels](cli-logging-output-at-default-debug-and-warning-levels.md) · [Previous source context](cli-logging-dispatcher-and-common-log-level-setup.md) · [Following source context](cli-logging-output-at-default-debug-and-warning-levels.md)
