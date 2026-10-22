# What’s New in Python 2.2 / Related Links

### Related Links

What you’ve read here amounts to a brisk tour of the additions, supplying just enough explanation to get you coding, while a lot of the finer points have been streamlined or skipped. So where do you turn for a fuller picture?

The [Descriptor Guide](https://docs.python.org/3.14/howto/descriptor.html#descriptorhowto) is a long tutorial-style introduction to the descriptor machinery, penned by Guido van Rossum. Should my account have piqued your curiosity, read that tutorial next, since it digs far deeper into the additions while still staying quite approachable.

After that, two PEPs are relevant, [**PEP 252**](https://peps.python.org/pep-0252/) and [**PEP 253**](https://peps.python.org/pep-0253/). [**PEP 252**](https://peps.python.org/pep-0252/) carries the title “Making Types Look More Like Classes” and walks through the descriptor API. [**PEP 253**](https://peps.python.org/pep-0253/), titled “Subtyping Built-in Types”, sets out the type-object changes that allow built-in objects to be subtyped. Of the pair, [**PEP 253**](https://peps.python.org/pep-0253/) is the knottier one, and here and there the required discussion of types and meta-types may make your head explode. Both PEPs were authored and implemented by Guido van Rossum, with hefty help from the remainder of the Zope Corp. team.

In the end there’s the final word of all: the source code. The bulk of the type-handling machinery sits in `Objects/typeobject.c`, but you should turn to it only once every other path has been used up, posting a question to python-list or python-dev included.

[Subject index](INDEX.md) · [Previous source section](attribute-access.md) · [Next source section](pep-234-iterators.md) · [Release/subject declaration](introduction.md)
