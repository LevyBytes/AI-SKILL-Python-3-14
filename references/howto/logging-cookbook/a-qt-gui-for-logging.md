# A Qt GUI for logging

### A Qt GUI for logging

One question that surfaces now and then concerns logging into a GUI application. The [Qt](https://www.qt.io/) framework is a widely used cross-platform UI toolkit, accessible from Python through the [PySide2](https://pypi.org/project/PySide2/) or [PyQt5](https://pypi.org/project/PyQt5/) libraries.

The example that follows demonstrates logging to a Qt GUI. It introduces a small `QtHandler` class that accepts a callable, which ought to be a slot running in the main thread to carry out GUI updates. A worker thread is set up as well, illustrating how you can log to the GUI both from the UI directly (through a button for manual logging) and from a background worker thread (which here merely logs messages at random levels separated by random brief pauses).

That worker thread relies on Qt's `QThread` class instead of the [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module, since in some situations `QThread` is required and it integrates more smoothly with the rest of `Qt`. The code ought to run on current releases of `PySide6`, `PyQt6`, `PySide2` or `PyQt5`, and you should be able to port the approach to older Qt versions. Consult the comments within the code snippet for fuller details.

[Subject index](INDEX.md) · [Following source continuation](qt-logging-imports-signals-handler-and-thread-names.md) · [Previous source context](cli-logging-output-at-default-debug-and-warning-levels.md)
