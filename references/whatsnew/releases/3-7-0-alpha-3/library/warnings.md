# Python 3.7.0 alpha 3 / library / warnings

[bpo-27535](https://bugs.python.org/issue?@action=redirect&bpo=27535): The warnings module no longer leaks memory through the hidden warnings registry under the "ignore" action of warnings filters. For that "ignore" action, the warn_explicit() function no longer inserts the warning key into the registry.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
