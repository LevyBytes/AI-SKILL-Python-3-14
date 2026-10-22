# Calltips

### Calltips

A calltip appears on its own as soon as one types ( following the name of an *accessible* function. The function name expression can contain dots and subscripts. The calltip stays until clicked, until the cursor leaves the argument area, or until ) is typed. Whenever the cursor lies in a definition’s argument part, choose Edit and “Show Call Tip” from the menu or press its shortcut to bring up a calltip.

A calltip comprises the function’s signature plus its docstring, stopping at the docstring’s first blank line or its fifth non-blank line. (Certain builtin functions have no accessible signature.) Within the signature a ‘/’ or ‘*’ marks that the arguments before or after it are passed positionally or by name (keyword) only. These specifics may change.

Inside Shell, which functions are accessible hinges on which modules have been imported into the user process — including those Idle itself imports — and which definitions have run, all since the most recent restart.

As an example, restart the Shell and type `itertools.count(`. A calltip shows up because Idle imports itertools into the user process for its own purposes. (This may change.) Type `turtle.write(` and nothing shows. Idle does not import turtle on its own. The menu entry and shortcut likewise do nothing. Type `import turtle`. Afterward, `turtle.write(` will produce a calltip.

Within an editor, import statements do nothing until the file is run. You may wish to run a file after entering import statements, after introducing function definitions, or after opening a file that already exists.

[Subject index](INDEX.md) · [Previous](completions.md) · [Continue](format-block.md)
