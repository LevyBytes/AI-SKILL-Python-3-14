# sys.monitoring — Callback function arguments

### Callback function arguments

 sys.monitoring.MISSING

A special value handed to a callback function to signal that the call carries no arguments.

The registered callback function runs whenever an active event arises. A callback function that returns an object other than `DISABLE` has no effect. The arguments handed to the callback function vary by event, as laid out below:

- `PY_START` and `PY_RESUME`:

```python
func(code: CodeType, instruction_offset: int) -> object

```

- `PY_RETURN` and `PY_YIELD`:

```python
func(code: CodeType, instruction_offset: int, retval: object) -> object

```

- `CALL`, `C_RAISE` and `C_RETURN` (*arg0* can be `MISSING` specifically):

```python
func(code: CodeType, instruction_offset: int, callable: object, arg0: object) -> object

```

*code* stands for the code object in which the call happens, while *callable* is the object on the verge of being called (and so the trigger of the event). When there are no arguments, *arg0* is set to `sys.monitoring.MISSING`.

With instance methods, *callable* is the function object as it sits on the class, and *arg0* holds the instance (that is, the method's `self` argument).

- `RAISE`, `RERAISE`, `EXCEPTION_HANDLED`, `PY_UNWIND`, `PY_THROW` and `STOP_ITERATION`:

```python
func(code: CodeType, instruction_offset: int, exception: BaseException) -> object

```

- `LINE`:

```python
func(code: CodeType, line_number: int) -> object

```

- `BRANCH_LEFT`, `BRANCH_RIGHT` and `JUMP`:

```python
func(code: CodeType, instruction_offset: int, destination_offset: int) -> object

```

Note that the *destination_offset* is where the code will next execute.

- `INSTRUCTION`:

```python
func(code: CodeType, instruction_offset: int) -> object

```

[Subject index](INDEX.md) · [Previous](registering-callback-functions.md) · [Continue](../sys-path-init/the-initialization-of-the-sys-path-module-search-path.md) · [Owning module, declaration or section: sys.monitoring](sys-monitoring-execution-event-monitoring.md)
