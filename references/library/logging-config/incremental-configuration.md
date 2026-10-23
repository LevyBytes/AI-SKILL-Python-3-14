# logging.config - Incremental Configuration

### Incremental Configuration

Offering full flexibility for incremental configuration is hard. For instance, since objects like filters and formatters are anonymous, once a configuration has been built it is impossible to point back at such anonymous objects when extending a configuration.

On top of that, there's no strong case for arbitrarily reshaping the object graph of loggers, handlers, filters, and formatters at run-time once a configuration is in place; the verbosity of loggers and handlers can be steered simply by setting levels (and, where loggers are concerned, propagation flags). Reshaping the object graph arbitrarily in a safe manner is tricky in a multi-threaded setting; while not out of reach, the payoff doesn't justify the complexity it would heap onto the implementation.

So, whenever the `incremental` key of a configuration dict is present and `True`, the system entirely disregards any `formatters` and `filters` entries, and handles only the `level` settings within the `handlers` entries, plus the `level` and `propagate` settings within the `loggers` and `root` entries.

Relying on a value in the configuration dict permits configurations to be shipped across the wire as pickled dicts to a socket listener. In this way the logging verbosity of a long-running application can be adjusted over time without having to halt and restart the application.

[Subject index](INDEX.md) · [Previous](dictionary-schema-details-code-example-handlers.md) · [Continue](object-connections.md) · [Owning module, declaration or section: logging.config](logging-config-logging-configuration.md)
