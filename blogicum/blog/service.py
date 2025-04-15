from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models.query import QuerySet
from django.utils import timezone

from blog.constants import POSTS_ON_PAGE
from blog.models import Post


def get_paginator_page(request, query_set, posts_on_page=POSTS_ON_PAGE):
    return Paginator(query_set, posts_on_page
                     ).get_page(request.GET.get('page'))


def get_published_posts(
    posts: QuerySet = Post.objects.all(),
    use_filtering: bool = True,
    use_select_related: bool = True,
    use_annotation: bool = True,
):
    if use_filtering:
        posts = posts.filter(
            pub_date__lt=timezone.now(),
            is_published=True,
            category__is_published=True
        )
    if use_select_related:
        posts = posts.select_related('category', 'location', 'author')
    if use_annotation:
        posts = posts.annotate(
            comment_count=Count('comments')
        ).order_by(
            *Post._meta.ordering
        )
    return posts
