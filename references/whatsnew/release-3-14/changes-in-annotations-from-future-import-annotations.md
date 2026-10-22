# What's new in Python 3.14 / Changes in annotations (**PEP 649** and **PEP 749**) / `from __future__ import annotations`

#### `from __future__ import annotations`

Back in Python 3.7, the [**PEP 563**](https://peps.python.org/pep-0563/) proposal added the `from __future__ import annotations` [future statement](https://docs.python.org/3.14/reference/simple_stmts.html#future), a directive that converts every annotation into a string.

That directive has since been marked deprecated, and a later Python release is slated to drop it. The drop is held off until Python 3.13 hits its end of life in 2029, since 3.13 stands as the final release that lacks deferred annotation evaluation.

Under Python 3.14, programs relying on `from __future__ import annotations` continue to behave exactly as before.

[Subject index](INDEX.md) · [Previous source section](changes-in-annotations-related-changes.md) · [Next source section](porting-to-python-3-14-changes-in-the-c-api.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](changes-in-annotations.md)
