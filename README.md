[![Build Status](https://travis-ci.org/vinicius0197/slack-kpi.png?branch=master)](https://travis-ci.org/vinicius0197/slack-kpi)
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

### Instalando a imagem Docker
Dentro do repositório do projeto, execute o comando:

```
docker build -t jarvis:latest .
```
O comando acima irá criar uma nova imagem a partir do `Dockerfile`, chamada **jarvis**.
Para rodar a imagem na porta 5000, é necessário executar o comando:

```
docker run -d -p 5000:5000 jarvis
```
Para a aplicação funcionar, é necessário enviar as variáveis de ambiente `SHEET_URL` e
`JSON_VALUES` para o container **Docker**.