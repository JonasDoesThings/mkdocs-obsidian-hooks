###
### This hook strips out all obsidian-like comments from the mkdocs markdown output
###

import re

COMMENT_REGEX = r'%%(.*?)%%'

def on_page_markdown(markdown, **kwargs):
    return re.sub(COMMENT_REGEX, '', markdown, flags=re.DOTALL)