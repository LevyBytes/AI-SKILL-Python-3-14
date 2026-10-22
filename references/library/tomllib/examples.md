# tomllib — Examples

### Examples

Parsing a TOML file:

```python
import tomllib

with open("pyproject.toml", "rb") as f:
    data = tomllib.load(f)

```

Parsing a TOML string:

```python
import tomllib

toml_str = """
python-version = "3.11.0"
python-implementation = "CPython"
"""

data = tomllib.loads(toml_str)

```

[Subject index](INDEX.md) · [Previous](tomllib-load-to-tomllib-tomldecodeerror.md) · [Continue](conversion-table.md) · [Owning module, declaration or section: tomllib](tomllib-load-to-tomllib-tomldecodeerror.md)
