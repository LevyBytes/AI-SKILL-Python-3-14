# tomllib — Conversion Table

### Conversion Table

| TOML | Python |
| --- | --- |
| TOML document | dict |
| string | str |
| integer | int |
| float | float (configurable with *parse_float*) |
| boolean | bool |
| offset date-time | datetime.datetime (`tzinfo` attribute set to an instance of `datetime.timezone`) |
| local date-time | datetime.datetime (`tzinfo` attribute set to `None`) |
| local date | datetime.date |
| local time | datetime.time |
| array | list |
| table | dict |
| inline table | dict |
| array of tables | list of dicts |

[Subject index](INDEX.md) · [Previous](examples.md) · [Owning module, declaration or section: tomllib](tomllib-load-to-tomllib-tomldecodeerror.md)
