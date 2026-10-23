# What's New In Python 3.3 / email / Policy Framework - email.compat32-message, email.generator, email.parser, email.policy

### email

#### Policy Framework

A [`policy`](https://docs.python.org/3.14/library/email.policy.html#module-email.policy) framework now ships inside the email package. Each [`Policy`](https://docs.python.org/3.14/library/email.policy.html#email.policy.Policy) bundles methods and properties that steer the package's behavior. Python 3.3 ships [`Compat32`](https://docs.python.org/3.14/library/email.policy.html#email.policy.Compat32) as the leading policy; it keeps you compatible with how the package worked back in Python 3.2. You can hand a `policy` to a [`parser`](https://docs.python.org/3.14/library/email.parser.html#module-email.parser) as it reads a message, attach one while building a [`Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message), or supply one as a [`generator`](https://docs.python.org/3.14/library/email.generator.html#module-email.generator) serializes mail. Barring an override, every `Message` and nested object the `parser` builds inherits the policy you gave that `parser`. A `generator`, by default, reuses whatever policy lives on the `Message` it is writing out. [`compat32`](https://docs.python.org/3.14/library/email.policy.html#email.policy.compat32) serves as the default policy.

These are the baseline controls that each `policy` object honors:

| max_line_length | When a `Message` gets serialized, this caps how long any single line may run, not counting the linesep character(s); the fallback value is 78. |
| --- | --- |
| linesep | This is the character that divides one serialized line from the next as a `Message` is written; it falls back to `\n`. |
| cte_type | Either `7bit` or `8bit`. Only a `Bytes` `generator` honors `8bit`, which permits non-ASCII wherever the protocol allows it (or wherever the original input already carried it). |
| raise_on_defect | With this on, a `parser` throws on a defect rather than appending it to the `defects` list of the `Message` object’s. |

To spin up a fresh policy instance carrying different settings, call the [`clone()`](https://docs.python.org/3.14/library/email.policy.html#email.policy.Policy.clone) method on a policy object. Hand `clone` any of those controls as keyword arguments; whatever you leave out simply keeps its fallback. So building a policy whose linesep characters are `\r\n` looks like this:

```python
mypolicy = compat32.clone(linesep='\r\n')

```

Lean on policies to streamline emitting messages in whatever layout your application requires. Rather than recalling that you must pass `linesep='\r\n'` at every `generator` call site, declare it a single time on the policy attached to either the `parser` or the `Message` your program leans on for making `Message` objects. Conversely, when several output shapes are required, you remain free to pass the arguments straight to the matching `generator` call. Alternatively, keep distinct policy instances per scenario and feed each one in as you build the `generator`.

[Subject index](INDEX.md) · [Previous source section](decimal-api-changes.md) · [Next source section](email-provisional-policy-with-new-header-api.md) · [Release/subject declaration](summary-release-highlights.md)
