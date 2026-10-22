# Why doesn’t Python have a “with” statement for attribute assignments?

### Why doesn’t Python have a “with” statement for attribute assignments?

Python’s [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement surrounds the running of a block, invoking code as you enter and again as you leave it. Certain languages provide a construct resembling the following:

```python
with obj:
    a = 1               # equivalent to obj.a = 1
    total = total + 1   # obj.total = obj.total + 1

```

Within Python, a construct of that sort would carry an ambiguity.

Languages of a different stripe — Object Pascal, Delphi, and C++ among them — rely on static types, which makes it perfectly clear which member an assignment targets. That clarity is exactly what static typing buys you: the compiler *always* has the scope of each variable pinned down at compile time.

Python, on the other hand, is dynamically typed. There is no telling ahead of time which attribute a given line will touch at runtime, and member attributes can be grafted onto or stripped from objects as the program runs. So merely reading the code leaves you unable to say what a reference points at: is it a local, a global, or a member attribute?

As a case in point, consider this unfinished fragment of code:

```python
def foo(a):
    with a:
        print(x)

```

Here the code presumes that `a` carries a member attribute named `x` — yet nothing in Python conveys that fact to the interpreter. And what ought to occur if `a` happens to be, say, an integer? Were a global variable called `x` to exist, would it come into play within the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) block? As this shows, Python’s dynamic character makes decisions like these far thornier.

That said, the chief payoff of [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) and comparable language features — cutting down on the amount of code — is readily had in Python through plain assignment. Rather than writing:

```python
function(args).mydict[index][index].a = 21
function(args).mydict[index][index].b = 42
function(args).mydict[index][index].c = 63

```

write this:

```python
ref = function(args).mydict[index][index]
ref.a = 21
ref.b = 42
ref.c = 63

```

A bonus of doing it this way is faster execution: since Python resolves name bindings while the program runs, the second form carries out that resolution a single time rather than repeatedly.

Related proposals aiming to add syntax that trims code volume even more — for example a ‘leading dot’ notation — have been turned down in favor of keeping things explicit (see [https://mail.python.org/pipermail/python-ideas/2016-May/040070.html](https://mail.python.org/pipermail/python-ideas/2016-May/040070.html)).

[Subject index](INDEX.md)
