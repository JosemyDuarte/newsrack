#!/usr/bin/env python
# vim:fileencoding=utf-8
from calibre.web.feeds.news import BasicNewsRecipe

class AdvancedUserRecipe1732211816(BasicNewsRecipe):
    title          = 'Daily Feeds'
    oldest_article = 1
    max_articles_per_feed = 100
    auto_cleanup   = True

    feeds          = [
        ('tldr;tech', 'https://tldr.tech/api/rss/tech'),
    ]