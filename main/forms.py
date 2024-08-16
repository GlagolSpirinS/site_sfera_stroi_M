from django import forms
from .models import applicant

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = applicant
        fields = ['name', 'surname', 'number', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Введите ваше имя'}),
            'surname': forms.TextInput(attrs={'placeholder': 'Введите вашу фамилию'}),
            'number': forms.TextInput(attrs={'placeholder': 'Введите номер телефона'}),
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40, 'placeholder': 'Опишите себя'}),
        }