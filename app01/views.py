from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
    return HttpResponse('index')


def addperson(request):
    # save()方法
    # person = Person(name='赵六',age=11,height=180)
    # person.save()
    #
    # create方法
    # Person.objects.create(name='王五',age=14)
    # data = [
    #     {'name':'A','age':12},
    #     {'name': 'B', 'age': 12},
    # ]
    # for i in data:
    #     Person.objects.create(**i)

    return HttpResponse('增加数据')

def getperson(request):
    # all()方法:返回一个queryset，是一个列表,所有符合条件的数据
    # data = Person.objects.all()
    # # print(data)
    # for one in data:
    #     print(one.name)
    #     print(one.age)
    #     print(one.height)

    # get()方法：返回一个对象，一条数据
    # data = Person.objects.get(id=1)
    # print(data)
    # print(data.name)

    # filter()：过滤查询，返回一个queryset，一个列表，符合条件的数据
    # data = Person.objects.filter(height='180')
    # print(data)
    # for one in data:
    #     print(one.name)

    # first()：返回一个对象，所有符合条件的数据的第一条
    # data = Person.objects.filter(height=180).first()
    # print(data)
    # print(data.name)

    # last()方法：返回一个对象，所有符合条件的数据的最后一条
    # data = Person.objects.all().last()
    # print(data.id)

    # order by:排序，根据指定字段进行排序，-代表逆序
    # data = Person.objects.all().order_by('-id')
    # print(data)
    # for one in data:
    #     print(one.id)

    # exclude():不包含
    # data = Person.objects.exclude(name='张三')
    # print(data)


    # values()
    # data = Person.objects.all().values()
    # print(data)

    # count():返回符合条件的数据的条数
    # data = Person.objects.filter(age__lt=18).count()
    # print(data)

    # exists():判断是否存在，返回布尔类型,不能跟在get 后面
    # data = Person.objects.filter(name='libai').exists()
    # print(data)

    # 切片,主键从1开始，下标从0开始
    # data = Person.objects.all()[2:5]
    # print(data)

    # 双下划线查询
    # __lt:小于
    # __lte:小于等于
    # data = Person.objects.filter(age__lt=18)
    # print(data)

    # __gt:大于
    # __gte:大于等于
    # data = Person.objects.filter(age__gte=18)
    # print(data)

    # data = Person.objects.filter(id__in=[1,2])
    # print(data)

    # __contains:区分大小写
    # data = Person.objects.filter(name__contains='A')
    # print(data)

    # __icontains:不区分大小写
    # data = Person.objects.filter(name__icontains='A')
    # print(data)

    # __range:范围，左闭右闭
    # data = Person.objects.filter(id__range=[1,3])
    # print(data)

    # __startswith   类似于'j%'
    # data = Person.objects.filter(name__startswith='j')
    # print(data)

    # __endswith 类似于'%j'
    # data = Person.objects.filter(name__endswith='e')
    # print(data)


    return HttpResponse('查询数据')

def updateperson(request):
    # save()方法
    # data = Person.objects.get(id = 2)
    # data.name = 'python'
    # data.save()

    # update方法
    # Person.objects.filter(id=3).update(name='jave')
     return HttpResponse('修改数据')

def deleteperson(request):
    # Person.objects.get(id=4).delete()
    return HttpResponse('删除数据')


def addOneMore(request):
    # 增加出版社
    # Publish.objects.create(name='清华出版社',address='北京')
    # Publish.objects.create(name='中国出版社',address='北京')
    # Publish.objects.create(name='河南出版社',address='洛阳')
    # Publish.objects.create(name='北大出版社',address='北京')

    # 增加图书
    # 第一种
    # Book.objects.create(name='python入门',publish_id = 1)
    #
    # publish = Publish.objects.get(name='中国出版社')
    # Book.objects.create(name='python高阶',publish_id = publish.id)

    # 第二种
    # Book.objects.create(name='python核心编程',publish = Publish.objects.get(name='河南出版社'))

    # 第三种
    # 正向操作：从表到主表
    # book = Book()
    # book.name = '笨办法学python'
    # book.publish = Publish.objects.get(name='北大出版社')
    # book.save()

    # 反向操作：主表到从表
    # publish_obj = Publish.objects.get(name='河南出版社')
    # publish_obj.book_set.create(name='利用python进行数据分析')
    return HttpResponse('一对多关系增加数据')

def getOneMore(request):
    # 第一种
    # 查询中国出版社出版的所有书
    # publish = Publish.objects.get(name='中国出版社')
    # book = Book.objects.filter(publish_id=publish.id).all()
    # for x in book:
    #     print(x.name)
    # 第二种
    # 正向查询
    # 查询python入门是哪个出版社出版的
    # book = Book.objects.filter(name='python入门').first()
    # print(book.name)
    # print(book.publish.name)
    # 反向查询
    # 查询中国出版社出版的所有书
    # publish = Publish.objects.filter(name='中国出版社').first()
    # book = publish.book_set.all()
    # print(book)
    # for x in book:
    #     print(x.name)


    return HttpResponse('一对多关系查询数据')