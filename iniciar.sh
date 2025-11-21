#!/bin/bash

echo "🚀 Iniciando Gerenciador de Fraseologias..."
echo ""

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado. Por favor, instale Python 3.11 ou superior."
    exit 1
fi

echo "✅ Python encontrado: $(python3 --version)"
echo ""

# Instalar dependências
echo "📦 Instalando dependências..."
pip3 install -q -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Erro ao instalar dependências."
    exit 1
fi

echo "✅ Dependências instaladas com sucesso!"
echo ""

# Executar migrações
echo "🔄 Verificando migrações..."
python3 manage.py migrate --noinput

echo ""
echo "✅ Tudo pronto!"
echo ""
echo "🌐 Iniciando servidor..."
echo "📍 Acesse: http://localhost:8000"
echo ""
echo "⚠️  Pressione Ctrl+C para parar o servidor"
echo ""

# Iniciar servidor
python3 manage.py runserver
