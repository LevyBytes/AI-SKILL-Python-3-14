# Completions

### Completions

When asked for and available, completions are offered for module names, attributes of classes or functions, or filenames. Every request method shows a completion box listing existing names. (One exception is tab completions, below.) In any box, adjust both the name under completion and the box’s highlighted item three ways: by typing and erasing characters; via the Up, Down, PageUp, PageDown, Home, and End keys; and through one click within the box. Dismiss the box using Escape, Enter, double Tab keys, or clicks beyond the box. A double click inside the box picks an item and closes.

A box can be opened by typing a key character and pausing for a preset interval. The default for this is 2 seconds; tune it in the settings dialog. (To suppress auto popups, raise the delay to a huge millisecond count, for example 100000000.) For attributes of imported modules or of a class or function, type ‘.’. For filenames within the root directory, type [`os.sep`](https://docs.python.org/3.14/library/os.html#os.sep) or [`os.altsep`](https://docs.python.org/3.14/library/os.html#os.altsep) right after an opening quote. (Under Windows you may name a drive first.) Descend into subdirectories by typing a directory name followed by a separator.

Rather than waiting, or once a box has closed, open a completion box at once via Show Completions on the Edit menu. C-space is the default hot key. Typing a prefix for the wanted name before opening the box makes the first match or close miss visible. The outcome matches entering a prefix once the box is shown. Following a quote, Show Completions completes filenames in the current directory rather than a root directory.

Pressing Tab after a prefix generally produces the same result as Show Completions. (Lacking a prefix, it indents.) Yet when only a single match exists for the prefix, that match is inserted straight into the editor text without any box appearing.

Calling ‘Show Completions’, or pressing Tab after a prefix, outside a string and lacking a preceding ‘.’ opens a box holding keywords, builtin names, and the available module-level names.

While editing code in an editor (rather than Shell), grow the available module-level names by running your code and then not restarting the Shell. This proves particularly handy once imports have been added at a file’s top. It also grows the possible attribute completions.

By default completion boxes leave out names that start with ‘_’ or, for modules, that ‘__all__’ omits. Reach those hidden names by typing ‘_’ after ‘.’, whether before or after the box opens.

[Subject index](INDEX.md) · [Previous](search-and-replace.md) · [Continue](calltips.md)
