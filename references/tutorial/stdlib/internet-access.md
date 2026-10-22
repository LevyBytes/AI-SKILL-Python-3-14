# 10.7. Internet access

### 10.7. Internet access

Several modules exist for reaching the internet and working with its protocols. Among the most basic pair are [`urllib.request`](https://docs.python.org/3.14/library/urllib.request.html#module-urllib.request), which pulls data down from URLs, and [`smtplib`](https://docs.python.org/3.14/library/smtplib.html#module-smtplib), which dispatches mail:

```python
>>> from urllib.request import urlopen
>>> with urlopen('https://docs.python.org/3/') as response:
...     for line in response:
...         line = line.decode()             # Convert bytes to a str
...         if 'updated' in line:
...             print(line.rstrip())         # Remove trailing newline
...
      Last updated on Nov 11, 2025 (20:11 UTC).

>>> import smtplib
>>> server = smtplib.SMTP('localhost')
>>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
... """To: jcaesar@example.org
... From: soothsayer@example.org
...
... Beware the Ides of March.
... """)
>>> server.quit()

```

(Keep in mind that running the second snippet requires a mailserver active on localhost.)

[Subject index](INDEX.md) · [Previous source section](mathematics.md) · [Following source section](dates-and-times.md)
