# typing - The type of class objects

### The type of class objects

A variable carrying the annotation `C` accepts any value whose type is `C`. By contrast, a variable annotated `type[C]` (or the deprecated `typing.Type[C]`) accepts values that are themselves classes — concretely, it admits the *class object* of `C`. For instance:

```python
a = 3         # Has type ``int``
b = int       # Has type ``type[int]``
c = type(a)   # Also has type ``type[int]``

```

Observe that `type[C]` is covariant:

```python
class User: ...
class ProUser(User): ...
class TeamUser(User): ...

def make_new_user(user_class: type[User]) -> User:
    # ...
    return user_class()

make_new_user(User)      # OK
make_new_user(ProUser)   # Also OK: ``type[ProUser]`` is a subtype of ``type[User]``
make_new_user(TeamUser)  # Still fine
make_new_user(User())    # Error: expected ``type[User]`` but got ``User``
make_new_user(int)       # Error: ``type[int]`` is not a subtype of ``type[User]``

```

Only classes, `Any`, type variables, and unions formed from any of these are valid parameters for [`type`](https://docs.python.org/3.14/library/functions.html#type). For instance:

```python
def new_non_team_user(user_class: type[BasicUser | ProUser]): ...

new_non_team_user(BasicUser)  # OK
new_non_team_user(ProUser)    # OK
new_non_team_user(TeamUser)   # Error: ``type[TeamUser]`` is not a subtype
                              # of ``type[BasicUser | ProUser]``
new_non_team_user(User)       # Also an error

```

`type[Any]` amounts to [`type`](https://docs.python.org/3.14/library/functions.html#type) itself, the root from which Python's [metaclass hierarchy](https://docs.python.org/3.14/reference/datamodel.html#metaclasses) springs.

[Subject index](INDEX.md) · [Previous](annotating-tuples.md) · [Continue](annotating-generators-and-coroutines.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md)
