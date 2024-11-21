#!/usr/bin/env python
# vim:fileencoding=utf-8
from calibre.web.feeds.news import BasicNewsRecipe

class AdvancedUserRecipe1732211893(BasicNewsRecipe):
    title          = 'Weekly Feeds'
    oldest_article = 7
    max_articles_per_feed = 100
    auto_cleanup   = True

    feeds          = [
        ('Irrational Exuberance', 'https://lethain.com/feeds.xml'),
    ]