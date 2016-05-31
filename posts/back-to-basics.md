---
publish_date: '2016-05-31'
title: Back to basics
---

Yet another blog rewrite! This time I'm going back to basics:

```
(master)⚡ % cat blog.py | wc -l
     159
```

Nothing fancy. My goal was to make it simple and flexible, like Jekyll when it first started working out. It's basically glue code for a handful of excellent Python packages:

- __click__ - CLI action
- __python-frontmatter__ -  Metadata handling
- __jinja2__ - So I don't need to type things over and over again
- __mistune__ - Everybody loves markdown
- __gitpython__ - For deploying to gh-pages

It honestly took more time to make it pretty than to code it. You can check it out in [GitHub](https://github.com/marksteve/blog). Right now, it can only handle plain markdown files. In the future, I want it to render [literate code](https://en.wikipedia.org/wiki/Literate_programming) so I can do fancy schmancy javascript walkthroughs.