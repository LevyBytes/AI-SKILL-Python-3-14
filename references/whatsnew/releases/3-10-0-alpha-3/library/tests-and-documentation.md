# Python 3.10.0 alpha 3 / library / tests and documentation

[bpo-5054](https://bugs.python.org/issue?@action=redirect&bpo=5054): CGIHTTPRequestHandler.run_cgi() parsed HTTP_ACCEPT incorrectly. The dedicated getallmatchingheaders is swapped for the general get_all method, with matching tests added.

Martin Panter wrote the original patch, which Senthil Kumaran then revised.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
