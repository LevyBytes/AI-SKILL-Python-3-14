# syslog — Simple example

### Examples

### Simple example

A short batch of examples:

```python
import syslog

syslog.syslog('Processing started')
if error:
    syslog.syslog(syslog.LOG_ERR, 'Processing started')

```

An illustration of configuring a few log options — here they fold the process ID into logged messages and route those messages to the destination facility reserved for mail logging:

```python
syslog.openlog(logoption=syslog.LOG_PID, facility=syslog.LOG_MAIL)
syslog.syslog('E-mail processing initiated...')

```

[Subject index](INDEX.md) · [Continue](../tabnanny/tabnanny-check-to-tabnanny-process-tokens.md) · [Owning module, declaration or section: syslog](syslog-syslog-to-syslog-log-debug.md)
