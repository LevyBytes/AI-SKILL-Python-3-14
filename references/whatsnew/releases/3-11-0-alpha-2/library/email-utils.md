# Python 3.11.0 alpha 2 / library / email utils

[bpo-45239](https://bugs.python.org/issue?@action=redirect&bpo=45239): Repaired [`email.utils.parsedate_tz()`](https://docs.python.org/3.14/library/email.utils.html#email.utils.parsedate_tz) crashing with [`UnboundLocalError`](https://docs.python.org/3.14/library/exceptions.html#UnboundLocalError) on some malformed input rather than handing back `None`. Ben Hoyt wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
