# Eventex

Sistema de eventos do curso WTTD 
[![Build Status](https://travis-ci.org/bmatheus91/eventex.svg?branch=master)](https://travis-ci.org/bmatheus91/eventex)
[![Code Health](https://landscape.io/github/bmatheus91/eventex/master/landscape.svg?style=flat)](https://landscape.io/github/bmatheus91/eventex/master)

## Como Desenvolver?

1. Clone o repositório
2. Crie um virtualenv com python 3.5
3. Ative o virtualenv
4. Instale as dependencias
5. Configure a instância com o .env
6. Execute os testes

```console
git clone https://github.com/bmatheus91/eventex.git wttd
cd wttd
python -m venv .wttd
source ./wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o Deploy?

1. Crie uma instância pro heroku
2. Envie as configurações pro heroku
3. Defina a SECRET_KEY
4. Defina DEGUB = False
5. Configure o serviço de Email
6. Envie o código pro heroku

```console
heroku create instancia
heroku config:push
heroku config:set SECRET_KEY=python contrib/secret_gen.py
heroku config:set DEBUG=False
#Configuração do email
git push heroku master --force
```