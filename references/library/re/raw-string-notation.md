# re — Raw String Notation

### Raw String Notation

Raw string notation (`r"text"`) is what keeps regular expressions manageable. Lacking it, you would have to double up every backslash (`'\'`) in a regular expression to escape it. As a case in point, the next two lines of code behave the same:

```python
>>> re.match(r"\W(.)\1\W", " ff ")
<re.Match object; span=(0, 4), match=' ff '>
>>> re.match("\\W(.)\\1\\W", " ff ")
<re.Match object; span=(0, 4), match=' ff '>

```

To match a literal backslash, you have to escape it inside the regular expression. Under raw string notation that comes out as `r"\\"`, whereas without raw string notation you are forced to write `"\\\\"` — which renders the lines of code below equivalent:

```python
>>> re.match(r"\\", r"\\")
<re.Match object; span=(0, 1), match='\\'>
>>> re.match("\\\\", r"\\")
<re.Match object; span=(0, 1), match='\\'>

```

[Subject index](INDEX.md) · [Previous](finding-all-adverbs-and-their-positions.md) · [Continue](writing-a-tokenizer.md) · [Owning module, declaration or section: re](re-regular-expression-operations.md)
