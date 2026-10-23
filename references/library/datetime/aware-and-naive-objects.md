# datetime - Aware and naive objects

### Aware and naive objects

Whether a date or time object carries time zone data determines if it is labeled “aware” or “naive”.

Given enough understanding of the relevant algorithmic and political time adjustments — for instance, time zone and daylight saving time data — an **aware** object can position itself with respect to other aware objects. Such an object denotes a particular instant that admits no other reading. [1]

A **naive** object lacks the data needed to place itself unambiguously next to other date/time objects. The program alone decides whether such an object stands for Coordinated Universal Time (UTC), local time, or a different time zone — in the same way the program alone decides whether a given number means metres, miles, or mass. They are simple to grasp and handle, though that simplicity comes from leaving out parts of reality.

When aware objects are needed, the `datetime` and `time` objects carry an optional time zone attribute, `tzinfo`, which may hold an instance of a subclass derived from the abstract `tzinfo` class. Such `tzinfo` objects record the UTC offset, the time zone’s name, and whether daylight saving time applies.

The `datetime` module ships exactly one concrete `tzinfo` class, namely the `timezone` class. The `timezone` class models straightforward time zones whose offset from UTC never varies, for instance UTC itself or the North American EST and EDT zones. Any richer treatment of time zones is left to the application to build. Worldwide rules for adjusting time are driven more by politics than by logic, shift often, and outside of UTC no single standard fits every use.

[Subject index](INDEX.md) · [Previous](datetime-basic-date-and-time-types.md) · [Continue](datetime-minyear-to-datetime-utc.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md)
