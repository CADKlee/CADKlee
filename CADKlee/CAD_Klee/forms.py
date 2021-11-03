from django import forms
from CAD_Klee.models import Clientes, Produtos, Usuario

class CadastroClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['__all__']

class AlterarClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['__all__']

class CadastroProdutoForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['__all__']

class AlterarProdutoForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['__all__']

class CadastroUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['__all__']

class LoginUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['email_USUARIO', 'senha_USUARIO']

class AlterarUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['__all__']
