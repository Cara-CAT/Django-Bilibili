# login/views.py

from django.shortcuts import render, redirect

from login import models


def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        message = "所有字段都必须填写！" #无论登录成功失败，都需要为用户添加提示信息
        if username and password:  # 确保用户名和密码都不为空
            username = username.strip()
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    return redirect('/index/')
                # 如果用户名、密码正确，跳转至index页面
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"
        return render(request, 'login/login.html',{"message":message})
    #添加message变量，用于保存提示信息。当有错误的时候，将错误信息打包成一个字典，然后作为第三个参数提供给render（）方法
    return render(request, 'login/login.html')


def register(request):
    pass
    return render(request, 'login/register.html')


def logout(request):
    pass
    return redirect('/index/')