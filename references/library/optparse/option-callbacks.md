# optparse — Option Callbacks

### Option Callbacks

When the built-in actions and types of `optparse` fall short of what you need, you have two paths: extend `optparse` or set up a callback option. Extending `optparse` is the more general route, but it's overkill for plenty of simple situations. Frequently a simple callback covers everything.

Defining a callback option takes two steps:

- define the option itself using the `"callback"` action

- write the callback; it is a function (or method) accepting no fewer than four arguments, described below

[Subject index](INDEX.md) · [Previous](optionparser-set-usage-to-optionparser-set-defaults.md) · [Continue](defining-a-callback-option.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)
