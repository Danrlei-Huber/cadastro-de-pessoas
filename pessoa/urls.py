from django.urls import path
from .views import listaPessoaView, PessoaCreateView

urlpatterns = [
    path('', listaPessoaView.as_view(),name='pessoa.index'),
    path('novo/',PessoaCreateView.as_view(), name='pessoa.novo')
]