import markdown
import re
from fenced_code_plus import FencedCodePlusExtension
import unittest
import pytest

unadorned_code_block_md = """\
```
def foo():
    bar = 4
    return 8
```
"""

unadorned_code_block_html = """\
<pre><code>def foo():
    bar = 4
    return 8
</code></pre>"""

only_language_md = """\
``` python

def foo():
    bar = 4
    return 8
```
"""

only_language_html = """\
<pre><code class="python">
def foo():
    bar = 4
    return 8
</code></pre>"""

language_hl_lines_md = """\
``` python hl_lines="4 5"

def foo():
    bar = 4
    return 8
```
"""

language_hl_lines_html = """\
<pre><code class="python" data-hl_lines="4 5">
def foo():
    bar = 4
    return 8
</code></pre>"""

language_hl_lines_numbering_md = """\
``` python number hl_lines="4 5"

def foo():
    bar = 4
    return 8
```
"""

language_hl_lines_numbering_html = """\
<pre><code class="python" data-hl_lines="4 5" data-number="0">
def foo():
    bar = 4
    return 8
</code></pre>"""

just_numbering_md = """\
``` number

def foo():
    bar = 4
    return 8
```
"""

just_numbering_html = """\
<pre><code data-number="0">
def foo():
    bar = 4
    return 8
</code></pre>"""

class TestFencedCodePlus(unittest.TestCase):
    def test_just_numbering(self):
        assert markdown.markdown(just_numbering_md, extensions=[FencedCodePlusExtension()]) ==\
            just_numbering_html

    def test_language_hl_lines_numbering(self):
        assert markdown.markdown(language_hl_lines_numbering_md, extensions=[FencedCodePlusExtension()]) ==\
            language_hl_lines_numbering_html

    def test_language_hl_lines(self):
        assert markdown.markdown(language_hl_lines_md, extensions=[FencedCodePlusExtension()]) ==\
            language_hl_lines_html

    def test_unadorned_code_block(self):
        assert markdown.markdown(unadorned_code_block_md, extensions=[FencedCodePlusExtension()]) ==\
            unadorned_code_block_html

    def test_only_language(self):
        assert markdown.markdown(only_language_md, extensions=[FencedCodePlusExtension()]) ==\
            only_language_html

if __name__ == '__main__':
    pytest.main()
