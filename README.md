# Formulário de contato do meu domínio

![](https://img.shields.io/badge/Python-3.12.0-blue.svg)
![](https://img.shields.io/badge/Django-4.2.20-blue.svg)

## Aplicação disponível em:

https://www.niltonpimentel.com.br/

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.12.
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env.
6. Execute os testes.

```console
git clone git@github.com:niltonpimentel02/nilton_pimentel.git nilton_pimentel
python -m venv .venv --upgrade-deps
source .venv/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
pytest
```
