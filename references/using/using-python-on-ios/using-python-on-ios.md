# 7. Using Python on iOS

## 7. Using Python on iOS

### 7. Using Python on iOS

Authors:

Russell Keith-Magee (2024-03)

The way Python works on iOS differs from how it behaves on desktop systems. With a desktop OS, Python typically lands as a shared system resource available to everyone using the machine. People then engage with Python by launching a **python** executable and typing commands into an interactive prompt, or alternatively by executing a Python script.

iOS has no notion of installing something as a shared system resource. Here, the sole unit through which software ships is an "app". Likewise, no console exists where a **python** executable could be launched or a Python REPL engaged.

Consequently, the one path to using Python on iOS runs through embedded mode — meaning you author a native iOS application, embed a Python interpreter via `libPython`, and call into Python code through the [Python embedding API](https://docs.python.org/3.14/extending/embedding.html#embedding). The complete Python interpreter, its standard library, and every line of your Python code then get bundled into one standalone package suitable for distribution through the iOS App Store.

Should this be your first attempt at building an iOS app with Python, frameworks like [BeeWare](https://beeware.org) and [Kivy](https://kivy.org) deliver a far friendlier on-ramp. They handle the intricacies of standing up an iOS project, leaving you free to focus solely on the Python code.

[Subject index](INDEX.md) · [Previous source section](../python-setup-and-usage/python-setup-and-usage.md) · [Following source section](ios-version-compatibility.md)
