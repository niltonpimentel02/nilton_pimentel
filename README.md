# Formulário de contato do meu domínio

[![Python application](https://github.com/niltonpimentel02/nilton_pimentel/actions/workflows/main.yml/badge.svg)](https://github.com/niltonpimentel02/nilton_pimentel/actions/workflows/main.yml)

## Aplicação disponível em:

https://www.niltonpimentel.com.br/

https://niltonpimentel.herokuapp.com/

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.9.0
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env.
6. Execute os testes.

```console
git clone git@github.com:niltonpimentel02/nilton_pimentel.git nilton_pimentel
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
pytest
```
