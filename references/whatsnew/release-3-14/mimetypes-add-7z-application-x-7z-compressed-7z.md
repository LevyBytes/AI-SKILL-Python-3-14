# Python 3.14 changes: Archive, Android and application MIME additions

- Add 7z `application/x-7z-compressed` (`.7z`)

  - Add Android Package `application/vnd.android.package-archive` (`.apk`) when not strict

  - Add deb `application/x-debian-package` (`.deb`)

  - Add glTF binary `model/gltf-binary` (`.glb`)

  - Add glTF JSON/ASCII `model/gltf+json` (`.gltf`)

  - Add M4V `video/x-m4v` (`.m4v`)

  - Add PHP `application/x-httpd-php` (`.php`)

  - Add RAR `application/vnd.rar` (`.rar`)

  - Add RPM `application/x-rpm` (`.rpm`)

  - Add STL `model/stl` (`.stl`)

  - Add Windows Media Video `video/x-ms-wmv` (`.wmv`)

  - De facto: Add WebM `audio/webm` (`.weba`)

  - [ECMA-376](https://ecma-international.org/publications-and-standards/standards/ecma-376/): Add `.docx`, `.pptx` and `.xlsx` types

  - [OASIS](https://docs.oasis-open.org/office/v1.2/cs01/OpenDocument-v1.2-cs01-part1.html#Appendix_C): Add OpenDocument `.odg`, `.odp`, `.ods` and `.odt` types

  - [W3C](https://www.w3.org/TR/epub-33/#app-media-type): Add EPUB `application/epub+zip` (`.epub`)

(This work came from Sahil Prajapati together with Hugo van Kemenade across [gh-84852](https://github.com/python/cpython/issues/84852); from Sasha “Nelie” Chernykh together with Hugo van Kemenade across [gh-132056](https://github.com/python/cpython/issues/132056); and from Hugo van Kemenade across [gh-89416](https://github.com/python/cpython/issues/89416), [gh-85957](https://github.com/python/cpython/issues/85957), plus [gh-129965](https://github.com/python/cpython/issues/129965).)

[Subject index](INDEX.md) · [Previous source section](mimetypes-opentype-layout-otf-font-otf.md) · [Next source section](multiprocessing.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](mimetypes-mimetypes.md) · [Preceding release/subject continuation](mimetypes-mimetypes.md)
