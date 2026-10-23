# email.headerregistry`email.headerregistry`: Custom Header Objects

*class *email.headerregistry.DateHeader

[**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html) lays out a highly precise format for dates inside email headers. The `DateHeader` parser knows that date format and additionally knows a number of variant shapes that crop up now and then “in the wild”.

The extra attributes this header type adds are:

 datetime

Whenever the header value can be read as a valid date in one form or another, this attribute holds a [`datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) instance standing for that date. Should the input date’s timezone be given as `-0000` (signaling UTC but carrying nothing about the source timezone), then `datetime` comes out as a naive `datetime`. Should a definite timezone offset turn up (`+0000` included), then `datetime` holds an aware `datetime` that records the timezone offset by way of [`datetime.timezone`](https://docs.python.org/3.14/library/datetime.html#datetime.timezone).

The header’s `decoded` value comes from formatting the `datetime` under the [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html) rules; that is, it is set to:

```python
email.utils.format_datetime(self.datetime)

```

While building a `DateHeader`, *value* is allowed to be a [`datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) instance. So, for instance, the snippet below is valid and behaves the way you would anticipate:

```python
msg['Date'] = datetime(2011, 7, 15, 21)

```

Since this is a naive `datetime`, it gets read as a UTC timestamp, and the value that results carries a timezone of `-0000`. A far more practical option is to reach for the [`localtime()`](https://docs.python.org/3.14/library/email.utils.html#email.utils.localtime) function out of the [`utils`](https://docs.python.org/3.14/library/email.utils.html#module-email.utils) module:

```python
msg['Date'] = utils.localtime()

```

This snippet assigns the date header the present time and date together with the present timezone offset.

[Subject index](INDEX.md) · [Previous](email-headerregistry-unstructuredheader-class.md) · [Continue](email-headerregistry-addressheader-class.md) · [Owning module, declaration or section: email.headerregistry](email-headerregistry-baseheader-class.md)
