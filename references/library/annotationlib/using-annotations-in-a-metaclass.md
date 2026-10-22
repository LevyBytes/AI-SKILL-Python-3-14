# annotationlib — Using annotations in a metaclass

### Recipes

### Using annotations in a metaclass

A [metaclass](https://docs.python.org/3.14/reference/datamodel.html#metaclasses) might wish to examine, or even alter, the annotations within a class body while the class is being created. That entails fetching the annotations out of the class namespace dictionary. With classes built under `from __future__ import annotations`, the annotations sit in the dictionary's `__annotations__` key. For other annotated classes, `get_annotate_from_class_namespace()` serves to obtain the annotate function, and `call_annotate_function()` serves to invoke it and fetch the annotations. The `FORWARDREF` format is usually the best pick here, since it lets the annotations mention names that are not yet resolvable while the class is being created.

When altering the annotations, the soundest approach is to build a wrapper annotate function that calls through to the original annotate function, applies whatever adjustments are needed, and returns the outcome.

What follows is an example of a metaclass that strips out every [`typing.ClassVar`](https://docs.python.org/3.14/library/typing.html#typing.ClassVar) annotation from the class and stashes them in a separate attribute:

```python
import annotationlib
import typing

class ClassVarSeparator(type):
   def __new__(mcls, name, bases, ns):
      if "__annotations__" in ns:  # from __future__ import annotations
         annotations = ns["__annotations__"]
         classvar_keys = {
            key for key, value in annotations.items()
            # Use string comparison for simplicity; a more robust solution
            # could use annotationlib.ForwardRef.evaluate
            if value.startswith("ClassVar")
         }
         classvars = {key: annotations[key] for key in classvar_keys}
         ns["__annotations__"] = {
            key: value for key, value in annotations.items()
            if key not in classvar_keys
         }
         wrapped_annotate = None
      elif annotate := annotationlib.get_annotate_from_class_namespace(ns):
         annotations = annotationlib.call_annotate_function(
            annotate, format=annotationlib.Format.FORWARDREF
         )
         classvar_keys = {
            key for key, value in annotations.items()
            if typing.get_origin(value) is typing.ClassVar
         }
         classvars = {key: annotations[key] for key in classvar_keys}

         def wrapped_annotate(format):
            annos = annotationlib.call_annotate_function(annotate, format, owner=typ)
            return {key: value for key, value in annos.items() if key not in classvar_keys}

      else:  # no annotations
         classvars = {}
         wrapped_annotate = None
      typ = super().__new__(mcls, name, bases, ns)

      if wrapped_annotate is not None:
         # Wrap the original __annotate__ with a wrapper that removes ClassVars
         typ.__annotate__ = wrapped_annotate
      typ.classvars = classvars  # Store the ClassVars in a separate attribute
      return typ

```

[Subject index](INDEX.md) · [Continue](creating-a-custom-callable-annotate-function.md) · [Owning module, declaration or section: annotationlib](annotationlib-functionality-for-introspecting-annotations.md)
