---
publish_date: 2014-1-5
title: Push-to-deploy static sites with Pelican, Flask and Github
---

After reading about [how Nicolas Gallagher deploys static sites with
Git](http://nicolasgallagher.com/simple-git-deployment-strategy-for-static-
sites/), I started wanting to develop my own push-to-deploy flow to use in a
[Pelican-generated](http://blog.getpelican.com/) [static
site](https://github.com/pythonph/pycon) I’ve been working on. Turns out it
was pretty easy to implement.

I wrote a deployer script which is basically a
[Flask](http://flask.pocoo.org/) app that receives Github webhook requests.
Decided to use Github webhooks as trigger instead of a `post-receive` hook
since the repo I was working with was in Github anyways. I also like using
their code editor for quick fixes. When the app receives a hook request, it
starts pulling the latest changesets. Then it runs `pelican` to build updated
static files and put them at the path I pointed `nginx` to serve. Simple.

Here’s a gist of the script:  
<https://gist.github.com/marksteve/8243318>

Right now it can only auto-deploy one repo. but I’ll definitely add support
for multiple repos when I get the time to.

Update: Now supports multiple repos :)