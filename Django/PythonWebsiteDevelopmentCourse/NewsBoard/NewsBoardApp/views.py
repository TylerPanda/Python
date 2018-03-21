from django.shortcuts import render
from NewsBoardApp import models
import math

# Create your views here.

page1 = 1

def index(request, pageindex = None):
    global page1
    pagesize = 8
    newsall = models.NewsUnit.objects.all().order_by('-id')
    datasize = len(newsall)
    totpage = math.ceil(datasize / pagesize)
    if pageindex == None:
        page1 = 1
        newsunits = models.NewsUnit.objects.filter(enabled = True).order_by('-id')[:pagesize]
    elif pageindex == "1":
        start = (page1 - 2) * pagesize
        if start >= 0:
            newsunits = models.NewsUnit.objects.filter(enabled = True).order_by('-id')[start:(start + pagesize)]
            page1 -= 1
    elif pageindex == "2":
        start = page1 * pagesize
        if start < datasize:
            newsunits = models.NewsUnit.objects.filter(enabled = True).order_by('-id')[start:(start + pagesize)]
            page1 += 1
    elif pageindex == "3":
        start = (page1 - 1) * pagesize
        newsunits = models.NewsUnit.objects.filter(enabled = True).order_by('-id')[start:(start + pagesize)]
    currentpage = page1
    return render(request, "index.html", locals())

def detail(request, detailid = None):
    unit = models.NewsUnit.objects.get(id = detailid)
    category = unit.category
    title = unit.title
    pubtime = unit.pubtime
    nickname = unit.nickname
    message = unit.message
    unit.press += 1
    unit.save()

    return render(request, "detail.html", locals())

def login(request):
    messages = ''
    if request.method == 'POST':
        name = request.POST['username'].strip()
        password = request.POST['password']
        user1 = authenticate(username = name, password = password)
        if user1 is not None:
            if user1.is_active:
                auth.login(request, user1)
                return redirect('/adminmain')
            else:
                messages = '帳號尚未啟用！'
        else:
            messages = '登入失敗！'
    return render(request, "login.html", locals())

def logout(request):
    auth.logout(request)
    return redirect('/index/')
