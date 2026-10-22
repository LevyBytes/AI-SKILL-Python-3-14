# datetime objects C API: `PyDateTime_CAPI`, `PyDateTimeAPI`

type PyDateTime_CAPI

Structure containing the fields for the datetime C API.

The fields of this structure are private and subject to change.

Do not use this directly; prefer `PyDateTime_*` APIs instead.

 PyDateTime_CAPI *PyDateTimeAPI

Dynamically allocated object containing the datetime C API.

This variable is only available once `PyDateTime_IMPORT` succeeds.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pydatetime-import.md) · [Following source contract](pydatetime-date.md)
