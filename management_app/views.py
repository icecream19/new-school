from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail

from .models import Teacher, Subject, StudentRegistration, Season, Registration
from .forms import DeterminingForm, RegistrationForm, ContactForm

def home(request):
    this_season = Season.objects.get(running=True)
    o_level = []
    a_level = []
    for item in this_season.subject.all():
        if item.level == '09' or item.level == '10':
            o_level.append(item)
        else:
            a_level.append(item)

    if request.method == 'POST':
        if 'contactphrase' in request.POST:
            contactform = ContactForm(request.POST, prefix='contactform')
            if contactform.is_valid():
                contact(contactform)
    contactform = ContactForm()
    
    context = {
        'total_teachers': Teacher.objects.all().count(),
        'total_subjects': Subject.objects.all().count(),
        'total_enrollments': Registration.objects.all().count(),
        'o_level': o_level,
        'a_level': a_level,
        'contactform': contactform,
    }

    return render(request, 'home.html', context)




def determining(request):
    if request.method == 'POST':
        if 'contactphrase' in request.POST:
            contactform = ContactForm(request.POST, prefix='contactform')
            if contactform.is_valid():
                contact(contactform)
        elif 'determiningphrase' in request.POST:
            form = DeterminingForm(request.POST, prefix='determiningform')
        
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
    contactform = ContactForm()

    context = {
        'form': form,
        'contactform': contactform,
    }

    return render(request, 'determining.html', context)



def admission(request):
    if request.method == 'POST':
        if 'contactphrase' in request.POST:
            contactform = ContactForm(request.POST, prefix='contactform')
            if contactform.is_valid():
                contact(contactform)
        elif 'admissionphrase' in request.POST:
            form = RegistrationForm(data=request.POST, selected_season=request.session['season'], prefix='registrationform')
            if form.is_valid():
                saved = form.save(commit=False)
                season = request.session.get('season')
                saved.selected_season = season
                saved = saved.save()
                return render(request, 'registered.html')
    form = RegistrationForm(selected_season=request.session['season'])
    contactform = ContactForm()

    context = {
        'form': form,
        'contactform': contactform
    }

    return render(request, 'admission.html', context)



def contact(request):

    send_mail(
        'Contact from website by '+request.cleaned_data['name'],
        request.cleaned_data['message']+'\nsender email: '+request.cleaned_data['email'],
        settings.EMAIL_HOST_USER,
        ['saxoya8501@emailhost99.com'],
        fail_silently=False,
    )
