# getopt — `getopt` — C-style parser for command line options — Code example: import getopt, sys

```python
import getopt, sys

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    output = None
    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-o", "--output"):
            output = a
        else:
            assert False, "unhandled option"
    process(args, output=output, verbose=verbose)

if __name__ == "__main__":
    main()

```

Bear in mind that an equivalent command line interface could be built with less code plus more helpful help and error messages by reaching for the [`optparse`](https://docs.python.org/3.14/library/optparse.html#module-optparse) module:

```python
import optparse

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option('-o', '--output')
    parser.add_option('-v', dest='verbose', action='store_true')
    opts, args = parser.parse_args()
    process(args, output=opts.output, verbose=opts.verbose)

```

The [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) module can likewise yield a roughly equivalent command line interface for this scenario:

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

Consult [Choosing an argument parsing library](https://docs.python.org/3.14/library/optparse.html#choosing-an-argument-parser) to learn where the `argparse` rendition of this code behaves differently from its `optparse` (and `getopt`) counterpart.

See also

Module [`optparse`](https://docs.python.org/3.14/library/optparse.html#module-optparse)

Declarative command line option parsing.

Module [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse)

More opinionated command line option and argument parsing library.

[Subject index](INDEX.md) · [Previous](getopt-error.md) · [Continue](../getpass/getpass-getpass-to-getpass-getuser.md) · [Owning module, declaration or section: getopt](getopt-getopt-to-getopt-getopterror.md) · [Owning module, declaration or section: getopt.error](getopt-error.md)
