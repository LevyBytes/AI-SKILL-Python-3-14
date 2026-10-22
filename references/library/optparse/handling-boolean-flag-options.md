# optparse — Handling boolean (flag) options

### Handling boolean (flag) options

Flag options—setting a variable to true or false once a particular option appears—are quite common. `optparse` supports them through two separate actions, `store_true` and `store_false`. For instance, you might have a `verbose` flag switched on with `-v` and off with `-q`:

```python
parser.add_option("-v", action="store_true", dest="verbose")
parser.add_option("-q", action="store_false", dest="verbose")

```

Here we have two distinct options sharing the same destination, which is perfectly OK. (It merely means you have to take a little care when setting default values—see below.)

When `optparse` meets `-v` on the command line, it sets `options.verbose` to `True`; when it meets `-q`, `options.verbose` is set to `False`.

[Subject index](INDEX.md) · [Previous](the-store-action.md) · [Continue](other-actions.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)
