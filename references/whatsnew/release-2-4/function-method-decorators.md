# Python 2.4 changes: Function and method decorator syntax

### PEP 318: Decorators for Functions and Methods

Although Python 2.2 broadened Python’s object model with static methods and class methods, it stopped short of broadening Python’s syntax to give any fresh way of declaring static or class methods. What you had to do instead was write a [`def`](https://docs.python.org/3.14/reference/compound_stmts.html#def) statement the ordinary way, then feed the resulting method into a [`staticmethod()`](https://docs.python.org/3.14/library/functions.html#staticmethod) or [`classmethod()`](https://docs.python.org/3.14/library/functions.html#classmethod) function that wrapped the function up as a method belonging to the new type. The resulting code resembled this:

```python
class C:
   def meth (cls):
       ...

   meth = classmethod(meth)   # Rebind name to wrapped-up class method

```

Whenever the method ran on for many lines, overlooking or forgetting that [`classmethod()`](https://docs.python.org/3.14/library/functions.html#classmethod) call sitting after the function body became easy.

There had always been a plan to introduce some syntax that would render such definitions clearer, but back when 2.2 shipped no good syntax stood out. Even now a good syntax *still* isn’t obvious, yet users keep requesting an easier route to the feature; to satisfy that demand a new piece of syntax has been introduced.

This addition goes by the name “function decorators”. The name springs from the notion that [`classmethod()`](https://docs.python.org/3.14/library/functions.html#classmethod), [`staticmethod()`](https://docs.python.org/3.14/library/functions.html#staticmethod), and their kin tuck extra data onto a function object; they’re *decorating* functions with further detail.

Borrowing from Java, the notation employs the `'@'` character as a marker. Written with the new syntax, the earlier example becomes:

```python
class C:

   @classmethod
   def meth (cls):
       ...

```

Here `@classmethod` stands in for the `meth=classmethod(meth)` assignment. To generalize, suppose you have this:

```python
@A
@B
@C
def f ():
    ...

```

That’s the same as the following code from before decorators existed:

```python
def f(): ...
f = A(B(C(f)))

```

You must place decorators on the line preceding a function definition — one per line — and they can’t share a line with the def statement, so `@A def f(): ...` is not allowed. Decorating is limited to function definitions, whether at module scope or within a class; class definitions can’t be decorated.

At bottom a decorator is simply a function that receives the function being decorated as its argument and gives back either that same function or some fresh object. The value the decorator returns doesn’t have to be callable (although usually it is), unless additional decorators are going to be layered onto the result. Rolling your own decorators is straightforward. Here’s a basic illustration that merely attaches an attribute to the function object:

```python
>>> def deco(func):
...    func.attr = 'decorated'
...    return func
...
>>> @deco
... def f(): pass
...
>>> f
<function f at 0x402ef0d4>
>>> f.attr
'decorated'
>>>

```

For a somewhat more practical case, the decorator below verifies that the argument handed in is an integer:

[Subject index](INDEX.md) · [Previous source section](pep-292-simpler-string-substitutions.md) · [Next source section](pep318-function-and-method-decorators.md) · [Release/subject declaration](pep-218-built-in-set-objects.md)
