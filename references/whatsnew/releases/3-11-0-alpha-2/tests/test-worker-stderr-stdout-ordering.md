# Python 3.11.0 alpha 2 / tests / libregrtest launches worker stderr flows into stdout message ordering

[bpo-45410](https://bugs.python.org/issue?@action=redirect&bpo=45410): When libregrtest launches a worker, its stderr now flows into stdout so message ordering is preserved. A single pipe carries both stdout and stderr rather than two separate pipes. Earlier, the out-of-order messages complicated reading buildbot logs. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
