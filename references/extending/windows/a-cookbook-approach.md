# A Cookbook Approach

### 5.1. A Cookbook Approach

Windows, like Unix, offers a pair of routes for putting together extension modules: hand the build over to the `setuptools` package, or drive everything by hand. For the majority of extensions the setuptools route does the job nicely, and you'll find guidance on wielding `setuptools` to compile and package extension modules under [Building C and C++ Extensions with setuptools](https://docs.python.org/3.14/extending/building.html#setuptools-index). Should the manual route turn out to be genuinely necessary, a worthwhile example to pore over is the project file belonging to the [winsound](https://github.com/python/cpython/tree/3.14/PCbuild/winsound.vcxproj) standard library module.

[Subject index](INDEX.md) · [Previous source section](building-c-and-c-extensions-on-windows.md) · [Next source section](differences-between-unix-and-windows-py-no-link-lib.md)
