# email.policy: Email policy model and message behavior

### `email.policy`: Policy Objects

Added in version 3.3.

**Source code:** [Lib/email/policy.py](https://github.com/python/cpython/tree/3.14/Lib/email/policy.py)

---

The central purpose of the [`email`](https://docs.python.org/3.14/library/email.html#module-email) package is to work with email messages as defined by the assorted email and MIME RFCs. That said, the broad structure of an email message — a set of header fields, each being a name then a colon then a value, with that whole set followed by an empty line and then some arbitrary ‘body’ — is a layout that has proven useful well beyond email itself. Certain of those other applications stick fairly tightly to the core email RFCs, while others stray from them. Even within email proper, occasions arise where stepping away from strict RFC adherence is preferable — for instance, producing messages that work with mail servers which themselves ignore the standards, or which add extensions you wish to leverage in ways the standards forbid.

Policy objects supply the email package with the adaptability needed to cope with all of these varied scenarios.

A `Policy` object bundles together a collection of attributes and methods that govern how the assorted parts of the email package behave while in use. You can hand `Policy` instances to the email package’s several classes and methods to change their default behavior. The values you can set, along with their defaults, are listed further down.

Every class in the email package relies on a default policy. For all the [`parser`](https://docs.python.org/3.14/library/email.parser.html#module-email.parser) classes plus the related convenience functions, and for the [`Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message) class, that default is the `Compat32` policy, supplied through its matching pre-defined instance `compat32`. That policy delivers full backward compatibility (and, in certain cases, even bug-for-bug compatibility) with the email package as it existed prior to Python 3.3.

For the *policy* keyword of [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage), the default value is the `EmailPolicy` policy, accessed through its pre-defined instance `default`.

Whenever a [`Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message) or [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage) object comes into being, it picks up a policy. Should a [`parser`](https://docs.python.org/3.14/library/email.parser.html#module-email.parser) build the message, then whatever policy was given to that parser becomes the policy of the message it produces. Should the program itself build the message, you may state the policy at creation time. Once a message is handed to a [`generator`](https://docs.python.org/3.14/library/email.generator.html#module-email.generator), that generator by default takes the policy off the message, yet you may instead supply the generator with its own policy that supersedes the one carried by the message object.

For the [`email.parser`](https://docs.python.org/3.14/library/email.parser.html#module-email.parser) classes and the parser convenience functions, the default *policy* keyword value **will be changing** in some later release of Python. For that reason you ought to **always specify explicitly which policy you want to use** whenever you invoke any of the classes and functions documented in the `parser` module.

This documentation opens by covering what `Policy` offers — an [abstract base class](https://docs.python.org/3.14/glossary.html#term-abstract-base-class) laying out the traits shared by every policy object, `compat32` among them. Included are several hook methods that the email package invokes internally, which a custom policy may override to produce alternative behavior. After that comes a description of the concrete classes `EmailPolicy` and `Compat32`, which fill in the hooks delivering, respectively, the standard behavior and the backward compatible behavior and features.

Although `Policy` instances cannot be mutated, you can clone them; cloning takes the same keyword arguments the class constructor takes and yields a fresh `Policy` instance that duplicates the original except for whatever attribute values you asked to change.

By way of illustration, the snippet below could serve to load an email message off a file on disk and route it to the system `sendmail` program on a Unix machine:

```pycon
>>> from email import message_from_binary_file
>>> from email.generator import BytesGenerator
>>> from email import policy
>>> from subprocess import Popen, PIPE
>>> with open('mymsg.txt', 'rb') as f:
...     msg = message_from_binary_file(f, policy=policy.default)
...
>>> p = Popen(['sendmail', msg['To'].addresses[0]], stdin=PIPE)
>>> g = BytesGenerator(p.stdin, policy=msg.policy.clone(linesep='\r\n'))
>>> g.flatten(msg)
>>> p.stdin.close()
>>> rc = p.wait()

```

Here we instruct [`BytesGenerator`](https://docs.python.org/3.14/library/email.generator.html#email.generator.BytesGenerator) to apply the RFC correct line separator characters as it builds the binary string fed into `sendmail's` `stdin`, whereas the default policy would instead apply `\n` line separators.

Certain email package methods take a *policy* keyword argument, so that the policy may be overridden just for that one method. As an illustration, the snippet below applies the [`as_bytes()`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message.as_bytes) method of the *msg* object from the earlier example and saves the message to a file with the line separators native to the platform it is executing on:

```python
>>> import os
>>> with open('converted.txt', 'wb') as f:
...     f.write(msg.as_bytes(policy=msg.policy.clone(linesep=os.linesep)))
17

```

You may likewise merge policy objects with the addition operator, yielding a policy object whose settings blend the non-default values drawn from each of the added objects:

```python
>>> compat_SMTP = policy.compat32.clone(linesep='\r\n')
>>> compat_strict = policy.compat32.clone(raise_on_defect=True)
>>> compat_strict_SMTP = compat_SMTP + compat_strict

```

That operation is not commutative — in other words, the sequence in which you add the objects is significant. By way of demonstration:

```python
>>> policy100 = policy.compat32.clone(max_line_length=100)
>>> policy80 = policy.compat32.clone(max_line_length=80)
>>> apolicy = policy100 + policy80
>>> apolicy.max_line_length
80
>>> apolicy = policy80 + policy100
>>> apolicy.max_line_length
100

```

[Subject index](INDEX.md) · [Continue](base-policy-settings-and-header-limits.md)
