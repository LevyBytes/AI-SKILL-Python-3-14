# http — HTTP status codes

### HTTP status codes

The [IANA-registered status codes](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml) that `http.HTTPStatus` supports are these:

| Code | Enum Name | Details |
| --- | --- | --- |
| `100` | `CONTINUE` | HTTP Semantics **RFC 9110**, Section 15.2.1 |
| `101` | `SWITCHING_PROTOCOLS` | HTTP Semantics **RFC 9110**, Section 15.2.2 |
| `102` | `PROCESSING` | WebDAV **RFC 2518**, Section 10.1 |
| `103` | `EARLY_HINTS` | An HTTP Status Code for Indicating Hints **RFC 8297** |
| `200` | `OK` | HTTP Semantics **RFC 9110**, Section 15.3.1 |
| `201` | `CREATED` | HTTP Semantics **RFC 9110**, Section 15.3.2 |
| `202` | `ACCEPTED` | HTTP Semantics **RFC 9110**, Section 15.3.3 |
| `203` | `NON_AUTHORITATIVE_INFORMATION` | HTTP Semantics **RFC 9110**, Section 15.3.4 |
| `204` | `NO_CONTENT` | HTTP Semantics **RFC 9110**, Section 15.3.5 |
| `205` | `RESET_CONTENT` | HTTP Semantics **RFC 9110**, Section 15.3.6 |
| `206` | `PARTIAL_CONTENT` | HTTP Semantics **RFC 9110**, Section 15.3.7 |
| `207` | `MULTI_STATUS` | WebDAV **RFC 4918**, Section 11.1 |
| `208` | `ALREADY_REPORTED` | WebDAV Binding Extensions **RFC 5842**, Section 7.1 (Experimental) |
| `226` | `IM_USED` | Delta Encoding in HTTP **RFC 3229**, Section 10.4.1 |
| `300` | `MULTIPLE_CHOICES` | HTTP Semantics **RFC 9110**, Section 15.4.1 |
| `301` | `MOVED_PERMANENTLY` | HTTP Semantics **RFC 9110**, Section 15.4.2 |
| `302` | `FOUND` | HTTP Semantics **RFC 9110**, Section 15.4.3 |
| `303` | `SEE_OTHER` | HTTP Semantics **RFC 9110**, Section 15.4.4 |
| `304` | `NOT_MODIFIED` | HTTP Semantics **RFC 9110**, Section 15.4.5 |
| `305` | `USE_PROXY` | HTTP Semantics **RFC 9110**, Section 15.4.6 |
| `307` | `TEMPORARY_REDIRECT` | HTTP Semantics **RFC 9110**, Section 15.4.8 |
| `308` | `PERMANENT_REDIRECT` | HTTP Semantics **RFC 9110**, Section 15.4.9 |
| `400` | `BAD_REQUEST` | HTTP Semantics **RFC 9110**, Section 15.5.1 |
| `401` | `UNAUTHORIZED` | HTTP Semantics **RFC 9110**, Section 15.5.2 |
| `402` | `PAYMENT_REQUIRED` | HTTP Semantics **RFC 9110**, Section 15.5.3 |
| `403` | `FORBIDDEN` | HTTP Semantics **RFC 9110**, Section 15.5.4 |
| `404` | `NOT_FOUND` | HTTP Semantics **RFC 9110**, Section 15.5.5 |
| `405` | `METHOD_NOT_ALLOWED` | HTTP Semantics **RFC 9110**, Section 15.5.6 |
| `406` | `NOT_ACCEPTABLE` | HTTP Semantics **RFC 9110**, Section 15.5.7 |
| `407` | `PROXY_AUTHENTICATION_REQUIRED` | HTTP Semantics **RFC 9110**, Section 15.5.8 |
| `408` | `REQUEST_TIMEOUT` | HTTP Semantics **RFC 9110**, Section 15.5.9 |
| `409` | `CONFLICT` | HTTP Semantics **RFC 9110**, Section 15.5.10 |
| `410` | `GONE` | HTTP Semantics **RFC 9110**, Section 15.5.11 |
| `411` | `LENGTH_REQUIRED` | HTTP Semantics **RFC 9110**, Section 15.5.12 |
| `412` | `PRECONDITION_FAILED` | HTTP Semantics **RFC 9110**, Section 15.5.13 |
| `413` | `CONTENT_TOO_LARGE` | HTTP Semantics **RFC 9110**, Section 15.5.14 |
| `414` | `URI_TOO_LONG` | HTTP Semantics **RFC 9110**, Section 15.5.15 |
| `415` | `UNSUPPORTED_MEDIA_TYPE` | HTTP Semantics **RFC 9110**, Section 15.5.16 |
| `416` | `RANGE_NOT_SATISFIABLE` | HTTP Semantics **RFC 9110**, Section 15.5.17 |
| `417` | `EXPECTATION_FAILED` | HTTP Semantics **RFC 9110**, Section 15.5.18 |
| `418` | `IM_A_TEAPOT` | HTCPCP/1.0 **RFC 2324**, Section 2.3.2 |
| `421` | `MISDIRECTED_REQUEST` | HTTP Semantics **RFC 9110**, Section 15.5.20 |
| `422` | `UNPROCESSABLE_CONTENT` | HTTP Semantics **RFC 9110**, Section 15.5.21 |
| `423` | `LOCKED` | WebDAV **RFC 4918**, Section 11.3 |
| `424` | `FAILED_DEPENDENCY` | WebDAV **RFC 4918**, Section 11.4 |
| `425` | `TOO_EARLY` | Using Early Data in HTTP **RFC 8470** |
| `426` | `UPGRADE_REQUIRED` | HTTP Semantics **RFC 9110**, Section 15.5.22 |
| `428` | `PRECONDITION_REQUIRED` | Additional HTTP Status Codes **RFC 6585** |
| `429` | `TOO_MANY_REQUESTS` | Additional HTTP Status Codes **RFC 6585** |
| `431` | `REQUEST_HEADER_FIELDS_TOO_LARGE` | Additional HTTP Status Codes **RFC 6585** |
| `451` | `UNAVAILABLE_FOR_LEGAL_REASONS` | An HTTP Status Code to Report Legal Obstacles **RFC 7725** |
| `500` | `INTERNAL_SERVER_ERROR` | HTTP Semantics **RFC 9110**, Section 15.6.1 |
| `501` | `NOT_IMPLEMENTED` | HTTP Semantics **RFC 9110**, Section 15.6.2 |
| `502` | `BAD_GATEWAY` | HTTP Semantics **RFC 9110**, Section 15.6.3 |
| `503` | `SERVICE_UNAVAILABLE` | HTTP Semantics **RFC 9110**, Section 15.6.4 |
| `504` | `GATEWAY_TIMEOUT` | HTTP Semantics **RFC 9110**, Section 15.6.5 |
| `505` | `HTTP_VERSION_NOT_SUPPORTED` | HTTP Semantics **RFC 9110**, Section 15.6.6 |
| `506` | `VARIANT_ALSO_NEGOTIATES` | Transparent Content Negotiation in HTTP **RFC 2295**, Section 8.1 (Experimental) |
| `507` | `INSUFFICIENT_STORAGE` | WebDAV **RFC 4918**, Section 11.5 |
| `508` | `LOOP_DETECTED` | WebDAV Binding Extensions **RFC 5842**, Section 7.2 (Experimental) |
| `510` | `NOT_EXTENDED` | An HTTP Extension Framework **RFC 2774**, Section 7 (Experimental) |
| `511` | `NETWORK_AUTHENTICATION_REQUIRED` | Additional HTTP Status Codes **RFC 6585**, Section 6 |

To keep older code working, the same enum values appear inside the [`http.client`](https://docs.python.org/3.14/library/http.client.html#module-http.client) module as constants. Each constant's name lines up with its enum's name (for instance, `http.HTTPStatus.OK` can equally be reached as `http.client.OK`).

Changed in version 3.7: Added `421 MISDIRECTED_REQUEST` status code.

Added in version 3.8: Added `451 UNAVAILABLE_FOR_LEGAL_REASONS` status code.

Added in version 3.9: Added `103 EARLY_HINTS`, `418 IM_A_TEAPOT` and `425 TOO_EARLY` status codes.

Changed in version 3.13: Adopted RFC9110 naming for the status constants. The former names stay around so older code keeps working: `413 REQUEST_ENTITY_TOO_LARGE`, `414 REQUEST_URI_TOO_LONG`, `416 REQUESTED_RANGE_NOT_SATISFIABLE` and `422 UNPROCESSABLE_ENTITY`.

[Subject index](INDEX.md) · [Previous](http-httpstatus-class.md) · [Continue](http-httpmethod-class.md) · [Owning module, declaration or section: http](http-httpstatus-class.md)
