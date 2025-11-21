from django.urls import path
from . import views

app_name = 'frases'
urlpatterns = [
    path('', views.lista_fraseologias, name='lista_fraseologias'),
    path('fraseologia/<int:pk>/', views.detalhe_fraseologia, name='detalhe_fraseologia'),
    path('fraseologia/nova/', views.criar_fraseologia, name='criar_fraseologia'),
    path('fraseologia/<int:pk>/editar/', views.editar_fraseologia, name='editar_fraseologia'),
    path('fraseologia/<int:pk>/deletar/', views.deletar_fraseologia, name='deletar_fraseologia'),
    path('estatisticas/', views.estatisticas, name='estatisticas'),
    path('categoria/nova/', views.criar_categoria, name='criar_categoria'),
    
    # API endpoints
    path('api/buscar/', views.buscar_fraseologias, name='buscar_fraseologias'),
    path('api/preview/', views.preview_template, name='preview_template'),
]
