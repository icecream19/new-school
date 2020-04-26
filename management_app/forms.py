from django import forms
from .models import Registration, Subject

SEASON_CHOICES = (
    (None,"Select from following choices"),
    ('running', 'Running season'),
    ('next', 'Next season' )
)


class DeterminingForm(forms.Form):
    prefix = 'determiningform'
    season = forms.ChoiceField(widget=forms.Select, choices=SEASON_CHOICES)


class RegistrationForm(forms.ModelForm):
    prefix = 'registrationform'
    student_address = forms.CharField(label='', widget=forms.Textarea(attrs={'class':'materialize-textarea'}))

    class Meta:
        model = Registration
        exclude = ['selected_season']

    def __init__(self, selected_season, *args, **kwargs):
        session_season = selected_season
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['selected_subject'].queryset = Subject.objects.filter(season=session_season)


class ContactForm(forms.Form):
    prefix = 'contactform'

    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    message = forms.CharField()