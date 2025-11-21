# 🎨 Gerenciador de Fraseologias - Versão Melhorada

## 📋 Descrição

Sistema completo de gerenciamento de fraseologias com interface moderna, busca em tempo real, dashboard com estatísticas e muito mais!

## ✨ Novos Recursos

### Interface Moderna
- 🎨 Design com gradientes (roxo, rosa, azul)
- 🌓 Modo escuro/claro com toggle
- ✨ Animações suaves e transições
- 📱 Design totalmente responsivo
- 🎯 Cards interativos com hover effects

### Funcionalidades
- 🔍 **Busca em tempo real** - Filtre fraseologias enquanto digita
- 📊 **Dashboard** - Estatísticas com gráficos interativos (Chart.js)
- 👁️ **Preview ao vivo** - Veja o resultado do template em tempo real
- 📋 **Copiar melhorado** - Feedback visual com toast notification
- ➕ **CRUD completo** - Criar, editar, visualizar e deletar
- 🏷️ **Categorias** - Organize suas fraseologias
- 🎨 **Filtros** - Por categoria e busca textual

### Melhorias Técnicas
- ⚡ API endpoints para busca e preview
- 🔄 Renderização de templates Django
- 💾 Banco de dados SQLite incluído com dados de exemplo
- 🎯 Código limpo e organizado

## 🚀 Como Executar Localmente

### Pré-requisitos
- Python 3.11 ou superior
- pip (gerenciador de pacotes Python)

### Passo a Passo

1. **Instalar dependências**
```bash
pip install -r requirements.txt
```

2. **Executar migrações** (já feito, mas caso precise)
```bash
python manage.py migrate
```

3. **Iniciar servidor**
```bash
python manage.py runserver
```

4. **Acessar aplicação**
Abra seu navegador em: `http://localhost:8000`

## 📁 Estrutura do Projeto

```
fraseologia_manager/
├── FraseologiaManager/      # Configurações do Django
│   ├── settings.py          # Configurações principais
│   ├── urls.py              # URLs principais
│   └── wsgi.py
├── frases/                  # App principal
│   ├── models.py            # Modelos (Categoria, Fraseologia)
│   ├── views.py             # Views e API endpoints
│   ├── urls.py              # URLs do app
│   └── templates/           # Templates HTML
│       └── frases/
│           ├── lista_fraseologias.html
│           ├── detalhe_fraseologia.html
│           ├── form_fraseologia.html
│           ├── confirmar_delete.html
│           ├── estatisticas.html
│           └── form_categoria.html
├── templates/               # Templates base
│   └── base.html            # Template base com navbar e sidebar
├── db.sqlite3               # Banco de dados (16 fraseologias incluídas)
├── manage.py                # Gerenciador Django
└── requirements.txt         # Dependências

```

## 🎯 Funcionalidades Detalhadas

### 1. Página Principal
- Cards com estatísticas (total de fraseologias, categorias, filtradas)
- Busca em tempo real
- Filtro por categoria
- Lista de fraseologias agrupadas por categoria
- Botões de visualizar e editar em cada card

### 2. Visualização de Fraseologia
- Informações completas (categoria, datas)
- Variáveis de exemplo
- Conteúdo renderizado
- Template original
- Botão copiar com feedback visual (toast)
- Botões de editar e deletar

### 3. Editor de Fraseologia
- Formulário completo
- Preview ao vivo do template
- Validação de campos
- Dicas de uso
- Suporte a variáveis Django template

### 4. Dashboard
- Estatísticas gerais
- Tabela de distribuição por categoria
- Gráfico de barras interativo (Chart.js)
- Porcentagens calculadas

### 5. Gerenciamento de Categorias
- Criar novas categorias
- Exemplos de categorias sugeridas

## 🎨 Temas e Cores

### Gradientes Utilizados
- **Primário**: Roxo (#667eea) → Roxo escuro (#764ba2)
- **Secundário**: Rosa (#f093fb) → Vermelho (#f5576c)
- **Sucesso**: Azul claro (#4facfe) → Ciano (#00f2fe)

### Modo Escuro/Claro
- Toggle no topo da página
- Preferência salva no localStorage
- Transições suaves entre temas

## 📊 Dados Incluídos

O banco de dados já vem com:
- **16 fraseologias** de exemplo
- **2 categorias**: "SAP e Rede" e "Orientações"
- Exemplos de templates com variáveis

## 🔧 Tecnologias Utilizadas

- **Backend**: Django 5.2.8
- **Frontend**: Bootstrap 5.3.3
- **Ícones**: Bootstrap Icons
- **Gráficos**: Chart.js 4.4.0
- **Banco de Dados**: SQLite3

## 💡 Dicas de Uso

### Variáveis nos Templates
Use a sintaxe Django template para variáveis:
```
{{ nome_cliente }}
{{ numero_chamado }}
{{ email_suporte }}
{{ data_hoje }}
```

### Criar Nova Fraseologia
1. Clique em "Nova Fraseologia"
2. Preencha título, categoria e template
3. Veja o preview ao vivo
4. Clique em "Salvar"

### Buscar Fraseologias
- Digite na caixa de busca para filtrar em tempo real
- Use o filtro de categoria para refinar
- O contador "Filtradas" atualiza automaticamente

## 🎉 Melhorias Implementadas

Comparado com a versão original:

1. ✅ Interface completamente redesenhada
2. ✅ Modo escuro/claro adicionado
3. ✅ Busca em tempo real implementada
4. ✅ Dashboard com gráficos criado
5. ✅ Sistema CRUD completo
6. ✅ Preview ao vivo no editor
7. ✅ Animações e transições suaves
8. ✅ Feedback visual melhorado
9. ✅ Design responsivo
10. ✅ API endpoints para funcionalidades assíncronas

## 📝 Notas

- O servidor roda por padrão em `http://localhost:8000`
- Para desenvolvimento, DEBUG está ativado
- ALLOWED_HOSTS configurado para aceitar qualquer host
- Banco de dados SQLite incluído e pronto para uso

## 🆘 Solução de Problemas

### Erro ao instalar dependências
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Porta 8000 já em uso
```bash
python manage.py runserver 8080
```
Depois acesse `http://localhost:8080`

### Resetar banco de dados
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

## 📧 Suporte

Em caso de dúvidas ou problemas, verifique:
1. Se todas as dependências foram instaladas
2. Se está usando Python 3.11+
3. Se o servidor está rodando corretamente

---

**Desenvolvido com ❤️ usando Django e Bootstrap**

Aproveite seu novo Gerenciador de Fraseologias! 🚀
