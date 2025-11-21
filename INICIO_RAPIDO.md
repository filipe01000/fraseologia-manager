# 🚀 Início Rápido - Gerenciador de Fraseologias

## ⚡ Método Mais Rápido

### Windows
1. Extraia o arquivo ZIP
2. Dê duplo clique em `iniciar.bat`
3. Aguarde a instalação automática
4. Acesse `http://localhost:8000` no navegador

### Linux/Mac
1. Extraia o arquivo ZIP
2. Abra o terminal na pasta extraída
3. Execute: `./iniciar.sh`
4. Acesse `http://localhost:8000` no navegador

## 📋 Método Manual

Se os scripts não funcionarem:

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Iniciar servidor
python manage.py runserver

# 3. Acessar no navegador
# http://localhost:8000
```

## 🎯 Primeiros Passos

1. **Explorar Fraseologias**
   - A página inicial mostra todas as 16 fraseologias de exemplo
   - Use a busca para filtrar em tempo real

2. **Testar Busca**
   - Digite "senha" na caixa de busca
   - Veja os resultados filtrarem instantaneamente

3. **Visualizar Dashboard**
   - Clique em "Dashboard" no menu lateral
   - Veja estatísticas e gráficos

4. **Criar Nova Fraseologia**
   - Clique em "Nova Fraseologia"
   - Preencha o formulário
   - Veja o preview ao vivo

5. **Testar Modo Escuro**
   - Clique no ícone de lua/sol no topo
   - Veja a interface mudar de tema

## 🎨 Recursos para Testar

### Busca em Tempo Real
- Digite: "SAP", "senha", "orientação"
- Use o filtro de categoria

### Copiar Fraseologia
- Clique em "Visualizar" em qualquer fraseologia
- Clique no botão "Copiar"
- Veja a notificação de sucesso

### Editor com Preview
- Crie ou edite uma fraseologia
- Digite no campo de template
- Veja o preview atualizar automaticamente

### Dashboard
- Veja distribuição por categoria
- Gráfico de barras interativo
- Estatísticas gerais

## ❓ Problemas Comuns

### "Python não encontrado"
- Instale Python 3.11+ de python.org
- Reinicie o terminal/prompt

### "Porta 8000 já em uso"
```bash
python manage.py runserver 8080
# Acesse http://localhost:8080
```

### "Erro ao instalar dependências"
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 📱 Acesso

Após iniciar o servidor, acesse:
- **URL**: http://localhost:8000
- **Parar servidor**: Pressione `Ctrl+C` no terminal

## 🎉 Pronto!

Agora você pode:
- ✅ Criar fraseologias
- ✅ Editar templates
- ✅ Buscar em tempo real
- ✅ Ver estatísticas
- ✅ Copiar conteúdos
- ✅ Usar modo escuro

**Divirta-se! 🚀**
