from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import Usuario, Clientes, Produtos


#-----------------------------USUARIO-----------------------------------------

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Requer um email valido')

    class Meta:
        model = Usuario
        fields = ("email", "username", "password1", "password2")

class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("LOGIN INVÁLIDO")

class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('email', 'username')

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                usuario = Usuario.objects.exclude(pk=self.instance.pk).get(email=email)
            except Usuario.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" já está em uso.' %email)

#-----------------------------USUARIO-----------------------------------------


#-----------------------------CLIENTE-----------------------------------------

class ClienteForm(ModelForm):
    class Meta:
        model = Clientes
        fields = '__all__'

#-----------------------------CLIENTE-----------------------------------------


