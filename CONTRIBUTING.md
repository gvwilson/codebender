---
layout: page
permalink: /contributing/
title: "Contributing"
---

Contributions of all kind are welcome,
from bug reports and suggestions for improvements to new material.

1.  All contributors must abide by our [Code of Conduct](../conduct/).
2.  By submitting a pull request,
    you agree that your contribution can be reshared
    under the [CC-BY License](../license/).

## Making Decisions

This project uses Martha's Rules for consensus decision making <cite>Minahan1986</cite>:

1.  Before each meeting, anyone who wishes may sponsor a proposal by filing an
    issue in the GitHub repository tagged `discuss`.  Proposals must be filed
    at least 24 hours before a meeting in order to be considered at that
    meeting, and must include:
    -   a one-line summary (the subject line of the issue)
    -   the full text of the proposal
    -   any required background information
    -   pros and cons
    -   possible alternatives

2.  A quorum is established in a meeting if half or more of voting members are
    present.

3.  Once a person has sponsored a proposal, they are responsible for it.  The
    group may not discuss or vote on the issue unless the sponsor or their
    delegate is present.  The sponsor is also responsible for presenting the
    item to the group.

4.  After the sponsor presents the proposal, a sense vote is cast for the
    proposal prior to any discussion:
    -   Who likes the proposal (thumbs up)?
    -   Who can live with the proposal (thumbs sideways)?
    -   Who is uncomfortable with the proposal (thumbs down)?

5.  If all of the group likes or can live with the proposal, it passes
    immediately.

6.  If most of the group is uncomfortable with the proposal, it is postponed for
    further rework by the sponsor.

7.  Otherwise, members who are uncomfortable can briefly state their objections.
    A timer is then set for a brief discussion moderated by the facilitator.
    After 10 minutes or when no one has anything further to add (whichever comes
    first), the facilitator calls for a yes-or-no vote on the question: "Should
    we implement this decision over the stated objections?"  If a majority votes
    "yes" the proposal is implemented.  Otherwise, the proposal is returned to
    the sponsor for further work.

## Setting up

1.  Clone <https://github.com/gvwilson/codebender/>.

1.  Run `pip install -r requirements.txt` to install the Python packages used
    by the tools in `./bin`.

1.  [Install Jekyll](https://jekyllrb.com/docs/installation/) to preview
    changes locally.

## Formatting

1.  The commands to rebuild the site, run a server for local preview, and
    check internal consistency are stored in `Makefile` and use the tools in
    `bin/`. Run `make` on its own to get a list of available actions.

1.  Each chapter or appendix is identified by a slug such as `some-topic`.  Its
    text lives in <code><em>slug</em>/index.md</code>
    or <code><em>slug</em>/index.html</code>, and there is an entry
    under the `chapters` key in `_config.yml` with its slug and its title. This
    list controls ordering.

1.  Use only level-2 headings within chapters and appendices and use "Sentence
    case" for the titles.

1.  To create cross-references:
    -   Use `{% raw %}[text](g#key){% endraw %}` for glossary entries.
        The key must appear in `_data/glossary.yml`.
    -   Use `{% raw %}[text](../slug/){% endraw %}` to link to a chapter
        or appendix.
    -   Use `{% raw %}<cite>key,key</cite>{% endraw %}` for bibliography
        citations.  The keys must appear in `./codebender.bib`.

1.  To create a figure, put the image file in the same directory as the chapter
    or appendix and use this to include it:

    ```
    {% raw %}{% include figure id="label" img="file.svg" alt="short text" width="xx%" %}{% endraw %}
    ```

    The `width` field is optional.
