from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
import random
from firstdjangoapp.models import student
from firstdjangoapp.form import PostForm

# Create your views here.
times = 0

def sayhello(request):
    return HttpResponse("Hello Django!")

def hello2(request, username):
    return HttpResponse("Hello " + username)

def hello3(request, username):
    now = datetime.now()
    return render(request, "hello3.html", locals())

def hello4(request, username):
    now = datetime.now()
    return render(request, "hello4.html", locals())

def dice(request):
    no = random.randint(1, 6)
    return render(request, "dice.html", {"no" : no})

def dice2(request):
    no1 = random.randint(1, 6)
    no2 = random.randint(1, 6)
    no3 = random.randint(1, 6)
    return render(request, "dice2.html", locals())

def dice3(request):
    global times
    times = times + 1
    local_times = times
    username = "David"
    dice_no = {"no" : random.randint(1, 6)}
    return render(request, "dice3.html", locals())

def show(request):
    person1 = {"name":"Amy", "phone":"049-1234567", "age":"20"}
    person2 = {"name":"Jack", "phone":"049-4455666", "age":"25"}
    person3 = {"name":"Nacy", "phone":"049-9876543", "age":"17"}
    persons = [person1, person2, person3]
    return render(request, "show.html", locals())

def filter(request):
    value = 4
    list1 = [1, 2, 3]
    pw = '芝麻開門'
    html = "<h1>Hello</h1>"
    value2 = False
    return render(request, "filter.html", locals())

def listone(request):
    try:
        unit = student.objects.get(cName = "Tyler")
    except:
        errormessage = "(讀取錯誤！)"
    return render(request, "listone.html", locals())

def listall(request):
    students = student.objects.all().order_by('id')
    return render(request, "listall.html", locals())

def index(request):
    students = student.objects.all().order_by('id')
    return render(request, "index.html", locals())

def post(request):
    if request.method == "POST":
        mess = request.POST['username']
    else:
        mess = "表單資料尚未送出！"
    return render(request, "post.html", locals())

def post1(request):
    if request.method == "POST":
        cName = request.POST['cName']
        cGender = request.POST['cGender']
        cBirthday = request.POST['cBirthday']
        cEmail = request.POST['cEmail']
        cPhone = request.POST['cPhone']
        cAddr = request.POST['cAddr']
        unit = student.objects.create(cName = cName, cGender = cGender, cBirthday = cBirthday, cEmail = cEmail, cPhone = cPhone, cAddr = cAddr)
        unit.save()
        return redirect('/index/')
    else:
       message = '請輸入資料（資料不做驗證）'
    return render(request, "post1.html", locals())

def postform(request):
    cName = 'David'
    cGender = 'M'
    cBirthday = '1995/12/23'
    cEmail = '123@django.com'
    cPhone = '12344321'
    cAddr = 'Section 2, Number1'
    postform = PostForm()
    return render(request, "postform.html", locals())

def post2(request):
    if request.method == "POST":
        postform - PostForm(request.POST)
        if postform.is_value():
            cName = postform.cleaned_data['cName']
            cGender = post.cleaned_data['cGender']
            cBirthday = post.cleaned_data['cBirthday']
            cEmail = post.cleaned_data['cEmail']
            cPhone = post.cleaned_data['cPhone']
            cAddr = post.cleaned_data['cAddr']
            unit = student.objects.create(cName = cName, cGender = cGender, cBirthday = cBirthday, cEmail = cEmail, cPhone = cPhone, cAddr =cAddr)
            unit.save()
            message = '以儲存...'
            return redirect('/index/')
        else:
            message = '驗證碼錯誤！'
    else:
        message = '姓名,性別,生日必須輸入！'
        postform = PostForm()
    return render(request, "post2.html", locals())

def edit(request, id = None, mode = None):
    if mode == "edit":
        unit = student.objects.get(id = id)
        unit.cName = request.GET['cName']
        unit.cGender = request.GET['cGender']
        unit.cBirthday = request.GET['cBirthday']
        unit.cPhone = request.GET['cPhone']
        unit.cAddr = request.GET['cAddr']
        unit.save()
        message = '以修改...!'
        return redirect('/index')
    else:
        try:
            unit = student.objects.get(id = id)
            strdate = str(unit.cBirthday)
            strdate2 = strdate.replace("年", "-")
            strdate2 = strdate.replace("月", "-")
            strdates = strdate.replace("日", "-")
            unit.cBirthday =strdate2
        except:
            message = "此id不存在！"
        return render(request, "edit.html", locals())
