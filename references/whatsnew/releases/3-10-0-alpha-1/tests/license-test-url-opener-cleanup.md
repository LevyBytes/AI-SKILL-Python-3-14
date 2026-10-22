# Python 3.10.0 alpha 1 / tests / license test url opener cleanup

[bpo-41939](https://bugs.python.org/issue?@action=redirect&bpo=41939): Repair test_site.test_license_exists_at_url() by calling `urllib.request.urlcleanup()` to reset the global `urllib.request._opener`. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
