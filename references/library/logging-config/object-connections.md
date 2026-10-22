# logging.config — Object connections

### Object connections

The schema lays out a collection of logging objects — loggers, handlers, formatters, filters — that link to one another within an object graph. The schema therefore has to capture the links among the objects. For instance, suppose that, after configuration, a given logger has a given handler attached to it. For the sake of this discussion, we can say the logger is the source, and the handler the destination, of a link between the two. Naturally, within the configured objects this shows up as the logger holding a reference to the handler. Inside the configuration dict, this is accomplished by handing each destination object an id that pins it down unambiguously, and then citing that id in the source object's configuration to declare that a link runs between the source and the destination object bearing that id.

So, for example, take the following YAML snippet:

```yaml
formatters:
  brief:
    # configuration for formatter with id 'brief' goes here
  precise:
    # configuration for formatter with id 'precise' goes here
handlers:
  h1: #This is an id
   # configuration of handler with id 'h1' goes here
   formatter: brief
  h2: #This is another id
   # configuration of handler with id 'h2' goes here
   formatter: precise
loggers:
  foo.bar.baz:
    # other configuration for logger 'foo.bar.baz'
    handlers: [h1, h2]

```

(Note: YAML appears here because it reads a touch more clearly than the equivalent Python source layout for the dictionary.)

The ids belonging to loggers are the logger names you would use programmatically to grab a reference to those loggers, e.g. `foo.bar.baz`. For Formatters and Filters, any string value works as an id (`brief`, `precise` shown earlier, for instance); such ids are transient, meaning they matter only while the configuration dictionary is being processed and serve to work out links among objects, and nothing persists them anywhere once the configuration call wraps up.

The snippet above states that the logger named `foo.bar.baz` should have two handlers attached, the ones identified by the handler ids `h1` and `h2`. The formatter for `h1` is the one identified by id `brief`, and the formatter for `h2` is the one identified by id `precise`.

[Subject index](INDEX.md) · [Previous](incremental-configuration.md) · [Continue](user-defined-objects.md) · [Owning module, declaration or section: logging.config](logging-config-logging-configuration.md)
