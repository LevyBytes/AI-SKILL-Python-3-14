# Mobile platforms

### Mobile platforms

For the most part, Android and iOS count as POSIX operating systems. The way File I/O, socket handling, and threading operate matches any POSIX operating system. That said, a few significant distinctions exist:

- On mobile platforms Python runs only in “embedded” mode. No Python REPL exists, and you cannot run standalone executables like **python** or **pip**. Getting Python code into a mobile app means relying on the [Python embedding API](https://docs.python.org/3.14/extending/embedding.html#embedding). Fuller coverage appears in [Using Python on Android](https://docs.python.org/3.14/using/android.html#using-android) and [Using Python on iOS](https://docs.python.org/3.14/using/ios.html#using-ios).

- Subprocesses:

  - Under Android, spawning subprocesses can be done yet is [officially unsupported](https://issuetracker.google.com/issues/128554619#comment4). Notably, no portion of the System V IPC API exists on Android, which leaves [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) unavailable.

  - Subprocessing, multiprocessing, and inter-process communication of every kind are off-limits to an iOS app. Should an iOS app try to spawn a subprocess, whichever process is doing the spawning will either freeze or crash. An iOS app sees nothing of the other running applications, and it has no way to talk to other running applications apart from the purpose-built iOS-specific APIs.

- Modifying system resources (the system clock, for example) is something mobile apps can do only to a limited degree. Such resources tend to be *readable*, though efforts to change them will generally fail.

- Console input and output:

  - Under Android, the native `stdout` and `stderr` go nowhere, so Python sets up its own streams that route messages into the system log. They show up beneath the tags `python.stdout` and `python.stderr` respectively.

  - The notion of console output is limited in iOS apps. Although `stdout` and `stderr` *exist*, and whatever gets written to `stdout` and `stderr` shows up in logs while running under Xcode, that content *won’t* land in the system log. Were a user who installed your app to hand over their app logs for diagnostics, nothing written to `stdout` or `stderr` would be in them.

  - There is no usable `stdin` whatsoever for mobile apps. Apps can bring up an on-screen keyboard, but that is a software feature rather than anything wired to `stdin`.

Owing to this, Python modules that drive console manipulation (for example [`curses`](https://docs.python.org/3.14/library/curses.html#module-curses) and [`readline`](https://docs.python.org/3.14/library/readline.html#module-readline)) cannot be used on mobile platforms.

[Subject index](INDEX.md) · [Previous](webassembly-platforms.md)
