# Using loggers as attributes in a class or passing them as parameters

### Using loggers as attributes in a class or passing them as parameters

There may be rare situations calling for this, but as a rule it serves no purpose, since loggers are singletons. Any code can reach a particular logger instance by name through `logging.getLogger(name)`, which makes passing instances around or keeping them as instance attributes futile. Bear in mind that languages like Java and C# frequently treat loggers as static class attributes. That pattern, however, is a poor fit for Python, where the module rather than the class is the unit of software decomposition.

[Subject index](INDEX.md) · [Previous source context](opening-the-same-log-file-multiple-times.md) · [Following source context](library-logger-handler-misuse.md)
