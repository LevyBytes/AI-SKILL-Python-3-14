# optparse - Generating help

### Generating help

The knack `optparse` has for generating help and usage text on its own comes in handy for building user-friendly command-line interfaces. All that's needed from you is a `help` value for each option, and optionally a short usage message covering your whole program. Below is an OptionParser stocked with user-friendly (documented) options:

```python
usage = "usage: %prog [options] arg1 arg2"
parser = OptionParser(usage=usage)
parser.add_option("-v", "--verbose",
                  action="store_true", dest="verbose", default=True,
                  help="make lots of noise [default]")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose",
                  help="be vewwy quiet (I'm hunting wabbits)")
parser.add_option("-f", "--filename",
                  metavar="FILE", help="write output to FILE")
parser.add_option("-m", "--mode",
                  default="intermediate",
                  help="interaction mode: novice, intermediate, "
                       "or expert [default: %default]")

```

When `optparse` meets either `-h` or `--help` on the command-line, or you simply call `parser.print_help()`, it prints the following to standard output:

```text
Usage: <yourscript> [options] arg1 arg2

Options:
  -h, --help            show this help message and exit
  -v, --verbose         make lots of noise [default]
  -q, --quiet           be vewwy quiet (I'm hunting wabbits)
  -f FILE, --filename=FILE
                        write output to FILE
  -m MODE, --mode=MODE  interaction mode: novice, intermediate, or
                        expert [default: intermediate]

```

(When the help output is set off by a help option, `optparse` exits once the help text has been printed.)

A great deal is happening here to help `optparse` build the best help message it can:

- the script defines its own usage message:

```python
usage = "usage: %prog [options] arg1 arg2"

```

`optparse` swaps `%prog` within the usage string for the running program's name, that is `os.path.basename(sys.argv[0])`. That expanded string then prints ahead of the detailed option help.

When you supply no usage string, `optparse` falls back on a bland but sensible default: `"Usage: %prog [options]"`, which works fine if your script takes no positional arguments.

-

each option supplies a help string while ignoring line-wrapping entirely—`optparse` handles the line wrapping and keeps the help output looking tidy.

- any option that accepts a value flags as much within its auto-generated help message—take the "mode" option, for instance:

```python
-m MODE, --mode=MODE

```

In this case, "MODE" serves as the meta-variable: it represents the argument the user is meant to provide to `-m`/`--mode`. Out of the box, `optparse` takes the destination variable name, uppercases it, and uses that as the meta-variable. Occasionally that isn't quite what you're after—for instance, the `--filename` option explicitly sets `metavar="FILE"`, yielding this automatically generated option description:

```python
-f FILE, --filename=FILE

```

This matters for reasons beyond conserving space, though: the hand-written help text leans on the meta-variable `FILE` to signal to the reader that the semi-formal syntax `-f FILE` and the plain-language description "write output to FILE" are linked. It's a small but effective trick to make your help text considerably clearer and more useful for the people using it.

- options carrying a default value may embed `%default` in the help string—`optparse` swaps it out for the [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) of the option's default value. When an option lacks a default value (or that default is `None`), `%default` expands to `none`.

[Subject index](INDEX.md) · [Previous](default-values.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md) · [Continue](grouping-options.md)
