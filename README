## Para execução local

# Instala o virtualenv, resposável por isolar as dependências e evitar conflitos
pip install virtualenv 

# Cria o ambiente virtual (só executar da primeira vez)
virtualenv --python python3 ENV

# Ativa o ambiente virtual
source ENV/bin/activate

# Encerra o ambiente virtual (usar ao finalizar a aplicação)
deactivate

# Instala as dependências listadas no arquivo com "pip freeze" (só executar da primeira vez)
pipenv install -r requirements.txt

# Instala o server gunicorn que talvez não seja instalado no comando anterior
pipenv install gunicorn

# Executa o arquivo o programa
gunicorn main:app

=================================================