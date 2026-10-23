# optparse - Putting it all together

### Putting it all together

Here's the shape that `optparse`-based scripts typically take:

```python
from optparse import OptionParser
...
def main():
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("-f", "--file", dest="filename",
                      help="read data from FILENAME")
    parser.add_option("-v", "--verbose",
                      action="store_true", dest="verbose")
    parser.add_option("-q", "--quiet",
                      action="store_false", dest="verbose")
    ...
    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.error("incorrect number of arguments")
    if options.verbose:
        print("reading %s..." % options.filename)
    ...

if __name__ == "__main__":
    main()

```

[Subject index](INDEX.md) · [Previous](how-optparse-handles-errors.md) · [Continue](optparse-optionparser-class.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)
