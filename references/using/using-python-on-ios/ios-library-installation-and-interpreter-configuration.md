# iOS library installation build phase and interpreter configuration

7.

Add a build step that handles the Python standard library along with your own Python binary dependencies. Within the “Build Phases” tab, insert a fresh “Run Script” build step *before* the “Embed Frameworks” step yet *after* the “Copy Bundle Resources” step. Title the step “Process Python libraries”, turn off the “Based on dependency analysis” checkbox, and put the following into the script body:

```bash
set -e
source $PROJECT_DIR/Python.xcframework/build/build_utils.sh
install_python Python.xcframework app

```

Should your XCframework reside somewhere other than your project's root, adjust the path given as the first argument.

8.

Add Objective C code to spin up and drive a Python interpreter in embedded mode. Take care that:

  - UTF-8 mode ([`PyPreConfig.utf8_mode`](https://docs.python.org/3.14/c-api/init_config.html#c.PyPreConfig.utf8_mode)) is *enabled*;

  - Buffered stdio ([`PyConfig.buffered_stdio`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.buffered_stdio)) is *disabled*;

  - Writing bytecode ([`PyConfig.write_bytecode`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.write_bytecode)) is *disabled*;

  - Signal handlers ([`PyConfig.install_signal_handlers`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.install_signal_handlers)) are *enabled*;

  - System logging ([`PyConfig.use_system_logger`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.use_system_logger)) is *enabled* (though optional, it comes on by default and is highly advisable);

  - the interpreter's [`PYTHONHOME`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONHOME) is set so it targets the `python` subfolder within your app’s bundle; and

  - The [`PYTHONPATH`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONPATH) for the interpreter includes:

    - the `python/lib/python3.X` subfolder of your app’s bundle,

    - the `python/lib/python3.X/lib-dynload` subfolder of your app’s bundle, and

    - the `app` subfolder of your app’s bundle

You can find your app's bundle location through `[[NSBundle mainBundle] resourcePath]`.

These instructions, at steps 7 and 8, presume one folder of purely Python application code goes by the name `app`. Where your app carries third-party binary modules, a few more steps come into play:

- Confirm that any folders holding third-party binaries are either tied to the app target or get copied explicitly during step 7. Step 7 ought to also strip out any binaries unsuited to the platform a given build targets (that is, remove device binaries whenever you build an app aimed at the simulator).

- When you keep third-party packages in a distinct folder, append that folder to the end of the `install_python` call in step 7, and fold it into the [`PYTHONPATH`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONPATH) setup in step 8.

- Whenever folders that hold third-party packages will include `.pth` files, register that folder as a *site directory* (via [`site.addsitedir()`](https://docs.python.org/3.14/library/site.html#site.addsitedir)) instead of tacking it onto [`PYTHONPATH`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONPATH) or [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) directly.

[Subject index](INDEX.md) · [Previous source section](adding-python-to-an-ios-project.md) · [Following source section](testing-a-python-package.md) · [iOS prerequisites](tools-for-building-ios-apps.md) · [Xcode project setup](adding-python-to-an-ios-project.md)
