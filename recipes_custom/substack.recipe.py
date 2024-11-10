import json
import re
import os
import sys

from calibre.web.feeds.news import BasicNewsRecipe

sys.path.append(os.environ["recipes_includes"])
from mechanize import Request

class Substack(BasicNewsRecipe):
    title = 'Substack'
    __author__ = 'Josemy'
    description = 'Use advanced menu if you want to add your own substack handles.'
    oldest_article = 7
    language = 'en'
    max_articles_per_feed = 5
    auto_cleanup = True
    auto_cleanup_keep = '//*[@class="subtitle"]'
    needs_subscription = 'optional'
    use_embedded_content = False
    masthead_url = 'https://substack.com/img/substack_wordmark.png'
    cover_url = 'https://substack.com/img/substack.png'
    extra_css = '.captioned-image-container, .image-container {font-size: small;}'

    handles = [
        "weskao",
    ]

    def __init__(self, *args, **kwargs):
        BasicNewsRecipe.__init__(self, *args, **kwargs)
        d = "7"
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
        for handle in self.handles:
            ans.append('https://' + handle + '.substack.com/feed')
        return ans

    def preprocess_html(self, soup):
        res = '600'
        for img in soup.findAll('img', attrs={'src': True}):
            img['src'] = re.sub(r'w_\d+', 'w_' + res, img['src'])
        for src in soup.findAll(['source', 'svg']):
            src.extract()
        for but in soup.findAll(attrs={'class': ['button-wrapper']}):
            but.extract()
        return soup