from django.shortcuts import render
from studentsapp.models import student

# Create your views here.

def post(request):
    if request.method == "POST":
        mess = request.POST['username']
    else:
        mess = "表單尚未送出！"
    return render(request, "post.html", locals())
