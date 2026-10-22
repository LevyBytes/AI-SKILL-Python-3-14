# Python 3.8.0 alpha 1 / library / urllib robotparser

[bpo-28612](https://bugs.python.org/issue?@action=redirect&bpo=28612): Site Maps support arrived for urllib's `RobotFileParser`, exposed through [`RobotFileParser.site_maps()`](https://docs.python.org/3.14/library/urllib.robotparser.html#urllib.robotparser.RobotFileParser.site_maps). Patch by Lady Red, building on a patch from Peter Wirtz.

[bpo-32861](https://bugs.python.org/issue?@action=redirect&bpo=32861): The urllib.robotparser's `__str__` representation now carries wildcard entries plus the "Crawl-delay" and "Request-rate" fields. It also drops the extra newlines that were getting tacked onto the string's end. Patch by Michael Lazar.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
