""" Hola mundo con Flask
Paquetes para levantar un servidor HTTP """
from flask import Flask, jsonify 
from flask_httpauth import HTTPTokenAuth


app = Flask(__name__)
auth = HTTPTokenAuth
tokens = ['mi-token']

data = [
{
    'id'    : 1,
    'name' : 'Jane',
    'lastName': 'Doe',
    'gender' : 'F'
},

{
    'id'    : 2,
    'name' : 'Cervey',
    'lastName': 'Doe',
    'gender' : 'F'
}

]

#Método para verificar token
@auth.verify.token
def verify_token(token):
    if token in tokens:
        return True
    return False


@app.route('/users')
def helloWorld():
    return jsonify(data)


@app.route('/users/<int:id>')
def singleUser(id):
    user = list(filter(lambda x: x['id'] == id, data))[0]
    return jsonify(user)

if __name__ == "__main__":
    app.run(debug=True)
