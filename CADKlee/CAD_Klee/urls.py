from django.urls import path

from .views import LoginPage, SingupPage, ForgetPassword, IndexPage, CadastroCliente, PesquisarCliente, ResultadoPesquisaCliente, \
    AlterarCliente, ExcluirCliente, AdicionarCliente, ControleEstoque, PesquisaProduto, IncluirProduto, EntradaSaidaEstoque, ResultadoPesquisaProduto, \
    AlterarProduto, ExcluirProduto, PerfilDoUsuario, PerfilEditar, AlterarSenha

urlpatterns = [
    path('', LoginPage.as_view(), name='entrar'),
    path('cadastro/', SingupPage.as_view(), name='cadastro'),
    path('recuperar_senha/', ForgetPassword.as_view(), name='recuperar'),
    path('inicio/', IndexPage.as_view(), name='inicio'),
    path('cadastro_de_clientes/', CadastroCliente.as_view(), name='cadastrar-cliente'),
    path('pesquisa_de_cliente/', PesquisarCliente.as_view(), name='pesquisar-cliente'),
    path('resultado_pesquisa_cliente/', ResultadoPesquisaCliente.as_view(), name='resultado-cliente'),
    path('editar_cliente/', AlterarCliente.as_view(), name='editar-cliente'),
    path('confirmar_exclusao/', ExcluirCliente.as_view(), name='excluir-cliente'),
    path('adicionar_cliente/', AdicionarCliente.as_view(), name='adicionar-cliente'),
    path('controle_estoque/', ControleEstoque.as_view(), name='controle-estoque'),
    path('pesquisa_produto/', PesquisaProduto.as_view(), name='pesquisa-produto'),
    path('adicionar_produto/', IncluirProduto.as_view(), name='incluir-produto'),
    path('entrada_saida/', EntradaSaidaEstoque.as_view(), name='entrada-saida-estoque'),
    path('resultado_pesquisa_produto/', ResultadoPesquisaProduto.as_view(), name='resultado-produto'),
    path('editar_produto/', AlterarProduto.as_view(), name='alterar-produto'),
    path('confirmar_exclusao_produto/', ExcluirProduto.as_view(), name='excluir-produto'),
    path('perfil/', PerfilDoUsuario.as_view(), name='perfil-usuario'),
    path('editar_perfil/', PerfilEditar.as_view(), name='editar-perfil'),
    path('alterar_senha/', AlterarSenha.as_view(), name='alterar-senha')
]