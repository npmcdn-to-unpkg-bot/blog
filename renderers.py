import mistune


class DefaultRenderer(mistune.Renderer):
    pass


class _2014Renderer(mistune.Renderer):

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
