# gettext - Deferred translations

### Deferred translations

In the majority of coding scenarios, strings get translated at the spot where they are coded. Now and then, however, you need to flag strings for translation but postpone the actual translation to a later point. A classic example is:

```python
animals = ['mollusk',
           'albatross',
           'rat',
           'penguin',
           'python', ]
# ...
for a in animals:
    print(a)

```

Here, you want to flag the strings in the `animals` list as translatable, yet you do not actually want to translate them until the moment they are printed.

One way you can deal with this situation is:

```python
def _(message): return message

animals = [_('mollusk'),
           _('albatross'),
           _('rat'),
           _('penguin'),
           _('python'), ]

del _

# ...
for a in animals:
    print(_(a))

```

This works because the dummy definition of `_()` merely returns the string unchanged. And that dummy definition will temporarily shadow any definition of `_()` in the built-in namespace (up until the [`del`](https://docs.python.org/3.14/reference/simple_stmts.html#del) command). Be careful, though, if you already have a definition of `_()` in the local namespace.

Note that the second use of `_()` will not flag "a" as translatable to the **gettext** program, since the parameter is not a string literal.

A different way to deal with this is the following example:

```python
def N_(message): return message

animals = [N_('mollusk'),
           N_('albatross'),
           N_('rat'),
           N_('penguin'),
           N_('python'), ]

# ...
for a in animals:
    print(_(a))

```

In this case, you are flagging translatable strings with the function `N_()`, which won't collide with any definition of `_()`. You will, though, have to instruct your message extraction program so it hunts for translatable strings flagged with `N_()`. **xgettext**, **pygettext**, `pybabel extract`, and **xpot** each enable this via the `-k` command-line switch. Picking `N_()` here is entirely arbitrary; it could equally well have been `MarkThisStringForTranslation()`.

[Subject index](INDEX.md) · [Previous](changing-languages-on-the-fly.md) · [Owning module, declaration or section: gettext](gettext-multilingual-internationalization-services.md)
