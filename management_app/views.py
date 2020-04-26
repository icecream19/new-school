from django.shortcuts import render, redirect
from .models import Teacher, Subject, StudentRegistration, Season, Registration
from .forms import DeterminingForm, RegistrationForm

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




def determining(request):
    if request.method == 'POST':
        form = DeterminingForm(request.POST)
        
        if form.is_valid():
            selected_season = form.cleaned_data['season']

            if selected_season == 'running':
                query = Season.objects.get(running=True)
                request.session['season'] = query.season
            else:
                query = Season.objects.last()
                request.session['season'] = query.season

            return redirect('management_app:admission-page')
    form = DeterminingForm()

    context = {
        'form': form,
    }

    return render(request, 'determining.html', context)



def admission(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST, selected_season=request.session['season'])
        if form.is_valid():
            saved = form.save(commit=False)
            season = request.session.get('season')
            saved.selected_season = season
            saved = saved.save()
            return render(request, 'registered.html')
    form = RegistrationForm(selected_season=request.session['season'])

    context = {
        'form': form
    }

    return render(request, 'admission.html', context)



# def contact(request, *args, **kwargs):
    