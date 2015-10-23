Forum
=============
#论坛基本功能
    app:https://github.com/byteweaver/django-forums

#论坛访问url
    url(r'^$', CategoryListView.as_view(), name='overview'),  论坛分类目录以及各分类下的论坛名称
    url(r'^(?P<pk>\d+)/$', ForumDetailView.as_view(), name='forum'),  某个论坛下的主题帖子
    url(r'^(?P<forum_id>\d+)/create/$', login_required(TopicCreateView.as_view()), name='topic_create'),新建主题帖子
    url(r'^topic/(?P<pk>\d+)/$', TopicDetailView.as_view(), name='topic'), 某个帖子的具体信息（回复列表）
    url(r'^topic/(?P<pk>\d+)/create/$', login_required(PostCreateView.as_view()), name='post_create'), 发表帖子回复
