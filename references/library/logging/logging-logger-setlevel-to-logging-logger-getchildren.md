# logging / Logger Objects: `setLevel()`, `isEnabledFor()`, `getEffectiveLevel()`, `getChild()`, `getChildren()`

level

The threshold of this logger, as set by the `setLevel()` method.

Note

Don't set this attribute directly: always go through `setLevel()`, which validates the level it's handed.

 parent

This logger's parent logger. It may shift as a result of loggers higher up the namespace hierarchy being instantiated later.

Note

This value should be treated as read-only.

 propagate

Should this attribute evaluate to true, events logged to this logger will be handed off to the handlers of higher level (ancestor) loggers, on top of any handlers attached to this logger. Messages go straight to the ancestor loggers' handlers — neither the level nor the filters of the ancestor loggers in question come into play.

When this evaluates to false, logging messages aren't passed on to the handlers of ancestor loggers.

To spell it out by example: should the propagate attribute belonging to the logger named `A.B.C` evaluate to true, then any event logged to `A.B.C` through a method call like `logging.getLogger('A.B.C').error(...)` will [provided it clears that logger's level and filter settings] reach, one after another, whatever handlers are attached to the loggers named `A.B`, `A` and the root logger, having first reached any handlers attached to `A.B.C`. Should any logger sitting on the chain `A.B.C`, `A.B`, `A` carry a `propagate` attribute set to false, then that logger becomes the final one whose handlers are offered the event for handling, and propagation stops right there.

The constructor sets this attribute to `True`.

Note

When you attach a handler to a logger *and* to one or more of its ancestors, it may emit the same record several times. As a rule, you shouldn't have to attach a handler to more than a single logger — if you simply attach it to the fitting logger sitting highest in the logger hierarchy, then it will see every event logged by all descendant loggers, as long as their propagate setting stays at `True`. One common pattern is to attach handlers solely to the root logger and to let propagation handle the remainder.

 handlers

The list of handlers directly attached to this logger instance.

Note

This attribute should be treated as read-only; ordinarily it's altered through the `addHandler()` and `removeHandler()` methods, which rely on locks to keep operation thread-safe.

 disabled

This attribute switches off handling of any events. The initializer sets it to `False`, and only logging configuration code ever changes it.

Note

This attribute should be treated as read-only.

 setLevel(*level*)

Sets this logger's threshold to *level*. Logging messages less severe than *level* will be disregarded; logging messages carrying severity *level* or above will be emitted by whatever handler or handlers serve this logger, unless a handler's level has been set to a severity higher than *level*.

At the moment a logger is created, its level is set to `NOTSET` (which leads to every message being processed where the logger happens to be the root logger, or to delegation to the parent where the logger happens to be a non-root one). Note that the root logger comes into being with level `WARNING`.

The phrase 'delegation to the parent' means that when a logger carries a level of NOTSET, its chain of ancestor loggers is walked until either an ancestor whose level isn't NOTSET turns up, or the root is reached.

Should an ancestor turn up whose level isn't NOTSET, then that ancestor's level counts as the effective level for the logger at which the ancestor search kicked off, and it governs how a logging event gets handled.

Should the root be reached while it carries a level of NOTSET, then every message will be processed. If not, the root's level serves as the effective level.

See Logging Levels for a list of levels.

Changed in version 3.2: As an alternative to the integer constants such as `INFO`, the *level* parameter now also takes a string spelling of the level such as ‘INFO’. Be aware, though, that internally levels live as integers, and methods like e.g. `getEffectiveLevel()` and `isEnabledFor()` will hand back, or expect to be handed, integers.

 isEnabledFor(*level*)

Reports whether a message of severity *level* would be processed by this logger. The method looks first at the module-level level established through `logging.disable(level)` and afterwards at the logger's effective level as worked out by `getEffectiveLevel()`.

 getEffectiveLevel()

Reports the effective level for this logger. When a value other than `NOTSET` has been set via `setLevel()`, that value comes back. Otherwise, the hierarchy is walked toward the root until a value other than `NOTSET` shows up, and that value is returned. The returned value is an integer, usually one of `logging.DEBUG`, `logging.INFO` etc.

 getChild(*suffix*)

Hands back a logger that is a descendant of this logger, as worked out from the suffix. So `logging.getLogger('abc').getChild('def.ghi')` would hand back the same logger that `logging.getLogger('abc.def.ghi')` would. This convenience method comes in handy when the parent logger is named with e.g. `__name__` rather than a literal string.

Added in version 3.2.

 getChildren()

Hands back a set of loggers that are immediate children of this logger. So for instance `logging.getLogger().getChildren()` might hand back a set holding loggers named `foo` and `bar`, but a logger named `foo.bar` wouldn't show up in the set. Similarly, `logging.getLogger('foo').getChildren()` might hand back a set holding a logger named `foo.bar`, though it wouldn't hold one named `foo.bar.baz`.

Added in version 3.12.

[Subject index](INDEX.md) · [Previous](logging-logger-class.md) · [Continue](logging-logger-debug-to-logging-logger-exception.md) · [Owning module, declaration or section: logging](logging-logging-facility-for-python.md) · [Owning module, declaration or section: logging.Logger; name](logging-logger-class.md) · [Owning module, declaration or section: Logger Objects](logging-logger-class.md)
