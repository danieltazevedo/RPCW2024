from flask import Flask, render_template, url_for
from datetime import datetime
import requests

app = Flask(__name__)

# data do sistema no formato ISO
data_hora_atual = datetime.now()
data_iso_formatada = data_hora_atual.strftime('%Y-%m-%dT%H:%M:%S')

# GraphDB endpoint
graphdb_endpoint = "http://localhost:7200/repositories/tab_periodica"

@app.route('/')
def index():
    return render_template('index.html',data = {"data" : data_iso_formatada})

@app.route('/elementos')
def elementos():
    sparql_query = """
prefix tp: <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
select * where {
	?s a tp:Element ;
        tp:name ?nome;
    	tp:symbol ?simb;
        tp:atomicNumber ?n;
    	tp:group ?grupo.
} order by ?n
""" 
    resposta = requests.get(graphdb_endpoint, 
                            params = {"query": sparql_query}, 
                            headers = {'Accept': 'application/sparql-results+json'})
    if resposta.status_code == 200 :
        dados = resposta.json()['results']['bindings']
        return render_template('elementos.html', data = dados)
    else: 
        return render_template('error.html', data = data_iso_formatada)

@app.route('/grupos')
def grupos():
    sparql_query = """
prefix tp: <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
select ?grupos where {
	?grupos a tp:Group ;
} 
""" 
    resposta = requests.get(graphdb_endpoint, 
                            params = {"query": sparql_query}, 
                            headers = {'Accept': 'application/sparql-results+json'})
    if resposta.status_code == 200 :
        dados = resposta.json()['results']['bindings']
        return render_template('grupos.html', data = dados)
    else: 
        return render_template('error.html', data = data_iso_formatada)

@app.route('/elementos/<nome>')
def elemento(nome):
    sparql_query = f'''
PREFIX tp: <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
select ?n ?simb ?grupo where {{
    ?s a tp:Element ;
        tp:name "{nome}" ;
    	tp:symbol ?simb;
        tp:atomicNumber ?n;
    	tp:group ?grupo.
}}
'''

    resposta = requests.get(graphdb_endpoint, 
                            params = {"query": sparql_query}, 
                            headers = {'Accept': 'application/sparql-results+json'})
    if resposta.status_code == 200 :
        dados = resposta.json()['results']['bindings']
        return render_template('elemento.html', nome = nome ,data = dados)
    else: 
        return render_template('error.html', data = data_iso_formatada)


@app.route('/grupos/<nome>')
def grupo(nome):
    sparql_query = f'''
prefix tp: <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
select ?elemento_nome where {{
    ?grupo a tp:Group .
    ?group tp:element ?elemento .
    ?elemento tp:name ?elemento_nome .
    filter(str(?grupo) = "http://www.daml.org/2003/01/periodictable/PeriodicTable#{nome}")
}}
'''

    resposta = requests.get(graphdb_endpoint, 
                            params = {"query": sparql_query}, 
                            headers = {'Accept': 'application/sparql-results+json'})
    if resposta.status_code == 200 :
        dados = resposta.json()['results']['bindings']
        print(dados)
        return render_template('grupo.html', nome = nome ,data = dados)
    else: 
        return render_template('error.html', data = data_iso_formatada)


if __name__ == '__main__':
    app.run(debug=True)