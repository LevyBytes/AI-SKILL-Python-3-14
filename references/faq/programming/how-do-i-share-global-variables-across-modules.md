# How do I share global variables across modules?

### How do I share global variables across modules?

The standard approach to sharing data among modules inside one program is to make a dedicated module (frequently named config or cfg). Simply import that config module in every module of your application; the module then turns into a global name. Since each module exists as just one instance, whatever modifications you make to the module object show up everywhere. For instance:

config.py:

```python
x = 0   # Default value of the 'x' configuration setting

```

mod.py:

```python
import config
config.x = 1

```

main.py:

```python
import config
import mod
print(config.x)

```

For that very reason, a module also underpins how the singleton design pattern gets implemented.

[Subject index](INDEX.md)
