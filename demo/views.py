from django.http import HttpResponse
def index(request):
    return HttpResponse('hello world')

def about(request):
    return HttpResponse('这是一个about页面')

def show(request):
    return HttpResponse('刘柯柯个怀熊')

def demo(request,year,mon,day):
    mons = [31,28,31,30,31,30,31,31,30,31,30,31]
    days = 0
    if int(year)%4==0 and int(year)%100!=0 or int(year)%400==0:
        if int(mon)<=2:
            for i in range(int(mon)-1):
                days = days+mons[i]
            days+=int(day)
            return HttpResponse('%s年%s月%s日是第%s天' % (year, mon, day, days))
        else:
            for i in range(int(mon)-1):
                days = days+mons[i]
            days = days+int(day)+1
            return HttpResponse('%s年%s月%s日是第%s天' % (year, mon, day, days))
    else:
        for i in range(int(mon)-1):
            days = days+mons[i]
        days = days+int(day)
        return HttpResponse('%s年%s月%s日是第%s天'%(year,mon,day,days))
from django.template import Template,Context
def gethtml(request):

    html = """
        <html>
            <head>
                <style>
                    h1{
                    color:red;
                    }
                </style>
            </head>
            <body>
            <h1>欢迎您的到来</h1>
            <h2>这是{{name}}</h2>
            <a href='https://baike.baidu.com/item/%E6%98%93%E7%83%8A%E5%8D%83%E7%8E%BA/221450?fr=aladdin',target='_blank'>
            <img src='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1568004506527&di=c383f4306da9e22d0839ad701a8d6429&imgtype=0&src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fq_70%2Cc_zoom%2Cw_640%2Fimages%2F20171006%2F55a494f24fff4e74bf20e49568216c36.jpeg',title='易烊千玺',alt='没找到'>
            </a>
            <p>{{content}}</p>
            </body>
        </html>
    """
    # 构建模板结构
    template_obj = Template(html)
    # 创建渲染模板
    parsms = dict(name='千玺',content='这是优秀的易烊千玺')
    context_obj = Context(parsms)
    # 进行数据渲染
    result = template_obj.render(context_obj)
    # 返回结果
    return HttpResponse(result)
# 模板调用第一种方法（最常用）
# 先导包
from django.shortcuts import render
def indextmp(request):
    name = '哈士奇111'
    # render三个参数：第一个为请求对象，第二个为html文件，第三个为字典（有就加）
    return render(request,'index.html',{'name':name})

# 模板调用第二种方法
from django.shortcuts import render_to_response
def abc(request):
    name = 'hello'
    return render_to_response('abc.html',{'name':name})

# 模板调用第三种方法
from django.template.loader import get_template
def abcd(request):
    template = get_template('abcd.html')
    name = 'world'
    result = template.render({'name':name})
    return HttpResponse(result)

# def yufa(request):
#     name = '张三'
#     age = 18
#     gender = '1.css'
#     hobby = ['吃','唱','跳','篮球','羽毛球']
#     score = {'Math':90,'English':88,'Chinese':99}
#     return render(request,'yufa.html',{'name':name,'age':age,'gender':gender,'hobby':hobby,'score':score})


class Say():
    def say(self):
        return 'hello'
def yufa(request,age):
    name = '张三'
    age = int(age)
    gender = '1.css'
    hobby = ['吃','唱','跳','篮球','羽毛球']
    score = {'Math':90,'English':88,'Chinese':99}
    say = Say()
    return render(request,'yufa.html',locals())

def staticdemo(request):
    params = [
        {'name':'易烊千玺','img':'yyqx.jpg','url':'https://baike.baidu.com/item/%E6%98%93%E7%83%8A%E5%8D%83%E7%8E%BA/221450'},
        {'name':'迪丽热巴','img':'dlrb.jpg','url':'https://baike.baidu.com/item/%E8%BF%AA%E4%B8%BD%E7%83%AD%E5%B7%B4/1180418'},
        {'name':'刘忻','img':'lx.jpg','url':'https://baike.baidu.com/item/刘忻/17268'},
        {'name':'邓伦','img':'dl.jpg','url':'https://baike.baidu.com/item/邓伦/10133303'},

    ]
    return render(request,'staticdemo.html',locals())