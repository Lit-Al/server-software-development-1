from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import Task
from django.forms import DateInput

class SignUpForm(UserCreationForm):
    error_messages = {
        'password_too_similar': "Пароль не должен быть слишком похож на другую вашу личную информацию.",
        'password_too_short': "Ваш пароль должен содержать как минимум 8 символов.",
        'password_too_common': "Пароль не должен быть слишком простым и распространенным.",
        'password_entirely_numeric': "Пароль не может состоять только из цифр."
    }

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        error_messages = {
            'password_mismatch': "Пароли не совпадают.",
        }



class TaskForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    deadline = forms.DateField(widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'completed', 'priority']
        widgets = {
            'deadline': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }