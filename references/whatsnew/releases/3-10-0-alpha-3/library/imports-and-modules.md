# Python 3.10.0 alpha 3 / library / imports and modules

[bpo-1635741](https://bugs.python.org/issue?@action=redirect&bpo=1635741): Convert _sre module types to heap types (PEP 384). Erlend E. Aasland supplied the patch.

[bpo-41713](https://bugs.python.org/issue?@action=redirect&bpo=41713): Move the `_signal` extension module over to the multi-phase initialization API ([**PEP 489**](https://peps.python.org/pep-0489/)). Victor Stinner and Mohamed Koubaa contributed the patch.

[bpo-42333](https://bugs.python.org/issue?@action=redirect&bpo=42333): Port _ssl extension module to heap types.

[bpo-1635741](https://bugs.python.org/issue?@action=redirect&bpo=1635741): Move the `_warnings` extension module over to the multi-phase initialization API ([**PEP 489**](https://peps.python.org/pep-0489/)). Victor Stinner contributed the patch.

[bpo-42299](https://bugs.python.org/issue?@action=redirect&bpo=42299): Dropped the `formatter` module, deprecated back in Python 3.4. The module is fairly obsolete, rarely used, and untested. Removal was first slated for Python 3.6, yet such removals were held off until past Python 2.7 EOL. Anyone still relying on it should copy whatever classes they need into their own code. Donghee Na and and Terry J. Reedy wrote the patch.

[bpo-31904](https://bugs.python.org/issue?@action=redirect&bpo=31904): Support signal module on VxWorks.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
