# round

round(*number*, *ndigits=None*)

Give back *number* rounded to *ndigits* digits of precision past the decimal point. When *ndigits* is left out or is `None`, the result is the integer nearest the input.

Across the built-in types that handle `round()`, each value snaps to the nearest multiple of 10 raised to the power of negative *ndigits*; should two multiples be exactly as near, the rounding favors the even option (which is why `round(0.5)` as well as `round(-0.5)` both yield `0`, while `round(1.5)` yields `2`). Whatever integer you give for *ndigits* works — positive, zero, or negative alike. When *ndigits* is omitted or `None` the result is an integer; otherwise the result carries the same type as *number*.

For an arbitrary Python object `number`, `round` hands the work off to `number.__round__`.

Note

What `round()` does with floats can catch you off guard: take `round(2.675, 2)`, which produces `2.67` rather than the `2.68` you'd anticipate. That's no defect — it stems from the reality that the majority of decimal fractions have no exact float representation. Consult [Floating-Point Arithmetic: Issues and Limitations](https://docs.python.org/3.14/tutorial/floatingpoint.html#tut-fp-issues) for further detail.

[Builtin task index](INDEX.md).
