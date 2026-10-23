# configparser - Exceptions

### Exceptions

 *exception *configparser.Error

Base class for every other `configparser` exception.

 *exception *configparser.NoSectionError

Exception raised when a named section can't be found.

 *exception *configparser.DuplicateSectionError

Exception raised when `add_section()` is invoked with the name of a section that already exists, or, in strict parsers, when a section turns up more than once in a single input file, string or dictionary.

Changed in version 3.2: The optional *source* and *lineno* attributes, along with the matching `__init__()` parameters, were added.

 *exception *configparser.DuplicateOptionError

Exception raised by strict parsers should one option appear two times as a single file, string or dictionary is read. It catches typos and case-sensitivity slips — for instance, a dictionary holding two keys that map to one and the same case-insensitive configuration key.

 *exception *configparser.NoOptionError

Exception raised when a named option can't be found within the named section.

 *exception *configparser.InterpolationError

Base class for exceptions raised when trouble arises during string interpolation.

 *exception *configparser.InterpolationDepthError

Exception raised when string interpolation can't finish because the iteration count goes past `MAX_INTERPOLATION_DEPTH`. Subclass of `InterpolationError`.

 *exception *configparser.InterpolationMissingOptionError

Exception raised when a value references an option that doesn't exist. Subclass of `InterpolationError`.

 *exception *configparser.InterpolationSyntaxError

Exception raised when the source text receiving the substitutions doesn't match the required syntax. Subclass of `InterpolationError`.

 *exception *configparser.MissingSectionHeaderError

Exception raised when you try to parse a file that has no section headers.

 *exception *configparser.ParsingError

[Subject index](INDEX.md) · [Previous](raw-config-section-and-value-mutation.md) · [Owning module, declaration or section: configparser](configparser-configuration-file-parser.md)
