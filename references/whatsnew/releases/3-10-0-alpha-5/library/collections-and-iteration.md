# Python 3.10.0 alpha 5 / library / collections and iteration

[bpo-38250](https://bugs.python.org/issue?@action=redirect&bpo=38250): [Enum] A flag made of just one bit now counts as canonical, and such flags are the only ones produced when you list or iterate a Flag class or one of its members. Flags spanning multiple bits count as aliases; they surface from lookups and from operations whose result lands on their value. Both Flag classes and Flag members iterate in definition order.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
