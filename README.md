## Iniciando o Projeto

Para rodar esse projeto na sua máquina, você vai precisar do Python 3 instalado. Crie um ambiente
virtual usando o `virtualenv` e faça um clone do repositório. Dentro da pasta principal, use o comando
`pip install -r requirements.txt` para instalar as dependências necessárias.

### Arquivos de Configuração

Esse projeto se comunica com a API do Slack e do Google Sheets, e por isso são necessárias chaves de
autenticação para as APIs.

Crie um arquivo chamado `config.yml` com o seguinte formato dentro da `root` do seu repositório local:

```
sheet_url: LINK_PARA_PLANILHA_GOOGLE_SHEETS
slack_token: TOKEN_DO_SLACK
```

Dentro de `app/common`, crie um arquivo chamado `client_secret.json`, que conterá as informações de acesso
à API do Google Sheets.

### Iniciando o Servidor

Para iniciar o servidor `Flask`, é necessário exportar a seguinte variável de ambiente:

```
export FLASK_APP=app/api/app.py
```

E então usar `flask run` para iniciar a aplicação.

### Rodando os testes

Para rodar os testes, basta usar o comando `pytest` dentro da `root` do repositório.
