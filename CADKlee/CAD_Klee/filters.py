import django_filters
from .models import Clientes

class ClientePesquisar(django_filters.FilterSet):
    class Meta:
        model = Clientes
        fields = ['nome_CLIENTE']