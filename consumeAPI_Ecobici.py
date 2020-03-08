import csv
from flask import Flask, jsonify 

app = Flask(__name__) #Flask levanta un servidor HTTP

    
def get_data():

    """ Reads csv data as dict """
    data = [] #Se define una lista
    with open('ecobici.csv', 'r') as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:
            data.append(row)

    return data



@app.route('/recorridos')
def recorridos():  
        datos = get_data()
        size = request.args.get('pageSize')
        return jsonify(datos[:100]) #Se transforma a json la lista y se filtran sólo los primeros 100 registros

if __name__ == "__main__":

    app.run()