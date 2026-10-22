# tkinter — Setting Options

### Handy Reference

### Setting Options

Options govern things such as a widget’s color and border width. There are three ways to set options:

At object creation time, using keyword arguments

```python
fred = Button(self, fg="red", bg="blue")

```

After object creation, treating the option name like a dictionary index

```python
fred["fg"] = "red"
fred["bg"] = "blue"

```

Use the config() method to update multiple attrs subsequent to object creation

```python
fred.config(fg="red", bg="blue")

```

For a full account of any particular option and how it behaves, consult the Tk man pages for the widget at hand.

Keep in mind that the man pages set out “STANDARD OPTIONS” and “WIDGET SPECIFIC OPTIONS” for every widget. The first is a list of options shared across many widgets; the second covers the options peculiar to that one widget. The Standard Options are documented on the *[options(3)](https://manpages.debian.org/options(3))* man page.

This document draws no line between standard and widget-specific options. Certain options simply don’t apply to certain kinds of widgets. Whether a particular widget honors a given option hinges on the widget’s class; buttons carry a `command` option, while labels do not.

Whatever options a particular widget accepts are written up in that widget’s man page; you can also discover them at runtime by invoking its `config()` method with no arguments, or by invoking its `keys()` method. What comes back from those calls is a dictionary keyed on each option’s name rendered as a string (say, `'relief'`), with 5-tuples for the values.

A few options — `bg` among them — are just synonyms for the commonly used long-name options (`bg` stands in for “background”). Hand `config()` a shorthand option name and you get back a 2-tuple instead of a 5-tuple. That 2-tuple holds the synonym’s name alongside the “real” option (for example, `('bg', 'background')`).

| Index | Meaning | Example |
| --- | --- | --- |
| 0 | the option’s name | `'relief'` |
| 1 | the option name used for database lookup | `'relief'` |
| 2 | the option class used for database lookup | `'Relief'` |
| 3 | the default | `'raised'` |
| 4 | the value in effect now | `'groove'` |

Example:

```python
>>> print(fred.config())
{'relief': ('relief', 'relief', 'Relief', 'raised', 'groove')}

```

Naturally, the printed dictionary lists every option on offer together with its value. The above is here purely for illustration.

[Subject index](INDEX.md) · [Owning module, declaration or section: tkinter](tkinter-python-interface-to-tcl-tk.md) · [Continue](the-packer.md)
