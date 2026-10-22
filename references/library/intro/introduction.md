# Introduction

## Introduction

### Introduction

Several distinct categories of component make up the “Python library.”

Among them are data types most people would treat as belonging to a language's “core,” numbers and lists being examples. With such types, literal syntax is laid down by the Python language core, which also imposes a handful of limits on their semantics without pinning those semantics down completely. (Conversely, syntactic matters — for instance how operators are spelled and ranked by priority — are indeed settled by the language core.)

Built-in functions and exceptions also live in the library — objects every piece of Python code may reach without first issuing an [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) statement. A portion are fixed by the core language itself, yet plenty are non-essential to core semantics and get their only documentation right here.

What forms the bulk of the library, though, is an assortment of modules, and that assortment can be sliced up in numerous ways. Certain modules are coded in C and compiled directly into the Python interpreter; others are coded in Python and pulled in from source. A few expose interfaces tied tightly to Python — emitting a stack trace, say — while a few expose interfaces bound to specific operating systems, such as reaching particular hardware, and still others expose interfaces tailored to one application area, the World Wide Web being one example. You can find some modules in every release and port of Python; certain others appear only where the host system supports or demands them; and a further group surfaces only when one particular configuration option was selected as Python was being compiled and set up.

The arrangement of this manual runs “from the inside out:” the built-in functions, data types and exceptions come first, with the modules — sorted into chapters of kindred modules — coming last.

Consequently, reading this manual straight through from the opening, and jumping to the following chapter the moment boredom sets in, will leave you with a fair sense of the modules on offer and the application areas the Python library covers. Naturally, you aren't *required* to read it the way you'd read a novel — flipping through the table of contents (placed up front), or hunting for a particular function, module or term in the index (placed at the back), works just as well. And lastly, for anyone who likes stumbling onto unexpected topics, pick a page number at random (consult the [`random`](https://docs.python.org/3.14/library/random.html#module-random) module) and dip into a section or two. Whatever order you choose for the sections here, beginning with the [Built-in Functions](https://docs.python.org/3.14/library/functions.html#built-in-funcs) chapter pays off, since everything after it presumes you already know that material.

Let the show begin!

[Subject index](INDEX.md) · [Continue](notes-on-availability.md)
