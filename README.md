# Criando uma API simples em Flask

## Desadio DIO

Criando uma APi simples em Python e Flask.

![flask](https://github.com/devcaiada/api-flask-dio/blob/main/images/Flask.png?raw=true)

Criei uma api em Flask a partir da tabela abaixo, transformando os dados em um arquivo JSON e retornando os valores.

![tabela](https://raw.githubusercontent.com/devcaiada/api-flask-dio/main/images/transferir.png)

## O Código

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def get_data():
    data = [
        {'Número': 1, 'Nome': 'Mahesh', 'Idade': 25, 'Cidade': 'Bangalore', 'País': 'Índia'},
        {'Número': 2, 'Nome': 'Alex', 'Idade': 26, 'Cidade': 'Londres', 'País': 'Reino Unido'},
        {'Número': 3, 'Nome': 'David', 'Idade': 27, 'Cidade': 'São Francisco', 'País': 'Estados Unidos'},
        {'Número': 4, 'Nome': 'John', 'Idade': 28, 'Cidade': 'Toronto', 'País': 'Canadá'},
        {'Número': 5, 'Nome': 'Chris', 'Idade': 29, 'Cidade': 'Paris', 'País': 'França'},
    ]
    json_data = jsonify(data)
    return json_data

if __name__ == '__main__':
    app.run(debug=True)
```

- O código acima usa o Flask para criar uma API simples.

- A função get_data() é o endpoint da API. Ele é chamado quando um usuário acessa a URL /.

- A função get_data() cria uma lista de dicionários, onde cada dicionário representa uma linha da tabela.

- A lista de dicionários é então convertida em um objeto JSON usando a função jsonify().

- O objeto JSON é finalmente retornado pela função.

## O Retorno

Executando o código e acessando o link: http://127.0.0.1:5000/ , temos o seguinte retorno:

![retorno](https://github.com/devcaiada/api-flask-dio/blob/main/images/retorno.png?raw=true)

---
