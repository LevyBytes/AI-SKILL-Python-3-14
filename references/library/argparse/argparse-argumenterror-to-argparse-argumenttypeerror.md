# argparse - Exceptions

### Exceptions

 *exception *argparse.ArgumentError

An error raised while an argument — optional or positional — is being created or used.

Turning this exception into a string gives you the message, padded out with details about whichever argument was responsible for it.

 *exception *argparse.ArgumentTypeError

Thrown if a problem arises while turning a command-line string into a type.

Guides and Tutorials

- [Argparse Tutorial](https://docs.python.org/3.14/howto/argparse.html)
- [Migrating `optparse` code to `argparse`](https://docs.python.org/3.14/howto/argparse-optparse.html)

[Subject index](INDEX.md) · [Previous](argumentparser-register.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
