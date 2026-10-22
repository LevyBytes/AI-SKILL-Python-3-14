# 2.3.4. Non-ASCII characters in names

### 2.3.4. Non-ASCII characters in names

Beyond the rules and grammar already laid out, names holding non-ASCII characters call for extra normalization and validation. To illustrate, `ř_1`, `蛇`, and `साँप` are valid names, while `r〰2`, `€`, and `🐍` are not.

The precise rules are spelled out in this section.

While parsing, every name is turned into the NFKC [normalization form](https://www.unicode.org/reports/tr15/#Norm_Forms). What this means, as one example, is that certain typographic variants of characters become their “basic” form. As an example, `ﬁⁿₐˡᵢᶻₐᵗᵢᵒₙ` normalizes to `finalization`, and so Python regards them as one and the same name:

```python
>>> ﬁⁿₐˡᵢᶻₐᵗᵢᵒₙ = 3
>>> finalization
3

```

Note

Only at the lexical level does normalization occur. Run-time functions that accept names as *strings* usually leave their arguments unnormalized. To illustrate, at run time the variable defined just above can be reached in the [`globals()`](https://docs.python.org/3.14/library/functions.html#globals) dictionary via `globals()["finalization"]`, though not via `globals()["ﬁⁿₐˡᵢᶻₐᵗᵢᵒₙ"]`.

In the same way that ASCII-only names may hold only letters, digits and the underscore and may not begin with a digit, a valid name must open with a character from the “letter-like” set `xid_start`, with every remaining character drawn from the “letter- and digit-like” set `xid_continue`.

The Unicode standard annex [UAX-31](https://www.unicode.org/reports/tr31/) defines the *XID_Start* and *XID_Continue* sets that these sets build on. Python additionally folds the underscore (`_`) into its `xid_start`. Keep in mind that Python does not necessarily conform to [UAX-31](https://www.unicode.org/reports/tr31/).

The [DerivedCoreProperties.txt](https://www.unicode.org/Public/16.0.0/ucd/DerivedCoreProperties.txt) file within the Unicode Character Database offers a non-normative listing of the characters in Unicode's *XID_Start* and *XID_Continue* sets. The rules for building the `xid_*` sets are set out below.

The set `id_start` is defined as the union of:

- Unicode category `<Lu>` - uppercase letters (includes `A` to `Z`)

- Unicode category `<Ll>` - lowercase letters (includes `a` to `z`)

- Unicode category `<Lt>` - titlecase letters

- Unicode category `<Lm>` - modifier letters

- Unicode category `<Lo>` - other letters

- Unicode category `<Nl>` - letter numbers

- {`"_"`} - the underscore

- `<Other_ID_Start>` - an explicit set of characters in [PropList.txt](https://www.unicode.org/Public/16.0.0/ucd/PropList.txt) to support backwards compatibility

The set `xid_start` then takes the closure of this set under NFKC normalization, stripping out every character whose normalization does not take the form `id_start id_continue*`.

The set `id_continue` is defined as the union of:

- `id_start` (see above)

- Unicode category `<Nd>` - decimal numbers (includes `0` to `9`)

- Unicode category `<Pc>` - connector punctuations

- Unicode category `<Mn>` - nonspacing marks

- Unicode category `<Mc>` - spacing combining marks

- `<Other_ID_Continue>` - another explicit set of characters in [PropList.txt](https://www.unicode.org/Public/16.0.0/ucd/PropList.txt) to support backwards compatibility

Once more, `xid_continue` takes the closure of this set under NFKC normalization.

The Unicode categories rely on the version of the Unicode Character Database bundled in the [`unicodedata`](https://docs.python.org/3.14/library/unicodedata.html#module-unicodedata) module.

See also

- [**PEP 3131**](https://peps.python.org/pep-3131/) – Supporting Non-ASCII Identifiers

- [**PEP 672**](https://peps.python.org/pep-0672/) – Unicode-related Security Considerations for Python

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Owning language section](names.md) · [Previous source section](reserved-classes-of-identifiers.md) · [Following source section](literals.md)
