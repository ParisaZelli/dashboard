from django import template
from ..models import post,Category

register=template.Library()

@register.simple_tag
def hello(arg):
    return 'hello world {}'.format(arg)

@register.filter
def upper(value):
    return value.upper()

@register.inclusion_tag('blog/blog-recent.html')
def recent_post():
    posts=post.objects.filter(Active=1).order_by('-updated_time')[0:2]

    return {'posts':posts}


@register.inclusion_tag('blog/blog-categories.html')
def categories():
    category=Category.objects.all()
    posts=post.objects.filter(Active=1)

    Dict={}

    for cat in category:
        Dict[cat]=posts.filter(category=cat).count()

    return {'Dict':Dict}

@register.inclusion_tag('blog/blog-tags.html')
def tagcloud():
    posts=post.objects.filter(Active=1)

    Dict={}

    for tag in tagcloud:
        Dict[tag]=posts.filter(tagcloud=tag).count()

    return {'Dict':Dict}