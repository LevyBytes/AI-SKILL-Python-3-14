# Modifying strings

### Modifying strings

So far we have only run searches over a fixed string. Another frequent use of regular expressions is reshaping strings in assorted manners, which the pattern methods below provide:

| Method/Attribute | Purpose |
| --- | --- |
| `split()` | Break the string into a list, dividing it at each spot the RE matches |
| `sub()` | Locate every substring the RE matches and swap each one for some other string |
| `subn()` | Performs the identical task as `sub()`, yet hands back the fresh string plus a count of swaps made |

[Subject index](INDEX.md) · [Previous source context](lookahead-assertions.md) · [Following source context](splitting-strings.md)
