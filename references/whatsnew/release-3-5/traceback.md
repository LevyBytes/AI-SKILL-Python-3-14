# What’s New In Python 3.5 / traceback - traceback

### traceback

To walk frame and [traceback objects](https://docs.python.org/3.14/reference/datamodel.html#traceback-objects) with ease, there are new [`walk_stack()`](https://docs.python.org/3.14/library/traceback.html#traceback.walk_stack) and [`walk_tb()`](https://docs.python.org/3.14/library/traceback.html#traceback.walk_tb) functions. Robert Collins contributed this (see [bpo-17911](https://bugs.python.org/issue?@action=redirect&bpo=17911)).

Several new lightweight classes have arrived: [`TracebackException`](https://docs.python.org/3.14/library/traceback.html#traceback.TracebackException), [`StackSummary`](https://docs.python.org/3.14/library/traceback.html#traceback.StackSummary), and [`FrameSummary`](https://docs.python.org/3.14/library/traceback.html#traceback.FrameSummary). Robert Collins added these (see [bpo-17911](https://bugs.python.org/issue?@action=redirect&bpo=17911)).

Negative values for the *limit* argument are now handled by the [`print_tb()`](https://docs.python.org/3.14/library/traceback.html#traceback.print_tb) and [`print_stack()`](https://docs.python.org/3.14/library/traceback.html#traceback.print_stack) functions alike. Dmitry Kazakov landed this (see [bpo-22619](https://bugs.python.org/issue?@action=redirect&bpo=22619)).

[Subject index](INDEX.md) · [Previous source section](tkinter.md) · [Next source section](types.md) · [Release/subject declaration](summary-release-highlights.md)
