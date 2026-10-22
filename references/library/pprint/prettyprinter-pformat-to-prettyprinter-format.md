# pprint: `PrettyPrinter.pformat()`, `PrettyPrinter.pprint()`, `PrettyPrinter.isreadable()`, `PrettyPrinter.isrecursive()`, `PrettyPrinter.format()`

`PrettyPrinter.pformat(*object*)`

Hands back the formatted representation of *object*, honoring the options that were handed to the `PrettyPrinter` constructor.

`PrettyPrinter.pprint(*object*)`

Writes the formatted representation of *object* to the configured stream, followed by a newline.

The methods below supply the implementations behind the like-named functions. Calling them on an instance is marginally faster, since there's no need to spin up fresh `PrettyPrinter` objects each time.

`PrettyPrinter.isreadable(*object*)`

Works out whether the object's formatted representation is “readable” — that is, whether [`eval()`](https://docs.python.org/3.14/library/functions.html#eval) could rebuild the value from it. Mind that recursive objects give back `False`. It also returns `False` whenever the `PrettyPrinter`'s *depth* parameter is set and the object runs deeper than that allows.

`PrettyPrinter.isrecursive(*object*)`

Works out whether the object calls for a recursive representation.

This method exists as a hook letting subclasses alter how objects turn into strings. The default version draws on the internals of the `saferepr()` implementation.

`PrettyPrinter.format(*object*, *context*, *maxlevels*, *level*)`

Gives back three values: the formatted form of *object* as a string, a flag telling whether the result is readable, and a flag telling whether recursion turned up. Its first argument is the object being presented. The second is a dictionary keyed by the [`id()`](https://docs.python.org/3.14/library/functions.html#id) of objects belonging to the current presentation context (the direct and indirect containers for *object* that shape the presentation); should an object that already appears in *context* need presenting, the third return value ought to be `True`. Each recursive call to the `format()` method should register further container entries in this dictionary. The third argument, *maxlevels*, states the requested recursion limit, which is `0` when no limit is requested; pass it along unchanged to recursive calls. The fourth argument, *level*, states the present level, and recursive calls should receive a value below that of the current call.

[Subject index](INDEX.md) · [Previous](pprint-prettyprinter-class.md) · [Continue](example-section-introduction-and-initial-examples.md) · [Owning module, declaration or section: pprint](pprint-data-pretty-printer.md) · [Owning module, declaration or section: pprint.PrettyPrinter](pprint-prettyprinter-class.md) · [Owning module, declaration or section: PrettyPrinter Objects](pprint-prettyprinter-class.md)
