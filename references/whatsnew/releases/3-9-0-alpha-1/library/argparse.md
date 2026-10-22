# Python 3.9.0 alpha 1 / library / argparse

[bpo-26967](https://bugs.python.org/issue?@action=redirect&bpo=26967): With `allow_abbrev=False` set, an [`ArgumentParser`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser) no longer breaks the grouping of short flags such as `-vv`; as documented, it only switches off long-flag abbreviation. Zac Hatfield-Dodds wrote the patch.

[bpo-29553](https://bugs.python.org/issue?@action=redirect&bpo=29553): Repaired [`argparse.ArgumentParser.format_usage()`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser.format_usage) where mutually exclusive groups were involved. Andrew Nester wrote the patch.

[bpo-8538](https://bugs.python.org/issue?@action=redirect&bpo=8538): argparse gained boolean actions such as `--foo` and `--no-foo`. Rémi Lapeyre supplied the patch.

[bpo-37785](https://bugs.python.org/issue?@action=redirect&bpo=37785): Fixed the xgettext warnings within [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse).

[bpo-38438](https://bugs.python.org/issue?@action=redirect&bpo=38438): Streamlined the [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) usage message produced for `nargs="*"`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
