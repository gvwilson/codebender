import re

import ivy

CITE = re.compile(r'<cite>(.+?)</cite>')


def _cite(match):
    keys = [key.strip() for key in match.group(1).strip().split(',')]
    keys = [f'<a href="@root/bibliography/#{key}">{key}</a>' for key in keys]
    return f"[{','.join(keys)}]"


@ivy.events.register("init")
def cite():
    def visitor(node):
        node.text = CITE.sub(_cite, node.text)
    ivy.nodes.root().walk(visitor)
