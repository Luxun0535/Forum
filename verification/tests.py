#encoding=utf-8
from django.test import TestCase, Client, SimpleTestCase
import json
from django.contrib.auth.models import User
# Create your tests here.
'''
class View_registTestCase(SimpleTestCase):
    def setUp(self):
        self.client=Client()

    def test_regist(self):
        request_data1 = {
            'email':"535091412@qq.com",
            'password1':'123456',
            'password2':'123456',
            'username':'654321'
        }
        response1 = self.client.post('/accounts/register/', json.JSONEncoder().encode(request_data1), 'application/json')
        import pdb; pdb.set_trace()
        print("************")
        print response1
        print("************")
        content1 = {}
        data1=json.loads(response1.content.decode('utf-8'))
        self.assertDictEqual(content1, data1)

class View_loginTestCase(SimpleTestCase):
    def setUp(self):
        self.client=Client()

    def test_login(self):
        user=User(username="123",password="321")
        user.save()

        request_data1 = {
            'username':"123",
            'password':"321",
        }
        response1 = self.client.post('/accounts/login/', json.JSONEncoder().encode(request_data1), 'application/json')
        print("************")
        print response1
        print("************")
        content1 = {}
        data1=json.loads(response1.content.decode('utf-8'))
        self.assertDictEqual(content1, data1)
'''
class View_weiboTestCase(SimpleTestCase):
    def setUp(self):
        self.client=Client()

    def test_regist(self):
        response = self.client.get('/verification/weiboLogin/')
        code=response.context['code']
        response1 = self.client.get('/verificationn/weibo_check/', {'code':code})
        username=response1.context['username']
        name='aa'
        self.assertEqual(username, name)

class View_QQTestCase(SimpleTestCase):
    def setUp(self):
        self.client=Client()

    def test_regist(self):
        response = self.client.get('/verification/QQLogin/')
        code=response.context['code']
        response1 = self.client.get('/verificationn/QQ_check/', {'code':code})
        username=response1.context['username']
        name='aa'
        self.assertEqual(username, name)


class View_WEIXINTestCase(SimpleTestCase):
    def setUp(self):
        self.client=Client()

    def test_regist(self):
        response= self.client.get('/verification/weixinLogin/')
        code=response.context['code']
        response1 = self.client.get('/verificationn/weixin_check/', {'code':code})
        username=response1.context['username']
        name='aa'
        self.assertEqual(username, name)

