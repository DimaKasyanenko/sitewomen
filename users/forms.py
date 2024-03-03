from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=255, label='Логин', widget=forms.TextInput(attrs={'class': 'form-input', }))
    password = forms.CharField(max_length=255, label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-input', }))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(max_length=255, label='Логин', widget=forms.TextInput(attrs={'class': 'form-input', }))
    password = forms.CharField(max_length=255, label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-input', }))
    password2 = forms.CharField(max_length=255, label='Повтор пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-input', }))

    email = forms.CharField(max_length=255, label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-input', }))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'password2', 'first_name', 'last_name']
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия'
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('E-mail уже существует')
        return email
