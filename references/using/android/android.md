# Android

# Android

### 6. Using Python on Android

Running Python on Android differs sharply from running it on a desktop. On the desktop, Python typically lands as a system-wide resource that anyone with an account on the machine can use. From there, people work with Python by launching a **python** executable and typing commands at an interactive prompt, or else by executing a Python script.

Android has no notion of installing something as a shared system resource. Its sole means of distributing software is the “app.” Nor is there a console in which you might launch a **python** executable or chat with a Python REPL.

Consequently, embedded mode is your only route to Python on Android — meaning you author a native Android application, fold a Python interpreter into it by way of `libpython`, and run Python code through the [Python embedding API](https://docs.python.org/3.14/extending/embedding.html#embedding). The entire interpreter, the standard library, and every line of your Python code then ship inside your app, for that app alone to use.

On Android the Python standard library comes with a few significant gaps and constraints. Consult the [API availability guide](https://docs.python.org/3.14/library/intro.html#mobile-availability) for the specifics.

### 6.1. Adding Python to an Android app

For a far smoother time, the majority of app developers ought to reach for one of these tools:

- [Briefcase](https://briefcase.beeware.org), from the BeeWare project

- [Buildozer](https://buildozer.readthedocs.io), from the Kivy project

- [Chaquopy](https://chaquo.com/chaquopy)

- [pyqtdeploy](https://www.riverbankcomputing.com/static/Docs/pyqtdeploy/)

- [Termux](https://termux.dev/en/)

Should you be certain you'd rather handle every bit of this by hand, keep reading. The [testbed app](https://github.com/python/cpython/tree/3.14/Android/testbed) can serve as your reference, and each of the steps that follow links to the file it concerns.

- To begin, obtain a Python build targeting Android:

  - Simplest of all is grabbing an Android release straight from [python.org](https://www.python.org/downloads/android/). You'll find the `prefix` directory referred to further down sitting at the package's top level.

  - Alternatively, to compile it on your own, work through what's laid out in [Android/README.md](https://github.com/python/cpython/tree/3.14/Android/README.md). That process puts the `prefix` directory under `cross-build/*HOST*`.

- Insert code into your [build.gradle](https://github.com/python/cpython/tree/3.14/Android/testbed/app/build.gradle.kts) file that brings the items below into your project. Everything other than your own Python code can be pulled from `prefix/lib`:

  - In your JNI libraries:

    - `libpython*.*.so`

    - `lib*_python.so` (outside libraries, OpenSSL being one example)

  - In your assets:

    - `python*.*` (the Python standard library)

    - `python*.*/site-packages` (your own Python code)

- Put code in your app that will [extract the assets to the filesystem](https://github.com/python/cpython/tree/3.14/Android/testbed/app/src/main/java/org/python/testbed/MainActivity.kt).

- Add code to your app that will [start Python in embedded mode](https://github.com/python/cpython/tree/3.14/Android/testbed/app/src/main/c/main_activity.c). That piece has to be C code reached through JNI.

### 6.2. Building a Python package for Android

You can produce Android wheels for Python packages and publish them to PyPI. The tool to reach for here is [cibuildwheel](https://cibuildwheel.pypa.io/en/stable/platforms/#android); it handles every detail of standing up a cross-compilation environment, assembling the wheel, and putting it through tests on an emulator.

[Subject index](INDEX.md)
