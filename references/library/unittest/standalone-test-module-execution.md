# unittest — Organizing test code — Contract: You can run the test module on its own from the command line.

- You can run the test module on its own from the command line.

- It becomes easier to keep the test code apart from the code you ship.

- There's less of a pull to bend test code to match the code under test without a sound reason.

- Test code ought to change far less often than the code it tests.

- Refactoring the tested code becomes easier.

- Tests covering modules written in C have to live in separate modules regardless, so consistency argues for the same treatment everywhere.

- Should the testing strategy shift, there's no call to touch the source code.

[Subject index](INDEX.md) · [Previous](test-code-organization-overview.md) · [Continue](re-using-old-test-code.md) · [Owning module, declaration or section: unittest](unittest-unit-testing-framework.md) · [Owning module, declaration or section: Organizing test code](test-code-organization-overview.md)
