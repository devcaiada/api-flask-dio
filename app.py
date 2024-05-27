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