# optparse — Populating the parser

### Populating the parser

The parser can be filled with options in a few different ways. The recommended approach uses `OptionParser.add_option()`, as demonstrated back in section Tutorial. There are two distinct ways to call `add_option()`:

- pass it an Option instance (as returned by `make_option()`)

- hand it whatever mix of positional and keyword arguments `make_option()` accepts (that is, the ones the Option constructor accepts), and it builds the Option instance on your behalf

Your other choice is to feed a list of already-built Option instances into the OptionParser constructor, like so:

```python
option_list = [
    make_option("-f", "--filename",
                action="store", type="string", dest="filename"),
    make_option("-q", "--quiet",
                action="store_false", dest="verbose"),
    ]
parser = OptionParser(option_list=option_list)

```

(`make_option()` works as a factory function that produces Option instances; for now it simply aliases the Option constructor. Down the road a later `optparse` release might break Option apart into several classes, and `make_option()` would then choose the correct class to instantiate. Never instantiate Option yourself directly.)

[Subject index](INDEX.md) · [Previous](optparse-optionparser-class.md) · [Continue](optionparser-add-option.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)
