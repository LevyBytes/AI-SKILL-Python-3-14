# 1.1. Alternate Implementations

### 1.1. Alternate Implementations

Even though a single Python build stands out as overwhelmingly the most widely adopted, a few competing builds exist that hold special appeal for distinct groups of users.

Known implementations include:

CPython

Coded in C, this is the founding build of Python and the one that receives the most upkeep. As a rule, fresh language capabilities show up in it ahead of anywhere else.

Jython

A Java-based build of Python. You can drive Java programs with it as their scripting layer, or you can assemble whole programs that draw on the Java class libraries. People also reach for it frequently to write tests against Java libraries. Further details are at [the Jython website](https://www.jython.org/).

Python for .NET

Under the hood this build leans on CPython, yet it runs as a managed .NET application and opens up the .NET libraries for use. Brian Lloyd built it. To learn more, consult the [Python for .NET home page](https://pythonnet.github.io/).

IronPython

A different take on Python for .NET. In contrast with Python.NET, this one is a full Python build that emits IL and turns Python source straight into .NET assemblies. Jim Hugunin, who first authored Jython, created it as well. To dig deeper, visit [the IronPython website](https://ironpython.net/).

PyPy

A Python build that is itself coded entirely in Python. It brings several sophisticated capabilities that rival builds lack, among them stackless operation and a Just in Time compiler. A driving aim behind the project is to invite tinkering with the language as such, since writing the interpreter in Python makes it far simpler to alter. More can be read on [the PyPy project’s home page](https://pypy.org/).

Every one of these builds departs in one respect or another from the language as set down in this manual, or else adds particular details that reach past what the standard Python documentation discusses. Do consult the documentation tied to your specific build to find out whatever further knowledge applies to the one you happen to run.

[Subject index](INDEX.md) · [Owning language section](introduction.md) · [Previous source section](introduction.md) · [Following source section](notation.md)
