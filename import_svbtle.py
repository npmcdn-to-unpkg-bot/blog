#!./venv/bin/python

import feedparser
import frontmatter
from html2text import html2text


def main():
    feed_url = 'http://blog.marksteve.com/feed'
    page = 1
    while True:
        d = feedparser.parse('{}?page={}'.format(feed_url, page))
        if not d.entries:
            break
        for entry in d.entries:
            id = entry.link.rsplit('/', 1)[1]
            body = html2text(entry.content[0]['value'])
            title = entry.title
            y, m, d = entry.published_parsed[:3]
            publish_date = '{}-{:02d}-{:02d}'.format(y, m, d)
            post = frontmatter.Post(body, title=title,
                                    publish_date=publish_date)
            with open('posts/{}.md'.format(id), 'wb') as f:
                f.write(frontmatter.dumps(post).encode('utf8'))
        page += 1


if __name__ == '__main__':
    main()

