# More metacharacters

### More metacharacters

A handful of metacharacters remain untouched so far. The bulk of them are addressed in this section.

A number of the metacharacters still to be discussed are *zero-width assertions*. Rather than moving the engine forward through the string, they consume nothing at all and merely either succeed or fail. As an example, `\b` asserts that the present position sits at a word boundary; the position is left unchanged by the `\b`. Consequently, zero-width assertions must never be repeated, since a single match at some spot means they could obviously be matched without limit.

`|`

Alternation, otherwise known as the “or” operator. Where *A* and *B* are regular expressions, `A|B` matches whatever string matches either *A* or *B*. The precedence of `|` is deliberately very low so that it behaves sensibly while you alternate strings of several characters. `Crow|Servo` matches either `'Crow'` or `'Servo'`, and not `'Cro'`, then a `'w'` or an `'S'`, then `'ervo'`.

For a literal `'|'`, reach for `\|`, or tuck it inside a character class, like `[|]`.

`^`

Matches where lines begin. Absent the [`MULTILINE`](https://docs.python.org/3.14/library/re.html#re.MULTILINE) flag, it matches only where the string begins. Under `MULTILINE` mode, it additionally matches right after each newline inside the string.

For instance, should you want to match the word `From` exclusively at a line's start, the RE you'd use is `^From`.

```python
>>> print(re.search('^From', 'From Here to Eternity'))
<re.Match object; span=(0, 4), match='From'>
>>> print(re.search('^From', 'Reciting From Memory'))
None

```

To match a literal `'^'`, use `\^`.

`$`

Matches where a line ends, defined as either the string's end or any spot that a newline character follows.

```python
>>> print(re.search('}$', '{block}'))
<re.Match object; span=(6, 7), match='}'>
>>> print(re.search('}$', '{block} '))
None
>>> print(re.search('}$', '{block}\n'))
<re.Match object; span=(6, 7), match='}'>

```

For a literal `'$'`, reach for `\$` or wrap it within a character class, like `[$]`.

`\A`

Matches only where the string begins. Outside of [`MULTILINE`](https://docs.python.org/3.14/library/re.html#re.MULTILINE) mode, `\A` and `^` amount to the same thing. Within `MULTILINE` mode they diverge: `\A` keeps matching only at the string's start, whereas `^` can match at any spot within the string that comes after a newline character.

`\z`

Matches only at the end of the string.

`\Z`

The same as `\z`. For compatibility with old Python versions.

`\b`

Word boundary. This zero-width assertion matches only where a word begins or ends. Since a word is taken to be a run of alphanumeric characters, a word's end is signalled by whitespace or by some non-alphanumeric character.

In the example below, `class` matches only as a standalone word; it fails to match when it is buried inside a larger word.

```python
>>> p = re.compile(r'\bclass\b')
>>> print(p.search('no class at all'))
<re.Match object; span=(3, 8), match='class'>
>>> print(p.search('the declassified algorithm'))
None
>>> print(p.search('one subclass is'))
None

```

Two fine points are worth bearing in mind whenever you reach for this special sequence. To begin with, this represents the nastiest clash between Python's string literals and the sequences of regular expressions. Within Python's string literals, `\b` stands for the backspace character, whose ASCII value is 8. Unless you employ raw strings, Python turns the `\b` into a backspace, and then your RE fails to match the way you intended. The next example seems identical to our earlier RE, save that it drops the `'r'` ahead of the RE string.

```python
>>> p = re.compile('\bclass\b')
>>> print(p.search('no class at all'))
None
>>> print(p.search('\b' + 'class' + '\b'))
<re.Match object; span=(0, 7), match='\x08class\x08'>

```

Next, within a character class, where this assertion serves no purpose, `\b` denotes the backspace character, to stay compatible with Python's string literals.

`\B`

A further zero-width assertion, the reverse of `\b`, this one matches solely when the present position is not sitting at a word boundary.

[Subject index](INDEX.md) · [Previous source context](more-pattern-power.md) · [Following source context](grouping.md)
