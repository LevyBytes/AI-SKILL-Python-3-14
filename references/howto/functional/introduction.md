# Introduction

### Introduction

Here we cover the foundational idea behind functional programming; readers who only care about Python's language constructs can jump ahead to the following section about Iterators.

There are several distinct strategies that programming languages offer for breaking problems down:

- The bulk of programming languages are **procedural**: a program is a sequence of statements directing the machine on what to do with its input. Procedural languages include C, Pascal, and Unix shells as well.

- With **declarative** languages, you author a specification stating the problem that needs solving, and it falls to the language implementation to determine an efficient way to carry out the computation. The declarative language you've probably encountered is SQL; a SQL query states which data set you wish to fetch, and it's the SQL engine that decides among scanning tables or using indexes, the ordering of subclauses, and so on.

- **Object-oriented** programs operate on collections of objects. Each object carries internal state plus methods that inspect or alter that state somehow. Smalltalk and Java are object-oriented languages. Both C++ and Python permit object-oriented programming, yet neither compels you to rely on object-oriented features.

- **Functional** programming splits a problem up into a collection of functions. In the ideal case, functions accept only inputs and yield outputs, carrying no internal state that would alter the output for a particular input. Among the recognized functional languages are the ML family (Standard ML, OCaml, and other variants) plus Haskell.

Certain language designers deliberately spotlight one specific style of programming. As a consequence, writing programs that follow a different style can become awkward. Other languages are multi-paradigm, accommodating several styles at once. Lisp, C++, and Python all qualify as multi-paradigm; within any of these you can author programs or libraries that are predominantly procedural, object-oriented, or functional. Within a sizable program, separate portions might each adopt a distinct style; perhaps the GUI is object-oriented while the processing logic stays procedural or functional, to give one example.

In a functional program, the input passes through a series of functions. Every function acts on what it receives and yields some result. The functional style steers you away from functions whose side effects alter internal state or introduce other changes not reflected in the function's return value. A function with zero side effects whatsoever is termed **purely functional**. Steering clear of side effects entails not relying on data structures that mutate while the program executes; the result of every function has to hinge solely on what was passed to it.

A handful of languages enforce purity rigidly and lack even assignment statements like `a=3` or `c = a + b`, but sidestepping every side effect proves hard, since things like printing to the screen or writing a disk file count too. Yet another instance is invoking the [`print()`](https://docs.python.org/3.14/library/functions.html#print) or [`time.sleep()`](https://docs.python.org/3.14/library/time.html#time.sleep) function, where neither hands back any useful value. Each is invoked purely for its side effect of emitting some text to the screen or halting execution briefly for a second.

Functional-style Python programs typically stop short of the extreme of shunning all I/O or every assignment; rather, they expose an interface that looks functional while leaning on non-functional mechanisms behind the scenes. As an illustration, a function's implementation may still assign to local variables, yet it refrains from altering global variables or causing other side effects.

You can regard functional programming as the inverse of object-oriented programming. Objects are small capsules holding some internal state together with a set of method calls allowing you to change that state, and a program amounts to applying the correct sequence of state changes. Functional programming aims to sidestep state changes whenever it can and instead deals with data passing among functions. Within Python you could blend both styles by authoring functions that accept and hand back instances standing for objects from your application (e-mail messages, transactions, and so on).

A functional design might appear to be a strange limitation to operate within. What's the reason to steer clear of objects and side effects? The functional approach brings both theoretical and practical upsides:

- Formal provability.

- Modularity.

- Composability.

- Ease of debugging and testing.

[Subject index](INDEX.md) · [Previous source context](functional-programming-howto.md) · [Following source context](formal-provability.md)
