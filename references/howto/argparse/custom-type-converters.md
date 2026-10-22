# Custom type converters

### Custom type converters

With the [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) module you can define your own type converters for command-line arguments. That gives you a chance to reshape what the user typed before it lands in the [`argparse.Namespace`](https://docs.python.org/3.14/library/argparse.html#argparse.Namespace). It comes in handy whenever the input needs some preprocessing ahead of being consumed by your program.

A custom type converter can be any callable that accepts one string argument (the value of the argument) and hands back the converted result. For trickier situations, though, you might instead supply a custom action class through the **action** parameter.

Suppose, for instance, you want to accept arguments carrying different prefixes and treat each accordingly:

```python
import argparse

parser = argparse.ArgumentParser(prefix_chars='-+')

parser.add_argument('-a', metavar='<value>', action='append',
                    type=lambda x: ('-', x))
parser.add_argument('+a', metavar='<value>', action='append',
                    type=lambda x: ('+', x))

args = parser.parse_args()
print(args)

```

Output:

```shell
$ python prog.py -a value1 +a value2
Namespace(a=[('-', 'value1'), ('+', 'value2')])

```

In this example, we:

- Built a parser whose prefix characters were customized by way of the `prefix_chars` parameter.

- Declared a pair of arguments, `-a` and `+a`, each relying on the `type` parameter to build a custom converter that tucks the value into a tuple alongside its prefix.

Had we left out those custom converters, `-a` and `+a` would have collapsed into one and the same argument — an outcome we didn't want. Thanks to the converters, we could keep the two arguments distinct.

[Subject index](INDEX.md) · [Previous source context](how-to-translate-the-argparse-output-continuation.md) · [Following source context](conclusion.md)
