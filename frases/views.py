from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Fraseologia, Categoria
from django.template import Template, Context
from django.db.models import Q, Count
import json

def lista_fraseologias(request):
    """
    Lista todas as fraseologias, agrupadas por categoria.
    """
    categorias = Categoria.objects.all().prefetch_related('fraseologia_set')
    total_fraseologias = Fraseologia.objects.count()
    total_categorias = Categoria.objects.count()
    
    context = {
        'categorias': categorias,
        'titulo': 'Gerenciador de Fraseologias',
        'total_fraseologias': total_fraseologias,
        'total_categorias': total_categorias,
    }
    return render(request, 'frases/lista_fraseologias.html', context)

def detalhe_fraseologia(request, pk):
    """
    Exibe o template da fraseologia para cópia.
    """
    fraseologia = get_object_or_404(Fraseologia, pk=pk)
    
    # Lógica de renderização do template
    template_content = fraseologia.conteudo_template
    
    # Exemplo de contexto. Em um sistema real, isso viria de um formulário ou outra fonte.
    exemplo_contexto = {
        'nome_cliente': 'João da Silva',
        'numero_chamado': 'CHM-2025-12345',
        'email_suporte': 'suporte@empresa.com',
        'data_hoje': '20 de Novembro de 2025',
    }
    
    try:
        template = Template(template_content)
        rendered_content = template.render(Context(exemplo_contexto))
    except Exception as e:
        rendered_content = f"Erro ao renderizar template: {str(e)}"
    
    context = {
        'fraseologia': fraseologia,
        'titulo': fraseologia.titulo,
        'rendered_content': rendered_content,
        'exemplo_contexto': exemplo_contexto,
    }
    return render(request, 'frases/detalhe_fraseologia.html', context)

def criar_fraseologia(request):
    """
    Cria uma nova fraseologia.
    """
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        categoria_id = request.POST.get('categoria')
        conteudo_template = request.POST.get('conteudo_template')
        
        if titulo and categoria_id and conteudo_template:
            categoria = get_object_or_404(Categoria, pk=categoria_id)
            fraseologia = Fraseologia.objects.create(
                titulo=titulo,
                categoria=categoria,
                conteudo_template=conteudo_template
            )
            return redirect('frases:detalhe_fraseologia', pk=fraseologia.pk)
    
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias,
        'titulo': 'Nova Fraseologia',
    }
    return render(request, 'frases/form_fraseologia.html', context)

def editar_fraseologia(request, pk):
    """
    Edita uma fraseologia existente.
    """
    fraseologia = get_object_or_404(Fraseologia, pk=pk)
    
    if request.method == 'POST':
        fraseologia.titulo = request.POST.get('titulo')
        categoria_id = request.POST.get('categoria')
        fraseologia.categoria = get_object_or_404(Categoria, pk=categoria_id)
        fraseologia.conteudo_template = request.POST.get('conteudo_template')
        fraseologia.save()
        return redirect('frases:detalhe_fraseologia', pk=fraseologia.pk)
    
    categorias = Categoria.objects.all()
    context = {
        'fraseologia': fraseologia,
        'categorias': categorias,
        'titulo': f'Editar: {fraseologia.titulo}',
    }
    return render(request, 'frases/form_fraseologia.html', context)

def deletar_fraseologia(request, pk):
    """
    Deleta uma fraseologia.
    """
    fraseologia = get_object_or_404(Fraseologia, pk=pk)
    if request.method == 'POST':
        fraseologia.delete()
        return redirect('frases:lista_fraseologias')
    
    context = {
        'fraseologia': fraseologia,
        'titulo': f'Deletar: {fraseologia.titulo}',
    }
    return render(request, 'frases/confirmar_delete.html', context)

# API endpoints para busca e filtros
def buscar_fraseologias(request):
    """
    API para busca em tempo real.
    """
    query = request.GET.get('q', '')
    categoria_id = request.GET.get('categoria', '')
    
    fraseologias = Fraseologia.objects.all()
    
    if query:
        fraseologias = fraseologias.filter(
            Q(titulo__icontains=query) | 
            Q(conteudo_template__icontains=query)
        )
    
    if categoria_id:
        fraseologias = fraseologias.filter(categoria_id=categoria_id)
    
    results = []
    for f in fraseologias[:20]:  # Limitar a 20 resultados
        results.append({
            'id': f.pk,
            'titulo': f.titulo,
            'categoria': f.categoria.nome,
            'categoria_id': f.categoria.pk,
            'preview': f.conteudo_template[:100] + '...' if len(f.conteudo_template) > 100 else f.conteudo_template,
        })
    
    return JsonResponse({'results': results})

def preview_template(request):
    """
    API para preview de template em tempo real.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            template_content = data.get('template', '')
            context_data = data.get('context', {})
            
            template = Template(template_content)
            rendered = template.render(Context(context_data))
            
            return JsonResponse({
                'success': True,
                'rendered': rendered
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
    
    return JsonResponse({'success': False, 'error': 'Método não permitido'})

def estatisticas(request):
    """
    Dashboard com estatísticas.
    """
    categorias_stats = Categoria.objects.annotate(
        total=Count('fraseologia')
    ).order_by('-total')
    
    total_fraseologias = Fraseologia.objects.count()
    total_categorias = Categoria.objects.count()
    
    context = {
        'titulo': 'Dashboard - Estatísticas',
        'categorias_stats': categorias_stats,
        'total_fraseologias': total_fraseologias,
        'total_categorias': total_categorias,
    }
    return render(request, 'frases/estatisticas.html', context)

# Gerenciamento de categorias
def criar_categoria(request):
    """
    Cria uma nova categoria.
    """
    if request.method == 'POST':
        nome = request.POST.get('nome')
        if nome:
            Categoria.objects.create(nome=nome)
            return redirect('frases:lista_fraseologias')
    
    context = {
        'titulo': 'Nova Categoria',
    }
    return render(request, 'frases/form_categoria.html', context)
