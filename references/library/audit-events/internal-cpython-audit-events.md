# Audit events table - Contract: These next events fire internally and map to no public API within CPython:

These next events fire internally and map to no public API within CPython:

| Audit event | Arguments |
| --- | --- |
| _winapi.CreateFile | `file_name`, `desired_access`, `share_mode`, `creation_disposition`, `flags_and_attributes` |
| _winapi.CreateJunction | `src_path`, `dst_path` |
| _winapi.CreateNamedPipe | `name`, `open_mode`, `pipe_mode` |
| _winapi.CreatePipe |  |
| _winapi.CreateProcess | `application_name`, `command_line`, `current_directory` |
| _winapi.OpenProcess | `process_id`, `desired_access` |
| _winapi.TerminateProcess | `handle`, `exit_code` |
| _posixsubprocess.fork_exec | `exec_list`, `args`, `env` |
| ctypes.PyObj_FromPtr | `obj` |

Added in version 3.14: The `_posixsubprocess.fork_exec` internal audit event.

[Subject index](INDEX.md) · [Previous](audit-events-table-winreg.md) · [Owning module, declaration or section: Audit events table](audit-events-table-section-introduction-and-initial-examples.md)
