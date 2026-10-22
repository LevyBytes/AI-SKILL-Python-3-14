# What's New In Python 3.7 / Changes in Python Behavior

### Changes in Python Behavior

- The [`async`](https://docs.python.org/3.14/reference/compound_stmts.html#async) and [`await`](https://docs.python.org/3.14/reference/expressions.html#await) names are now reserved keywords. Whenever some code adopts either name as an identifier, it will from now on trigger a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError). (Contributed by Jelle Zijlstra in [bpo-30406](https://bugs.python.org/issue?@action=redirect&bpo=30406).)

- [**PEP 479**](https://peps.python.org/pep-0479/) now applies to every piece of code in Python 3.7, which means [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) exceptions arising whether directly or indirectly inside coroutines and generators get converted into [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) exceptions. (Contributed by Yury Selivanov in [bpo-32670](https://bugs.python.org/issue?@action=redirect&bpo=32670).)

- Declaring [`object.__aiter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__aiter__) methods as asynchronous is no longer allowed. (Contributed by Yury Selivanov in [bpo-31709](https://bugs.python.org/issue?@action=redirect&bpo=31709).)

- Through an oversight, the syntax shown below was mistakenly tolerated by earlier Python versions:

```python
f(1 for x in [1],)

class C(1 for x in [1]):
    pass

```

Python 3.7 today properly raises a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError): a generator expression must sit immediately inside its own pair of parentheses and may not carry a comma to its left or right, while the doubled parentheses can be skipped solely on calls. Serhiy Storchaka delivered this work — refer to [bpo-32012](https://bugs.python.org/issue?@action=redirect&bpo=32012) and [bpo-32023](https://bugs.python.org/issue?@action=redirect&bpo=32023).

- With the [`-m`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-m) switch in play, the starting working directory is from now on appended to [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path), in place of an empty string (which had dynamically stood for whatever the working directory happened to be at each import). Code that tests for the empty string, or that otherwise leans on how this used to behave, will require updating to suit (for instance by additionally testing `os.getcwd()` or `os.path.dirname(__main__.__file__)`, according to the reason that empty-string check existed at the outset).

[Subject index](INDEX.md) · [Previous source section](porting-to-python-3-7.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](changes-in-the-python-api.md)
