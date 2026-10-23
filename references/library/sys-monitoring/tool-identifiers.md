# sys.monitoring - Tool identifiers

### Tool identifiers

A tool identifier pairs an integer with an associated name. The point of tool identifiers is to keep tools from stepping on one another and to let several tools run at once. As things stand, tools are entirely independent and one cannot be used to watch another. That restriction may be relaxed down the line.

A tool ought to pick an identifier before it registers or activates events. Identifiers are integers spanning 0 through 5 inclusive.

[Subject index](INDEX.md) · [Previous](sys-monitoring-execution-event-monitoring.md) · [Continue](registering-and-using-tools.md) · [Owning module, declaration or section: sys.monitoring](sys-monitoring-execution-event-monitoring.md)
