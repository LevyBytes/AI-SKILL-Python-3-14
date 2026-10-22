# Adding contextual information to your logging output

### Adding contextual information to your logging output

There are times when you'd like your logging output to carry contextual details beyond just the parameters supplied to the logging call. As an example, in a networked application it can be useful to record client-specific details in the log (such as the remote client's username or IP address). The *extra* parameter is one way to accomplish this, though passing the information through that channel isn't always convenient. Creating [`Logger`](https://docs.python.org/3.14/library/logging.html#logging.Logger) instances per connection might look appealing, but it's a poor approach since such instances never get garbage collected. That isn't an issue under normal use, yet when the count of `Logger` instances scales with the level of granularity you want for logging an application, things can become difficult to manage once the number of `Logger` instances grows effectively without bound.

[Subject index](INDEX.md) · [Previous source context](running-a-logging-socket-listener-in-production.md) · [Following source context](using-loggeradapters-to-impart-contextual-information.md)
