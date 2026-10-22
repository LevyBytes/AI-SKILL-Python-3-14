# urllib.request: `Request.get_header()`, `Request.header_items()`

Set up the request to route through a proxy server. The supplied *host* and *type* take the place of the instance's own, while the selector on the instance is set to the URL originally handed to the constructor.

 Request.get_header(*header_name*, *default=None*)

Hand back the value associated with the named header. Should that header be missing, hand back the default instead.

 Request.header_items()

Hand back a list of tuples (header_name, header_value) for the Request headers.

Changed in version 3.4: Deprecated ever since 3.3, the request methods add_data, has_data, get_data, get_type, get_host, get_selector, get_origin_req_host and is_unverifiable are now gone.

[Subject index](INDEX.md) · [Continue](openerdirector-add-handler-to-openerdirector-error.md) · [Owning module, declaration or section: urllib.request](urllib-request-urlopen-to-urllib-request-build-opener.md) · [Owning module, declaration or section: Request Objects](request-full-url-to-request-set-proxy.md) · [Owning module, declaration or section: Request.set_proxy](request-full-url-to-request-set-proxy.md) · [Preceding source contract and version conditions](request-full-url-to-request-set-proxy.md)
