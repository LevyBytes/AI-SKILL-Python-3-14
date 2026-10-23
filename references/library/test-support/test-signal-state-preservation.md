# test.support`test.support` - Utilities for the Python test suite

*class *test.support.SaveSignals

A class for preserving and reinstating signal handlers that the Python signal handler has registered.

 save(*self*)

Records the signal handlers into a dictionary that maps signal numbers to their present signal handler.

 restore(*self*)

Applies the signal numbers from the `save()` dictionary back to the handler that was saved.

[Subject index](INDEX.md) · [Previous](test-support-suppresscrashreport-class.md) · [Continue](test-matcher-class-and-value-matching.md) · [Owning module, declaration or section: test.support](test-support-testfailed-to-test-support-internet-timeout.md)
