# optparse - Terminology

### Terminology

argument

a string typed at the command-line and handed by the shell to `execl()` or `execv()`. In Python, arguments are members of `sys.argv[1:]` (`sys.argv[0]` is the name of the program currently running). Unix shells additionally call this a "word".

Now and then it's handy to swap in an argument list other than `sys.argv[1:]`, so read "argument" as "a member of `sys.argv[1:]`, or of some other list standing in for `sys.argv[1:]`".

option

an argument supplying extra information that guides or customizes how a program runs. Options come in many syntaxes; the traditional Unix syntax is a hyphen ("-") trailed by a single letter, for example `-x` or `-F`. Traditional Unix syntax also lets several options merge into one argument, so `-x -F` is the same as `-xF`. The GNU project brought in `--` trailed by a run of hyphen-separated words, for example `--file` or `--dry-run`. Those two are the only option syntaxes `optparse` offers.

A few other option syntaxes the world has witnessed include:

- a hyphen trailed by a handful of letters, e.g. `-pf` (this is *not* the same thing as several options merged into one argument)

- a hyphen trailed by an entire word, e.g. `-file` (strictly this matches the previous syntax, though you don't usually find both in one program)

- a plus sign trailed by a single letter, a handful of letters, or a word, e.g. `+f`, `+rgb`

- a slash trailed by a letter, a handful of letters, or a word, e.g. `/f`, `/file`

`optparse` does not support these option syntaxes, and it never will. That's on purpose: the first three are non-standard in any environment, and the last only makes sense if you're targeting Windows exclusively or certain legacy platforms (such as VMS, MS-DOS).

option argument

an argument that comes after an option, is tightly bound to that option, and is taken out of the argument list along with that option. Under `optparse`, option arguments may sit in a separate argument from their option:

```text
-f foo
--file foo

```

or ride within the same argument:

```text
-ffoo
--file=foo

```

As a rule, a given option either takes an argument or it doesn't. Plenty of people want an "optional option arguments" feature, meaning some options would take an argument when they spot one and skip it otherwise. This is rather contentious, since it makes parsing ambiguous: if `-a` takes an optional argument and `-b` is a wholly separate option, how should we read `-ab`? Owing to this ambiguity, `optparse` does not support the feature.

positional argument

whatever is left in the argument list after options have been parsed, that is, once options and their arguments have been parsed out of the argument list and removed.

required option

an option that has to appear on the command-line; mind you, the phrase "required option" contradicts itself in English. `optparse` won't stop you from building required options, but it won't lend you much of a hand either.

For instance, take this hypothetical command-line:

```python
prog -v --report report.txt foo bar

```

`-v` and `--report` are both options. Taking it that `--report` takes one argument, `report.txt` is an option argument. `foo` and `bar` are positional arguments.

[Subject index](INDEX.md) · [Previous](background.md) · [Continue](what-are-options-for.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)
