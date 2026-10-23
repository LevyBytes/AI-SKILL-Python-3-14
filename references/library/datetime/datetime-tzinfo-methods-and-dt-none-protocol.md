# datetime - datetime.tzinfo methods and dt/None protocol

If `None` is supplied, the author of the class chooses how to respond. As one case, handing back `None` makes sense when the class wants to signal that time objects opt out of the `tzinfo` protocols. Having `utcoffset(None)` hand back the standard UTC offset can be more practical, because no alternative scheme exists for finding out the standard offset.

If a `datetime` value arrives as the argument to a `datetime` method, `dt.tzinfo` refers to the very same object as *self*. The `tzinfo` methods may count on this, except where user code invokes `tzinfo` methods on its own. The plan here is that the `tzinfo` methods read *dt* as a local-time value and don't have to fuss over objects sitting in other time zones.

A subclass might also want to override one further `tzinfo` method:

[Subject index](INDEX.md) · [Continue](tzinfo-fromutc.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md) · [Owning module, declaration or section: datetime.tzinfo methods and dt/None protocol](datetime-tzinfo-class.md) · [Preceding source contract and version conditions](tzinfo-utcoffset-to-tzinfo-tzname.md)
