# 6.17. Operator precedence

### 6.17. Operator precedence

Operator precedence in Python is laid out in the table that follows, running from the highest (most binding) down to the lowest (least binding). Whatever operators share a box share a precedence. Operators count as binary unless their syntax is spelled out otherwise. Operators within one box group from left to right (exponentiation and conditional expressions being the exceptions, which group from right to left).

Bear in mind that comparisons, membership tests, and identity tests all carry equal precedence and chain left to right, just as the Comparisons section describes.

| Operator | Description |
| --- | --- |
| `(expressions...)`, `[expressions...]`, `{key: value...}`, `{expressions...}` | Bound or parenthesized expression, plus list, dictionary, and set displays |
| `x[index]`, `x[index:index]` `x(arguments...)`, `x.attribute` | Subscription (slicing included), invocation, attribute lookup |
| `await x` | The await expression |
| `**` | Raising to a power [5] |
| `+x`, `-x`, `~x` | Unary plus, unary minus, bitwise NOT |
| `*`, `@`, `/`, `//`, `%` | Product, matrix product, division, floor division, and remainder [6] |
| `+`, `-` | Sum and difference |
| `<<`, `>>` | Bit shifts |
| `&` | Bitwise AND |
| `^` | Bitwise XOR |
| `|` | Bitwise OR |
| `in`, `not in`, `is`, `is not`, `<`, `<=`, `>`, `>=`, `!=`, `==` | Comparisons, which take in membership and identity tests |
| `not x` | Boolean NOT |
| `and` | Boolean AND |
| `or` | Boolean OR |
| `if` – `else` | The conditional expression |
| `lambda` | The lambda expression |
| `:=` | The assignment expression |

Footnotes

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Previous source section](evaluation-order.md)
