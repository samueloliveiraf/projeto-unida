# Projeto-UNIDA
## Trata-se de aplicação Django para gerenciamento de Usuários
### Configuração para rodar o projeto

Download Project

    git clone https://github.com/samueloliveiraf/projeto-unida.git


Install PostgreSQL
    
    sudo apt -y install postgresql postgresql-contrib
    
PostgreSQL

    sudo su - postgres
    psql
    CREATE DATABASE dbname;
    

Intall Python
    
    sudo apt -y install build-essential python3-venv python3-dev libpq-dev
    
---------------------------------------------------------------------
### Os camandos a seguir tem ser executado dentro da pasta do projeto
---------------------------------------------------------------------
   
Run Project

    python3 -m venv .venv

Active venv

    source venv/bin/activate
    
Install Requirements

    pip install -r requeriments.txt

Config .env

    touch .env
    vim .env
 Exemple: 
    
    DB_NAME=dbname
    DB_USER=postgres
    DB_PASSWORD=159753got42
    DB_HOST=localhost
    DB_PORT=5432

    DEBUG=True
    SECRET_KEY=django-insecure-s8j1i^3&daow=)x!%l&+6-sx-#$73%c$c2$8or=zjbhg*o!gmr
    
-------------------------------------------------------------------
### A SECRET_KEY acima é a oficial do projeto
-------------------------------------------------------------------

Comands ends

    python manage.py migrate
    
Run

    python manage.py runserver
    
