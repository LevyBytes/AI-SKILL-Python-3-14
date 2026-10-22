# optparse — Choosing an argument parsing library — Section introduction and initial examples

### Choosing an argument parsing library

Three argument parsing libraries ship with the standard library:

- [`getopt`](https://docs.python.org/3.14/library/getopt.html#module-getopt): a module hewing closely to the procedural C `getopt` API. Part of the standard library since before Python 1.0 first shipped.

- `optparse`: a declarative stand-in for `getopt` delivering the same functionality while sparing each application from coding its own procedural option parsing logic. Part of the standard library since the Python 2.3 release.

- [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse): a more opinionated take next to `optparse`, providing more functionality out of the box at the cost of less application control over precisely how arguments get processed. Bundled into the standard library starting with the Python 2.7 and 3.2 releases.

When no more particular argument parsing design constraints apply, [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) is the suggested pick for building command line applications, since it delivers the most baseline functionality for the least application level code.

[`getopt`](https://docs.python.org/3.14/library/getopt.html#module-getopt) survives almost wholly for backwards compatibility purposes. That said, it also fills a niche role as a means of prototyping and testing command line argument handling in `getopt`-based C applications.

You should weigh `optparse` against [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) in these situations:

- an application already relies on `optparse` and prefers not to chance the subtle behavioural shifts that could surface when migrating to [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse)

- the application needs more control over how options and positional parameters are interleaved on the command line (up to and including switching the interleaving feature off altogether)

- the application wants tighter command over the incremental parsing of command line elements (although `argparse` does back this, its precise real-world behavior proves unwanted for certain use cases)

- the application needs more control over handling options that accept parameter values which may begin with `-` (for example delegated options bound for invoked subprocesses)

- the application needs some other command line parameter processing behavior that `argparse` lacks, but which is implementable on top of the lower level interface `optparse` exposes

For those same reasons, `optparse` tends to make a stronger foundation for library authors building third party command line argument processing libraries.

To make this concrete, look at the two command line argument parsing setups below, the first built on `optparse`, the second on `argparse`:

```python
import optparse

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option('-o', '--output')
    parser.add_option('-v', dest='verbose', action='store_true')
    opts, args = parser.parse_args()
    process(args, output=opts.output, verbose=opts.verbose)

```

```python
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output')
    parser.add_argument('-v', dest='verbose', action='store_true')
    parser.add_argument('rest', nargs='*')
    args = parser.parse_args()
    process(args.rest, output=args.output, verbose=args.verbose)

```

The clearest contrast is that, in the `optparse` version, the non-option arguments get handled separately by the application once option processing has finished. In the `argparse` version, positional arguments are declared and handled the same way the named options are.

Yet the `argparse` version also handles certain parameter combinations differently than the `optparse` version would. As one example (among other differences):

- handing in `-o -v` yields `output="-v"` and `verbose=False` under `optparse`, but a usage error under `argparse` (grumbling that no value was given for `-o/--output`, because `-v` reads as the verbosity flag)

- likewise, handing in `-o --` yields `output="--"` and `args=()` under `optparse`, but a usage error under `argparse` (again grumbling that no value was given for `-o/--output`, because `--` reads as ending option processing and treating every remaining value as a positional argument)

[Subject index](INDEX.md) · [Previous](optparse-parser-for-command-line-options.md) · [Continue](argparse-option-value-differences.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)
