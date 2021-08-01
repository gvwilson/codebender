---
layout: page
---

The [FAIR Principles](g#fair) encourage researchers to make data findable,
accessible interoperable, and reusable <cite>Wilkinson2016</cite>.
The tips below, taken from <cite>Lin2020</cite>, will
help you turn those principles into practice.

## 1. Design for a wide range of users

You might think only a few experts know your field well enough to care
about your data, newcomers also need to use your work to gain
experience, and other people may access your work in translation or
via a screen reader.  Establish context, to use clear and concise
language, and minimize the use of jargon.

## 2. Design with the end in mind

Think ahead about the things you would want to be found at the
completion of the project, including relevant preprints, and then
decide what should go where. For example:

- Finalized laboratory data can be stored in [Dryad](https://datadryad.org/) so that you can
  cite the same data source in multiple publications with a single
  DOI.
 
- Lab protocols can be maintained in [Protocols.io](https://www.protocols.io/) so that future
  collaborators can find them using a [DOI](g#doi) while keeping incomplete
  protocol drafts private.

- Analysis code can be deposited in [Zenodo](https://zenodo.org/), which you can cite and
  update as code evolves.

- Research manuscripts can be posted to sites like [arXiv](https://arxiv.org/).
  
- Your [ORCID](g#orcid) can be linked to each of the DOIs created by these
  repositories.

## 3. Use textual structure

A key part of searching the web is scanning the text returned by
search engines to see if it contains target information.  Textual
structure helps that process: formatted headers (rather than just
enlarged text), bulleted or numbered lists, and highlighted terms all
make both the information and its structure easier to understand.
Other examples include:

- GitHub allows users to add tags to issues and commit messages which
  can then be searched across projects.

- Electronic lab notebooks can use XML schemas like [Darwin Core](https://www.tdwg.org/standards/dwc/).

- Using specific Google Docs heading levels creates a table of
  contents in real time, visible when the file is open.

- CSV files do not have a standard way to store metadata, but authors
  commonly created a README or MANIFEST file that describes the
  structure and content of the files in a collection.

## 4. Add metadata

All modern operating systems allow you to add information to the
properties of a file or directory. Databases, word processors, and
website construction programs also have built-in metadata
capabilities, though application-specific metadata can quickly become
inconsistent. Creating a list of terms and writing a small program to
check that only terms from that list goes a long way toward preventing
this.

## 5. Use search and browsing

People search *and* browse when they're trying to find information, so
design for both. As people browse, they build a mental map of the
content they could possibly find, then search based on that map.  You
should therefore make information accessible both ways and make it
easy to move from searching to browsing and back again. Tags and other
metadata help with searching, while structural clues tell users about
the content contained in the information they are looking at.

## 6. Mimic real world directions

File paths and breadcrumb trails on websites give users a sense of
where information is and suggest new paths they can take. For example,
the URLs of a website might all include the name of a section of the
site, such as `/papers/` or `/blog/`, while DOIs and ORCIDs serve as
beacons that people can always get back to.

Research shows that people scan but don't read: they click on the
first close thing they see and give up very, very quickly.  Markers
and directions should therefore be as consistent as highway signs with
regards to appearance, style, and type of information.

## 7. Use meaningful names

Filenames and URLs are the one kind of metadata you can't avoid
creating, so always choose ones that are human-readable and that
convey information about what they name, both when navigated to *and*
when returned in search results. For example, it's easy to call a
paper `nature2021.pdf`, but since other people will publish papers
there that year, a longer name like `wilson-managing-rse-plos-2021.pdf
will convey more information at a glance and retain that information
after the paper has been downloaded and put in a folder with dozens of
others.

Remember that the more generic a term is, the harder it is to search
for. A quick test is to search for the name before adopting it: if
dozens of unrelated results come up, you may want to pick a different
name.

## 8. Use tags

After meaningful names, tags are the easiest and most effective
metadata you can create. Most tools support tagging, and most search
tools use them to narrow the scope of queries.  This means that you
can now file a single thing in multiple "locations", which was not
possible in the pre-digital era. Multiple tags also assist users from
varied backgrounds because the terms can be customized to be inclusive
of a diverse set of users.

Where possible, used established subject terms taken from article
databases, data repositories, and library catalogs that you and your
users might already be familiar with, such as the National Cancer
Institute (NCI) Thesaurus and the Medical Subject Headings (MeSH).

## 9. Understand the difference between format and subject

Format describes what your content *is*, while subject describes what
it is *about*: for example, this *is* a web page, but it is *about*
making information findable. You can rely on filename suffixes to
distinguish computational notebooks from PDF files, tabular data sets,
or slide decks, but should use tagging, a filename convention, or a
description in a README to tell people whether the contents are raw
information, tidied-up data, or an aggregation of several underlying
datasets.

Since file formats can change (e.g., slides can be printed as a PDF),
naming and metadata conventions tend to be more robust as well as more
informative than relying on file types. Once again, structural clues
can help: a folder specifically for conference presentations may
contain one sub-folder for each presentation, which in turn contains
the PowerPoint and PDF versions of the presentation with exactly the
same names but different filetype suffixes.

## 10. Do not abbrvt

Acronyms and abbreviations make communication between those who know
them more efficient at the price of making them less accessible to
newcomers. Spell out acronyms and abbreviations that you take for
granted (or hyperlink to their definitions), but remember that
acronyms are often repurposed by different professions or disciplines,
so write them *all* out the first time they appear or point to a
glossary.
