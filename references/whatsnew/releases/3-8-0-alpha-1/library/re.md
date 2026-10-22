# Python 3.8.0 alpha 1 / library / re

[bpo-34844](https://bugs.python.org/issue?@action=redirect&bpo=34844): logging.Formatter improvement — making sure the styles and fmt agree in logging.Formatter — a validate method was added to each format style class: StrFormatStyle, PercentStyle, StringTemplateStyle. — The logging.Formatter constructor calls this method. — The KeyError is additionally re-raised in the format method of each style class, making it clearer that the trouble stems from invalid format fields.

[bpo-34636](https://bugs.python.org/issue?@action=redirect&bpo=34636): Made re scanning faster across long stretches of non-matching characters for s w and d inside bytes objects. (microoptimization)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
