"""
Addons for mistune
"""
import mistune, parse
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html

highlightOuter = '<div class="highlight">{}</div>'
highlightInner = parse.compile(highlightOuter)
class HighlightRendererMixin():
    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        highlighted = highlight(code, lexer, formatter)
        inner = highlightInner.parse(highlighted)[0]
        result = highlightOuter.format("\n<div class='expander'></div>\n"+inner)
        #formatter = html.HtmlFormatter(linenos=True)
        return result
