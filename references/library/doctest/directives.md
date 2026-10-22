# doctest — Directives

### Directives

Doctest directives let you tweak the option flags for one specific example. A doctest directive is a special Python comment trailing an example's source code:

```text

directive:             "#" "doctest:" directive_options
directive_options:     directive_option ("," directive_option)*
directive_option:      on_or_off directive_option_name
on_or_off:             "+" | "-"
directive_option_name: "DONT_ACCEPT_BLANKLINE" | "NORMALIZE_WHITESPACE" | ...
```

No whitespace may sit between the `+` or `-` and the directive option name. That directive option name may be any of the option flag names covered above.

The doctest directives on an example alter doctest's behavior solely for that one example. Apply `+` to switch on the named behavior, or `-` to switch it off.

For example, this test passes:

```pycon
>>> print(list(range(20)))  # doctest: +NORMALIZE_WHITESPACE
[0,   1,  2,  3,  4,  5,  6,  7,  8,  9,
10,  11, 12, 13, 14, 15, 16, 17, 18, 19]

```

Lacking the directive, the example would not pass: the real output omits the pair of blanks ahead of each single-digit element, and the genuine output occupies just one line. The following test passes as well, and it too needs a directive to succeed:

```pycon
>>> print(list(range(20)))  # doctest: +ELLIPSIS
[0, 1, ..., 18, 19]

```

You can apply several directives within one physical line by separating each with a comma:

```pycon
>>> print(list(range(20)))  # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
[0,    1, ...,   18,    19]

```

When more than one directive comment attaches to the same example, doctest merges them together:

```pycon
>>> print(list(range(20)))  # doctest: +ELLIPSIS
...                         # doctest: +NORMALIZE_WHITESPACE
[0,    1, ...,   18,    19]

```

The example just above demonstrates that you may append `...` lines carrying nothing but directives. That trick helps when an example runs too long for a directive to sit neatly on the same line:

```pycon
>>> print(list(range(5)) + list(range(10, 20)) + list(range(30, 40)))
... # doctest: +ELLIPSIS
[0, ..., 4, 10, ..., 19, 30, ..., 39]

```

Keep in mind that every option starts off disabled, and a directive governs only the one example where it sits, so turning options on (with `+` inside a directive) is normally the sole choice worth making. That said, you can also hand option flags to the functions that execute doctests, which sets up alternative defaults. Under those conditions, switching an option off using `-` within a directive becomes worthwhile.

[Subject index](INDEX.md) · [Previous](doctest-reporting-flags-to-doctest-register-optionflag.md) · [Owning module, declaration or section: doctest](interactive-example-testing-overview.md) · [Continue](warnings.md)
