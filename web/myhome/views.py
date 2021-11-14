from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def index(request):
    # return HttpResponse('Hello world')
    return render(request, 'b/index.html')


def demo(request):
    # 添加数据
    # obj = models.Stu()
    # obj.name = '张三'
    # obj.age = 26
    # obj.sex = '1'
    # obj.address = '辽宁'
    # r = obj.save()
    # print(r, type(r))

    # data = {'name': '王五', 'age': 22, 'sex': 0, 'address': '西安'}
    # # 关键字传参
    # obj = models.Stu(**data)
    # obj.save()

    # 查询数据 返回的是QuerySet查询集,里面的元素是对象

    # 1. 获取所有的数据对象
    # data = models.Stu.objects.all()
    # print(data)  # <QuerySet [<Stu: Stu object (1)>, <Stu: Stu object (2)>, <Stu: Stu object (3)>]>
    # for i in data:
    #     print(i.name)

    # 2. 通过id获取数据对象 get()==>没有数据或者多个数据都会报错,所以只能获取一个
    # obj = models.Stu.objects.get(id=3)
    # 通过主键获取
    # obj = models.Stu.objects.get(pk=3)
    # 通过age获取
    # obj = models.Stu.objects.get(age=26)
    # print(obj, obj.name)  # Stu object (3) 王五

    # 3. 过滤器获取数据对象
    # objs = models.Stu.objects.filter(age=22)
    # print(objs)  # <QuerySet [<Stu: Stu object (id:2, name:李四)>, <Stu: Stu object (id:3, name:王五)>]>

    # 删除数据
    # obj = models.Stu.objects.get(id=3)
    # obj.delete()

    # 修改数据
    obj = models.Stu.objects.last()
    obj.name = '田七'
    obj.save()
    return HttpResponse('demo')








def love(request):
    # HttpResponse 做出响应
    # render 只能响应模板文件

    s = '牛皮网'
    n = '123'
    return render(request, 'a/index.html', {'tit': s, 'n': n})

def abc(request):
    return HttpResponse('abc')

def abcd(request, num):
    return HttpResponse(f'abcd:{num}')

def special_case_2003(request):
    return HttpResponse('special_case_2003')


def year_archive(request, year):
    return HttpResponse(f'year_archive:{year}')


def month_archive(request):
    return HttpResponse('month_archive')


def article_detail(request):
    return HttpResponse('article_detail')

