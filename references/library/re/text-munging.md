# re — Text Munging

### Text Munging

`sub()` swaps out each instance of a pattern for a string or for whatever a function returns. The example here pairs `sub()` with a function to “munge” text — shuffling the order of the characters inside every word of a sentence while leaving the first and last characters fixed:

```python
>>> def repl(m):
...     inner_word = list(m.group(2))
...     random.shuffle(inner_word)
...     return m.group(1) + "".join(inner_word) + m.group(3)
...
>>> text = "Professor Abdolmalek, please report your absences promptly."
>>> re.sub(r"(\w)(\w+)(\w)", repl, text)
'Poefsrosr Aealmlobdk, pslaee reorpt your abnseces plmrptoy.'
>>> re.sub(r"(\w)(\w+)(\w)", repl, text)
'Pofsroser Aodlambelk, plasee reoprt yuor asnebces potlmrpy.'

```

[Subject index](INDEX.md) · [Previous](making-a-phonebook.md) · [Continue](finding-all-adverbs.md) · [Owning module, declaration or section: re](re-regular-expression-operations.md)
