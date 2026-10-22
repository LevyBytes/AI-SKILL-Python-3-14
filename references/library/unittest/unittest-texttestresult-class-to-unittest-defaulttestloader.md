# unittest: `unittest.TextTestResult`, `unittest.defaultTestLoader`

*class *unittest.TextTestResult(*stream*, *descriptions*, *verbosity*, ***, *durations=None*)

A worked-out `TestResult` implementation that the `TextTestRunner` relies on. Any subclass ought to take `**kwargs` so it stays compatible whenever the interface shifts.

Added in version 3.2.

Changed in version 3.12: Added the *durations* keyword parameter.

 unittest.defaultTestLoader

A shared instance of the `TestLoader` class. When you have no need to tailor the `TestLoader`, reach for this instance rather than spinning up fresh ones over and over.

[Subject index](INDEX.md) · [Previous](test-result-unexpected-success-and-duration.md) · [Continue](unittest-texttestrunner-class-to-unittest-main.md) · [Owning module, declaration or section: Loading and running tests](unittest-testloader-class.md)
