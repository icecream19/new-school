from django.contrib import admin
from .models import Teacher, Subject, StudentRegistration, Season, Registration

admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(StudentRegistration)
admin.site.register(Season)
admin.site.register(Registration)