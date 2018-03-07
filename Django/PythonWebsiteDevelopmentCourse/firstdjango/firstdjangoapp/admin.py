from django.contrib import admin
from firstdjangoapp.models import student

# Register your models here.

# admin.site.register(student)
# class studentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'cName', 'cGender', 'cBirthday', 'cEmail', 'cPhone', 'cAddr')
# admin.site.register(student, studentAdmin)

class studentAdmin(admin.ModelAdmin):
    list_display = ('id', 'cName', 'cGender', 'cBirthday', 'cEmail', 'cPhone', 'cAddr')
    list_filter = ('cName', 'cGender')
    search_fields = ('cName',)
    ordering = ('id',)

admin.site.register(student, studentAdmin)
