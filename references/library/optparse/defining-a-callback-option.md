# optparse — Defining a callback option

### Defining a callback option

As ever, the simplest path to defining a callback option runs through the `OptionParser.add_option()` method. Beyond `action`, the lone option attribute you must give is `callback`, the function to invoke:

```python
parser.add_option("-c", action="callback", callback=my_callback)

```

Since `callback` is a function (or any other callable object), `my_callback()` has to already exist by the moment this callback option gets defined. Here, in this simple case, `optparse` has no idea whether `-c` accepts arguments, which usually means the option accepts none—the mere presence of `-c` on the command-line is everything `optparse` requires. Under some circumstances, though, you may want your callback to gobble up an arbitrary number of command-line arguments. That's where writing callbacks turns tricky; it's covered later in this section.

`optparse` always feeds your callback four particular arguments, and it only passes extra arguments when you specify them via `callback_args` and `callback_kwargs`. So the minimal callback function signature is:

```python
def my_callback(option, opt, value, parser):

```

The four arguments to a callback are described below.

There are several other option attributes you may supply when defining a callback option:

`type`

keeps its ordinary meaning: much like the `"store"` or `"append"` actions, it tells `optparse` to take in one argument and turn it into `type`. But instead of saving the converted value(s) anywhere, `optparse` passes them along to your callback function.

`nargs`

also keeps its ordinary meaning: provided and > 1, `optparse` will take in `nargs` arguments, every one of which must be convertible to `type`. It then hands a tuple of converted values to your callback.

`callback_args`

a tuple of extra positional arguments to pass to the callback

`callback_kwargs`

a dictionary of extra keyword arguments to pass to the callback

[Subject index](INDEX.md) · [Previous](option-callbacks.md) · [Continue](parser-largs-to-parser-values.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)
