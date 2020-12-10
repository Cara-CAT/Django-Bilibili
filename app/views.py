from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def hello(request):
    if request.method=='GET':
        return HttpResponse('hello world!')

#登录
def login(request):
    if request.method=='GET':
        request.session['username']=''
        return render(request,'index.html')

#注册
def register(request):
    pass

#显示结果
def result(request):
     pass
