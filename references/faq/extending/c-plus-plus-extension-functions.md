# Can I create my own functions in C++?

### Can I create my own functions in C++?

Yes: lean on the C compatibility facilities that C++ provides. Wrap the Python include files in `extern "C" { ... }`, and prefix `extern "C"` to every function the Python interpreter is meant to invoke. Steer clear of global or static C++ objects that carry constructors.

[Subject index](INDEX.md)
