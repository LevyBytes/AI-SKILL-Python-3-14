# typing: `typing.ReadOnly`, `typing.Annotated`

typing.ReadOnly

A special typing construct that flags a `TypedDict` item as read-only.

For example:

```python
class Movie(TypedDict):
   title: ReadOnly[str]
   year: int

def mutate_movie(m: Movie) -> None:
   m["year"] = 1999  # allowed
   m["title"] = "The Matrix"  # type checker error

```

There is no runtime checking for this property.

See `TypedDict` and [**PEP 705**](https://peps.python.org/pep-0705/) for more details.

Added in version 3.13.

 typing.Annotated

Special typing form to add context-specific metadata to an annotation.

Attach metadata `x` onto a given type `T` through the annotation `Annotated[T, x]`. Metadata supplied via `Annotated` is available to static analysis tools or at runtime. While the program runs, that metadata lives in a `__metadata__` attribute.

Should a library or tool come across an annotation `Annotated[T, x]` and carry no dedicated handling for the metadata, it ought to disregard the metadata and just treat the annotation as `T`. For that reason, `Annotated` can help code that wishes to repurpose annotations for goals beyond Python's static typing system.

Writing `Annotated[T, x]` as an annotation continues to permit static typechecking of `T`, because type checkers will just disregard the metadata `x`. On this point, `Annotated` parts ways with the `@no_type_check` decorator, which can likewise be used to attach annotations beyond the typing system's reach, but which switches off typechecking entirely for a function or class.

Deciding how the metadata should be read falls to whichever tool or library runs into an `Annotated` annotation. A tool or library that meets an `Annotated` type can walk through the metadata elements to work out whether any are relevant (for instance, via [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance)).

[Subject index](INDEX.md) · [Previous](typing-classvar-to-typing-notrequired.md) · [Continue](special-forms.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Special forms](typing-union-class.md)
