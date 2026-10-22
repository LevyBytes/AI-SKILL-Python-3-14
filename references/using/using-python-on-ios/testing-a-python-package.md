# 7.2.3. Testing a Python package

### 7.2.3. Testing a Python package

Within the CPython source tree sits [a testbed project](https://github.com/python/cpython/tree/3.14/Apple/iOS/testbed) used to run the CPython test suite against the iOS simulator. You can repurpose this same testbed to run your own Python library's test suite on iOS.

Once you've built or acquired an iOS XCFramework (consult [Apple/iOS/README.md](https://github.com/python/cpython/tree/3.14/Apple/iOS/README.md) for the specifics), make a clone of the Python iOS testbed project. Where you relied on the `Apple` build script to produce the XCframework, run:

```bash
$ python cross-build/iOS/testbed clone --app <path/to/module1> --app <path/to/module2> app-testbed

```

Alternatively, if you've supplied your own XCframework, run:

```bash
$ python Apple/testbed clone --platform iOS --framework <path/to/Python.xcframework> --app <path/to/module1> --app <path/to/module2> app-testbed

```

Every folder named through the `--app` flag gets copied into the cloned testbed project. That produces the resulting testbed inside the `app-testbed` folder. Here, `module1` and `module2` would be modules you can import at runtime. Where your project pulls in extra dependencies, install them under the `app-testbed/Testbed/app_packages` folder (with `pip install --target app-testbed/Testbed/app_packages` or something comparable).

From there, the `app-testbed` folder lets you run your app's test suite. As an example, when `module1.tests` is the entry point into your test suite, you could run:

```bash
$ python app-testbed run -- module1.tests

```

That mirrors running `python -m module1.tests` against a desktop Python build. Whatever arguments come after the `--` reach the testbed exactly as though they were arguments handed to `python -m` on a desktop machine.

Opening the testbed project in Xcode is likewise possible by running:

```bash
$ open app-testbed/iOSTestbed.xcodeproj

```

That gives you the entire Xcode toolset for debugging purposes.

The test plan is where the arguments that drive the test suite are defined. To adjust the test plan, click the test plan node within the project tree (it ought to be the root node's first child), then open the “Configurations” tab. Change the “Arguments Passed On Launch” value to alter the testing arguments.

Beyond that, the test plan switches off parallel testing and calls for the `Testbed.lldbinit` file to supply the debugger's configuration. By default, the debugger setup turns off automatic breakpoints on the `SIGINT`, `SIGUSR1`, `SIGUSR2`, and `SIGXFSZ` signals.

[Subject index](INDEX.md) · [Previous source section](ios-library-installation-and-interpreter-configuration.md) · [Following source section](app-store-compliance.md)
