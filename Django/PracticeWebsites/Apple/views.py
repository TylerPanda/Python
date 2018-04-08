from django.shortcuts import render
from django.views import generic

# Create your views here.
# class IndexView(generic.ListView):
#     template_name = "Apple/index.html"

def index(request):
    return render(request, "Apple/index.html", locals())
