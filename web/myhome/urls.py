
from django.urls import path, re_path
from . import views
urlpatterns = [
    # 常规字符串定义
    # path('', views.index),
    # path('love/', views.love),

    # 正则匹配 ^限制开始, $限制结束
    # re_path('^$', views.index),
    # re_path('^love/$', views.abcde),

    # 不需要添加前导斜杠，因为每个 URL 都有。例如，它是articles，不是/articles
    # path('articles/2003/', views.special_case_2003),
    # 关键字传参 关键字为year,类型是int
    # path('articles/<int:year>/', views.year_archive),
    # path('articles/<int:year>/<int:month>/', views.month_archive),
    # path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),

    # re_path('^abc/123/$', views.abc),
    # 小括号() 中属于无关键字的传参,所以定义的abcd视图函数一定要接收这个参数
    # re_path('^abcd/([0-9]{3})/$', views.abcd),
    # 小括号() 中的 ?P<num> 是命名关键字的传参,所以定义的函数一定要有num这个关键字接收参数
    # re_path('^abcd/(?P<num>[0-9]{3})/$', views.abcd),

    # 给路由定义名字 第三个关键字参数 name,通过name名字解析路由规则
    # re_path('^aqs/123/$', views.abc, name="myhome_abc"),
    # re_path('^abc/([0-9]{3})/$', views.abcd, name="myhome_abcd"),


    path('', views.index, name='myhome_index'),
    path('demo/', views.demo, name='myhome_demo'),

]