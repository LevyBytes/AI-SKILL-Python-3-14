# optparse — Understanding option actions

### Understanding option actions

Actions tell `optparse` what to do once it meets an option on the command line. `optparse` has a fixed set of actions hard-coded in; adding new actions is an advanced topic taken up in section Extending optparse. Most actions tell `optparse` to store a value into some variable—for instance, pull a string off the command line and store it in an attribute of `options`.

When you specify no option action, `optparse` defaults to `store`.

[Subject index](INDEX.md) · [Previous](tutorial.md) · [Continue](the-store-action.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)
