import json
from mechanize import Request
from calibre.web.feeds.news import BasicNewsRecipe
from recipes_shared import BasicNewsrackRecipe, format_title, get_date_format

_name = 'Wes Kao'

class WesKaoSubstack(BasicNewsrackRecipe, BasicNewsRecipe):
    title          = 'Substack'
    oldest_article = 7
    language = 'en'
    max_articles_per_feed = 5
    auto_cleanup   = True
    needs_subscription = 'optional'
    use_embedded_content = True
    
    remove_tags = [dict(name='div', class_='paywall-jump')]

    feeds = [
        (_name, 'https://weskao.substack.com/feed'),
    ]

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
            self.title = format_title(_name, article.utctime)
