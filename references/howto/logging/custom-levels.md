# Custom Levels

### Custom Levels

You can define levels of your own, though it should rarely be needed, since the existing levels were picked from real-world experience. Still, if you are sure custom levels are warranted, take great care in adding them, and *defining custom levels while you build a library is potentially a very poor idea*. The reason: when many library authors each define their own custom levels, the logging output from those several libraries used together may prove hard for the consuming developer to manage or make sense of, because the same numeric value can carry different meanings across different libraries.

[Subject index](INDEX.md) · [Previous source context](logging-levels.md) · [Following source context](useful-handlers.md)
