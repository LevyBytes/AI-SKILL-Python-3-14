# Beyond Very High Level Embedding: An overview

### 1.2. Beyond Very High Level Embedding: An overview

With the high level interface you can run arbitrary chunks of Python code out of your application, yet passing data values back and forth is awkward, to put it mildly. Should you need that, the lower level calls are the way to go. Paying the price of writing extra C code buys you the ability to accomplish nearly anything.

Worth noting is that extending and embedding Python amount to much the same undertaking, their aims aside. The bulk of what the earlier chapters covered still holds. As a demonstration, think about what the extension code traveling from Python to C is actually doing:

1.

Translate data values out of Python and into C,

2.

Make a function call to a C routine that uses those translated values, and

3.

Translate the call's resulting data values back from C into Python.

While embedding Python, the interface code instead carries out:

1.

Translate data values out of C and into Python,

2.

Make a function call to a Python interface routine that uses those translated values, and

3.

Translate the call's resulting data values back from Python into C.

As you can tell, the data conversion steps merely trade places to suit the opposite direction of the cross-language transfer. What alone differs is the routine you invoke between the two conversions. Extending has you call a C routine; embedding has you call a Python routine.

How to convert data between Python and C in either direction is not something this chapter takes up. It likewise takes for granted that you grasp the correct handling of references and of errors. Because none of that differs from extending the interpreter, the earlier chapters supply whatever information you need.

[Subject index](INDEX.md) · [Previous source section](very-high-level-embedding-and-pyrun-simplefile.md) · [Next source section](pure-embedding-and-py-finalizeex.md)
