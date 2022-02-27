---
title: "Project Checklist"
template: page
---

## Project Management

1.  A shared Google Drive with a doc called "Roles and Responsibilities"
    -   Google Doc because some collaborators aren't comfortable with Git
        -   And to make it easier to paste in figures and screenshots
    -   Defines roles and explains what each is responsible for in one page
    -   Each role has a doc of its own with its checklists
1.  The same shared Google Drive has one doc per year called (e.g.) "Progress 2022"
    -   Section headings are weekly meeting dates
        -   Table for each week with columns `Name`, `Progress`, `Plans`, and `Problems`
	-   Cells filled with short bullet points
        -   Anything too long to fit comfortably in the table is linked to an issue in the project's GitHub repository
    -   Project has a little script that lists issues and PRs touched by each person (reminder)
1.  Weekly hour-long status meeting (which often finishes early)
    -   On Tuesday so that people aren't scrambling on Friday or a weekend (or holiday Monday) to write status updates
    -   Rotating moderator: last week's moderator is this week's note-taker
    -   At start of meeting, members star points in the status doc they want to discuss
    -   Moderator amends agenda based on starred items
1.  Proposals can be done as either Google Docs (in shared folder) or GitHub issues
    -   Must be flagged to moderator the day before the meeting for inclusion
    -   Added to agenda
1.  Project has a single repo with code, website, tutorials, etc.
    -   So that releases are in sync
1.  Uses Google Docs for publicity materials (again, because non-programmers)
    -   All materials are owned by project account, not personal accounts
    -   Every change larger than a typo produces a new doc
    -   Every doc has date in title, e.g., "University Press Release 2022-05-13"
1.  Budgets for grant proposals, job contracts, etc., are stored in university system
    -   Legal requirement
1.  `GOVERNANCE.md` in root directory of project explains Martha's Rules
    -   And membership rule:
        anyone who has had a PR merged in the last year or made some other significant contribution
	as determined by majority vote
    -   List of active members and alumni is in the foot of `GOVERNANCE.md`
1.  Another small script checks that the tags in each project repository are consistent
    and that each issue has at least one tag
1.  Project website has a "skills ladder" on the "Positions" page (even when positions aren't open)
    -   "What we mean by each of these terms for the research and coding tracks"
1.  Project website has a value statement and a contact address that *isn't* anyone's personal address
    -   Plus a page for publications
    -   Plus a page pointing at all repositories
    -   Plus a "Getting Started" page
    -   And a "Who's Using Us How" page
    -   And a "People" page
1.  The "help" option for the software includes the URL to the project page

## Setup

1.  Create a mailing list for the project.
    -   The team voted 2:1 for email over Slack because they want better search and fewer interruptions.
1.  Create a new GitHub organization for the project and add everyone to it.
    -   So that nothing belonging to the project is under a personal account.
1.  Create a new repo within that GitHub organization.
    -   Everything is in one repo for now, but that might change.
1.  Redefine the tags in that repo.
    -   Governance: `discussion` (including questions) and `proposal` (for votable items).
    -   Issues: `bug` and `request`.
    -   Pull requests: `fix`, `enhancement`, `docs`, and `refactor`.
    -   Meta: `paused`, `helped wanted`, `good first issue`.
1.  Add `README`, `LICENSE`, `CODE_OF_CONDUCT`, `GOVERNANCE`, `Makefile`, and `.gitignore` to the repo.
    -   We settled on Make because nobody could agree on what to use instead.
1.  Create two `pip` requirements files:
    -   `requirements.txt` is a minimal setup for using the software.
    -   `development.txt` sources that and adds everything needed for building, testing, and documenting.
1.  Create `socks`, `docs`, and `tests` directories in the root of the repo along with a `setup.py` file.
    -   Pretty standard structure for a `pip`-installable Python package (and no, "socks" isn't its real name).
1.  Set up `pytest` for running tests and `pdoc` for building documentation.
    -   `tests/conftest.py` for `pytest`.
    -   A docstring in every `__init__.py` file (rather than leaving it empty) to make `pdoc` happy.
    -   Use [Google-style docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings).
1.  Add targets to `Makefile` to:
    -   Build the package.
    -   Run the tests.
    -   Run the tests with coverage and display the coverage report (to identify untested code).
    -   Rebuild the documentation.
    -   Run `flake8`, `black`, and `isort` to check that the code meets style guidelines.
1.  Add a `workflow.yml` file with pre-commit checks.
1.  Use [Ivy](https://www.dmulholl.com/docs/ivy/dev/) to turn hand-written documentation into HTML.
    -   The team has Markdown design notes and the beginnings of a tutorial that they want to put beside the `pdoc` docs.
    -   And a `glossary.md` file in [glosario](https://github.com/carpentries/glosario) format.
1.  Add a `data` directory with sample data for testing and a couple of real datasets.
    -   Each dataset is in its own subdirectory with a `MANIFEST.yml` file describing files, columns, provenance, etc.
1.  Add a `CITATION.cff` file with citation information.
    -   And make sure every contributor has an ORCID.
1.  Add a `bin` directory at the top level with various utility scripts.
    -   Most of which use the code in the `socks` directory directly (rather than through a local install of the package).
1.  Add a `results` directory at the top level with one sub-directory for each paper.
    -   Each sub-directory under `results` has its own `Makefile`.
    -   `make all` in the project sub-directory regenerates everything.
    -   We haven't added a [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/) template yet, but we will.
1.  Add a short Ivy extension to convert CSV files to HTML.
1.  Add a `static` directory with some CSS and JavaScript files.
    -   Because everyone wants their HTML tables to be dynamically sortable…
1.  Add a BibTeX file to the root `results` directory to be used by all project papers.
    -   And another Ivy extension to convert it to HTML using [Pybtex](https://pybtex.org/).
1.  Write a short code review checklist.
    -   How to run pre-commit checks, how and why to use the `logging` library, what exceptions to use for what, etc.
1.  Add a small utility script for loading program configurations.
    -   In order: system config, personal config, project config, config file specified on the command line, command-line flags.
1.  Choose a project logo.
    -   Which made the rest of the discussion look calm and rational…
