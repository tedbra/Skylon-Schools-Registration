from django.contrib import admin
from .models import Student, Grade, Payment

# Register your models here.

admin.site.register(Student)
admin.site.register(Grade)
admin.site.register(Payment)

