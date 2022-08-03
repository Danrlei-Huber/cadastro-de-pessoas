from django.urls import path
from .views import listaPessoaView, PessoaCreateView, PessoaUpdateView, PessoaDeleteView

urlpatterns = [
    path('', listaPessoaView.as_view(),name='pessoa.index'),
    path('novo/',PessoaCreateView.as_view(), name='pessoa.novo'),
    path('editar/<int:pk>',PessoaUpdateView.as_view(), name='pessoa.editar'),
    path('remover/<int:pk>',PessoaDeleteView.as_view(), name='pessoa.remover'),
]