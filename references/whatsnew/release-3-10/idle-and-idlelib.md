# What's New In Python 3.10 / IDLE and idlelib - sys

### IDLE and idlelib

Get IDLE to call [`sys.excepthook()`](https://docs.python.org/3.14/library/sys.html#sys.excepthook) (assuming it launched without ‘-n’). Hooks set by the user used to be skipped. (Contributed by Ken Hilton in [bpo-43008](https://bugs.python.org/issue?@action=redirect&bpo=43008).)

Reorganize the settings dialog. Carve the General tab apart into Windows and Shell/Ed tabs. Relocate help sources, the things that extend the Help menu, over to the Extensions tab. Free up room for additional options and trim the dialog down. Shrinking it lets the dialog sit better on small screens. (Contributed by Terry Jan Reedy in [bpo-40468](https://bugs.python.org/issue?@action=redirect&bpo=40468).) Shift the indent space setting away from the Font tab and onto the new Windows tab. (Mark Roseman with Terry Jan Reedy contributed this in [bpo-33962](https://bugs.python.org/issue?@action=redirect&bpo=33962).)

A 3.9 maintenance release received a backport of the changes listed above.

Add a Shell sidebar. Relocate the primary prompt (‘>>>’) over to the sidebar. Tack secondary prompts (’…’) onto the sidebar as well. A left click, optionally dragged, picks out one or more lines of text, just like the line number sidebar in the editor. A right click after some text lines are selected pops up a context menu offering ‘copy with prompts’. That command stitches the sidebar prompts together with lines drawn from the selected text. The same option turns up on the text’s context menu too. (Contributed by Tal Einat in [bpo-37903](https://bugs.python.org/issue?@action=redirect&bpo=37903).)

Indent interactive code with spaces in place of tabs. That way interactive code entries ‘look right’. Pulling this off was a big reason the shell sidebar was added. (Contributed by Terry Jan Reedy in [bpo-37892](https://bugs.python.org/issue?@action=redirect&bpo=37892).)

Highlight the new [soft keywords](https://docs.python.org/3.14/reference/lexical_analysis.html#soft-keywords) [`match`](https://docs.python.org/3.14/reference/compound_stmts.html#match), `case`, and [`_`](https://docs.python.org/3.14/reference/compound_stmts.html#wildcard-patterns) inside pattern-matching statements. That said, the highlighting isn't flawless and will go wrong in a few uncommon situations, among them certain `_`-s appearing in `case` patterns. (Contributed by Tal Einat in [bpo-44010](https://bugs.python.org/issue?@action=redirect&bpo=44010).)

New in 3.10 maintenance releases.

Give `.pyi` files syntax highlighting. (Alex Waygood with Terry Jan Reedy contributed this in [bpo-45447](https://bugs.python.org/issue?@action=redirect&bpo=45447).)

Include prompts while saving the Shell along with its inputs and outputs. (Contributed by Terry Jan Reedy in [gh-95191](https://github.com/python/cpython/issues/95191).)

### importlib.metadata

[Subject index](INDEX.md) · [Previous source section](hmac.md) · [Release/subject declaration](summary-release-highlights.md) · [Following release/subject continuation](importlib-metadata.md)
