# Python 3.8.0 alpha 4 / library / functions and types

[bpo-25451](https://bugs.python.org/issue?@action=redirect&bpo=25451): Bring transparency methods to `tkinter.PhotoImage`. Zackery Spytz authored the patch.

[bpo-36492](https://bugs.python.org/issue?@action=redirect&bpo=36492): It is now deprecated to hand mandatory arguments such as *func* as keyword arguments to functions that are meant to take arbitrary keyword arguments and relay them onward. Arbitrary keyword arguments, even ones named ?self? and ?func?, may now flow through these functions as long as the mandatory ones arrive positionally.

[bpo-36227](https://bugs.python.org/issue?@action=redirect&bpo=36227): The keyword arguments `default_namespace` and `xml_declaration` are now accepted by the `ElementTree.tostring()` and `ElementTree.tostringlist()` functions.

[bpo-28238](https://bugs.python.org/issue?@action=redirect&bpo=28238): xml.etree.ElementTree's `.find*()` methods are now able to match wildcards such as `{*}tag` and `{ns}*`, which respectively pick up a tag across every namespace or every tag within one namespace. Stefan Behnel wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
