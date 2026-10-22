# logging.handlers: `logging.handlers.BaseRotatingHandler`

### BaseRotatingHandler

Found in the `logging.handlers` module, the `BaseRotatingHandler` class is the base class behind the rotating file handlers, `RotatingFileHandler` and `TimedRotatingFileHandler`. You shouldn't have to instantiate this class, yet it carries attributes and methods you might need to override.

 *class *logging.handlers.BaseRotatingHandler(*filename*, *mode*, *encoding=None*, *delay=False*, *errors=None*)

The parameters match those for `FileHandler`. The attributes are:

[Subject index](INDEX.md) · [Previous](watched-file-reopen-and-emission.md) · [Continue](base-handler-rotation-name-and-operation.md) · [Owning module, declaration or section: logging.handlers](handler-types-overview.md)
