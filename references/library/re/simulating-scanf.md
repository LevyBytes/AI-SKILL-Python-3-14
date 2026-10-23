# re - Simulating scanf()

### Simulating scanf()

At present Python ships no counterpart to `scanf()`. By and large, regular expressions outdo `scanf()` format strings in power, even if they run wordier. The following table sets out roughly matching correspondences from `scanf()` format tokens to regular expressions.

| `scanf()` Token | Regular Expression |
| --- | --- |
| `%c` | `.` |
| `%5c` | `.{5}` |
| `%d` | `[-+]?\d+` |
| `%e`, `%E`, `%f`, `%g` | `[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?` |
| `%i` | `[-+]?(0[xX][\dA-Fa-f]+|0[0-7]*|\d+)` |
| `%o` | `[-+]?[0-7]+` |
| `%s` | `\S+` |
| `%u` | `\d+` |
| `%x`, `%X` | `[-+]?(0[xX])?[\dA-Fa-f]+` |

To pull the filename together with the numbers out of a string such as

```python
/usr/sbin/sendmail - 0 errors, 4 warnings

```

you would reach for a `scanf()` format along the lines of

```python
%s - %d errors, %d warnings

```

Its matching regular expression comes out as

```python
(\S+) - (\d+) errors, (\d+) warnings

```

[Subject index](INDEX.md) · [Previous](checking-for-a-pair.md) · [Continue](re-search.md) · [Owning module, declaration or section: re](re-regular-expression-operations.md)
