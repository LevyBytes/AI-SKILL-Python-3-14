# importlib.resources.abc: `importlib.resources.abc.TraversableResources`

*class *importlib.resources.abc.TraversableResources

An abstract base class meant for resource readers that can serve the [`importlib.resources.files()`](https://docs.python.org/3.14/library/importlib.resources.html#importlib.resources.files) interface. It subclasses `ResourceReader` and fills in concrete versions of the `ResourceReader`'s abstract methods. As a result, whatever loader hands over `TraversableResources` hands over `ResourceReader` as well.

A loader aiming to back resource reading is meant to implement this interface.

 *abstractmethod *files()

Hands back an `importlib.resources.abc.Traversable` object covering the loaded package.

[Subject index](INDEX.md) · [Previous](traversable-resource-interface.md) · [Continue](../importlib-resources/resource-anchors-and-filesystem-context.md) · [Owning module, declaration or section: importlib.resources.abc](importlib-resources-abc-resourcereader-class.md)
