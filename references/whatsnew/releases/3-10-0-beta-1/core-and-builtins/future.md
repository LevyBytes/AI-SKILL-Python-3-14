# Python 3.10.0 beta 1 / core and builtins / future

[bpo-42737](https://bugs.python.org/issue?@action=redirect&bpo=42737): With `from __future__ import annotations` in effect, annotations on complex targets (anything other than plain names) produce no runtime consequences anymore.

[bpo-38605](https://bugs.python.org/issue?@action=redirect&bpo=38605): The change that made `from __future__ import annotations` the default has been reverted. This tracks the Steering Council's call to defer PEP 563 changes to Python 3.11 at the earliest. The original announcement explaining that decision lives here: [https://mail.python.org/archives/list/python-dev@python.org/thread/CLVXXPQ2T2LQ5MP2Y53VVQFCXYWQJHKZ/](https://mail.python.org/archives/list/python-dev@python.org/thread/CLVXXPQ2T2LQ5MP2Y53VVQFCXYWQJHKZ/). Pablo Galindo wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
