# difflib / Helpers for computing deltas: `difflib.HtmlDiff`, `__init__()`, `make_file()`, `make_table()`

*class *difflib.HtmlDiff

You can use this class to build an HTML table (or an entire HTML file wrapping that table) that lays out a side by side, line by line comparison of text with both inter-line and intra-line changes highlighted. You may render the table in either full or contextual difference mode.

This class is constructed by:

 __init__(*tabsize=8*, *wrapcolumn=None*, *linejunk=None*, *charjunk=IS_CHARACTER_JUNK*)

Initializes instance of `HtmlDiff`.

*tabsize* is an optional keyword argument that sets tab stop spacing; its default is `8`.

*wrapcolumn* is an optional keyword that names the column at which lines are broken and wrapped; its default of `None` leaves lines unwrapped.

*linejunk* and *charjunk* are optional keyword arguments forwarded into `ndiff()` (which `HtmlDiff` calls to produce the side by side HTML differences). Consult the `ndiff()` documentation for the default values and descriptions of these arguments.

These methods are public:

 make_file(*fromlines*, *tolines*, *fromdesc=''*, *todesc=''*, *context=False*, *numlines=5*, ***, *charset='utf-8'*)

Contrasts *fromlines* and *tolines* (lists of strings) and gives back a string holding a full HTML file whose table presents line by line differences with inter-line and intra-line changes highlighted.

*fromdesc* and *todesc* are optional keyword arguments that supply the from/to file column header strings (each defaults to an empty string).

*context* and *numlines* are each optional keyword arguments. Pass `True` for *context* whenever contextual differences should appear; otherwise the default `False` displays the full files. The default for *numlines* is `5`. With *context* set to `True`, *numlines* governs how many context lines bracket the difference highlights. With *context* set to `False`, *numlines* governs how many lines precede a difference highlight when the "next" hyperlinks are used (a value of zero makes the "next" hyperlinks drop the next difference highlight at the top of the browser with no leading context).

Note

*fromdesc* and *todesc* are read as unescaped HTML and ought to be escaped correctly when their input arrives from untrusted sources.

Changed in version 3.5: the keyword-only *charset* argument arrived. An HTML document's default charset shifted from `'ISO-8859-1'` over to `'utf-8'`.

 make_table(*fromlines*, *tolines*, *fromdesc=''*, *todesc=''*, *context=False*, *numlines=5*)

Contrasts *fromlines* and *tolines* (lists of strings) and gives back a string holding a full HTML table that presents line by line differences with inter-line and intra-line changes highlighted.

This method takes the same arguments as the `make_file()` method.

[Subject index](INDEX.md) · [Previous](difflib-differ-class.md) · [Continue](difflib-context-diff-to-difflib-get-close-matches.md) · [Owning module, declaration or section: difflib](difflib-sequencematcher-class.md)
