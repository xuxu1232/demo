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

def updateonemore(request):
    # save
    # book = Book.objects.get(id=3)
    # book.publish = Publish.objects.get(name='中国出版社')
    # book.save()

    # update
    # book = Book.objects.filter(name='python高阶')
    # pub = Publish.objects.get(name='北大出版社')
    # book.update(publish=pub)

    # set
    # pub = Publish.objects.get(name='清华出版社')
    # book = Book.objects.get(id=3)
    # pub.book_set.set([book])

    return HttpResponse('一对多更新数据')

def manytomanyadd(request):
    # 增加teacher
    # Teacher.objects.create(name='老张',gender='男')
    # Teacher.objects.create(name='老李',gender='女')
    # Teacher.objects.create(name='老温',gender='男')
    # Teacher.objects.create(name='老刘',gender='女')

    # 增加person
    # pass

    # 增加teacher_person
    # create:增加新学员Mike,学习老张的课
    # teacher_obj = Teacher.objects.filter(name='老张').first()
    # teacher_obj.person.create(name='Mike',age=15,height=190)

    # add:老学员张三  学习老刘的课
    # teacher_obj = Teacher.objects.filter(name='老刘').first()
    # person_obj = Person.objects.filter(name='张三').first()
    # teacher_obj.person.add(person_obj)

    # teacher_obj = Teacher.objects.filter(name='老温').first()
    # person_obj = Person.objects.filter(name='jave').first()
    # teacher_obj.person.add(person_obj)

    return HttpResponse('多对多增加数据')

def manytomanyget(request):
    # 正向查询
    # # 查询老刘教过的学生
    # teacher_obj = Teacher.objects.filter(name='老刘').first()
    # data = teacher_obj.person.all()
    # print(data)

    # 反向
    # 查询张三学了谁的课
    # person_obj = Person.objects.filter(name='张三').first()
    # data = person_obj.teacher_set.all()
    # print(data)

    return HttpResponse('多对多查询')

def manytomanyupdate(request):
    # 正向
    # 修改 老李的学生为java
    # teacher_obj = Teacher.objects.filter(name='老李').first()
    # person1 = Person.objects.filter(name='jave').first()
    # teacher_obj.person.set([person1])

    # 反向
    # 修改张三的老师为老温
    # person_obj = Person.objects.filter(name='张三').first()
    # teacher1 = Teacher.objects.filter(name='老温').first()
    # person_obj.teacher_set.set([teacher1])

    return HttpResponse('多对多数据更新')

def manytomanydelete(request):
    # remove ：解除关系
    # 老温不教张三
    # 正向
    # person_obj = Person.objects.filter(name='张三').first()
    # teacher_obj = Teacher.objects.filter(name='老温').first()
    # teacher_obj.person.remove(person_obj)

    # 反向
    # jave不学老李的课
    # person_obj = Person.objects.filter(name='jave').first()
    # teacher_obj = Teacher.objects.filter(name='老李').first()
    # person_obj.teacher_set.remove(teacher_obj)

    # delete():删除数据，解除关系
    # 老温离职
    # Teacher.objects.filter(name='老温').first().delete()

    # jave辍学
    # Person.objects.filter(name='jave').first().delete()


    return HttpResponse('多对多删除')

from django.db.models import Avg,Max,Min,Sum,Count,F,Q
def juhequery(request):

    # data = Person.objects.all().aggregate(Avg('age'))
    # data = Person.objects.all().aggregate(avg_age=Avg('age'))
    # print(data)
    # data = Person.objects.all().aggregate(Max('age'))
    # print(data)

    # data = Person.objects.all().aggregate(Min('age'))
    # print(data)

    return HttpResponse('聚合查询')

def Ftest(request):
    # data = Book.objects.filter(num__gt=F('salled'))
    # print(data)

    return HttpResponse('F object test')

def Qtest(request):
    # and   &
    # data = Book.objects.filter(Q(num=10)&Q(salled=100))
    # print(data)

    # or  |
    # data = Book.objects.filter(Q(num=10)|Q(salled=100))
    # print(data)

    # not  ~
    # data = Book.objects.filter(~Q(num=10)|~Q(num=100))
    # print(data)
    return HttpResponse('Q object test')
