# optparse — What are positional arguments for?

### What are positional arguments for?

Positional arguments cover the pieces of information that your program absolutely, positively must have to run.

A good user interface ought to carry as few absolute requirements as it can. If your program demands 17 separate pieces of information before it can run successfully, it scarcely matters *how* you pull that information out of the user—most people will give up and walk away before they ever get the program running. The same applies no matter if the user interface happens to be a command-line, a configuration file, or a GUI: pile that many demands on your users and most of them will simply quit.

In short, work to keep the amount of information users absolutely have to give to a minimum—reach for sensible defaults wherever you can. Of course, you also want your programs to stay reasonably flexible. That's the purpose of options. Again, it makes no difference whether they're entries in a config file, widgets in a GUI's "Preferences" dialog, or command-line options—the more options you build in, the more flexible your program grows, and the more complicated its implementation becomes. Too much flexibility brings drawbacks of its own, naturally; too many options can swamp users and make your code far harder to maintain.

[Subject index](INDEX.md) · [Previous](what-are-options-for.md) · [Continue](tutorial.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)
