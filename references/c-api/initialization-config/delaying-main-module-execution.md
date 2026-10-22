# Delaying main module execution

### Delaying main module execution

For certain embedding scenarios, you may wish to keep interpreter initialization apart from running the main module.

You reach that split by assigning `PyConfig.run_command` the empty string while initializing (so the interpreter does not fall through to the interactive prompt), and then afterward running whatever main-module code you intend with `__main__.__dict__` serving as the global namespace.

[Subject index](INDEX.md) · [Previous source contract](py-getargcargv.md)
