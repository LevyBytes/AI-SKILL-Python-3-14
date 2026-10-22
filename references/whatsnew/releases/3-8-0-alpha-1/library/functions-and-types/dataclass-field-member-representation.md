# Python 3.8.0 alpha 1 / library / alter dataclasses fields repr relies each member s repr rather

[bpo-33495](https://bugs.python.org/issue?@action=redirect&bpo=33495): Alter the dataclasses.Fields repr so it relies on each member's repr rather than str. The result clarifies what every field genuinely stands for, most notably for the "type" member.

[Subject index](INDEX.md) · [Release version, date and status](../../release-overview/overview.md)
