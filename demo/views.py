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


def add():
    pass


