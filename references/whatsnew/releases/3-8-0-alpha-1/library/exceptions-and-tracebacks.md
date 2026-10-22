# Python 3.8.0 alpha 1 / library / exceptions and tracebacks

[bpo-26502](https://bugs.python.org/issue?@action=redirect&bpo=26502): Added a `traceback.FrameSummary.__len__()` method so that compatibility with the legacy tuple API is retained.

[bpo-8525](https://bugs.python.org/issue?@action=redirect&bpo=8525): Calling help() against a type now lists builtin subclasses. The main goal here is to surface more precise exception subclasses.

Patch by Sanyam Khurana.

[bpo-35717](https://bugs.python.org/issue?@action=redirect&bpo=35717): Resolved a KeyError exception that surfaced when combining enums with compile. Patch contributed by Rémi Lapeyre.

[bpo-33034](https://bugs.python.org/issue?@action=redirect&bpo=33034): Supplying a clear error message when the port property gets cast to anything other than an integer value through `urlparse()` and `urlsplit()`. Patch by Matt Eaton.

[bpo-30167](https://bugs.python.org/issue?@action=redirect&bpo=30167): Stopped a site.main() exception from firing when PYTHONSTARTUP is set. Patch by Steve Weber.

[bpo-33805](https://bugs.python.org/issue?@action=redirect&bpo=33805): Made the error message from dataclasses.replace() clearer when an InitVar is left unspecified

[bpo-33197](https://bugs.python.org/issue?@action=redirect&bpo=33197): Refresh the error message produced when building invalid inspect.Parameters Patch by Donghee Na.

[bpo-30249](https://bugs.python.org/issue?@action=redirect&bpo=30249): Sharpen struct.unpack_from() exception messages covering trouble with the buffer size and offset.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
