# datetime - Determining if an object is aware or naive

### Determining if an object is aware or naive

Objects of the `date` type are always naive.

An object of type `time` or `datetime` may be aware or naive.

A `datetime` object `d` qualifies as aware when both of these are satisfied:

1.

`d.tzinfo` is not `None`

2.

`d.tzinfo.utcoffset(d)` does not return `None`

Otherwise, `d` is naive.

A `time` object `t` qualifies as aware when both of these are satisfied:

1.

`t.tzinfo` is not `None`

2.

`t.tzinfo.utcoffset(None)` does not return `None`.

Otherwise, `t` is naive.

For `timedelta` objects the aware-versus-naive split has no meaning.

[Subject index](INDEX.md) · [Previous](common-properties.md) · [Continue](timedelta-objects.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md)
