from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .models import Clientes
from .forms import ClienteForm

#---------------------USUARIO------------------------------------

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            usuario = authenticate(email=email, password=raw_password)
            login(request, usuario)
            return  redirect('inicio')
        else:
            context['registration_form'] = form
    else: #GET request
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'CAD_Klee/singup_page.html', context)


def logout_view(request):
    logout(request)
    return redirect('entrar')

def login_view(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            return redirect('entrar')

    return render(request, "CAD_Klee/login_page.html")

# def login_view(request, *args, **kwargs):
#
#     context = {}
#
#     user = request.user
#     if user.is_authenticated:
#         return redirect("inicio")
#
#     destination = get_redirect_if_exists(request)
#     if request.POST:
#         form = AccountAuthenticationForm(request.POST)
#         if form.is_valid():
#             email = request.POST['email']
#             password = request.POST['password']
#             user = authenticate(email=email, password=password)
#             if user:
#                 login(request, user)
#                 destination = get_redirect_if_exists(request)
#                 if destination:
#                     return redirect(destination)
#                 return redirect('entrar')
#         else:
#             context['login_form'] = form
#             return render(request, 'CAD_Klee/login_page.html', context)

    # if request.POST:
    #     form = AccountAuthenticationForm(request.POST)
    #     if form.is_valid():
    #         email = request.POST['email']
    #         password = request.POST['password']
    #         user = authenticate(email=email, password=password)
    #
    #         if user:
    #             login(request, user)
    #             return redirect("inicio")
    #     else:
    #         form = AccountAuthenticationForm()


# def get_redirect_if_exists(request):
#     redirect = None
#     if request.GET:
#         if request.GET.get("next"):
#             redirect = str(request.GET.get("next"))
#     return redirect

# class LoginPage(TemplateView):
#     template_name = 'CAD_Klee/login_page.html'
#
# class SingupPage(TemplateView):
#     template_name = 'CAD_Klee/singup_page.html'

class ForgetPassword(TemplateView):
    template_name = 'CAD_Klee/forgetpassword_page.html'


class PerfilDoUsuario(TemplateView):
    template_name = 'CAD_Klee/perfil_usuario.html'

def account_view(request):

    if not request.user.is_authenticated:
        return redirect('entrar')

    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = AccountUpdateForm(
            initial= {
                "email": request.user.email,
                "nome": request.user.username,
            }
        )
    context['account_form'] = form
    return render(request, 'CAD_Klee/editar_perfil.html', context)

# class PerfilEditar(TemplateView):
#     template_name = 'CAD_Klee/editar_perfil.html'

class AlterarSenha(TemplateView):
    template_name = 'CAD_Klee/alterar_senha.html'

#---------------------USUARIO------------------------------------


#------------------------PAGINAS-------------------------------------

class IndexPage(TemplateView):
    template_name = 'CAD_Klee/index_page.html'

#------------------------PAGINAS-------------------------------------


#------------------------CLIENTES------------------------------------

class CadastroCliente(TemplateView):
    template_name = 'CAD_Klee/cadastro_clientes.html'

def PesquisarCliente(request):
    qs = Clientes.objects.all()
    nome_CLIENTE_query = request.GET.get('nome_CLIENTE')
    print(nome_CLIENTE_query)
    context = {
        'queryset': qs
    }
    return render(request, 'CAD_Klee/pesquisar_cliente.html', context)

# class PesquisarCliente(TemplateView):
#     template_name = 'CAD_Klee/pesquisar_cliente.html'

class ResultadoPesquisaCliente(TemplateView):
    template_name = 'CAD_Klee/resultado_pesquisa_cliente.html'

class AlterarCliente(TemplateView):
    template_name = 'CAD_Klee/editar_cliente.html'

class ExcluirCliente(TemplateView):
    template_name = 'CAD_Klee/excluir_cliente.html'


def AdicionarCliente(request):

    form = ClienteForm()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            dados = form.save()
            print('DADOS: %s' %dados)
            return  redirect('cadastrar-cliente')

    context = {'client_registration_form': form}
    return render(request, 'CAD_Klee/adicionar_cliente.html', context)

# class AdicionarCliente(TemplateView):
#     template_name = 'CAD_Klee/adicionar_cliente.html'

#------------------------CLIENTES------------------------------------


#------------------------ESTOQUE-------------------------------------
class ControleEstoque(TemplateView):
    template_name = 'CAD_Klee/controle_estoque.html'

class PesquisaProduto(TemplateView):
    template_name = 'CAD_Klee/pesquisar_produto.html'

class IncluirProduto(TemplateView):
    template_name = 'CAD_Klee/adicionar_produto.html'

class EntradaSaidaEstoque(TemplateView):
    template_name = 'CAD_Klee/entrada_saida.html'

class ResultadoPesquisaProduto(TemplateView):
    template_name = 'CAD_Klee/resultado_pesquisa_produto.html'

class AlterarProduto(TemplateView):
    template_name = 'CAD_Klee/editar_produto.html'

class ExcluirProduto(TemplateView):
    template_name = 'CAD_Klee/excluir_produto.html'

#------------------------ESTOQUE-------------------------------------



# Create your views here.
