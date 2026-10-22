# optparse — Cleanup

### Cleanup

Every OptionParser instance carries several cyclic references. Python's garbage collector should handle these without trouble, but you might choose to sever the cyclic references yourself by calling `destroy()` on your OptionParser once you've finished with it. This pays off especially in long-running applications where big object graphs can be reached from your OptionParser.

[Subject index](INDEX.md) · [Previous](conflicts-between-options.md) · [Continue](optionparser-set-usage-to-optionparser-set-defaults.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)
