# webbrowser - Browser controller objects

### Browser controller objects

Each browser controller exposes the `name` attribute together with the three methods below, which mirror the convenience functions offered at module level:

 controller.name

The browser's name, which depends on the system.

 controller.open(*url*, *new=0*, *autoraise=True*)

Show *url* via the browser this controller manages. With *new* set to 1, a fresh browser window opens where it can; with *new* set to 2, a fresh browser page (a “tab”) opens where it can.

 controller.open_new(*url*)

Where feasible, open *url* in a fresh window of the browser this controller manages; otherwise, open *url* in the lone browser window. This aliases `open_new()`.

 controller.open_new_tab(*url*)

Where feasible, open *url* in a fresh page (a “tab”) of the browser this controller manages; if not, the behavior is the same as `open_new()`.

Footnotes

[Subject index](INDEX.md) · [Previous](webbrowser-register.md) · [Continue](../windows/ms-windows-specific-services.md) · [Owning module, declaration or section: webbrowser](webbrowser-convenient-web-browser-controller.md)
