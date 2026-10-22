# Introduction

### Introduction

**urllib.request** is the Python module you reach for when you need to retrieve URLs (Uniform Resource Locators). Its most basic entry point is the *urlopen* function, which keeps things straightforward while still being able to pull URLs over many different protocols. On top of that it exposes a somewhat richer interface for the cases you run into often — think basic authentication, cookies, proxies, and the like — and those capabilities come from objects known as handlers and openers.

Across a wide range of “URL schemes” (the part of a URL that comes before the `":"` — so, for instance, `"ftp"` is the scheme in `"ftp://python.org/"`), urllib.request can fetch resources by speaking the matching network protocol (FTP, HTTP, and others). Here we'll concentrate on HTTP, since that's the case you'll meet most.

When the situation is uncomplicated, *urlopen* is a breeze to work with. The moment you run into errors or trickier scenarios while opening HTTP URLs, though, you'll want at least a working grasp of the HyperText Transfer Protocol. For HTTP, the definitive and most thorough reference is [**RFC 2616**](https://datatracker.ietf.org/doc/html/rfc2616.html) — a technical specification that was never written to be a light read. The goal of this HOWTO is to walk you through *urllib* while supplying just enough HTTP background to get you by. Rather than standing in for the [`urllib.request`](https://docs.python.org/3.14/library/urllib.request.html#module-urllib.request) documentation, it accompanies it.

[Subject index](INDEX.md) · [Previous source context](howto-fetch-internet-resources-using-the-urllib-package.md) · [Following source context](fetching-urls.md)
