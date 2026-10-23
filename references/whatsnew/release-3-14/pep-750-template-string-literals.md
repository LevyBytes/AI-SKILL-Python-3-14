# What's new in Python 3.14 / **PEP 750**: Template string literals - string.templatelib

### [**PEP 750**](https://peps.python.org/pep-0750/): Template string literals

Template strings deliver a fresh approach to bespoke string handling. Their syntax mirrors that of f-strings, yet rather than yielding a plain [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), they hand back an object capturing both the literal and the interpolated segments of the string.

A t-string is written with a `'t'` prefix where you'd otherwise put an `'f'`:

```pycon
>>> variety = 'Stilton'
>>> template = t'Try some {variety} cheese!'
>>> type(template)
<class 'string.templatelib.Template'>

```

A [`Template`](https://docs.python.org/3.14/library/string.templatelib.html#string.templatelib.Template) object exposes the literal segments and the interpolated ones (the bits inside curly braces) *before* anything stitches them together. Looping over a `Template` instance walks its segments in sequence:

```pycon
>>> list(template)
['Try some ', Interpolation('Stilton', 'variety', None, ''), ' cheese!']

```

Authoring (or invoking) logic that handles `Template` instances is straightforward. As an illustration, the function below lowercases the literal pieces while uppercasing every [`Interpolation`](https://docs.python.org/3.14/library/string.templatelib.html#string.templatelib.Interpolation) instance:

```python
from string.templatelib import Interpolation

def lower_upper(template):
    """Render static parts lowercase and interpolations uppercase."""
    parts = []
    for part in template:
        if isinstance(part, Interpolation):
            parts.append(str(part.value).upper())
        else:
            parts.append(part.lower())
    return ''.join(parts)

name = 'Wenslydale'
template = t'Mister {name}'
assert lower_upper(template) == 'mister WENSLYDALE'

```

Since a `Template` instance keeps literal strings and interpolations separate at runtime, it lends itself well to cleaning up user-supplied input. Coding an `html()` routine that escapes user input for HTML is left as an exercise for you! Logic that handles templates can deliver greater adaptability. As one example, a beefier `html()` routine might take a `dict` of HTML attributes supplied straight in the template:

```python
attributes = {'src': 'limburger.jpg', 'alt': 'lovely cheese'}
template = t'<img {attributes}>'
assert html(template) == '<img src="limburger.jpg" alt="lovely cheese" />'

```

Naturally, code that processes templates is under no obligation to give back a string-like value. A still *more* sophisticated `html()` might yield a bespoke type modeling a DOM-like tree.

Once t-strings are available, programmers can build tooling that sanitises SQL, performs safe shell operations, sharpens logging, embraces contemporary web-development approaches (HTML, CSS, and the like), and rolls out lightweight bespoke business DSLs.

> (Contributed by Jim Baker, Guido van Rossum, Paul Everitt, Koudai Aono, Lysandros Nikolaou, Dave Peck, Adam Turner, Jelle Zijlstra, Bénédikt Tran, and Pablo Galindo Salgado in [gh-132661](https://github.com/python/cpython/issues/132661).)

See also

[**PEP 750**](https://peps.python.org/pep-0750/).

[Subject index](INDEX.md) · [Previous source section](pep-734-multiple-interpreters-in-the-standard-library.md) · [Next source section](pep-768-safe-external-debugger-interface.md) · [Release/subject declaration](summary-release-highlights.md)
