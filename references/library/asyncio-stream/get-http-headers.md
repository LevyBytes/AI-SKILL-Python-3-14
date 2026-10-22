# Get HTTP headers

### Get HTTP headers

A small example that fetches the HTTP headers for whatever URL is given on the command line:

```python
import asyncio
import urllib.parse
import sys

async def print_http_headers(url):
    url = urllib.parse.urlsplit(url)
    if url.scheme == 'https':
        reader, writer = await asyncio.open_connection(
            url.hostname, 443, ssl=True)
    else:
        reader, writer = await asyncio.open_connection(
            url.hostname, 80)

    query = (
        f"HEAD {url.path or '/'} HTTP/1.0\r\n"
        f"Host: {url.hostname}\r\n"
        f"\r\n"
    )

    writer.write(query.encode('latin-1'))
    while True:
        line = await reader.readline()
        if not line:
            break

        line = line.decode('latin1').rstrip()
        if line:
            print(f'HTTP header> {line}')

    # Ignore the body, close the socket
    writer.close()
    await writer.wait_closed()

url = sys.argv[1]
asyncio.run(print_http_headers(url))

```

Usage:

```python
python example.py http://example.com/path/page.html

```

or with HTTPS:

```python
python example.py https://example.com/path/page.html

```

[Subject index](INDEX.md) · [Previous](tcp-echo-server-using-streams.md) · [Continue](register-an-open-socket-to-wait-for-data-using-streams.md)
