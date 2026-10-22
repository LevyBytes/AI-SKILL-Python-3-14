# pkgutil / Package extension utility: Dotted and colon-separated resolve_name syntax

`W(.W)*`

- `W(.W)*:(W(.W)*)?`

That first form exists purely for backward compatibility. It takes some leading slice of the dotted name to be a package and the remainder to be an object somewhere inside that package, perhaps nested within further objects. Since inspection alone can't reveal where the package ends and the object hierarchy begins, this form demands repeated import attempts.

With the second form, the caller spells out the dividing point by inserting a single colon: everything in the dotted name to the colon's left is a package to import, while everything to its right is the object hierarchy inside that package. Just one import is required for this form. Where it finishes on the colon, a module object comes back.

The function either returns an object (which may well be a module) or raises one of the exceptions listed here:

[`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) – when *name* fails to match a recognised format.

[`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) – when an import that ought to have worked instead failed.

[`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) – when something went wrong while walking the object hierarchy inside the imported package on the way to the target object.

Added in version 3.9.

[Subject index](INDEX.md) · [Previous](pkgutil-walk-packages-to-pkgutil-resolve-name.md) · [Owning module, declaration or section: pkgutil](pkgutil-moduleinfo-class-to-pkgutil-iter-modules.md)
