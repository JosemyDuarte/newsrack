#!/usr/bin/env python
# vim:fileencoding=utf-8
#
# Title:        Substack
# License:      GNU General Public License v3 – https://www.gnu.org/licenses/gpl-3.0.html
# Copyright:    Nathan Cook (nathan.cook@gmail.com)
##
# Written:      2020-12-18
# Updated:      2024-11-04
##

__license__ = 'GNU General Public License v3 – https://www.gnu.org/licenses/gpl-3.0.html'
__copyright__ = 'Nathan Cook – 2020-12-19'
__version__ = 'v0.1.1'
__date__ = '2020-12-19'
__author__ = 'topynate'

import json
import re

from mechanize import Request

from calibre.web.feeds.news import BasicNewsRecipe


class Substack(BasicNewsRecipe):
    title = 'Substack'
    __author__ = 'topynate, unkn0wn'
    description = 'Use advanced menu if you want to add your own substack handles.'
    oldest_article = 7
    language = 'en'
    max_articles_per_feed = 100
    auto_cleanup = True
    auto_cleanup_keep = '//*[@class="subtitle"]'
    needs_subscription = 'optional'
    use_embedded_content = False
    masthead_url = 'https://substack.com/img/substack_wordmark.png'
    cover_url = 'https://substack.com/img/substack.png'
    extra_css = '.captioned-image-container, .image-container {font-size: small;}'

    recipe_specific_options = {
        'auths': {
            'short': 'enter the @handles you subscribe to:\nseperated by a space',
            'long': 'julianmacfarlane ianleslie .... ....',
            'default': 'weskao',
        },
        'days': {
            'short': 'Oldest article to download from this news source. In days ',
            'long': 'For example, 0.5, gives you articles from the past 12 hours',
            'default': str(oldest_article),
        },
        'res': {
            'short': 'For hi-res images, select a resolution from the\nfollowing options: 800, 1000, 1200 or 1500',
            'long': 'This is useful for non e-ink devices, and for a lower file size\nthan the default, use 400 or 300.',
            'default': '600',
        },
    }

    def __init__(self, *args, **kwargs):
        BasicNewsRecipe.__init__(self, *args, **kwargs)
        d = self.recipe_specific_options.get('days')
        if d and isinstance(d, str):
            self.oldest_article = float(d)

    # Every Substack publication has an RSS feed at https://{name}.substack.com/feed.
    # The same URL provides either all posts, or all free posts + previews of paid posts,
    # depending on whether you're logged in.
    # feeds          = [
    #     ('Novum Lumen', 'https://novumlumen.substack.com/feed'),    # gratuitously self-promotional example
    # ]

    def get_browser(self):
        br = BasicNewsRecipe.get_browser(self)
        if self.username is not None and self.password is not None:
            br.open('https://substack.com/account/login?redirect=%2F&email=&with_password=')
            data = json.dumps({'email': self.username, 'password': self.password, 'captcha_response':None})
            req = Request(
                url='https://substack.com/api/v1/email-login',
                headers={
                    'Accept': '*/*',
                    'Content-Type': 'application/json',
                    'Origin': 'https://substack.com',
                    'Referer': 'https://substack.com/account/login?redirect=%2F&email=&with_password=',
                },
                data=data,
                method='POST')
            res = br.open(req)
            if res.getcode() != 200:
                raise ValueError('Login failed, check username and password')
        return br

    def get_feeds(self):
        ans = []
        u = self.recipe_specific_options.get('auths')
        if u and isinstance(u, str):
            for x in u.split():
                ans.append('https://' + x.replace('@', '') + '.substack.com/feed')
        return ans

    def preprocess_html(self, soup):
        res = '600'
        w = self.recipe_specific_options.get('res')
        if w and isinstance(w, str):
            res = w
        for img in soup.findAll('img', attrs={'src': True}):
            img['src'] = re.sub(r'w_\d+', 'w_' + res, img['src'])
        for src in soup.findAll(['source', 'svg']):
            src.extract()
        for but in soup.findAll(attrs={'class': ['button-wrapper']}):
            but.extract()
        return soup