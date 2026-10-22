# How can I organize my code to make it easier to change the base class?

### How can I organize my code to make it easier to change the base class?

One option is to bind the base class to an alias and inherit from that alias. From then on the only edit needed is the value the alias points to. As an aside, the same trick helps when you want to pick a base class at run time (for example, according to which resources are available). Example:

```python
class Base:
    ...

BaseAlias = Base

class Derived(BaseAlias):
    ...

```

[Subject index](INDEX.md)
