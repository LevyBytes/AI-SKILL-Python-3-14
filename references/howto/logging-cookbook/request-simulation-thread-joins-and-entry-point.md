# Request simulation, thread joins and entry point

Open the [complete example modules](../../examples/request-context-logging/INDEX.md) for the complete definitions, imports and entrypoint.

When you run the code above, you'll observe that about half of the requests land in `app1.log` while the remainder go to `app2.log`, and every one of the requests is recorded in `app.log`. Each webapp-specific log holds only the entries belonging to that particular webapp, and the request information shows up consistently throughout the log (that is, the details from each dummy request always stay grouped together on a single log line). The shell output below illustrates this:

[Subject index](INDEX.md) · [Coupled example phase](imports-request-data-formatter-and-context-variables.md) · [Coupled example phase](context-injecting-filter-and-whole-webapp-class.md) · [Following source continuation](context-variable-logging-output.md) · [Imports, request data, formatter and context variables](imports-request-data-formatter-and-context-variables.md) · [Context-injecting filter and whole WebApp class](context-injecting-filter-and-whole-webapp-class.md) · [Previous source context](context-injecting-filter-and-whole-webapp-class.md)
