from django.db import models

# Create your models here.

class Person(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32,verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    height = models.DecimalField(max_digits=5,decimal_places=2,verbose_name='身高',null=True)
    birthday = models.DateField(auto_now=True,verbose_name='生日')

    # 设置添加的用户在站点管理显示的内容
    # def __str__(self):
    #     return self.name

    class Meta:
        db_table = 'person'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        # 用于排序，按指定字段排序
        # ordering = ['age','-id']



class Publish(models.Model):
    name = models.CharField(max_length=32,verbose_name='出版社')
    address = models.CharField(max_length=32,verbose_name='地址')

    class Meta:
        db_table = 'publish'
        verbose_name = '出版社'
        verbose_name_plural = verbose_name

class Book(models.Model):
    name = models.CharField(max_length=32,verbose_name='书名')
    publish = models.ForeignKey(to=Publish,to_field='id',on_delete=models.CASCADE)

    class Meta:
        db_table = 'book'
        verbose_name = '图书'
        verbose_name_plural = verbose_name