# What's New In Python 3.3 / email / Provisional Policy with New Header API — email.header, email.policy

#### Provisional Policy with New Header API

The framework earns its keep on its own, yet the real reason it exists is to open the door to fresh policies that bring new email-package features online while leaving anyone who skips those policies fully backward compatible. Since a new API rides along with these policies, Python 3.3 ships them tagged as a [provisional policy](https://docs.python.org/3.14/glossary.html#term-provisional-package). Should the core developers find it warranted, breaking changes — even pulling the code entirely — remain on the table.

[`EmailPolicy`](https://docs.python.org/3.14/library/email.policy.html#email.policy.EmailPolicy) instances make up the new policies, and they bring these extra controls:

| refold_source | This governs whether the `generator` refolds headers that a `parser` already read. Allowed values are `none`, `long`, or `all`. With the default of `long`, any source header whose line runs past `max_line_length` is refolded. Picking `none` refolds nothing, while `all` refolds every line. |
| --- | --- |
| header_factory | A callable that take a `name` and `value` and produces a custom header object. |

Everything new in these policies hinges on the `header_factory`. Switch one on and every header you pull off a `Message` arrives as something the `header_factory` built, while every header you store onto a `Message` likewise turns into a `header_factory` product. Each such header object carries a `name` attribute matching the header's name. On top of that, Address and Date headers expose extra attributes opening up the header's parsed contents. The upshot is that you can now write code such as:

```python
>>> m = Message(policy=SMTP)
>>> m['To'] = 'Éric <foo@example.com>'
>>> m['to']
'Éric <foo@example.com>'
>>> m['to'].addresses
(Address(display_name='Éric', username='foo', domain='example.com'),)
>>> m['to'].addresses[0].username
'foo'
>>> m['to'].addresses[0].display_name
'Éric'
>>> m['Date'] = email.utils.localtime()
>>> m['Date'].datetime
datetime.datetime(2012, 5, 25, 21, 39, 24, 465484, tzinfo=datetime.timezone(datetime.timedelta(-1, 72000), 'EDT'))
>>> m['Date']
'Fri, 25 May 2012 21:44:27 -0400'
>>> print(m)
To: =?utf-8?q?=C3=89ric?= <foo@example.com>
Date: Fri, 25 May 2012 21:44:27 -0400

```

Notice how serializing the message quietly encodes the unicode display name as `utf-8`, whereas reading the header straight back hands you the unicode form. That spares you from ever touching the [`email.header`](https://docs.python.org/3.14/library/email.header.html#module-email.header) [`decode_header()`](https://docs.python.org/3.14/library/email.header.html#email.header.decode_header) or [`make_header()`](https://docs.python.org/3.14/library/email.header.html#email.header.make_header) functions.

Building addresses out of pieces is also supported:

```python
>>> m['cc'] = [Group('pals', [Address('Bob', 'bob', 'example.com'),
...                           Address('Sally', 'sally', 'example.com')]),
...            Address('Bonzo', addr_spec='bonz@laugh.com')]
>>> print(m)
To: =?utf-8?q?=C3=89ric?= <foo@example.com>
Date: Fri, 25 May 2012 21:44:27 -0400
cc: pals: Bob <bob@example.com>, Sally <sally@example.com>;, Bonzo <bonz@laugh.com>

```

The decode back into unicode happens for you:

```python
>>> m2 = message_from_string(str(m))
>>> m2['to']
'Éric <foo@example.com>'

```

Once a message is parsed, reach for the `addresses` and `groups` attributes on the header objects to walk the groups along with each individual address:

```python
>>> m2['cc'].addresses
(Address(display_name='Bob', username='bob', domain='example.com'), Address(display_name='Sally', username='sally', domain='example.com'), Address(display_name='Bonzo', username='bonz', domain='laugh.com'))
>>> m2['cc'].groups
(Group(display_name='pals', addresses=(Address(display_name='Bob', username='bob', domain='example.com'), Address(display_name='Sally', username='sally', domain='example.com')), Group(display_name=None, addresses=(Address(display_name='Bonzo', username='bonz', domain='laugh.com'),))

```

To sum up: pick one of the new policies and header handling behaves as it should — your code stays in unicode strings, and behind the scenes the email package encodes and decodes between that unicode and the RFC standard Content Transfer Encodings.

[Subject index](INDEX.md) · [Previous source section](email-policy-framework.md) · [Next source section](email-other-api-changes.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](email-policy-framework.md)
