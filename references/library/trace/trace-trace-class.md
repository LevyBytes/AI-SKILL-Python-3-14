# trace: `trace.Trace`

### Programmatic Interface

 *class *trace.Trace(*count=1*, *trace=1*, *countfuncs=0*, *countcallers=0*, *ignoremods=()*, *ignoredirs=()*, *infile=None*, *outfile=None*, *timing=False*)

Make an object that traces how a lone statement or expression executes. Every parameter is optional. *count* switches on counting of line numbers. *trace* switches on line-by-line execution tracing. *countfuncs* switches on a listing of the functions invoked during the run. *countcallers* switches on tracking of call relationships. *ignoremods* names a list of modules or packages to skip. *ignoredirs* names a list of directories whose modules or packages get skipped. *infile* is the file to read previously stored count information from. *outfile* is the file to write refreshed count information into. *timing* switches on showing a timestamp measured from when tracing began.

[Subject index](INDEX.md) · [Previous](filters.md) · [Continue](trace-trace-run-to-trace-trace-results.md) · [Owning module, declaration or section: trace](coverage-py.md)
