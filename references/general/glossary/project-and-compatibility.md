# Project and compatibility

Open when checking Python definitions for project and compatibility.

## PEP

Python Enhancement Proposal. A PEP is a design document that conveys information to the Python community, or that lays out a new feature for Python or for its processes or environment. A PEP ought to deliver a concise technical specification together with a rationale for the features it proposes.

PEPs are meant to be the chief vehicles for proposing major new features, for gathering community feedback on a topic, and for recording the design decisions baked into Python. Building consensus across the community and capturing dissenting opinions is the responsibility of the PEP author.

See [**PEP 1**](https://peps.python.org/pep-0001/).

## BDFL

Benevolent Dictator For Life, a.k.a. [Guido van Rossum](https://gvanrossum.github.io/), Python's creator.

## Python 3000

A nickname for the Python 3.x release line (coined long ago, back when shipping version 3 lay somewhere in the distant future.) It is also shortened to “Py3k”.

## Pythonic

An idea or fragment of code that hews closely to the most common idioms of the Python language, instead of writing code with concepts borrowed from other languages. To illustrate, one common Python idiom is iterating over every element of an iterable by means of a [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) statement. A great many other languages lack this kind of construct, so people new to Python sometimes reach for a numerical counter in its place:

```python
for i in range(len(food)):
    print(food[i])

```

Versus the tidier, Pythonic approach:

```python
for piece in food:
    print(piece)

```

## Zen of Python

A listing of Python design principles and philosophies that help in grasping and using the language. You can bring up the listing by typing "`import this`" at the interactive prompt.

## provisional API

A provisional API is an interface that has been intentionally kept out of the standard library's backwards compatibility guarantees. Large changes to these interfaces are not anticipated, but for as long as they carry the provisional label, backwards incompatible changes (right up to and including removing the interface) may happen if core developers judge it necessary. Such changes will not occur gratuitously – they will happen only where serious fundamental flaws come to light that escaped notice before the API was included.

Even where an API is provisional, backwards incompatible changes are treated as a “solution of last resort” - every effort will still go toward finding a backwards compatible fix for any problems that are identified.

This procedure lets the standard library keep evolving over time, free of locking problematic design mistakes in place for long stretches. Consult [**PEP 411**](https://peps.python.org/pep-0411/) for fuller details.

## provisional package

See provisional API.

## soft deprecated

A soft deprecated API ought not to appear in new code, though it stays safe for code that already exists to keep using it. The API goes on being documented and tested, but it will receive no further enhancement.

Soft deprecation, in contrast to ordinary deprecation, has no plan to take the API away and emits no warnings.

See [PEP 387: Soft Deprecation](https://peps.python.org/pep-0387/#soft-deprecation).

## EAFP

Easier to ask for forgiveness than permission. Under this widespread Python convention, one presumes that the keys or attributes are valid and traps exceptions should that presumption turn out wrong. Numerous [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) and [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) statements mark this tidy, quick approach. It stands opposed to the LBYL style prevalent in many other languages, C among them.

## LBYL

Look before you leap. Under this coding style, pre-conditions are checked outright before any calls or lookups occur. It stands in opposition to the EAFP approach and shows itself through an abundance of [`if`](https://docs.python.org/3.14/reference/compound_stmts.html#if) statements.

Within a multi-threaded setting, LBYL can open the door to a race condition that falls between “the looking” and “the leaping”. As an example, the snippet `if key in mapping: return mapping[key]` may break if some other thread deletes *key* out of *mapping* once the test has run but before the lookup happens. Locks, or switching to the EAFP approach, can resolve this problem. See also thread-safe.

[Glossary context index](INDEX.md).
