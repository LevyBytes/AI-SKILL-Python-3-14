# exceptions: Assertion, attribute, import and lookup exceptions

### Concrete exceptions

The exceptions that follow are the ones typically raised.

 *exception *AssertionError

Raised whenever an [`assert`](https://docs.python.org/3.14/reference/simple_stmts.html#assert) statement does not hold.

 *exception *AttributeError

Raised whenever an attribute reference (see [Attribute references](https://docs.python.org/3.14/reference/expressions.html#attribute-references)) or assignment does not succeed. (Where an object offers no support for attribute references or attribute assignments whatsoever, `TypeError` gets raised instead.)

The optional keyword-only arguments *name* and *obj* assign the matching attributes:

 name

The name belonging to the attribute whose access was attempted.

 obj

The object on which the named attribute was accessed.

Changed in version 3.10: Added the `name` and `obj` attributes.

 *exception *EOFError

Raised whenever the [`input()`](https://docs.python.org/3.14/library/functions.html#input) function reaches an end-of-file condition (EOF) before any data has been read. (Note: when they reach EOF, the [`io.TextIOBase.read()`](https://docs.python.org/3.14/library/io.html#io.TextIOBase.read) and [`io.IOBase.readline()`](https://docs.python.org/3.14/library/io.html#io.IOBase.readline) methods give back an empty string.)

 *exception *FloatingPointError

Not currently used.

 *exception *GeneratorExit

Raised at the point where a [generator](https://docs.python.org/3.14/glossary.html#term-generator) or [coroutine](https://docs.python.org/3.14/glossary.html#term-coroutine) gets closed; see [`generator.close()`](https://docs.python.org/3.14/reference/expressions.html#generator.close) and [`coroutine.close()`](https://docs.python.org/3.14/reference/datamodel.html#coroutine.close). Because it is, strictly speaking, not an error, it inherits straight from `BaseException` rather than `Exception`.

 *exception *ImportError

Raised whenever the [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) statement runs into difficulty while attempting to load a module. It is also raised when the "from list" of `from ... import` references a name that cannot be located.

The optional keyword-only arguments *name* and *path* assign the matching attributes:

 name

The name belonging to the module whose import was attempted.

 path

The path of whatever file set off the exception.

Changed in version 3.3: Added the `name` and `path` attributes.

 *exception *ModuleNotFoundError

A subclass of `ImportError` that [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) raises whenever a module is not able to be located. It also gets raised should `None` turn up in [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules).

Added in version 3.6.

 *exception *IndexError

Raised whenever a sequence subscript lies beyond the valid range. (Slice indices get quietly clamped to land within the permitted range; where an index is not an integer, `TypeError` is raised.)

 *exception *KeyError

Raised whenever a mapping (dictionary) key cannot be found among the keys that already exist.

 *exception *KeyboardInterrupt

Raised whenever the user presses the interrupt key (usually Control-C or Delete). The interpreter checks for interrupts at regular intervals throughout execution. So that code catching `Exception` does not accidentally swallow it and thereby stop the interpreter from exiting, this exception inherits from `BaseException`.

Note

Handling a `KeyboardInterrupt` calls for special care. Since it can arise at points you cannot predict, under certain circumstances it may leave the program that is running in an inconsistent state. As a rule, the wisest course is to let `KeyboardInterrupt` terminate the program as fast as possible, or else to avoid raising it in the first place. (See [Note on Signal Handlers and Exceptions](https://docs.python.org/3.14/library/signal.html#handlers-and-exceptions).)

 *exception *MemoryError

Raised whenever an operation exhausts memory, though recovery may still be possible (by removing some objects). The associated value is a string identifying which sort of (internal) operation ran short on memory. Bear in mind that, owing to the underlying memory management architecture (C's `malloc()` function), the interpreter cannot always fully recover from this state; nonetheless it raises an exception so a stack traceback can be printed, on the chance that a run-away program was to blame.

 *exception *NameError

Raised whenever a local or global name cannot be located. This holds only for names that are unqualified. The associated value is an error message carrying the name that could not be located.

The optional keyword-only argument *name* assigns the attribute:

[Subject index](INDEX.md) · [Previous](baseexception-to-lookuperror.md) · [Continue](notimplementederror-to-pythonfinalizationerror.md)
