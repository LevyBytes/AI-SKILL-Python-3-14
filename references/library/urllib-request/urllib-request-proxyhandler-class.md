# urllib.request: `urllib.request.ProxyHandler`

*class *urllib.request.ProxyHandler(*proxies=None*)

Route requests through a proxy. When *proxies* is supplied, it must be a dictionary mapping protocol names to proxy URLs. By default the proxy list is read from the `<protocol>_proxy` environment variables. When no proxy environment variables exist, proxy settings come from the registry's Internet Settings section in a Windows environment, and from the System Configuration Framework in a macOS environment.

Pass an empty dictionary to switch off autodetected proxies.

The `no_proxy` environment variable serves to name hosts that should not be reached through a proxy; once set, its value is a list of hostname suffixes separated by commas, each optionally followed by `:port`, such as `cern.ch,ncsa.uiuc.edu,some.host:8080`.

Note

`HTTP_PROXY` will be ignored if a variable `REQUEST_METHOD` is set; see the documentation on `getproxies()`.

[Subject index](INDEX.md) · [Previous](urllib-request-httpcookieprocessor-class.md) · [Continue](urllib-request-httppasswordmgr-class.md) · [Owning module, declaration or section: urllib.request](urllib-request-urlopen-to-urllib-request-build-opener.md)
