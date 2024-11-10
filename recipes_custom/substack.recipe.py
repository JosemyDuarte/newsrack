import json
import re
import os
import sys

from calibre.web.feeds.news import BasicNewsRecipe

sys.path.append(os.environ["recipes_includes"])
from recipes_shared import BasicNewsrackRecipe, format_title
from mechanize import Request

class WesKaoSubstack(BasicNewsrackRecipe, BasicNewsRecipe):
    title          = 'Substack'
    oldest_article = 7
    language = 'en'
    max_articles_per_feed = 5
    auto_cleanup   = True
    needs_subscription = 'optional'
    use_embedded_content = False
    masthead_url = 'https://substack.com/img/substack_wordmark.png'
    cover_url = 'https://substack.com/img/substack.png'
    remove_tags = [dict(name='div', class_='paywall-jump')]

    recipe_specific_options = {
        'auths': {
            'short': 'enter the @handles you subscribe to:\nseperated by a space',
            'long': 'weskao',
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
    
    def populate_article_metadata(self, article, __, _):
        if (not self.pub_date) or article.utctime > self.pub_date:
            self.pub_date = article.utctime
            self.title = format_title('substack', article.utctime)


    def get_feeds(self):
        ans = []
        u = self.recipe_specific_options.get('auths')
        if u and isinstance(u, str):
            for x in u.split():
                ans.append('https://' + x.replace('@', ' ') + '.substack.com/feed')
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