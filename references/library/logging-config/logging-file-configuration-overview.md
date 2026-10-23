# logging.config - Configuration file format - Section introduction and initial examples

### Configuration file format

The configuration file format that `fileConfig()` reads builds on [`configparser`](https://docs.python.org/3.14/library/configparser.html#module-configparser) functionality. Such a file is required to hold sections named `[loggers]`, `[handlers]` and `[formatters]`, which name the entities of each kind that the file defines. Every one of those entities then gets its own separate section spelling out how it is configured. So a logger named `log01` listed in the `[loggers]` section keeps its configuration details in a section `[logger_log01]`. In the same vein, a handler named `hand01` in the `[handlers]` section stores its configuration in a section called `[handler_hand01]`, and a formatter named `form01` in the `[formatters]` section has its configuration laid out in a section called `[formatter_form01]`. As for the root logger, its configuration has to live in a section called `[logger_root]`.

Note

Predating the `dictConfig()` API, the `fileConfig()` API lacks functionality for certain facets of logging. You cannot, for instance, set up [`Filter`](https://docs.python.org/3.14/library/logging.html#logging.Filter) objects — which filter messages on grounds beyond plain integer levels — by means of `fileConfig()`. Whenever your logging configuration calls for `Filter` instances, `dictConfig()` is what you must turn to. Keep in mind that upcoming additions to configuration functionality will land in `dictConfig()`, so moving over to this newer API once it suits you is worth weighing.

Below are examples of these sections as they appear in the file.

```ini
[loggers]
keys=root,log02,log03,log04,log05,log06,log07

[handlers]
keys=hand01,hand02,hand03,hand04,hand05,hand06,hand07,hand08,hand09

[formatters]
keys=form01,form02,form03,form04,form05,form06,form07,form08,form09

```

A level together with a list of handlers must be given for the root logger. Here is a sample root logger section.

```ini
[logger_root]
level=NOTSET
handlers=hand01

```

The `level` entry may take any one of `DEBUG, INFO, WARNING, ERROR, CRITICAL` or `NOTSET`. In the case of the root logger alone, `NOTSET` signifies that every message gets logged. Level values are [evaluated](https://docs.python.org/3.14/library/functions.html#func-eval) within the namespace of the `logging` package.

The `handlers` entry holds a comma-separated list of handler names, each of which has to show up in the `[handlers]` section. Those names are required both to appear in the `[handlers]` section and to have matching sections elsewhere in the configuration file.

Loggers other than the root one call for a bit more information. The example below brings this out.

```ini
[logger_parser]
level=DEBUG
handlers=hand01
propagate=1
qualname=compiler.parser

```

Here the `level` and `handlers` entries carry the same meaning they do for the root logger, with one twist: if a non-root logger has its level set to `NOTSET`, the system looks to loggers further up the hierarchy to work out that logger's effective level. Setting the `propagate` entry to 1 says messages from this logger should travel up to handlers higher in the logger hierarchy, while 0 says messages are **not** carried up to handlers above. The `qualname` entry gives the logger's hierarchical channel name — in other words, the name the application uses to fetch the logger.

The following illustrates sections that lay out handler configuration.

```ini
[handler_hand01]
class=StreamHandler
level=NOTSET
formatter=form01
args=(sys.stdout,)

```

The `class` entry names the handler's class (worked out via [`eval()`](https://docs.python.org/3.14/library/functions.html#eval) within the `logging` package's namespace). The `level` carries the same meaning it has for loggers, and `NOTSET` is read as 'log everything'.

The `formatter` entry names the key of the formatter belonging to this handler. Left blank, a default formatter (`logging._defaultFormatter`) takes over. When a name is given, it has to appear in the `[formatters]` section and have a matching section in the configuration file.

Once [evaluated](https://docs.python.org/3.14/library/functions.html#func-eval) within the `logging` package's namespace, the `args` entry supplies the list of arguments passed to the handler class's constructor. Look to the constructors of the relevant handlers, or to the examples further down, to see how typical entries take shape. Absent a value, it defaults to `()`.

The optional `kwargs` entry, after being [evaluated](https://docs.python.org/3.14/library/functions.html#func-eval) within the `logging` package's namespace, gives the keyword-argument dict handed to the handler class's constructor. Absent a value, it defaults to `{}`.

[Subject index](INDEX.md) · [Previous](configuring-queuehandler-and-queuelistener.md) · [Continue](configuration-file-format-code-example-handler-hand02.md) · [Owning module, declaration or section: logging.config](logging-config-logging-configuration.md)
