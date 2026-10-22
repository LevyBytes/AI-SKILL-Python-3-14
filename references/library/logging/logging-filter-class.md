# logging: `logging.Filter`

### Filter Objects

`Handlers` and `Loggers` can use `Filters` for filtering more sophisticated than levels provide. The base filter class admits only events that sit below a certain point in the logger hierarchy. For instance, when a filter is initialized with "A.B", it admits events from logger "A.B", and equally from "A.B.C", from "A.B.C.D", from "A.B.D" etc., yet not from "A.BB", "B.A.B" etc. Initialized with the empty string, it passes all events.

 *class *logging.Filter(*name=''*)

Returns an instance of the `Filter` class. When *name* is supplied, it names a logger which, along with its children, will have its events admitted through the filter. When *name* is the empty string, every event is admitted.

[Subject index](INDEX.md) · [Previous](buffering-formatter-class-and-format.md) · [Continue](logging-filter-filter.md) · [Owning module, declaration or section: logging](logging-logging-facility-for-python.md)
