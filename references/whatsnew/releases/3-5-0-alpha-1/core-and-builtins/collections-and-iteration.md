# Python 3.5.0 alpha 1 / core and builtins / collections and iteration

[bpo-21052](https://bugs.python.org/issue?@action=redirect&bpo=21052): Refrain from raising ImportWarning whenever sys.path_hooks or sys.meta_path get set to None.

[bpo-21205](https://bugs.python.org/issue?@action=redirect&bpo=21205): Give generators a new `__qualname__` attribute holding the qualified name, then use it in a generator's representation (`repr(gen)`). A generator's default name (the `__name__` attribute) is now sourced from the function rather than the code. Reach for `gen.gi_code.co_name` to obtain the code's name.

[bpo-21435](https://bugs.python.org/issue?@action=redirect&bpo=21435): On rare occasions, while finalizers ran on objects sitting in cyclic trash, a bad pointer dereference might happen owing to a subtle flaw within the internal iteration logic.

[bpo-20637](https://bugs.python.org/issue?@action=redirect&bpo=20637): Key-sharing now extends to the instance dictionaries of subclasses too. Peter Ingebretson supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
