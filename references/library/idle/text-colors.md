# Text colors

### Text colors

Idle starts out with black text on white, yet colors text that has special meaning. In the shell, those are shell output, shell error, user output, and user error. In Python code, whether at the shell prompt or in an editor, those are keywords, builtin class and function names, names that follow `class` and `def`, strings, and comments. In any text window, those are the cursor (where present), found text (where possible), and selected text.

IDLE additionally highlights the [soft keywords](https://docs.python.org/3.14/reference/lexical_analysis.html#soft-keywords) [`match`](https://docs.python.org/3.14/reference/compound_stmts.html#match), `case`, and [`_`](https://docs.python.org/3.14/reference/compound_stmts.html#wildcard-patterns) in pattern-matching statements. That highlighting, however, is imperfect and will be wrong in some uncommon cases, among them certain `_`-s appearing in `case` patterns.

Because text coloring runs in the background, uncolorized text shows briefly now and then. Use the Configure IDLE dialog Highlighting tab to switch color schemes. The marking of debugger breakpoint lines in the editor, and of text in popups and dialogs, cannot be configured by the user.

[Subject index](INDEX.md) · [Previous](shell-window.md) · [Continue](startup-and-code-execution.md)
