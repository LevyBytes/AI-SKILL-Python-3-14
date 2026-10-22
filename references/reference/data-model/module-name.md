# module.__name__

module.__name__

The identifier by which the import system distinguishes this module uniquely. When a module runs directly, this gets set to `"__main__"`.

The value of this attribute has to be the module's fully qualified name. It should equal the value of [`module.__spec__.name`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ModuleSpec.name).

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Owning language section](modules.md) · [Owning language section](import-related-attributes-on-module-objects.md) · [Previous source section](import-related-attributes-on-module-objects.md) · [Following source section](module-spec.md)
