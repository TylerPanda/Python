"""firstdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from firstdjangoapp.views import sayhello, hello2, hello3, hello4, dice, dice2, dice3, show, filter, listone, listall, index, post, post1, postform, post2, edit
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', sayhello),
    path('hello/', sayhello),
    path('hello2/<username>/', hello2),
    path('hello3/<username>/', hello3),
    path('hello4/<username>/', hello4),

    path('dice/', dice),
    path('dice2/', dice2),
    path('dice3/', dice3),
    path('show/', show),
    path('filter/', filter),

    path('listone/', listone),
    path('listall/', listall),
    path('', index),
    path('index/', index),

    path('post/', post),
    path('post1/', post1),
    path('post2/', post2),
    #
    # path('delete/(\d+)/', delete),
    #
    path('edit/<int:id>/', edit),
    # path('edit/(\d+)/(\w+)', edit),
    #
    # path('edit2/(\d+)/(\w+)', edit2),
    path('postform/', postform),

]
