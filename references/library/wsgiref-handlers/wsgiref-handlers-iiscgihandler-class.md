# wsgiref.handlers: `wsgiref.handlers.IISCGIHandler`

*class *wsgiref.handlers.IISCGIHandler

A specialized variant of `CGIHandler`, meant for deployments on Microsoft’s IIS web server where the config allowPathInfo option (IIS>=7) or the metabase allowPathInfoForScriptMappings (IIS<7) has not been set.

Out of the box, IIS supplies a `PATH_INFO` that repeats the `SCRIPT_NAME` at the start, which trips up WSGI applications attempting to implement routing. This handler removes any such duplicated path.

IIS can be set up to deliver the right `PATH_INFO`, but doing so surfaces another bug in which `PATH_TRANSLATED` is wrong. Fortunately that variable sees little use and isn’t guaranteed by WSGI. On IIS<7, however, the setting is only adjustable at the vhost level, which touches all the other script mappings — many of which break once exposed to the `PATH_TRANSLATED` bug. That’s why IIS<7 is hardly ever deployed with the fix (and even IIS7 seldom applies it, since there’s still no UI for it.).

CGI code has no way of knowing whether the option was enabled, hence a distinct handler class is supplied. You use it just as you would `CGIHandler`, that is, by calling `IISCGIHandler().run(app)`, where `app` is the WSGI application object you intend to invoke.

Added in version 3.2.

[Subject index](INDEX.md) · [Previous](wsgiref-handlers-cgihandler-class.md) · [Continue](wsgiref-handlers-basecgihandler-class.md) · [Owning module, declaration or section: wsgiref.handlers](wsgiref-handlers-cgihandler-class.md)
