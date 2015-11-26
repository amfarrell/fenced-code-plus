import markdown
import re
from extended_code_plus import FencedCodePlusExtension
test_md = """\
and so you will want to use the following:

``` python hl_lines="4 5" number

def foo():
    bar = 4
    return 8


```

but don't avoid that
"""
print(markdown.markdown(test_md, extensions=[FencedCodePlusExtension()]))

FENCED_BLOCK_RE = re.compile(r'''
(?P<fence>^(?:~{3,}|`{3,}))[ ]*
(?P<code>.*?)(?<=\n)
(?P=fence)[ ]*$''', re.MULTILINE | re.DOTALL | re.VERBOSE)

