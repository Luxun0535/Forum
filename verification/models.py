from django.db import models

# Create your models here.
class APIClient(object):
    def __init__(self, app_key, app_secret, redirect_uri):
        self.client_id = app_key
        self.client_secret = app_secret
        self.redirect_uri = redirect_uri
    def get_authorize_url(self):
        return 'https://api.weibo.com/oauth2/authorize?response_type=code&client_id=%s&redirect_uri=%s' % (self.client_id, _encode(self.redirect_uri))
