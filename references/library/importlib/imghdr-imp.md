# Imghdr, Imp

# Imghdr, Imp

## Overview

Topics here: imghdr — Determine the type of an image; imp — Access the import internals.

## imghdr — Determine the type of an image

### `imghdr` — Determine the type of an image

Marked deprecated as of version 3.11; taken out in version 3.13.

You will no longer find this module bundled with the Python standard library. Having first been deprecated back in Python 3.11, it was eventually [removed in Python 3.13](https://docs.python.org/3.14/whatsnew/3.13.html#whatsnew313-pep594). That call traces back to [**PEP 594**](https://peps.python.org/pep-0594/).

If you need a stand-in, several third-party offerings on PyPI fit the bill: [filetype](https://pypi.org/project/filetype/), [puremagic](https://pypi.org/project/puremagic/), and [python-magic](https://pypi.org/project/python-magic/). Bear in mind that none of these falls under the upkeep or backing of the Python core team.

If you still need the `imghdr` module, the final release to ship it was [Python 3.12](https://docs.python.org/3.12/library/imghdr.html).

## imp — Access the import internals

### `imp` — Access the import internals

Flagged as deprecated starting with version 3.4; dropped at version 3.12.

This module has dropped out of the Python standard library for good. Its deprecation reached back to Python 3.4, and the [removal in Python 3.12](https://docs.python.org/3.14/whatsnew/3.12.html#whatsnew312-removed-imp) followed from that.

For anyone porting code away from `imp` toward [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib), the [removal notice](https://docs.python.org/3.14/whatsnew/3.12.html#whatsnew312-removed-imp) lays out how to make that switch.

For the `imp` module, the closing release to include it was [Python 3.11](https://docs.python.org/3.11/library/imp.html).

[Subject index](INDEX.md)
