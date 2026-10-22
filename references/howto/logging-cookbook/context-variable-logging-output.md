# Context-variable logging output

```shell
~/logging-contextual-webapp$ python main.py
app1 processed 51 requests
app2 processed 49 requests
~/logging-contextual-webapp$ wc -l *.log
  153 app1.log
  147 app2.log
  300 app.log
  600 total
~/logging-contextual-webapp$ head -3 app1.log
Thread-3 (process_request) app1 __main__  jim    192.168.3.21 POST Request processing started
Thread-3 (process_request) app1 webapplib jim    192.168.3.21 POST Hello from webapplib!
Thread-5 (process_request) app1 __main__  jim    192.168.3.21 POST Request processing started
~/logging-contextual-webapp$ head -3 app2.log
Thread-1 (process_request) app2 __main__  sheila 192.168.2.21 GET  Request processing started
Thread-1 (process_request) app2 webapplib sheila 192.168.2.21 GET  Hello from webapplib!
Thread-2 (process_request) app2 __main__  jim    192.168.2.20 GET  Request processing started
~/logging-contextual-webapp$ head app.log
Thread-1 (process_request) app2 __main__  sheila 192.168.2.21 GET  Request processing started
Thread-1 (process_request) app2 webapplib sheila 192.168.2.21 GET  Hello from webapplib!
Thread-2 (process_request) app2 __main__  jim    192.168.2.20 GET  Request processing started
Thread-3 (process_request) app1 __main__  jim    192.168.3.21 POST Request processing started
Thread-2 (process_request) app2 webapplib jim    192.168.2.20 GET  Hello from webapplib!
Thread-3 (process_request) app1 webapplib jim    192.168.3.21 POST Hello from webapplib!
Thread-4 (process_request) app2 __main__  fred   192.168.2.22 GET  Request processing started
Thread-5 (process_request) app1 __main__  jim    192.168.3.21 POST Request processing started
Thread-4 (process_request) app2 webapplib fred   192.168.2.22 GET  Hello from webapplib!
Thread-6 (process_request) app1 __main__  jim    192.168.3.21 POST Request processing started
~/logging-contextual-webapp$ grep app1 app1.log | wc -l
153
~/logging-contextual-webapp$ grep app2 app2.log | wc -l
147
~/logging-contextual-webapp$ grep app1 app.log | wc -l
153
~/logging-contextual-webapp$ grep app2 app.log | wc -l
147

```

Output belongs to the [context-variable request example](imports-request-data-formatter-and-context-variables.md). Counts and thread ordering are sample run results.

[Subject index](INDEX.md).
