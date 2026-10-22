# Python 3.5.0 beta 1 / library / functions and types

[bpo-24298](https://bugs.python.org/issue?@action=redirect&bpo=24298): Correct inspect.signature() so it properly unwraps the wrappers placed around bound methods.

[bpo-23086](https://bugs.python.org/issue?@action=redirect&bpo=23086): The index() mixin of the collections.abc.Sequence() abstract base class gained *start* and *stop* parameters. Devin Jeanpierre supplied the patch.

[bpo-24257](https://bugs.python.org/issue?@action=redirect&bpo=24257): Corrected a segmentation fault in the sqlite3.Row constructor when a faked cursor type is used.

[bpo-15836](https://bugs.python.org/issue?@action=redirect&bpo=15836): assertRaises(), assertRaisesRegex(), assertWarns() and assertWarnsRegex() assertments now examine the type of the first argument so a likely user error is caught. Daniel Wagner-Hall's patch was the basis.

[bpo-9858](https://bugs.python.org/issue?@action=redirect&bpo=9858): Supply the missing method stubs on _io.RawIOBase. Laura Rupprecht supplied the patch.

[bpo-13866](https://bugs.python.org/issue?@action=redirect&bpo=13866): A *quote_via* argument was added to urllib.parse.urlencode.

[bpo-22486](https://bugs.python.org/issue?@action=redirect&bpo=22486): The math.gcd() function was added. The fractions.gcd() function is now deprecated. Mark Dickinson's patch was the basis.

[bpo-23796](https://bugs.python.org/issue?@action=redirect&bpo=23796): When called on a closed object, the peek and read1 methods of BufferedReader now raise ValueError. John Hergenroeder supplied the patch.

[bpo-20274](https://bugs.python.org/issue?@action=redirect&bpo=20274): Strip the ignored and faulty "kwargs" parameters off three METH_VARARGS methods on _sqlite.Connection.

[bpo-24190](https://bugs.python.org/issue?@action=redirect&bpo=24190): Add the inspect.BoundArgument.apply_defaults() method. Yury Selivanov contributed this.

[bpo-20691](https://bugs.python.org/issue?@action=redirect&bpo=20691): Give inspect.Signature.from_callable() and inspect.signature() a "follow_wrapped" argument. Yury Selivanov contributed this.

[bpo-23898](https://bugs.python.org/issue?@action=redirect&bpo=23898): Repair inspect.classify_class_attrs() so attributes with overloaded __eq__ and __bool__ are handled. Mike Bayer supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
