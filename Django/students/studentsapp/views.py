from django.shortcuts import render
from studentsapp.models import student

# Create your views here.
def listone(request):
    try:
        unit = student.objects.get(cName = 'Tyler')
    except:
        errormessage = "(讀取錯誤！)"
    return render(request, "listone.html", locals())

def listall(request):
    students = student.objects.all().order_by('id')
    return render(request, "listall.html", locals())

def index(request):
    students = student.objects.all().order_by('id')
    return render(request, "index.html", locals())
