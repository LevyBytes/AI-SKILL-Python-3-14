# --check-hash-based-pycs default/always/never

--check-hash-based-pycs default|always|never

Govern how hash-based `.pyc` files are validated. See [Cached bytecode invalidation](https://docs.python.org/3.14/reference/import.html#pyc-invalidation). With `default`, both checked and unchecked hash-based bytecode cache files are validated following their usual semantics. With `always`, every hash-based `.pyc` file — checked or not — is validated against the source file it corresponds to. With `never`, hash-based `.pyc` files are skipped for validation against their corresponding source files.

This option leaves the semantics of timestamp-based `.pyc` files untouched.

[Subject index](INDEX.md) · [Previous source section](disable-bytecode-files.md) · [Following source section](parser-debugging.md)
