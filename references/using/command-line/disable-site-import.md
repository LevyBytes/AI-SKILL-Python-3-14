# -S

-S

Skip importing the [`site`](https://docs.python.org/3.14/library/site.html#module-site) module along with the site-dependent adjustments to [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) that come with it. These adjustments stay off as well if `site` is imported explicitly afterward (invoke [`site.main()`](https://docs.python.org/3.14/library/site.html#site.main) should you want to trigger them).

[Subject index](INDEX.md) · [Previous source section](disable-user-site.md) · [Following source section](unbuffered-streams.md)
