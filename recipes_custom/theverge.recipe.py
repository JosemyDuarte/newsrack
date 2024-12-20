#!/usr/bin/env python
# vim:fileencoding=utf-8
from calibre.web.feeds.news import BasicNewsRecipe


class HindustanTimes(BasicNewsRecipe):
    title = u'The Verge'
    language = 'en'
    __author__ = 'Krittika Goyal'
    oldest_article = 1  # days
    max_articles_per_feed = 25
    use_embedded_content = False

    no_stylesheets = True
    auto_cleanup = True
    auto_cleanup_keep = '//div[@class="story-image shadowbox entry-content-asset"]'

    recipe_specific_options = {
        'days': {
            'short': 'Oldest article to download from this news source. In days ',
            'long': 'For example, 0.5, gives you articles from the past 12 hours',
            'default': str(oldest_article)
        }
    }

    def __init__(self, *args, **kwargs):
        BasicNewsRecipe.__init__(self, *args, **kwargs)
        d = self.recipe_specific_options.get('days')
        if d and isinstance(d, str):
            self.oldest_article = float(d)

    feeds = [
        ('News',
         'http://www.theverge.com/rss/index.xml'),
    ]