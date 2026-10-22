# What's New In Python 3.6 / email — email, email.compat32-message, email.generator, email.message, email.mime, email.policy

### email

The new email API, switched on through the *policy* keyword passed to assorted constructors, has dropped its provisional standing. The [`email`](https://docs.python.org/3.14/library/email.html#module-email) documentation got restructured and rewritten to center on the new API, though it preserves the older documentation for the legacy API. (Contributed by R. David Murray in [bpo-24277](https://bugs.python.org/issue?@action=redirect&bpo=24277).)

Each of the [`email.mime`](https://docs.python.org/3.14/library/email.mime.html#module-email.mime) classes now takes an optional *policy* keyword. (Contributed by Berker Peksag in [bpo-27331](https://bugs.python.org/issue?@action=redirect&bpo=27331).)

The [`DecodedGenerator`](https://docs.python.org/3.14/library/email.generator.html#email.generator.DecodedGenerator) now handles the *policy* keyword.

A new [`policy`](https://docs.python.org/3.14/library/email.policy.html#module-email.policy) attribute, [`message_factory`](https://docs.python.org/3.14/library/email.policy.html#email.policy.Policy.message_factory), now decides which class the parser reaches for by default while building new message objects. Under the [`email.policy.compat32`](https://docs.python.org/3.14/library/email.policy.html#email.policy.compat32) policy that class is [`Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message), whereas the newer policies use [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage). (Contributed by R. David Murray in [bpo-20476](https://bugs.python.org/issue?@action=redirect&bpo=20476).)

[Subject index](INDEX.md) · [Previous source section](distutils.md) · [Next source section](encodings.md) · [Release/subject declaration](summary-release-highlights.md)
