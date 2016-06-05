import mistune


class DefaultRenderer(mistune.Renderer):

    def block_code(self, code, lang=None):
        code = code.rstrip('\n')
        if not lang:
            code = mistune.escape(code, smart_amp=False)
            return '<pre class="microlight"><code>%s\n</code></pre>\n' % code
        code = mistune.escape(code, quote=True, smart_amp=False)
        return '<pre class="microlight"><code class="lang-%s">%s\n</code></pre>\n' % (
            lang, code)


class _2014Renderer(DefaultRenderer):

    def header(self, text, level, raw=None):
        header = super(_2014Renderer, self).header(text, level, raw)
        if level == 3:
            return u'<section class="p2 border-box border">' + header
        return header

    def hrule(self):
        return '</section>'


def get_from_path(path):
    if path == '2014':
        return _2014Renderer()
    return DefaultRenderer()
