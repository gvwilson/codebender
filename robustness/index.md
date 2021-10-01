---
layout: page
---

Robust software is software that works for people other than the
original author, on machines other than its creators'. More
specifically:

- it can be installed on more than one computer with relative ease,
- it works consistently as advertised, and
- it can be integrated with other tools.

These rules from <cite>Taschuk2017</cite> will help ensure that
what you build can do these things.

## 1. Use version control

Put everything created manually into version control as soon as it is
created, including programs, original field observations, and the
source files for papers. Files that can be regenerated at need, such
as compiled programs or intermediate files generated during data
analysis, should not be versioned; instead, use an archiving system
for them and store the metadata describing their contents in version
control.

## 2. Explain how to use your code

[Documentation](../communication/) explaining what you have is welcome,
but almost everyone starts by copying and modifying examples.
[tldr.sh](https://tldr.sh/) and similar sites are good examples to follow.

## 3. Make common operations easy to control

1. Allow the most commonly changed parameters to be configured from the command line
   so that people can drive your code with shell scripts and other glue.

2. Check that all input values are in a reasonable range at startup:
   few things are as annoying as having a program announce after running
   for two hours that it isn't going to save its results because the
   requested directory doesn't exist.

3. Choose reasonable defaults where they exist but
   set no defaults at all when there aren't any reasonable ones.
   (And check that what's reasonable for you is reasonable for other people.)

4. *Never* hard-code changeable values:
   if people have to edit your software in order to run it,
   you have done something wrong.

5. Allow people to control the program using configuration files.
   This is better for rarely-changed values than adding another obscure command-line flag,
   and configuration files can be archived or put in version control
   along with results
   to ensure reproducibility.

## 4. Version your releases

1. Use [semantic versioning](g#semantic-versioning),
   i.e.,
   give every release of the software a version number of the form
   `major.minor` or `major.minor.patch`.
   `major` is incremented when significant features are added
   or changes break backward compatibility;
   changes to `minor` represent incremental improvements,
   while `patch` is updated for minor bug fixes and the like.

2. Display the version of the software when people use the `--v` or `--version` flag
   on the command line,
   and include the full version number in all of the program's output
   (particularly debugging traces).

3. Ensure that old releases continue to be available.
   This can be done by adding a tag to your version control repository,
   creating a release on GitHub,
   or deploying your software on [CRAN](https://cran.r-project.org/)
   or [PyPI](https://pypi.org/).

## 6. Use build tools and package manager

Use whatever [build manager](g#build-manager) your language expects:
`pip` or `conda` for Python,
`devtools` for R,
and so on.
You should also organize code and files the way that build tool expects,
which we discuss [here](../mechanics/).

The converse of this is that you should avoid depending on scripts and
tools which are not available as packages. In many cases, a program's
author may not realize that some tool was built locally, and doesn't
exist elsewhere. At present, the only sure way to discover such
unknown dependencies is to install on a system administered by someone
else and see what breaks.

## 7. Do not require special privileges

Installing or running with root privileges is often convenient,
since it automatically bypasses safety checks.
However, those checks are there for a reason:
scientific software packages may not intentionally be malware,
but one small bug or over-eager file-matching expression
can certainly make them behave as if they were.
Outside of very unusual circumstances,
packages should not require root privileges to set up or use.

People may also want to try out a new package before installing it system-wide on a cluster.
Requiring root privileges will frustrate such efforts,
as will hard-coded installation paths.

## 8. Eliminate hard-coded paths

And speaking of hard-coded paths:
it's easy to write software that always reads a file called `mydata.csv`,
but it's also very limiting.
People should therefore be able to set the names and locations of input and output files
as command-line parameters.
This rule applies to reference data sets as well as the user's own data:
if someone wants to try a new gene identification algorithm
using a different set of genes as a training set,
they should not have to edit the software to do so.

To save typing,
it is often convenient to allow users to specify an input or output directory
and then require that there be files with particular names in that directory.
This practice is an example of *convention over configuration*,
and is used by many frameworks such as WordPress to reduce complexity.

## 9. Include sanity tests

Every package should come with a set of tests people can run after installation
to ensure the software works,
and to serve as an example of how to use it.
Make sure these tests are easy to find:
a script in the project's root directory named `runtests.sh` is hard to miss.

And make sure the test script's output easy to interpret.
Screens full of correlation coefficients do not qualify:
instead, the script's output should be one line per test
with the test's name and its pass/fail status,
followed by a single summary line saying
how many tests were run and how many passed or failed.

## 10. Produce identical results for identical inputs

A particular version of a program should produce the same results every time it is run
with the same parameters and input data;
without this,
testing and debugging (and reproducibility) are effectively impossible.

However,
even minor changes to code can cause minor changes in output because of floating-point issues,
and many applications rely on randomized algorithms to improve performance or runtimes.
These problems can be tackled by:

1. Specifying explicit tolerances in tests,
   such as "actual value is within 1% of expected value".
   Error bars are normal in most experimental sciences;
   they are useful in computational work as well.

2. Allow (or require) people to provide the random number seed as a parameter
   so that the program's output is deterministic for those cases where it matters.

## 11. Use a logging library

A [logging](g#logging) library lets you leave `print` statements in your code
but turn them on or off selectively.
It also lets you send output to multiple destinations,
so that you can combine messages from several programs in a data analysis pipeline while debugging.

In order of increasing severity,
the usual logging levels are:

- `DEBUG`: very detailed information used for localizing errors.
- `INFO`: confirmation that things are working as expected.
- `WARNING`: something unexpected happened, but the program will keep going.
- `ERROR`: something has gone badly wrong, but the program hasn't hurt anything.
- `CRITICAL`: potential loss of data, security breach, etc.

Many programs allow users to specify logging levels and log filenames as command-line parameters.
At its simplest,
a single flag changes the logging level from `WARNING` (the usual default)
to `DEBUG` (the noisiest level).
Another flag can tell the logging library to send messages to a centralized logging server,
or to a rotating file
so that the system always has messages from the last few hours
but doesn't fill up the disk.
You don't need any of these when you start,
but the data engineers and system administrators
who eventually have to install and maintain your programs
will be very grateful if this is place.
