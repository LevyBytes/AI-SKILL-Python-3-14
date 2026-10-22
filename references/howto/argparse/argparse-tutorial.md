# Argparse Tutorial

### Argparse Tutorial

author:

Tshepang Mbambo

Think of this walkthrough as an easygoing first look at [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse), the command-line parsing module that the Python standard library suggests you reach for.

Note

Two other standard-library modules also deal with command-line parameter handling: the lower level [`optparse`](https://docs.python.org/3.14/library/optparse.html#module-optparse) module (which can take more setup code for a given application, yet lets an application ask for behaviors `argparse` doesn't offer), plus the very low level [`getopt`](https://docs.python.org/3.14/library/getopt.html#module-getopt) (which is meant to mirror the `getopt()` family of functions that C programmers have access to). Although this guide doesn't cover either module on its own, a lot of the central ideas in `argparse` were first born in `optparse`, which means parts of this tutorial carry over to `optparse` users too.

[Subject index](INDEX.md) · [Following source context](concepts.md)
