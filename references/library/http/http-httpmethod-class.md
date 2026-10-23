# http - HTTP status category

### HTTP status category

Added in version 3.12.

The enum values have several properties to indicate the HTTP status category:

| Property | Indicates that | Details |
| --- | --- | --- |
| `is_informational` | `100 <= status <= 199` | HTTP Semantics **RFC 9110**, Section 15 |
| `is_success` | `200 <= status <= 299` | HTTP Semantics **RFC 9110**, Section 15 |
| `is_redirection` | `300 <= status <= 399` | HTTP Semantics **RFC 9110**, Section 15 |
| `is_client_error` | `400 <= status <= 499` | HTTP Semantics **RFC 9110**, Section 15 |
| `is_server_error` | `500 <= status <= 599` | HTTP Semantics **RFC 9110**, Section 15 |

>

Usage:

```python
>>> from http import HTTPStatus
>>> HTTPStatus.OK.is_success
True
>>> HTTPStatus.OK.is_client_error
False

```

 *class *http.HTTPMethod

Added in version 3.11.

A subclass of [`enum.StrEnum`](https://docs.python.org/3.14/library/enum.html#enum.StrEnum) that defines a set of HTTP methods and descriptions written in English.

Usage:

```python
>>> from http import HTTPMethod
>>>
>>> HTTPMethod.GET
<HTTPMethod.GET>
>>> HTTPMethod.GET == 'GET'
True
>>> HTTPMethod.GET.value
'GET'
>>> HTTPMethod.GET.description
'Retrieve the target.'
>>> list(HTTPMethod)
[<HTTPMethod.CONNECT>,
 <HTTPMethod.DELETE>,
 <HTTPMethod.GET>,
 <HTTPMethod.HEAD>,
 <HTTPMethod.OPTIONS>,
 <HTTPMethod.PATCH>,
 <HTTPMethod.POST>,
 <HTTPMethod.PUT>,
 <HTTPMethod.TRACE>]

```

[Subject index](INDEX.md) · [Previous](http-status-codes.md) · [Continue](http-methods.md) · [Owning module, declaration or section: http](http-httpstatus-class.md)
