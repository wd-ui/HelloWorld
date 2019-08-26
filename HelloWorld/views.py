from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request):
    # return HttpResponse("Hello_World")
    return render(request,"hello.html")
#小括号的字符串最终会响应到前端页面
def hello(request):
    return render(request,'hello.html')