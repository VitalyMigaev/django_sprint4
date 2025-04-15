from django.core.paginator import Paginator

from blog.constants import POSTS_ON_PAGE


def get_paginator_page(request, query_set, posts_on_page=POSTS_ON_PAGE):
    return Paginator(query_set, posts_on_page
                     ).get_page(request.GET.get('page'))
