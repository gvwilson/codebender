# Contributing

Contributions are very welcome;
please contact us [by email][email] or by filing an issue in [our repository][repo].
All contributors must abide by our [Code of Conduct](./CODE_OF_CONDUCT.md).

## Setup and Operation

-   Install [uv][uv].
-   Create a virtual environment by running `uv venv --python 3.12` in the root directory.
-   Activate it by running `source .venv/bin/activate` in your shell.
-   Install dependencies by running `uv sync`.
-   This project uses [McCole][mccole] to generate HTML and check the project's structure
-   Run `make` on its own to see a list of common commands

| make task | effect                            |
| --------- | ----------------------------------|
| build     | render HTML pages                 |
| clean     | clean up                          |
| commands  | show available commands (default) |
| links     | check links in published site     |
| lint      | check structure and content       |
| serve     | serve generated HTML              |

## Structure

-   Lessons are in `nn_slug` directories
    -   `nn` is two-digit sequence number
    -   `slug` is short mnemonic
    -   Each lesson must have an `index.md` file containing its content
-   Diagrams should be SVG files created with [draw.io][draw-io]
-   `bibliography.md` has the bibliography as a definition list
    -   Citation keys have IDs for linking
    -   Use an inline HTML link `b:key` in files to create links
-   `glossary.md` has the glossary as definition list
    -   Reference keys have IDs for linking
    -   Use an inline HTML link `g:key` in files to create links
-   The `static` directory contains static files
-   The `templates` directory contains [Jinja][jinja] templates used to generate HTML
    -   `page.html`: template for website pages

## FAQ

Do you need any help?
:   Yes—please see the issues in [our repository][repo].

What sort of feedback would be useful?
:   Everything is welcome,
    from pointing out mistakes in the code to suggestions for better explanations.

Can I add a new section?
:   Absolutely, but please [reach out][email] before doing so.

Why is this material free to read?
:   Because if we all give a little, we all get a lot.

## <a id="contributors">Contributors</a>

-   [*Greg Wilson*][wilson-greg] is a programmer, author, and educator based in Toronto.
    He was the co-founder and first Executive Director of Software Carpentry
    and received ACM SIGSOFT's Influential Educator Award in 2020.

[draw-io]: https://www.drawio.com/
[email]: mailto:gvwilson@third-bit.com
[jinja]: https://jinja.palletsprojects.com/
[mccole]: https://pypi.org/project/mccole/
[repo]: https://github.com/gvwilson/change
[uv]: https://github.com/astral-sh/uv
[wilson-greg]: https://third-bit.com/
