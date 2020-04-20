from django.shortcuts import render
from .models import Teacher, Subject, StudentRegistration, Season

def home(request):
    this_season = Season.objects.get(running=True)
    o_level = []
    a_level = []
    for item in this_season.subject.all():
        if item.level == '09' or item.level == '10':
            o_level.append(item)
        else:
            a_level.append(item)
    
    

    context = {
        'total_teachers': Teacher.objects.all().count(),
        'total_subjects': Subject.objects.all().count(),
        'total_enrollments': StudentRegistration.objects.all().count(),
        'o_level': o_level,
        'a_level': a_level,
    }

    return render(request, 'home.html', context)
