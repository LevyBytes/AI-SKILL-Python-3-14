# Match literals, OR patterns and tuple captures

### 4.7. `match` Statements

A [`match`](https://docs.python.org/3.14/reference/compound_stmts.html#match) statement evaluates an expression and weighs its result against one pattern after another, each laid out in a case block. On the surface this looks like the switch statement of C, Java or JavaScript (and plenty of other languages), but it lines up far better with the pattern matching of languages such as Rust or Haskell. Only the earliest pattern that fits is run, and it can additionally pull pieces (sequence elements or object attributes) out of the value and into variables. When no case fits, not one of the branches runs.

In its plainest form it weighs a subject value against a single literal or several:

```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

```

Observe the final block: there the “variable name” `_` serves as a *wildcard* and is guaranteed to match.

Multiple literals can be merged into one pattern by means of `|` (“or”):

```python
case 401 | 403 | 404:
    return "Not allowed"

```

Patterns may resemble unpacking assignments, and they serve to bind variables:

```python
# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")

```

Give that one close study! Its opening pattern holds two literals, and you can regard it as building on the literal pattern demonstrated earlier. The two that follow, however, pair a literal with a variable, where the variable *binds* a value drawn from the subject (`point`). The pattern in fourth place grabs two values, which leaves it conceptually akin to the unpacking assignment `(x, y) = point`.

[Subject index](INDEX.md) · [Previous source section](pass-statements.md) · [Following source section](match-class-attributes-positional-fields-and-nested-patterns.md) · [Related tutorial example and explanation](match-class-attributes-positional-fields-and-nested-patterns.md) · [Related tutorial example and explanation](match-guards-mapping-patterns-captures-and-named-constants.md)
