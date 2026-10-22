# Repeating things

### Repeating things

The ability to match assorted sets of characters is the first thing regular expressions bring that the plain string methods cannot already do. Yet were that their sole extra trick, regexes would hardly count as a step forward. They add another capability: you can declare that pieces of the RE have to repeat a given number of times.

The opening repetition metacharacter we will examine is `*`. `*` won’t match a literal `'*'` character; rather, it declares that the character before it may appear zero or more times over, not just a single time.

So `ca*t` matches `'ct'` (0 `'a'` characters), `'cat'` (1 `'a'`), `'caaat'` (3 `'a'` characters), and onward in that vein.

A repetition like `*` is *greedy*; while repeating part of a RE, the matching engine aims to repeat it the maximum number of times it can. Should a later stretch of the pattern fail to line up, the engine then retreats and has another go using fewer repetitions.

Walking through it step by step makes the behavior clearer. Take the expression `a[bcd]*b`. It matches the letter `'a'`, then zero or more letters drawn from the class `[bcd]`, and closes with a `'b'`. Picture running this RE over the string `'abcbd'`.

| Step | Matched | Explanation |
| --- | --- | --- |
| 1 | `a` | The RE’s `a` lines up. |
| 2 | `abcbd` | Consuming `[bcd]*`, the engine pushes forward as much as possible, reaching the string’s final position. |
| 3 | *Failure* | Now `b` needs to match, yet the cursor sits past the last character, so no match happens. |
| 4 | `abcb` | The engine retreats, letting `[bcd]*` give back one character. |
| 5 | *Failure* | Another go at `b`, but the cursor rests on the closing `'d'` character. |
| 6 | `abc` | Retreat once more, leaving `[bcd]*` covering just `bc`. |
| 7 | `abcb` | One more `b` attempt. Here the cursor’s character is `'b'`, and the match goes through. |

The RE has now been fully consumed, yielding a match of `'abcb'`. This shows the matching engine first reaching as far forward as possible, and whenever that fails it keeps stepping back to re-run the rest of the RE repeatedly. The backing off continues down to zero matches for `[bcd]*`, and if even that comes up short, the engine decides the string never matched the RE.

The other repeating metacharacter is `+`, standing for one or more occurrences. Mind the gap between `*` and `+` closely; `*` allows *zero* or more, so the repeated thing might be wholly absent, whereas `+` demands at least *one* appearance. By way of a parallel example, `ca+t` matches `'cat'` (1 `'a'`) and `'caaat'` (3 `'a'`s), yet does not match `'ct'`.

Two further repetition operators, or quantifiers, remain. The question mark, `?`, matches either zero or one time; picture it as flagging something optional. So `home-?brew` matches either `'homebrew'` or `'home-brew'`.

The trickiest quantifier is `{m,n}`, with *m* and *n* being decimal integers. The notation calls for no fewer than *m* repetitions and no more than *n*. So `a/{1,3}b` matches `'a/b'`, `'a//b'`, and `'a///b'`. It rejects `'ab'`, which carries no slashes, and `'a////b'`, which carries four.

Either *m* or *n* may be left out; whichever is absent gets a sensible default. Leaving out *m* sets the lower bound to 0, while leaving out *n* sets the upper bound to infinity.

In the plainest form `{m}` matches the item before it exactly *m* times. So `a/{2}b` matches only `'a//b'`.

A reader of minimalist inclination might observe that the remaining three quantifiers are all expressible through this notation. `{0,}` equals `*`, `{1,}` matches `+`, and `{0,1}` equals `?`. Reaching for `*`, `+`, or `?` is preferable wherever feasible, just because they are briefer and read more easily.

[Subject index](INDEX.md) · [Previous source context](matching-characters.md) · [Following source context](using-regular-expressions.md)
