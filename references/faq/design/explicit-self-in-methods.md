# Why must 'self' be used explicitly in method definitions and calls?

### Why must 'self' be used explicitly in method definitions and calls?

This notion came from Modula-3. It proves quite handy, for several reasons.

To begin with, it's clearer that you're working with a method or instance attribute rather than a local variable. Seeing `self.x` or `self.meth()` leaves no doubt that an instance variable or method is at play, even when you haven't memorized the class definition. In C++, you can roughly guess from the absence of a local variable declaration (provided globals are uncommon or simple to spot) ? but Python has no local variable declarations, so you'd be forced to check the class definition to know for certain. Certain C++ and Java coding standards require instance attributes to carry an `m_` prefix, so this explicitness retains its value in those languages as well.

Second, no special syntax becomes necessary when you wish to explicitly reference or invoke the method belonging to a specific class. In C++, should you want a method from a base class that a derived class overrides, you must employ the `::` operator ? whereas in Python you may write `baseclass.methodname(self, <argument list>)`. That comes in especially handy for [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) methods, and more broadly whenever a derived class method seeks to extend the like-named base class method and must therefore call the base class method by some means.

Lastly, where instance variables are concerned, it resolves a syntactic difficulty around assignment: because local variables in Python are (by definition!) the variables that receive a value within a function body (and that aren't declared global explicitly), there must be a way to signal to the interpreter that an assignment was intended to target an instance variable instead of a local variable, and ideally that signal should be syntactic (for efficiency reasons). C++ handles this via declarations, yet Python lacks declarations and it would be a shame to add them solely for this end. The explicit `self.var` resolves it neatly. In the same vein, when using instance variables, having to write `self.var` means that references to unqualified names within a method needn't search the instance's directories. Put differently, local variables and instance variables occupy two separate namespaces, and you have to tell Python which namespace applies.

[Subject index](INDEX.md)
