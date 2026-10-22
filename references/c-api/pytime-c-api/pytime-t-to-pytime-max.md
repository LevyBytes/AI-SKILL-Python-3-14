# Types

### Types

 type PyTime_t

A signed 64-bit integer that holds a timestamp or a duration measured in nanoseconds.

Which reference point a timestamp uses depends on the clock involved. As an example, `PyTime_Time()` yields timestamps measured against the UNIX epoch.

Values are supported across roughly [-292.3 years; +292.3 years]. Anchoring on the Unix epoch (January 1st, 1970), this corresponds to a date span of about [1677-09-21; 2262-04-11]. Constants expose the precise boundaries:

 PyTime_t PyTime_MIN

Minimum value of `PyTime_t`.

 PyTime_t PyTime_MAX

Maximum value of `PyTime_t`.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytime-c-api.md) · [Following source contract](pytime-monotonic-to-pytime-time.md)
