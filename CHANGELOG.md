# 📝 Changelog - Gerenciador de Fraseologias

## Versão 1.4 - 20/11/2025

### 🎨 Correções de Cores Globais no Modo Escuro

#### Contraste Aplicado em Toda a Aplicação
- ✅ **Todos os títulos** (h1-h6) em branco (#ffffff)
- ✅ **Parágrafos** em cinza claro (#d1d1d1)
- ✅ **Labels de formulários** em cinza claro (#e4e4e4)
- ✅ **Textos de ajuda** em cinza médio (#b8b8b8)
- ✅ **Tabelas** (td, th) em cinza claro (#e4e4e4)
- ✅ **Texto muted** em cinza (#9ca3af)
- ✅ **Listas** (li) em cinza claro (#d1d1d1)
- ✅ **Badges e alerts** em branco (#ffffff)
- ✅ **Definições** (dt, dd) em cinza claro (#e4e4e4)

#### Problema Resolvido
As correções de contraste estavam aplicadas apenas na página principal. Agora TODO o aplicativo tem cores adequadas no modo escuro:
- Dashboard com estatísticas legíveis
- Formulários com labels visíveis
- Páginas de detalhes com texto claro
- Tabelas com boa legibilidade

---

## Versão 1.3 - 20/11/2025

### 📏 Correções de Espaçamento

#### Título Principal com Espaçamento Adequado
- ✅ **Título "Gerenciador de Fraseologias"** agora com espaçamento superior
- ✅ **Todas as páginas** com títulos bem posicionados
- ✅ **Margem de 20px** adicionada no topo
- ✅ **Padding aumentado** (pt-4, pb-3, mb-4)

#### Problema Resolvido
O título principal estava colado na navbar roxa, sem respiro visual. Agora tem espaçamento adequado em todas as páginas.

---

## Versão 1.2 - 20/11/2025

### 🎨 Correções de Alinhamento

#### Ícones Alinhados Verticalmente
- ✅ **Links da sidebar** agora com ícones perfeitamente alinhados
- ✅ **Títulos das páginas** (h1, h2) com ícones centralizados
- ✅ **Todos os headings** (h1-h6) com alinhamento vertical correto
- ✅ **Flexbox aplicado** para garantir alinhamento consistente

#### Problema Resolvido
Os ícones estavam desalinhados verticalmente com os textos, ficando muito acima ou abaixo. Agora todos estão perfeitamente centralizados.

---

## Versão 1.1 - 20/11/2025

### 🎨 Correções de Interface

#### Modo Escuro - Melhorias de Contraste
- ✅ **Títulos dos cards** agora aparecem em branco (#ffffff) no modo escuro
- ✅ **Textos descritivos** em cinza claro (#b8b8b8) para melhor legibilidade
- ✅ **Títulos de seção (h2)** em branco para destaque adequado
- ✅ **Todos os h5** (subtítulos) também em branco no modo escuro

#### Problema Resolvido
Antes os textos ficavam quase invisíveis no modo noturno devido ao baixo contraste entre o texto escuro e o fundo escuro. Agora todos os textos têm contraste adequado e são perfeitamente legíveis.

#### Alterações Técnicas
Arquivo modificado: `templates/base.html`

Adicionado CSS específico para modo escuro:
```css
[data-theme="dark"] .card-title {
    color: #ffffff !important;
}

[data-theme="dark"] .card-text {
    color: #b8b8b8 !important;
}

[data-theme="dark"] h2 {
    color: #ffffff !important;
}

[data-theme="dark"] h5 {
    color: #ffffff !important;
}
```

---

## Versão 1.0 - 20/11/2025

### 🎉 Lançamento Inicial

#### Recursos Implementados
- ✨ Interface moderna com gradientes
- 🌓 Modo escuro/claro com toggle
- 🔍 Busca em tempo real
- 📊 Dashboard com estatísticas
- 👁️ Preview ao vivo no editor
- 📋 Sistema CRUD completo
- 🎨 Design responsivo
- 💾 16 fraseologias de exemplo
- 📁 2 categorias pré-configuradas

---

## 🔄 Como Atualizar

Se você já tem a versão anterior instalada:

1. Faça backup do seu banco de dados atual (`db.sqlite3`)
2. Extraia a nova versão
3. Substitua apenas o arquivo `templates/base.html`
4. Ou substitua tudo e copie seu `db.sqlite3` de volta

---

**Última atualização**: 20/11/2025 às 18:14
