# optparse — What are options for?

### What are options for?

Options exist to supply extra information that tunes or customizes how a program runs. In case it wasn't obvious, options are normally *optional*. A program ought to run just fine with no options at all. (Grab a random program from the Unix or GNU toolsets. Can it run with no options whatsoever and still make sense? The chief exceptions are `find`, `tar`, and `dd`—every one of them a mutant oddball that has been justly criticized for its non-standard syntax and baffling interface.)

Plenty of people wish their programs had "required options". Think it through. If something is required, then it's *not optional*! When there's a piece of information your program absolutely must have to run successfully, that's exactly what positional arguments are for.

For a model of solid command-line interface design, consider the humble `cp` utility, used to copy files. Trying to copy files without naming a destination and at least one source makes little sense. So `cp` fails when you run it with no arguments. Even so, it has a flexible, useful syntax requiring no options whatsoever:

```python
cp SOURCE DEST
cp SOURCE ... DEST-DIR

```

That alone gets you quite far. Most `cp` implementations offer a pile of options to fine-tune precisely how files are copied: you can preserve mode and modification time, decline to follow symlinks, prompt before clobbering existing files, and so on. Yet none of that detracts from the core mission of `cp`, which is to copy one file to another or several files to a directory.

[Subject index](INDEX.md) · [Previous](terminology.md) · [Continue](what-are-positional-arguments-for.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)
