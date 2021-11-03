from django.shortcuts import render
from django.views.generic import TemplateView
from CAD_Klee.models import Clientes, Produtos, Usuario

class LoginPage(TemplateView):
    template_name = 'CAD_Klee/login_page.html'

class SingupPage(TemplateView):
    template_name = 'CAD_Klee/singup_page.html'

class ForgetPassword(TemplateView):
    template_name = 'CAD_Klee/forgetpassword_page.html'

class IndexPage(TemplateView):
    template_name = 'CAD_Klee/index_page.html'

class CadastroCliente(TemplateView):
    template_name = 'CAD_Klee/cadastro_clientes.html'

class PesquisarCliente(TemplateView):
    template_name = 'CAD_Klee/pesquisar_cliente.html'

class ResultadoPesquisaCliente(TemplateView):
    template_name = 'CAD_Klee/resultado_pesquisa_cliente.html'

class AlterarCliente(TemplateView):
    template_name = 'CAD_Klee/editar_cliente.html'

class ExcluirCliente(TemplateView):
    template_name = 'CAD_Klee/excluir_cliente.html'

class AdicionarCliente(TemplateView):
    template_name = 'CAD_Klee/adicionar_cliente.html'

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

class PerfilDoUsuario(TemplateView):
    template_name = 'CAD_Klee/perfil_usuario.html'

class PerfilEditar(TemplateView):
    template_name = 'CAD_Klee/editar_perfil.html'

class AlterarSenha(TemplateView):
    template_name = 'CAD_Klee/alterar_senha.html'

# Create your views here.
