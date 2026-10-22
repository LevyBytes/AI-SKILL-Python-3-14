# logging.handlers: `logging.handlers.TimedRotatingFileHandler`

### TimedRotatingFileHandler

Found in the `logging.handlers` module, the `TimedRotatingFileHandler` class supports rotation of disk log files at given timed intervals.

 `*class *logging.handlers.TimedRotatingFileHandler(*filename*, *when='h'*, *interval=1*, *backupCount=0*, *encoding=None*, *delay=False*, *utc=False*, *atTime=None*, *errors=None*)`

Hands back a fresh instance of the `TimedRotatingFileHandler` class. The named file is opened and serves as the stream for logging. While rotating it likewise sets the filename suffix. Rotating is driven by the product of *when* and *interval*.

The *when* lets you state the type of *interval*. The roster of allowed values follows. Note that they are not case sensitive.

| Value | Type of interval | If/how *atTime* is used |
| --- | --- | --- |
| `'S'` | Seconds | Ignored |
| `'M'` | Minutes | Ignored |
| `'H'` | Hours | Ignored |
| `'D'` | Days | Ignored |
| `'W0'-'W6'` | Weekday (0=Monday) | Used to compute initial rollover time |
| `'midnight'` | Roll over at midnight, if *atTime* not specified, else at time *atTime* | Used to compute initial rollover time |

For weekday-based rotation, give 'W0' for Monday, 'W1' for Tuesday, and onward through 'W6' for Sunday. Here, whatever value is passed for *interval* goes unused.

The system keeps old log files by tacking extensions onto the filename. Those extensions are date-and-time based, drawing on the strftime format `%Y-%m-%d_%H-%M-%S` or a leading slice of it, depending on the rollover interval.

While computing the next rollover time on this very first occasion (at handler creation), the calculation of when the next rotation will take place draws on the last modification time of an existing log file, or otherwise the current time.

When the *utc* argument is true, UTC times are used; otherwise local time applies.

When *backupCount* is nonzero, no more than *backupCount* files are retained, and if rollover would produce more than that, the oldest one is removed. The deletion logic leans on the interval to decide which files to remove, so altering the interval may leave old files hanging around.

When *delay* is true, opening the file is held off until `emit()` is first called.

When *atTime* is not `None`, it has to be a `datetime.time` instance stating the time of day at which rollover takes place, for the situations where rollover is configured to occur "at midnight" or "on a particular weekday". Keep in mind that in those situations the *atTime* value effectively drives computation of the *initial* rollover, while later rollovers would be worked out through the normal interval calculation.

When *errors* is given, it decides how encoding errors get handled.

Note

The initial rollover time is computed at the moment the handler is initialised. Later rollover times are computed solely when rollover happens, and rollover happens solely when emitting output. Failing to bear this in mind could breed some confusion. For instance, when an interval of "every minute" is set, that doesn't guarantee you'll always see log files whose times (in the filename) are a minute apart; should logging output be produced more often than once a minute while the application runs, *then* you can look forward to log files whose times are a minute apart. If, conversely, logging messages come out only once every five minutes (say), then the file times will have gaps spanning the minutes during which no output (and so no rollover) happened.

Changed in version 3.4: *atTime* parameter was added.

Changed in version 3.6: Beyond string values, [`Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) objects are now accepted too for the *filename* argument.

Changed in version 3.9: The *errors* parameter was added.

[Subject index](INDEX.md) · [Previous](rotating-file-rollover-policy.md) · [Continue](timed-rotation-rollover-methods.md) · [Owning module, declaration or section: logging.handlers](handler-types-overview.md)
