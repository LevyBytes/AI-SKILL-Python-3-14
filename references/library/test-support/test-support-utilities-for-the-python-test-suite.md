# test.support — `test.support` — Utilities for the Python test suite

@test.support.requires_lzma

Decorator that skips tests when [`lzma`](https://docs.python.org/3.14/library/lzma.html#module-lzma) is absent.

 @test.support.requires_resource(*resource*)

Decorator for skipping tests if *resource* is not available.

 @test.support.requires_docstrings

Decorator for only running the test if `HAVE_DOCSTRINGS`.

 @test.support.requires_limited_api

[Subject index](INDEX.md) · [Previous](test-warning-and-certificate-validation-helpers.md) · [Owning module, declaration or section: test.support](test-support-testfailed-to-test-support-internet-timeout.md) · [Required continuation of the source contract](musl-detection-and-unraisable-exception-helpers.md)
