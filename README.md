This is a markdown extension that lets users add a filename and numbering to fenced code blocks in addition to the language.

intended syntax:

    ```python number=30 path="example-code.py" hl_lines="1 3"
    def shrubbery(herring):
        foo = 5
        bar = 9
        return herring.eggs
    ```

Which will produce html that looks like

    <pre><code class="python" data-hl_lines="1 3" data-number="30" data-path="example-code.py">
    def foo():
        bar = 4
        return 8
    </code></pre>


