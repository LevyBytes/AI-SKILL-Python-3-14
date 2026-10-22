# logging.handlers.NTEventLogHandler: `close()`, `emit()`, `getEventCategory()`, `getEventType()`, `getMessageID()`

close()

Here you could strip the application name out of the registry as a source of event log entries. Do that, though, and the events will not show up the way you meant them to in the Event Log Viewer — it has to reach the registry to obtain the .dll name. The present version refrains from doing this.

 emit(*record*)

Works out the message ID, event category and event type, then records the message into the NT event log.

 getEventCategory(*record*)

Hands back the event category for the record. Override it to supply categories of your own. As shipped, this version hands back 0.

 getEventType(*record*)

Hands back the event type for the record. Override it to supply types of your own. As shipped, this version performs a lookup against the handler's typemap attribute, which `__init__()` populates with a dictionary holding mappings for `DEBUG`, `INFO`, `WARNING`, `ERROR` and `CRITICAL`. Should you run levels of your own, you will have to either override this method or drop a suitable dictionary into the handler's *typemap* attribute.

 getMessageID(*record*)

Hands back the message ID for the record. If you run your own messages, one way is to make the *msg* given to the logger an ID instead of a format string, then perform a dictionary lookup in here to fetch the message ID. As shipped, this version hands back 1, the base message ID found in `win32service.pyd`.

[Subject index](INDEX.md) · [Previous](logging-handlers-nteventloghandler-class.md) · [Continue](logging-handlers-smtphandler-class.md) · [Owning module, declaration or section: logging.handlers](handler-types-overview.md) · [Owning module, declaration or section: logging.handlers.NTEventLogHandler](logging-handlers-nteventloghandler-class.md) · [Owning module, declaration or section: NTEventLogHandler](logging-handlers-nteventloghandler-class.md)
