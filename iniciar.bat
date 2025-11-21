@echo off
echo 🚀 Iniciando Gerenciador de Fraseologias...
echo.

REM Verificar se Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python não encontrado. Por favor, instale Python 3.11 ou superior.
    pause
    exit /b 1
)

echo ✅ Python encontrado
echo.

REM Instalar dependências
echo 📦 Instalando dependências...
pip install -q -r requirements.txt

if %errorlevel% neq 0 (
    echo ❌ Erro ao instalar dependências.
    pause
    exit /b 1
)

echo ✅ Dependências instaladas com sucesso!
echo.

REM Executar migrações
echo 🔄 Verificando migrações...
python manage.py migrate --noinput

echo.
echo ✅ Tudo pronto!
echo.
echo 🌐 Iniciando servidor...
echo 📍 Acesse: http://localhost:8000
echo.
echo ⚠️  Pressione Ctrl+C para parar o servidor
echo.

REM Iniciar servidor
python manage.py runserver

pause
