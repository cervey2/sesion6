""" Hola mundo con Flask
Paquetes para levantar un servidor HTTP """
from flask import Flask, jsonify 

app = Flask(__name__)

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

@app.route('/users')
def helloWorld():
    return jsonify(data)


@app.route('/users/<int:id>')
def singleUser(id):
    user = list(filter(lambda x: x['id'] == id, data))[0]
    return jsonify(user)

if __name__ == "__main__":
    app.run(debug=True)

