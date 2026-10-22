# Openers and Handlers

### Openers and Handlers

Retrieving a URL means working through an opener — an instance of the somewhat awkwardly named [`urllib.request.OpenerDirector`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.OpenerDirector). Up to now we've leaned on the default opener by way of `urlopen`, yet you're able to build your own. Openers rely on handlers, and it's the handlers that perform all the “heavy lifting”. A given handler understands how to open URLs for one particular URL scheme (http, ftp, and so on), or how to manage some facet of opening URLs — HTTP redirections or HTTP cookies, say.

Building your own opener becomes worthwhile when you want to fetch URLs with certain handlers in place — for example, to obtain an opener that deals with cookies, or one that declines to follow redirections.

Making an opener is a matter of instantiating an `OpenerDirector` and then invoking `.add_handler(some_handler_instance)` as many times as needed.

A second option is `build_opener`, a convenience routine that produces opener objects in a single call. By default `build_opener` installs a handful of handlers, while still giving you a fast way to tack on extras and/or supersede the defaults.

Still other handlers you might reach for cover proxies, authentication, and further common-but-somewhat-specialized cases.

You can promote an `opener` object to the (global) default opener with `install_opener`, after which every `urlopen` call will route through the opener you've put in place.

Each opener object carries an `open` method you can call straight away to fetch urls exactly as the `urlopen` function does — there's no requirement to call `install_opener` beyond convenience.

[Subject index](INDEX.md) · [Previous source context](info-and-geturl.md) · [Following source context](basic-authentication.md)
