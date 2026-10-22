# Python 3.5.0 alpha 4 / tools demos / functions and types

[bpo-23944](https://bugs.python.org/issue?@action=redirect&bpo=23944): Long impl prototypes are now wrapped by Argument Clinic at column 78.

[bpo-20586](https://bugs.python.org/issue?@action=redirect&bpo=20586): Argument Clinic now guarantees signatures for functions lacking docstrings.

[bpo-23500](https://bugs.python.org/issue?@action=redirect&bpo=23500): Argument Clinic is now cleverer when producing the "#ifndef" (empty) definition for the methoddef macro: it gets generated a single time even when Argument Clinic handles one symbol repeatedly, and it lands at the close of all processing instead of right after the first use.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
