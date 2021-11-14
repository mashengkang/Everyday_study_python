# Django

## 1.安装

```
pip install Django==2.2.*
检测当前是否安装Django及版本
python -m django --version
pip show django
```

## 2.创建项目

```
django-admin startproject [web项目名]
```

## 3. 启动项目

进入到项目目录中,在manage.py文件的统计目录中,执行命令

```
python manage.py runserver
```

## 4.打开浏览器

```
访问地址  http://127.0.0.1:8000
```

## 5.创建应用

```
python manage.py startapp [应用名]
python manage.py startapp myhome
```

## 6.输出一个hello world

1. 在创建好的应用中,写view视图函数 myhome/views.py

   ```python
   # file: myhome/views.py
   from django.shortcuts import render
   from django.http import HttpResponse
   
   # Create your views here.
   def index(request):
   
       return HttpResponse('Hello world') 
   ```

2. 给当前的视图函数配置一个路由 myhome/urls.py ,这个urls.py手动创建

   ```python
   # file: myhome/urls.py
   from django.urls import path
   from . import views
   urlpatterns = [
       path('', views.index),
   ]
   ```

3. 在根路由中配置当前应用的路径 web/urls.py

   ```python
   # file:  web/urls.py
   from django.contrib import admin
   from django.urls import path,include
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('myhome.urls')),
   ]
   ```


## 7.在项目中使用模板

修改setting.py 模板引擎的配置目录 setting.py/TEMPLATES/DIRS配置项

```
'DIRS': [os.path.join(BASE_DIR, 'templates')],
```

1. 在manage.py文件同级目录下,创建templates 文件夹

2. 在模板文件夹中创建 模板文件.html 文件

3. 在视图函数中使用模板文件 myhome/views.py

   ```python
   # file: myhome/views.py
   def abcde(request):
       # HttpResponse 做出响应
       return render(request, 'a/index.html')
   
   # file: myhome/urls.py
   path('love/', views.abcde),
   ```

## 8.在项目中使用静态文件

(css,js,img...)

修改setting.py 模板引擎的配置目录 setting.py

```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```

1. 在manage.py文件同级目录下,创建 static 文件夹

2. 在静态文件夹中创建 静态文件

3. 在模板文件夹中使用 静态文件 /static/js/1.js

   ```css
   # file:static/1.css
   h1{
       color:#369;
   }
   
   # templates/a/a.html
   <link rel="stylesheet" href="/static/1.css">
   
   ```

## 9.当前的项目结构目录

```
E: web					--项目目录
│  db.sqlite3			--django默认的数据库配置,生成的数据库文件
│  manage.py			--管理文件,当前项目唯一的入口文件
├─myhome				--自定义创建的 应用
│  │  admin.py			--用于django自动化后的配置文件
│  │  apps.py			
│  │  models.py			--当前应用中的 模型文件
│  │  tests.py
│  │  urls.py			--当前应用中的路由文件,(子路由,创建完应用后手动创建的文件)
│  │  views.py			--当前应用中的视图函数
│  │  __init__.py
│  ├─migrations
│  │      __init__.py

├─static				-- 静态文件夹
│      1.css
│
├─templates  			--模板文件夹
│  └─a
│          index.html
│
└─web					--和项目名同名的目录,当前项目的配置和管理...
    │  settings.py
    │  urls.py
    │  wsgi.py
    │  __init__.py
```

## 10.相关的一些概念

- 路由: 就是去定义用户访问时的url,并且把定义的url路径和对应的视图函数产生映射
- 视图:就是一个函数或方法,也可以定义成类,主要就是用于接收用户的请求,并且做出响应,项目中的主要逻辑代码都在视图函数中
- 模板: 在django框架中,有一个模板引擎,可以做到把html和python逻辑代码分离并且在视图函数中需要给用户响应模板时,返回或传递数据
- 静态文件:专门存放 在模板中需要使用的静态文件的目录,如css, js, font, img等
- 模型: 专门处理数据层的,模型在django框架中,可以通过定义一个模型类,来实现对数据库中的数据进行管理(增 删 改 查). 在开发中,对类中的数据进行的操作,会映射到数据库,转化成对数据的具体执行(sql)

## 11.框架的设计思想(设计模式)

核心思想: 就是把 **逻辑代码 ,数据控制和页面的展示**完全分离, 降低程序模块之间的耦合(低耦合,高内聚)

MVC 设计模式

M Model 		 模型 ==> 数据层的管理

V View 			 视图 ==> 模块的管理 页面的展示

C Controller	控制器==> 逻辑代码的管理



MVT 设计模式 Django, Flask

M Model 		 模型 ==> 数据层的管理,数据的处理

V View 			 视图 ==> 逻辑层的管理,逻辑代码,流程控制....

T Template	  模板 ==> 模板的管理,页面的展示

## 12.路由匹配方法学习

**路径转换器**[¶](https://docs.djangoproject.com/zh-hans/2.1/topics/http/urls/#path-converters)

默认情况下可以使用以下路径转换器：

- `str`- 匹配任何非空字符串，不包括路径分隔符`'/'`. 如果表达式中不包含转换器，则这是默认设置。
- `int`- 匹配零或任何正整数。返回一个int。
- `slug`- 匹配由 ASCII 字母或数字以及连字符和下划线字符组成的任何 slug 字符串。例如， `building-your-1st-django-site`。
- `uuid`- 匹配格式化的 UUID。为防止多个 URL 映射到同一页面，必须包含破折号且字母必须为小写。例如，`075194d3-6885-417e-a8a8-6c931e272f00`。返回一个 [`UUID`](https://docs.python.org/3/library/uuid.html#uuid.UUID)实例。
- `path`- 匹配任何非空字符串，包括路径分隔符 `'/'`. 这允许您匹配完整的 URL 路径，而不是像`str`.

```python
# file:myhome/urls.py
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
    re_path('^aqs/123/$', views.abc, name="myhome_abc"),
    re_path('^abc/([0-9]{3})/$', views.abcd, name="myhome_abcd"),
    path('love/', views.love),
]


# file:templates/a/index.html
        <a href="/abc/123">硬编码:跳转</a><br>
        <a href="{% url 'myhome_abc' %}">通过name路由名:跳转</a><br>
        <a href="{% url 'myhome_abcd' n %}">带参数的</a>
        
        
# file:myhome/views.py
def love(request):
    # HttpResponse 做出响应
    # render 只能响应模板文件

    s = '牛皮网'
    n = '123'
    return render(request, 'a/index.html', {'tit': s, 'n': n})

def abcd(request, num):
    return HttpResponse(f'abcd:{num}')
```

## 13.model数据管理层

### 13.1给当前的项目配置一个数据库

- 确认当前是否安装了mysql数据库

- 在mysql数据库中创建一个库mydb

  ```python
   create database mydb default charset=utf8mb4;
  ```

- 修改当前项目中的数据库配置 setting.py/DATABASES

  ```python
  # file:setting.py
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'mydb',
          'USER': 'root',
          'PASSWORD': 'root',
          'HOST': 'localhost',
          'PORT': '3306',
      }
  }
  ```

- 如果当前环境中没有安装MysqlDB的替代包,会报错

  ```shell
  django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module.
  Did you install mysqlclient?
  ```

  解决方法:

  1. 安装 mysqlclient	`pip install mysqlclient`
  2. 安装pymysql 安装后需要配置

### 13.2定义模型

- 在创建模型之前,确保当前的应用已经在配置文件中定义好 setting.py/ INSTALLESD_APPS

  ```python
  # file:setting.py
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'myhome',
  ]
  ```

  

- 在应用中的models.py中定义模型

  ```python
  # file:myhome/models.py
  class Stu(models.Model):
      name = models.CharField(max_length=20)
      age = models.IntegerField(default=24)
      sex = models.CharField(max_length=1,default='0')
      address = models.CharField(max_length=50, null=True)
  ```

  在这里的字段,默认都不为空,如果可以空的话,需要设置 `null=True`

- 生成迁移文件

```python
python manage.py makemigrations
```

定义模型中没有id主键字段,但是会自动生成

```python
('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
```

- 执行迁移文件

  ```shell
  python manage.py migrate
  ```

  ```shell
  # 此时查看数据库mydb库中,会生成定义模型的class stu 的表
  # sex设置的默认值,不在表中显示,而在应用层
  mysql> desc myhome_stu;
  +---------+-------------+------+-----+---------+----------------+
  | Field   | Type        | Null | Key | Default | Extra          |
  +---------+-------------+------+-----+---------+----------------+
  | id      | int         | NO   | PRI | NULL    | auto_increment |
  | name    | varchar(20) | NO   |     | NULL    |                |
  | age     | int         | NO   |     | NULL    |                |
  | sex     | varchar(1)  | NO   |     | NULL    |                |
  | address | varchar(50) | YES  |     | NULL    |                |
  +---------+-------------+------+-----+---------+----------------+
  5 rows in set (0.34 sec)
  ```

  

