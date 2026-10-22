# optparse — The store action

### The store action

The most frequent option action is `store`, which tells `optparse` to grab the next argument (or the rest of the current argument), confirm it is of the right type, and store it to the destination you picked.

For example:

```python
parser.add_option("-f", "--file",
                  action="store", type="string", dest="filename")

```

Now let's invent a fake command line and have `optparse` parse it:

```python
args = ["-f", "foo.txt"]
(options, args) = parser.parse_args(args)

```

Once `optparse` spots the option string `-f`, it grabs the next argument, `foo.txt`, and stores it in `options.filename`. So once this `parse_args()` call finishes, `options.filename` holds `"foo.txt"`.

A couple of other option types `optparse` supports are `int` and `float`. Here's an option expecting an integer argument:

```python
parser.add_option("-n", type="int", dest="num")

```

Observe that this option has no long option string, which is perfectly fine. There's also no explicit action, since the default is `store`.

Let's parse another fake command-line. This time, we'll cram the option argument right against the option: because `-n42` (one argument) is the same as `-n 42` (two arguments), the code

```python
(options, args) = parser.parse_args(["-n42"])
print(options.num)

```

will print `42`.

When you don't specify a type, `optparse` assumes `string`. Together with the fact that the default action is `store`, this means our first example can be a good deal shorter:

```python
parser.add_option("-f", "--file", dest="filename")

```

When you don't provide a destination, `optparse` derives a reasonable one out of the option strings: should the first long option string be `--foo-bar`, the default destination becomes `foo_bar`. Lacking any long option strings, `optparse` consults the first short option string: for `-f` the default destination is `f`.

`optparse` also bundles in the built-in `complex` type. Adding types is taken up in section Extending optparse.

[Subject index](INDEX.md) · [Previous](understanding-option-actions.md) · [Continue](handling-boolean-flag-options.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)
