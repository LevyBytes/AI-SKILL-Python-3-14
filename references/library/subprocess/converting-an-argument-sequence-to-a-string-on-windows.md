# subprocess - Converting an argument sequence to a string on Windows

### Converting an argument sequence to a string on Windows

Under Windows, an *args* sequence gets turned into a string parseable by the rules set out below, which mirror those the MS C runtime applies:

1.

White space — a space or a tab — is what separates one argument from the next.

2.

Text wrapped in double quotation marks counts as one argument, no matter what white space sits inside it. Such a quoted string may also be planted in the middle of an argument.

3.

When a backslash sits just ahead of a double quotation mark, that mark is taken as a literal double quotation mark.

4.

Each backslash is read literally, except where it comes right before a double quotation mark.

5.

Where backslashes fall right before a double quotation mark, each pair of them stands for one literal backslash. Should the backslash count be odd, the final backslash escapes the double quotation mark that follows, exactly as rule 3 lays out.

See also

[`shlex`](https://docs.python.org/3.14/library/shlex.html#module-shlex)

A module supplying a function that parses and escapes command lines.

[Subject index](INDEX.md) · [Previous](timeout-behavior.md) · [Continue](disable-use-of-posix-spawn.md) · [Owning module, declaration or section: subprocess](subprocess-subprocess-management.md)
