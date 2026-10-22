# optparse.Option.take_action custom action example

To illustrate, suppose we introduce an `"extend"` action. It resembles the built-in `"append"` action, except that rather than pulling one value off the command line and tacking it onto a list already in place, `"extend"` accepts several values packed into one comma-separated string and grows the existing list with all of them. In other words, given that `--names` is declared as an `"extend"` option whose type is `"string"`, this command line

```python
--names=foo,bar --names blah --names ding,dong

```

should yield the following list

```python
["foo", "bar", "blah", "ding", "dong"]

```

As before, we derive a subclass from Option:

```python
class MyOption(Option):

    ACTIONS = Option.ACTIONS + ("extend",)
    STORE_ACTIONS = Option.STORE_ACTIONS + ("extend",)
    TYPED_ACTIONS = Option.TYPED_ACTIONS + ("extend",)
    ALWAYS_TYPED_ACTIONS = Option.ALWAYS_TYPED_ACTIONS + ("extend",)

    def take_action(self, action, dest, opt, value, values, parser):
        if action == "extend":
            lvalue = value.split(",")
            values.ensure_value(dest, []).extend(lvalue)
        else:
            Option.take_action(
                self, action, dest, opt, value, values, parser)

```

Features of note:

- Since `"extend"` requires a value from the command line and also has to place that value somewhere, it belongs to `STORE_ACTIONS` as well as `TYPED_ACTIONS`.

- so that `optparse` hands the fallback type of `"string"` to any `"extend"` action, we also register the `"extend"` action under `ALWAYS_TYPED_ACTIONS`.

- `MyOption.take_action()` handles only this single added action and delegates everything else to `Option.take_action()`, which covers the usual `optparse` actions.

- `values` here is an object of the optparse_parser.Values class, and that class exposes the handy `ensure_value()` method. Think of `ensure_value()` as [`getattr()`](https://docs.python.org/3.14/library/functions.html#getattr) plus a fallback guard; you invoke it like so

```python
values.ensure_value(attr, value)

```

When the `attr` attribute on `values` is missing or holds `None`, ensure_value() assigns `value` to it and hands `value` back to you. That behavior is convenient for actions such as `"extend"`, `"append"`, and `"count"`, since each of them builds up data in a variable that has to hold a particular type (a list for the first pair, an integer for the third). Relying on `ensure_value()` frees scripts that use your action from having to pre-seed a default on the relevant option destinations; they can simply leave it as `None`, and `ensure_value()` will sort out the correct starting value at the moment it matters.

### Exceptions

 *exception *optparse.OptionError

Thrown when an `Option` object is built with arguments that are invalid or contradict one another.

 *exception *optparse.OptionConflictError

Thrown when options that clash with each other are registered on an `OptionParser`.

 *exception *optparse.OptionValueError

Thrown when a bad value for an option turns up on the command line.

 *exception *optparse.BadOptionError

Thrown when an unrecognized option appears on the command line.

 *exception *optparse.AmbiguousOptionError

Thrown when an option given on the command line is ambiguous.

[Subject index](INDEX.md) · [Owning API and preceding source contract](option-actions-to-option-always-typed-actions.md) · [Preceding source contract and version conditions](option-actions-to-option-always-typed-actions.md)
