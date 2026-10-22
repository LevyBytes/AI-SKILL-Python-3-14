# 4.9.3.5. Recap

#### 4.9.3.5. Recap

Your particular scenario dictates which kind of parameters belong in the definition:

```python
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):

```

As guidance:

- Reach for positional-only whenever you would rather keep parameter labels hidden from whoever calls the code. It pays off when the labels carry no genuine significance, when you mean to lock in the argument sequence at call time, or when you must accept a few positional values alongside arbitrary keywords.

- Choose keyword-only where the labels do carry meaning and spelling them out makes the definition clearer, or where you wish to stop callers from depending on an argument's position.

- When designing an API, lean on positional-only so that renaming a parameter down the road won't break callers.

[Subject index](INDEX.md) · [Previous source section](positional-only-names-shared-with-keyword-dictionaries.md) · [Following source section](arbitrary-argument-lists.md)
