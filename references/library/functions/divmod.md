# divmod

divmod(*a*, *b*, */*)

Accept two (non-complex) numbers and hand back a pair of numbers, namely their quotient and remainder under integer division. Where the operand types are mixed, the conventions for binary arithmetic operators take over. With integers, the outcome matches `(a // b, a % b)`. With floating-point numbers the outcome is `(q, a % b)`, in which *q* is normally `math.floor(a / b)` though it can fall 1 short of that. Regardless, `q * b + a % b` stays very near *a*; when `a % b` is non-zero its sign matches that of *b*, and `0 <= abs(a % b) < abs(b)`.

[Builtin task index](INDEX.md).
