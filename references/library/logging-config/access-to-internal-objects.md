# logging.config — Access to internal objects

### Access to internal objects

Beyond external objects, there is now and then a need to point at objects within the configuration as well. The configuration system handles that implicitly for the things it already understands. To illustrate, the string value `'DEBUG'` given for a `level` on a logger or handler is converted automatically into the value `logging.DEBUG`, while the `handlers`, `filters` and `formatter` entries accept an object id and resolve to the matching destination object.

That said, a more general mechanism becomes necessary for user-defined objects the [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging) module knows nothing about. Take [`logging.handlers.MemoryHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.MemoryHandler) as an example: it accepts a `target` argument, namely another handler it forwards to. Since this class is already familiar to the system, within the configuration the supplied `target` only has to be the object id of the appropriate target handler, and the system resolves to the handler from that id. But if a user writes a `my.package.MyHandler` sporting an `alternate` handler, the configuration system has no way of knowing that `alternate` denotes a handler. To handle that case, a general resolution system lets the user state:

```yaml
handlers:
  file:
    # configuration of file handler goes here

  custom:
    (): my.package.MyHandler
    alternate: cfg://handlers.file

```

The literal string `'cfg://handlers.file'` gets resolved much as strings bearing the `ext://` prefix do, except the lookup happens inside the configuration itself in place of the import namespace. This mechanism permits access via dot or via index, along the lines of what `str.format` offers. So, with the snippet that follows:

```yaml
handlers:
  email:
    class: logging.handlers.SMTPHandler
    mailhost: localhost
    fromaddr: my_app@domain.tld
    toaddrs:
      - support_team@domain.tld
      - dev_team@domain.tld
    subject: Houston, we have a problem.

```

within the configuration, the string `'cfg://handlers'` points to the dict keyed by `handlers`, the string `'cfg://handlers.email` points to the dict keyed by `email` inside the `handlers` dict, and onward in that fashion. The string `'cfg://handlers.email.toaddrs[1]` lands on `'dev_team@domain.tld'`, whereas the string `'cfg://handlers.email.toaddrs[0]'` lands on the value `'support_team@domain.tld'`. You could reach the `subject` value with either `'cfg://handlers.email.subject'` or, equally, `'cfg://handlers.email[subject]'`. That second form is only called for when the key holds spaces or characters that aren't alphanumeric. Do bear in mind that the characters `[` and `]` may not appear in the keys. When an index value is made up solely of decimal digits, the lookup is first tried with the matching integer value, dropping back to the string value should that be necessary.

Take a string `cfg://handlers.myhandler.mykey.123`: it resolves to `config_dict['handlers']['myhandler']['mykey']['123']`. Should the string instead be given as `cfg://handlers.myhandler.mykey[123]`, the system first tries to pull the value from `config_dict['handlers']['myhandler']['mykey'][123]`, then falls back to `config_dict['handlers']['myhandler']['mykey']['123']` if that comes up empty.

[Subject index](INDEX.md) · [Previous](access-to-external-objects.md) · [Continue](import-resolution-and-custom-importers.md) · [Owning module, declaration or section: logging.config](logging-config-logging-configuration.md)
