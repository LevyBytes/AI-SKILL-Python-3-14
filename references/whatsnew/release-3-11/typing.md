# What's New In Python 3.11 / typing — typing

### typing

For major changes, see New Features Related to Type Hints.

- [`typing.assert_never()`](https://docs.python.org/3.14/library/typing.html#typing.assert_never) plus [`typing.Never`](https://docs.python.org/3.14/library/typing.html#typing.Never) were added. You can lean on `typing.assert_never()` to have a type checker verify that a given line stays unreachable. When run, it raises an [`AssertionError`](https://docs.python.org/3.14/library/exceptions.html#AssertionError). (Contributed by Jelle Zijlstra in [gh-90633](https://github.com/python/cpython/issues/90633).)

- [`typing.reveal_type()`](https://docs.python.org/3.14/library/typing.html#typing.reveal_type) was added. It lets you query a type checker about whatever type it deduced for some expression. When run, it emits the type of the value passed in. (Contributed by Jelle Zijlstra in [gh-90572](https://github.com/python/cpython/issues/90572).)

- [`typing.assert_type()`](https://docs.python.org/3.14/library/typing.html#typing.assert_type) was added. It lets you have a type checker verify that whatever type it deduced for some expression lines up with the supplied type. When run, it merely gives back the value passed in. (Contributed by Jelle Zijlstra in [gh-90638](https://github.com/python/cpython/issues/90638).)

- [`typing.TypedDict`](https://docs.python.org/3.14/library/typing.html#typing.TypedDict) types may now be generic. (Contributed by Samodya Abeysiriwardane in [gh-89026](https://github.com/python/cpython/issues/89026).)

- [`NamedTuple`](https://docs.python.org/3.14/library/typing.html#typing.NamedTuple) types may now be generic. (Contributed by Serhiy Storchaka in [bpo-43923](https://bugs.python.org/issue?@action=redirect&bpo=43923).)

- Subclassing of [`typing.Any`](https://docs.python.org/3.14/library/typing.html#typing.Any) is now permitted. This helps you sidestep type checker complaints around extremely dynamic classes, mocks being one example. (Contributed by Shantanu Jain in [gh-91154](https://github.com/python/cpython/issues/91154).)

- The [`typing.final()`](https://docs.python.org/3.14/library/typing.html#typing.final) decorator now applies the `__final__` attributed on whatever object it decorates. (Contributed by Jelle Zijlstra in [gh-90500](https://github.com/python/cpython/issues/90500).)

- The [`typing.get_overloads()`](https://docs.python.org/3.14/library/typing.html#typing.get_overloads) function lets you introspect a function's overloads. To wipe every registered overload belonging to a function, use [`typing.clear_overloads()`](https://docs.python.org/3.14/library/typing.html#typing.clear_overloads). (Contributed by Jelle Zijlstra in [gh-89263](https://github.com/python/cpython/issues/89263).)

- For [`Protocol`](https://docs.python.org/3.14/library/typing.html#typing.Protocol) subclasses, the [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) method is now retained. (Contributed by Adrian Garcia Badarasco in [gh-88970](https://github.com/python/cpython/issues/88970).)

- How empty tuple types (`Tuple[()]`) are represented has been streamlined. Introspection feels this; for instance, `get_args(Tuple[()])` now resolves to `()` rather than `((),)`. (Contributed by Serhiy Storchaka in [gh-91137](https://github.com/python/cpython/issues/91137).)

- By dropping the callable check inside the private `typing._type_check` function, runtime expectations for type annotations have been relaxed. (Contributed by Gregory Beauregard in [gh-90802](https://github.com/python/cpython/issues/90802).)

- [`typing.get_type_hints()`](https://docs.python.org/3.14/library/typing.html#typing.get_type_hints) can now evaluate strings as forward references within [PEP 585 generic aliases](https://docs.python.org/3.14/library/stdtypes.html#types-genericalias). (Contributed by Niklas Rosenstein in [gh-85542](https://github.com/python/cpython/issues/85542).)

- [`typing.get_type_hints()`](https://docs.python.org/3.14/library/typing.html#typing.get_type_hints) stopped tacking [`Optional`](https://docs.python.org/3.14/library/typing.html#typing.Optional) onto parameters whose default is `None`. (Contributed by Nikita Sobolev in [gh-90353](https://github.com/python/cpython/issues/90353).)

- [`typing.get_type_hints()`](https://docs.python.org/3.14/library/typing.html#typing.get_type_hints) can now evaluate bare stringified [`ClassVar`](https://docs.python.org/3.14/library/typing.html#typing.ClassVar) annotations. (Contributed by Gregory Beauregard in [gh-90711](https://github.com/python/cpython/issues/90711).)

- [`typing.no_type_check()`](https://docs.python.org/3.14/library/typing.html#typing.no_type_check) stopped altering outside classes and functions. On top of that, it now properly flags classmethods as exempt from type checking. (Contributed by Nikita Sobolev in [gh-90729](https://github.com/python/cpython/issues/90729).)

[Subject index](INDEX.md) · [Previous source section](traceback.md) · [Next source section](unicodedata.md) · [Release/subject declaration](summary-release-highlights.md)
