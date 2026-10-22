# What's New In Python 3.4 / textwrap — textwrap

### textwrap

The [`TextWrapper`](https://docs.python.org/3.14/library/textwrap.html#textwrap.TextWrapper) class gained two new attributes that double as constructor arguments: [`max_lines`](https://docs.python.org/3.14/library/textwrap.html#textwrap.TextWrapper.max_lines), capping how many lines land in the output, and [`placeholder`](https://docs.python.org/3.14/library/textwrap.html#textwrap.TextWrapper.placeholder), a string that shows up at the tail of the output whenever it has been cut short on account of *max_lines*. Leveraging those features, a new convenience function [`shorten()`](https://docs.python.org/3.14/library/textwrap.html#textwrap.shorten) squashes every run of whitespace in the input down to single spaces and emits one line of a chosen *width* terminating with the *placeholder* (which defaults to `[...]`). (Contributed by Antoine Pitrou and Serhiy Storchaka in [bpo-18585](https://bugs.python.org/issue?@action=redirect&bpo=18585) and [bpo-18725](https://bugs.python.org/issue?@action=redirect&bpo=18725).)

[Subject index](INDEX.md) · [Previous source section](tarfile.md) · [Next source section](threading.md) · [Release/subject declaration](release-highlights.md)
