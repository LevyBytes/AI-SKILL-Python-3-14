# 10.5. String pattern matching

### 10.5. String pattern matching

For sophisticated text work, the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module supplies regular expression tooling. When the matching or rewriting gets intricate, regular expressions deliver compact, well-tuned answers:

```python
>>> import re
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'

```

For straightforward needs, plain string methods win out, since they read more clearly and are simpler to debug:

```python
>>> 'tea for too'.replace('too', 'two')
'tea for two'

```

[Subject index](INDEX.md) · [Previous source section](error-output-redirection-and-program-termination.md) · [Following source section](mathematics.md)
