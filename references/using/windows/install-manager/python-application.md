# 4.2.1. Python application

### 4.2.1. Python application

Users of an application written in Python need not necessarily realize that it is. In such a case the embedded distribution can bundle a private copy of Python into an install package. How transparent it ought to be (or, put differently, how professional it should look) leaves you two choices.

Going with a specialized executable as a launcher takes some coding but delivers the most seamless experience for users. With a tailored launcher there is nothing visibly signaling that the program runs on Python: icons can be customized, company and version details can be set, and file associations behave correctly. Typically a custom launcher need only call `Py_Main` with a hard-coded command line.

The easier route is to ship a batch file or a generated shortcut that directly invokes `python.exe` or `pythonw.exe` with the necessary command-line arguments. With this, the application will look like Python rather than its real name, and users may struggle to tell it apart from other running Python processes or file associations.

Under that latter route, packages ought to be installed as directories beside the Python executable so they sit on the path. With the specialized launcher, packages may live elsewhere, since there is a chance to declare the search path before the application starts.

[Subject index](INDEX.md) · [Previous source section](the-embeddable-package.md) · [Following source section](embedding-python.md)
