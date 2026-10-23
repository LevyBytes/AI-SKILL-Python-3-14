# Configuring filters with `dictConfig()`

### Configuring filters with [`dictConfig()`](https://docs.python.org/3.14/library/logging.config.html#logging.config.dictConfig)

You *can* set up filters with [`dictConfig()`](https://docs.python.org/3.14/library/logging.config.html#logging.config.dictConfig), although the way to do it may not jump out at first (which is why this recipe exists). Given that [`Filter`](https://docs.python.org/3.14/library/logging.html#logging.Filter) is the sole filter class bundled in the standard library, and that it's unlikely to meet many needs (it sits there merely as a base class), you'll generally have to write your own `Filter` subclass with an overridden [`filter()`](https://docs.python.org/3.14/library/logging.html#logging.Filter.filter) method. For that, supply the `()` key in the filter's configuration dictionary, naming a callable that will build the filter (a class is the most obvious choice, but any callable returning a `Filter` instance works). A full example follows:

The complete program is in the [upstream source](https://docs.python.org/3.14/howto/logging-cookbook.html#configuring-filters-with-dictconfig).

This example illustrates how you can hand configuration data to the callable that constructs the instance, supplied as keyword parameters. Once run, the script above will print:

```none
changed: hello

```

which demonstrates that the filter behaves as configured.

A couple of additional points worth noting:

- When you can't name the callable directly in the configuration (say it resides in another module that you can't import where the configuration dictionary lives), you can fall back on the `ext://...` form covered in [Access to external objects](https://docs.python.org/3.14/library/logging.config.html#logging-config-dict-externalobj). For instance, in the example above you could have used the text `'ext://__main__.MyFilter'` in place of `MyFilter`.

- Beyond filters, the same technique also serves to configure custom handlers and formatters. Consult [User-defined objects](https://docs.python.org/3.14/library/logging.config.html#logging-config-dict-userdef) for more on how logging supports user-defined objects within its configuration, and review the other cookbook recipe Customizing handlers with dictConfig() above.

[Subject index](INDEX.md) · [Previous source context](using-custom-message-objects.md) · [Following source context](customized-exception-formatting.md)
