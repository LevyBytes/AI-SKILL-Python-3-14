# Python 3.8.0 alpha 3 / library / functions and types

[bpo-36320](https://bugs.python.org/issue?@action=redirect&bpo=36320): The typing.NamedTuple() class now deprecates the _field_types attribute, favoring the __annotations__ attribute that holds the identical information. Both attributes were also moved from OrderedDict to an ordinary dict.

[bpo-36324](https://bugs.python.org/issue?@action=redirect&bpo=36324): Give statistics.NormalDist a method that computes the inverse cumulative normal distribution.

[bpo-36321](https://bugs.python.org/issue?@action=redirect&bpo=36321): collections.namedtuple() got an attribute name wrong. For consistency with typing.NamedTuple, that attribute ought to have read "_field_defaults" instead of "_fields_defaults". To preserve backwards compatibility, both spellings now exist. The misspelled one might disappear later on.

[bpo-36169](https://bugs.python.org/issue?@action=redirect&bpo=36169): Give statistics.NormalDist an overlap() method. It works out the overlapping coefficient between two normal distributions.

[bpo-21269](https://bugs.python.org/issue?@action=redirect&bpo=21269): Give mock call objects `args` and `kwargs` properties. Kumar Akshay contributed this.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
