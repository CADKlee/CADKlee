"""CADKlee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CAD_Klee.urls')),

    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)

    #------------------------------------------------------ALTERAR SENHA----------------------------------------------------------------
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='CAD_Klee/alteracao_senha_completa.html'),
         name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='CAD_Klee/alterar_senha.html'),
         name='password_change'),
    #------------------------------------------------------ALTERAR SENHA----------------------------------------------------------------

    #-----------------------------------------------------RESET DE SENHA----------------------------------------------------------------
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='CAD_Klee/reset_done.html'), #PAGINA DE CONFIRMAÇÃO QUE A SENHA FOI RESETADA E FOI ENVIADO UM EMAIL DIZENDO PARA VOCÊ IR NELE.
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='CAD_Klee/reset_senha_conta_confirmacao.html'), #PAGINA ONDE DEVE DIGITAR E REDIGITAR A NOVA SENHA
         name='password_reset_confirm'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='CAD_Klee/forgetpassword_page.html'), #PAGINA DE ESQUECI A SENHA NA TELA DE LOGIN
         name='password_reset'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='CAD_Klee/reset_senha_completa.html'), #PAGINA ONDE O PASSWORD FOI REDEFINIDO E TE MANDA PRA LOGAR NOVAMENTE
         name='password_reset_complete'),
    # -----------------------------------------------------RESET DE SENHA----------------------------------------------------------------

]
