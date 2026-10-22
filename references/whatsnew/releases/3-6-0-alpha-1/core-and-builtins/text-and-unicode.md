# Python 3.6.0 alpha 1 / core and builtins / text and unicode

[bpo-25709](https://bugs.python.org/issue?@action=redirect&bpo=25709): Repair the issue affecting in-place string concatenation alongside the utf-8 cache.

[bpo-25301](https://bugs.python.org/issue?@action=redirect&bpo=25301): For the error handlers `ignore`, `replace` and `surrogateescape`, the UTF-8 decoder now runs up to 15 times as fast.

[bpo-24848](https://bugs.python.org/issue?@action=redirect&bpo=24848): Repair a set of bugs affecting the UTF-7 decoding of misformed data.

[bpo-25267](https://bugs.python.org/issue?@action=redirect&bpo=25267): For the error handlers `ignore`, `replace`, `surrogateescape`, `surrogatepass`, the UTF-8 encoder now runs up to 75 times as fast. Serhiy Storchaka co-wrote the patch.

[bpo-24965](https://bugs.python.org/issue?@action=redirect&bpo=24965): Bring [**PEP 498**](https://peps.python.org/pep-0498/) "Literal String Interpolation" to life. With it you can place expressions within f-strings, and those get turned into ordinary strings as the program runs. So when x=3, the result `f'value={x}'` == "value=3" holds. Eric V. Smith wrote the patch.

[bpo-26516](https://bugs.python.org/issue?@action=redirect&bpo=26516): A Python built in release mode now accepts the [`PYTHONMALLOCSTATS`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONMALLOCSTATS) environment variable as well. Setting it to an empty string now leaves it with no effect.

[bpo-26464](https://bugs.python.org/issue?@action=redirect&bpo=26464): Repair str.translate() for the case where the string is ASCII and the first replacement deletes a character while a later replacement supplies a non-ASCII character or a string of more than 1 character. This regression had entered in Python 3.5.0.

[bpo-26302](https://bugs.python.org/issue?@action=redirect&bpo=26302): Adjust the behavior so a comma is rejected as a valid character within cookie names.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
