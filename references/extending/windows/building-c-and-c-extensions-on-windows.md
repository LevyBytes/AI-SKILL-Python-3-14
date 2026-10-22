# Building C and C++ Extensions on Windows

# Windows

### 5. Building C and C++ Extensions on Windows

This chapter gives a quick walkthrough of building a Windows extension module for Python with Microsoft Visual C++, then fills in deeper background on the mechanics. That background serves two audiences: the Windows developer picking up Python extension construction, and the Unix developer who wants their software to compile cleanly under both Unix and Windows.

Rather than the technique laid out here, those writing modules are urged to lean on the distutils route when constructing their extension modules. Either way, the C compiler that produced your Python build is still required — on Windows that is normally Microsoft Visual C++.

Note

Several filenames cited in this chapter bake a Python version number into themselves. Throughout, that embedded version is written as `XY`; when you apply it, `'X'` stands for the major version number and `'Y'` for the minor version number of whichever Python release you happen to be using. To illustrate, with Python 2.2.1 the `XY` placeholder resolves to `22`.

[Subject index](INDEX.md) · [Next source section](a-cookbook-approach.md)
