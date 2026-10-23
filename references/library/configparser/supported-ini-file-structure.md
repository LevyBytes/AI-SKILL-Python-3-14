# configparser - Supported INI File Structure

### Supported INI File Structure

Sections make up a configuration file; each one opens with a `[section]` header and is then followed by key/value entries that a particular string separates (the defaults being `=` or `:` [1]). Out of the box, section names respect case whereas keys do not [1]. Surrounding whitespace gets trimmed from both keys and values. When the parser is set up to permit it [1], values may be left out, and in that situation the key/value delimiter can be dropped too. A value can also stretch across several lines, provided each continuation sits more deeply indented than the value's opening line. Whether blank lines join a multiline value or get skipped hinges on the parser's mode.

Out of the box, any string lacking a ‘\n' qualifies as a valid section name. To alter that, consult `ConfigParser.SECTCRE`.

Should the parser be set up to permit an unnamed top level section via `allow_unnamed_section=True`, the very first section name can be dropped. Then `UNNAMED_SECTION` serves to fetch those keys/values, for instance `config[UNNAMED_SECTION]`.

Comments are allowed inside configuration files, marked off by certain characters (`#` and `;` out of the box [1]). A comment can stand alone on a line that's otherwise blank, and that line may be indented. [1]

For example:

```ini
[Simple Values]
key=value
spaces in keys=allowed
spaces in values=allowed as well
spaces around the delimiter = obviously
you can also use : to delimit keys from values

[All Values Are Strings]
values like this: 1000000
or this: 3.14159265359
are they treated as numbers? : no
integers, floats and booleans are held as: strings
can use the API to get converted values directly: true

[Multiline Values]
chorus: I'm a lumberjack, and I'm okay
    I sleep all night and I work all day

[No Values]
key_without_value
empty string value here =

[You can use comments]
# like this
; or this

# By default only in an empty line.
# Inline comments can be harmful because they prevent users
# from using the delimiting characters as parts of values.
# That being said, this can be customized.

    [Sections Can Be Indented]
        can_values_be_as_well = True
        does_that_mean_anything_special = False
        purpose = formatting for readability
        multiline_values = are
            handled just fine as
            long as they are indented
            deeper than the first line
            of a value
        # Did I mention we can indent comments, too?

```

[Subject index](INDEX.md) · [Previous](fallback-values.md) · [Continue](unnamed-sections.md) · [Owning module, declaration or section: configparser](configparser-configuration-file-parser.md)
