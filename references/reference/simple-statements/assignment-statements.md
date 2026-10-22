# 7.2. Assignment statements

### 7.2. Assignment statements

Assignment statements serve to (re)bind names to values and to alter attributes or items belonging to mutable objects:

```text

assignment_stmt: (target_list "=")+ (starred_expression | yield_expression)
target_list:     target ("," target)* [","]
target:          identifier
                 | "(" [target_list] ")"
                 | "[" [target_list] "]"
                 | attributeref
                 | subscription
                 | "*" target
```

(Consult the section [Primaries](https://docs.python.org/3.14/reference/expressions.html#primaries) for the grammar definitions of *attributeref* and *subscription*.)

An assignment statement evaluates the expression list (recall that this might be one expression or a comma-separated series, where the series produces a tuple) and binds the single resulting object to each target list, proceeding left to right.

The meaning of assignment is recursive and varies with the shape of the target (list). Whenever a target sits within a mutable object (an attribute reference or a subscription), that mutable object is ultimately responsible for carrying out the assignment and judging whether it is valid, and it may raise an exception should the assignment be unacceptable. The conventions that the various types follow and the exceptions they raise appear alongside the definition of those object types (refer to the section [The standard type hierarchy](https://docs.python.org/3.14/reference/datamodel.html#types)).

Binding an object to a target list ? which may be wrapped in parentheses or square brackets ? has the following recursive definition.

- When the target list is one target with no trailing comma, perhaps wrapped in parentheses, the object is bound to that target.

- Else:

  - When the target list holds a single target preceded by an asterisk, termed a ?starred? target: the object has to be an iterable holding at least as many items as the target list has targets, less one. The iterable's leading items are bound, left to right, to the targets that come before the starred target. The iterable's trailing items are bound to the targets that come after the starred target. Whatever items remain in the iterable are then collected into a list and bound to the starred target (and that list may be empty).

  - Else: the object has to be an iterable holding exactly as many items as the target list has targets, and the items are bound, left to right, to their matching targets.

Binding an object to a single target has the following recursive definition.

- When the target is an identifier (name):

  - When the name appears in no `global` or `nonlocal` statement within the current code block: the name gets bound to the object inside the current local namespace.

  - Otherwise: the name gets bound to the object inside the global namespace, or the enclosing namespace identified by `nonlocal`, as appropriate.

Should the name already be bound, it gets rebound. Doing so can drop the reference count of the object that was formerly bound to that name down to zero, which leads to that object being deallocated and its destructor (when it has one) being invoked.

- When the target is an attribute reference: the primary expression within the reference is evaluated. It ought to produce an object that has assignable attributes; when it does not, [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised. That object is next requested to bind the assigned object to the named attribute; when it is unable to do so, it raises an exception (commonly though not always [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError)).

Note: When the object is a class instance and the attribute reference shows up on both sides of the assignment operator, the right-hand side expression `a.x` may reach either an instance attribute or (when no instance attribute is present) a class attribute. The left-hand side target `a.x` is invariably stored as an instance attribute, being created if it does not yet exist. So the two appearances of `a.x` need not point to the same attribute: when the right-hand side expression reaches a class attribute, the left-hand side makes a fresh instance attribute that serves as the target of the assignment:

```python
class Cls:
    x = 3             # class variable
inst = Cls()
inst.x = inst.x + 1   # writes inst.x as 4 leaving Cls.x as 3

```

This account does not always hold for descriptor attributes, for instance properties built with [`property()`](https://docs.python.org/3.14/library/functions.html#property).

- When the target is a subscription: the primary expression within the reference is evaluated. After that, the subscript expression is evaluated. Then the primary's [`__setitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__setitem__) method runs with two arguments: the subscript together with the assigned object.

Generally, [`__setitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__setitem__) is provided on mutable sequence objects (lists, for example) and mapping objects (dictionaries, for example), and works in the following way.

When the primary is a mutable sequence object (a list, say), the subscript must produce an integer. Should it be negative, the sequence's length is added onto it. The value that results must be a nonnegative integer below the sequence's length, and the sequence is then asked to bind the assigned object to its item at that index. Should the index fall outside the valid range, [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError) is raised (assigning to a subscripted sequence is unable to append new items to a list).

When the primary is a mapping object (a dictionary, say), the subscript must carry a type that the mapping's key type accepts, and the mapping is then asked to form a key/value pair tying the subscript to the assigned object. This may either overwrite an existing key/value pair holding the same key value, or add a fresh key/value pair (when no key with that same value was present).

When the target is a slicing: evaluating the primary expression ought to yield a mutable sequence object (a list, say). The object being assigned ought to be [iterable](https://docs.python.org/3.14/glossary.html#term-iterable). The lower and upper bounds of the slicing should be integers; when they are `None` (or absent), zero and the sequence's length serve as the defaults. Should either bound be negative, the sequence's length is added onto it. The bounds that result are clamped to fall between zero and the sequence's length, inclusive. At last, the sequence object is asked to swap the slice for the items of the assigned sequence. The slice's length need not match the assigned sequence's length, so the target sequence's length may change, provided the target sequence permits it.

Even though the definition of assignment suggests that overlaps between the left-hand side and the right-hand side happen ?simultaneously? (so that `a, b = b, a` swaps two variables, for example), overlaps *within* the group of assigned-to variables play out left-to-right, which can occasionally cause confusion. As an example, the program below prints `[0, 2]`:

```python
x = [0, 1]
i = 0
i, x[i] = 1, 2         # i is updated, then x[i] is updated
print(x)

```

See also

[**PEP 3132**](https://peps.python.org/pep-3132/) - Extended Iterable Unpacking

The specification for the `*target` feature.

[Subject index](INDEX.md) · [Owning language section](simple-statements.md) · [Previous source section](expression-statements.md) · [Following source section](augmented-assignment-statements.md)
