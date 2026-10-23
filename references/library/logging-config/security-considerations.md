# logging.config - Security considerations

### Security considerations

The logging configuration machinery aims to be convenient, and part of how it does so is by providing the means to turn text inside configuration files into Python objects employed in logging configuration — for instance, as described in User-defined objects. That said, these very mechanisms (importing callables out of user-defined modules and invoking them with parameters drawn from the configuration) could equally be turned to running any code at all, and for that reason you should handle configuration files originating from untrusted sources with *extreme caution* and convince yourself that nothing harmful can result from loading them, before you actually do load them.

[Subject index](INDEX.md) · [Previous](logging-config-fileconfig-to-logging-config-stoplistening.md) · [Continue](configuration-dictionary-schema.md) · [Owning module, declaration or section: logging.config](logging-config-logging-configuration.md)
