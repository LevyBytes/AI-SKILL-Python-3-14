# Introduction

### Introduction

C and C++ developers can reach into the Python interpreter through the Application Programmer's Interface to Python, which exposes that interpreter at several different levels. Although it works just as well from C++, this interface is most often called the Python/C API for the sake of conciseness. People reach for the Python/C API for two essentially distinct purposes. One purpose is to author *extension modules* aimed at particular goals; these C modules build additional capability onto the Python interpreter. That is likely the use you'll encounter most often. The other purpose is to treat Python as one piece inside some bigger program; this approach is usually described as *embedding* Python within an application.

Building an extension module follows a fairly well-charted path, and a "cookbook" style of working serves you nicely. A number of utilities will handle parts of the job automatically. Although developers have been embedding Python into other programs ever since the language first appeared, embedding Python tends to be trickier than building an extension.

A great many API functions stay useful no matter whether you are embedding or extending Python; what's more, nearly every program that embeds Python also has to supply a bespoke extension, so getting comfortable with extension authoring before you try to embed Python in an actual application is generally wise.

[Subject index](INDEX.md) · [Following source contract](language-version-compatibility.md)
