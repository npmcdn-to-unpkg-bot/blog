#!./venv/bin/python

import os
import tempfile
from distutils.dir_util import copy_tree

import mistune
from jinja2 import Environment, FileSystemLoader

import click
import frontmatter
from git import Repo
from git.exc import GitCommandError


class Post(object):

    def __init__(self, source, metadata, content):
        self.source = source
        self.metadata = metadata
        self.content = content

    def __unicode__(self):
        return self.render()

    @property
    def path(self):
        id = self.metadata.get('id')
        if id:
            return id
        return os.path.basename(self.source) \
            .rsplit('.', 1)[0]

    def render(self):
        if self.source.endswith('.md'):
            return mistune.markdown(self.content)
        raise NotImplementedError


class Blog(object):

    def __init__(self, **config):
        self.config = config
        self.config.setdefault('posts_dir', './posts')
        self.config.setdefault('layouts_dir', './layouts')
        self.config.setdefault('assets_dir', './assets')
        self.config.setdefault('build_dir', './build')
        self.config.setdefault('remote_branch', 'gh-pages')
        self.config.setdefault('remote_url',
                               'git@github.com:marksteve/blog.git')
        self.config.setdefault('cname_host', 'blog.marksteve.com')
        self.env = Environment(
            loader=FileSystemLoader(self.config['layouts_dir']),
        )

    def write_posts(self):
        for dirpath, _, filenames in os.walk(self.config['posts_dir']):
            paths = map(lambda fn: os.path.join(dirpath, fn), filenames)
            posts = map(self.create_post, paths)
        for post in posts:
            post_dir = os.path.join(self.config['build_dir'], post.path)
            try:
                os.mkdir(post_dir)
            except OSError:
                pass
            output = os.path.join(post_dir, 'index.html')
            with open(output, 'wb') as f:
                f.write(self.render_post(post).encode('utf-8'))
            yield post

    def create_post(self, source):
        fm = frontmatter.load(source)
        post = Post(source, fm.metadata, fm.content)
        return post

    def render_post(self, post):
        layout = post.metadata.get('layout', 'default.html')
        template = self.env.get_template(layout)
        return template.render(post=post)

    def write_index(self, posts):
        output = os.path.join(self.config['build_dir'], 'index.html')
        with open(output, 'wb') as f:
            f.write(self.render_index(posts).encode('utf-8'))

    def render_index(self, posts):
        posts = sorted(posts, key=lambda p: p.metadata['publish_date'],
                       reverse=True)
        template = self.env.get_template('index.html')
        return template.render(posts=posts)

    def copy_assets(self):
        output_dir = os.path.join(self.config['build_dir'],
                                  self.config['assets_dir'])
        if output_dir.strip() == '/':
            raise RuntimeError
        copy_tree(self.config['assets_dir'], output_dir)

    def write_cname(self):
        with open(os.path.join(self.config['build_dir'], 'CNAME'), 'wb') as f:
            f.write(self.config['cname_host'])


@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = Blog()


@cli.command()
@click.pass_context
def build(ctx):
    blog = ctx.obj
    click.secho("Generating posts...", fg='yellow')
    posts = blog.write_posts()
    rendered_posts = []
    for post in posts:
        click.secho("Wrote {}".format(post.path), fg='green')
        rendered_posts.append(post)
    click.secho("Generating index...", fg='yellow')
    blog.write_index(rendered_posts)
    click.secho("Copying assets...", fg='yellow')
    blog.copy_assets()
    click.secho("Generating CNAME...", fg='yellow')
    blog.write_cname()
    click.secho("Done!", fg='green')


@cli.command()
@click.pass_context
@click.option('-m', '--message', default="Update build", help="Commit message.")
def deploy(ctx, message):
    blog = ctx.obj
    branch = blog.config['remote_branch']
    click.secho("Checking out {}...".format(branch), fg='yellow')
    tmpdir = tempfile.mkdtemp()
    click.secho(tmpdir, fg='green')
    try:
        repo = Repo.clone_from(blog.config['remote_url'], tmpdir,
                               branch=branch)
    except GitCommandError:
        repo = Repo.init(tmpdir)
        repo.git.checkout(b=branch)
    click.secho("Updating build...", fg='yellow')
    copy_tree(blog.config['build_dir'], tmpdir)
    repo.git.add(A=True)
    # FIXME: Prevent empty commits
    repo.index.commit(message)
    click.secho("Pushing updates...", fg='yellow')
    if repo.remotes and repo.remotes.origin.exists():
        remote = repo.remotes.origin
    else:
        remote = repo.create_remote('origin', blog.config['remote_url'])
    remote.push(branch)
    click.secho("Done!", fg='green')


if __name__ == '__main__':
    cli()
