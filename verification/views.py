# encoding=utf-8
from django.shortcuts import render
from weibo import APIClient
from datetime import datetime
import urllib,urllib2
from django.http import HttpResponse
import json
from django.http import HttpResponseRedirect
from Forum import settings
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request, 'registration/index.html', {})
'''
#注册
def regist(request):
    if request.method == 'POST':
        try:
            account=request.POST.get('account')
            password = request.POST.get('password')
        except Exception as e:
            return HttpResponse(type(e))
        User.
        user= User(account=account,password=password)
        user.save()
        return HttpResponse('Regist successfully')

    else:
        return HttpResponse('please send a post')
'''

# http://github.liaoxuefeng.com/sinaweibopy/
# 微博登录"""
def weiboLogin():
    client = APIClient(app_key=settings.WEIBO_APP_KEY, app_secret=settings.WEIBO_APP_SERCET, redirect_uri=settings.WEIBO_CALLBACK_URL)
    url = client.get_authorize_url()
    return HttpResponseRedirect(url)

# 由settings中的CALLBACK_URL调用
def weibo_check(request):
    code = request.GET.get('code', None)
    now = datetime.datetime.now()
    if code:
        client = APIClient(app_key=settings.WEIBO_APP_KEY, app_secret=settings.WEIBO_APP_SERCET, redirect_uri=settings.WEIBO_CALLBACK_URL)
        r = client.request_access_token(code)
        access_token = r.access_token   # 返回的token，类似abc123xyz456
        expires_in = r.expires_in	   # token过期的UNIX时间：http://zh.wikipedia.org/wiki/UNIX%E6%97%B6%E9%97%B4
        uid = r.uid
        # 在此可保存access token
        client.set_access_token(access_token, expires_in)
        request.session['access_token'] = access_token
        request.session['expires_in'] = expires_in
        request.session['uid'] = uid

        # http://open.weibo.com/wiki/2/users/show
        data=client.user.show.get(uid)
        user=User(username=uid)
        user.save()
        name=data.get('name')
        return HttpResponseRedirect()
        # user = SupserWeibo(access_token=access_token, uid=uid, request=request)	  # 实例化超级微博类
        '''
        # 更新数据库
        if MyUser.objects.filter(uid=uid).exists():
            MyUser.objects.filter(uid=uid).update(last_login=now)
            user.Login()	# 登陆
            return HttpResponseRedirect('/')#返回主页
        else:
            # 创建用户并登陆
            u_id = user.createUser()
        if u_id:
            return HttpResponseRedirect('/manage/user/%s/' %u_id)
        '''
    return HttpResponse('/404/') #未获得新浪微博返回的CODE





# 以上的信息是要自己去申请开发网站时给开发者分配的
# http://wiki.open.qq.com/wiki/website/使用Authorization_Code获取Access_Token#Step1.EF.BC.9A.E8.8E.B7.E5.8F.96Authorization_Code
def QQLogin():
    url = "https://graph.qq.com/oauth2.0/authorize"
    url1 = url+"?response_type=code&client_id="+settings.QQ_CLIENT_ID+"&redirect_uri="+settings.QQ_REDIRECT_URI+"&state="+settings.QQ_STATE
    return HttpResponse(url1)

def QQ_check(request):
    code=request.GET.get('code')
    url1 = "https://graph.qq.com/oauth2.0/token"
    url1 = url1+"?grant_type=authorization_code"+"&client_id="+settings.QQ_CLIENT_ID+"&client_secret="+settings.QQ_CLIENT_SERCET+"&code="+code+"&redirect_uri="+settings.QQ_REDIRECT_URI
    req1 = urllib2.Request(url1)
    response1 = urllib2.urlopen(req1)
    m = ((response1.read()).split('&'))[0]
    access_token = (m.split('='))[1]
# 这里由于返回的是一个字符串，所以对返回的字符串操作，从中获取access_token
    url2 = "https://graph.qq.com/oauth2.0/me"
    url2 = url2+"?access_token="+access_token
    req2 = urllib2.Request(url2)
    response2 = urllib2.urlopen(req2)
    dic = (response2.read())[10:-3]
    ajson = json.loads(dic)
    openid=ajson['openid']
    user=User(username=openid)
    user.save()
    # 这里返回的是一个json字典，所以可以通过json模块解析其中的信息，以获得openid

# 一下是一个例子，用来获取用户的基本信息
    url3="https://graph.qq.com/user/get_user_info?"+ \
      "access_token="+access_token+ \
      "&oauth_consumer_key="+settings.QQ_CLIENT_ID+ \
      "&openid="+openid
    req3=urllib2.Request(url3)
    response3=urllib2.urlopen(req3)
    data_dic=json.loads(response3.read())
    nickname=data_dic['openid']

    return HttpResponseRedirect()

def wenxinLogin():
    # 参数详见https://open.weixin.qq.com/cgi-bin/showdocument?action=dir_list&t=resource/res_list&verify=1&id=open1419316505&token=&lang=zh_CN
    # url="https://open.weixin.qq.com/connect/qrconnect?appid=APP_ID&redirect_uri=REDIRECT_URI&response_type=code&scope=SCOPE&state=STATE#wechat_redirect"
    url = "https://open.weixin.qq.com/connect/qrconnect"
    url1 = url+"?appid="+settings.WEIXIN_APP_ID+"&redirect_uri="+settings.WEIXIN_REDIRECT_URI+"&response_type=code&scope="+settings.WEIXIN_SCOPE+"&state="+settings.WEIXIN_STATE+"#wechat_redirect"
    return HttpResponse(url1)
# 微信检验
def wenxin_check(request):
    code = request.GET.get('CODE')     # 如果登录时用户禁止授权将不返回该参数
    state = request.GET.get('state')
    # https://api.weixin.qq.com/sns/oauth2/access_token?appid=APPID&secret=SECRET&code=CODE&grant_type=authorization_code
    url="https://api.weixin.qq.com/sns/oauth2/access_token"
    token_url = '%s?%s'%(url, urllib.urlencode({
                                'appid': settings.WEIXIN_APP_ID,
                                'secret': settings.WEIXIN_APP_SECRET,
                                'code': code,
                                'grant_type': 'authorization_code',
                            }))
    req = urllib2.Request(token_url)
    resp = urllib2.urlopen(req)
    data_dic=json.loads(resp.read())
    access_token=data_dic['access_token']
    openid = data_dic['openid']


    # https://api.weixin.qq.com/sns/userinfo?access_token=ACCESS_TOKEN&openid=OPENID
    url2 = "https://api.weixin.qq.com/sns/userinfo"
    openod_url = '%s?%s'%(url2, urllib.urlencode({
                                'access_token': access_token,
                                'openid': openid,
                            }))
    req2 = urllib2.Request(openod_url)
    resp2 = urllib2.urlopen(req2)
    usrinfo_dic = json.loads(resp2.read())
    unionid = usrinfo_dic['unionid']
    user=User(username=unionid)
    user.save()
    return HttpResponseRedirect()
