from flask import Flask, render_template, url_for
from datetime import datetime
import requests

app = Flask(__name__)

# data do sistema no formato ISO
data_hora_atual = datetime.now()
data_iso_formatada = data_hora_atual.strftime('%Y-%m-%dT%H:%M:%S')

# GraphDB endpoint
graphdb_endpoint = "http://localhost:7200/repositories/cinema"

@app.route('/')
def index():
    return render_template('index.html',data = {"data" : data_iso_formatada})

@app.route('/films')
def films():
    sparql_query = """ 
    PREFIX : <http://rpcw.di.uminho.pt/2024/cinema/>
    
    select ?film ?duration ?release where {
        ?film a :Film ;
          :duration ?duration;
          :date ?release      
    }
    """
    
    resposta = requests.get(graphdb_endpoint, 
                            params = {"query": sparql_query}, 
                            headers = {'Accept': 'application/sparql-results+json'})
    if resposta.status_code == 200 :
        dados = resposta.json()['results']['bindings']
        return render_template('films.html', data = dados)
    else: 
        return render_template('error.html', data = data_iso_formatada)
    
@app.route('/actors')
def actors():
    sparql_query = """ 
    PREFIX : <http://rpcw.di.uminho.pt/2024/cinema/>

    select ?actor ?db  where {
    ?actor a :Actor ;
    :birthDate ?db;
    }
    """
    
    resposta = requests.get(graphdb_endpoint, 
                            params = {"query": sparql_query}, 
                            headers = {'Accept': 'application/sparql-results+json'})
    if resposta.status_code == 200 :
        dados = resposta.json()['results']['bindings']
        return render_template('actors.html', data = dados)
    else: 
        return render_template('error.html', data = data_iso_formatada)

@app.route('/directors')
def directors():
    sparql_query = """
    PREFIX : <http://rpcw.di.uminho.pt/2024/cinema/>

    select ?director ?db  where {
    ?director a :Director ;
    :birthDate ?db;
    }
    """
    
    resposta = requests.get(graphdb_endpoint, 
                            params = {"query": sparql_query}, 
                            headers = {'Accept': 'application/sparql-results+json'})
    if resposta.status_code == 200 :
        dados = resposta.json()['results']['bindings']
        return render_template('directors.html', data = dados)
    else: 
        return render_template('error.html', data = data_iso_formatada)

@app.route('/writers')
def writers():
    sparql_query = """
    PREFIX : <http://rpcw.di.uminho.pt/2024/cinema/>

    select ?writer ?db  where {
    ?writer a :Writer ;
    :birthDate ?db;
    }
    """
    
    resposta = requests.get(graphdb_endpoint, 
                            params = {"query": sparql_query}, 
                            headers = {'Accept': 'application/sparql-results+json'})
    if resposta.status_code == 200 :
        dados = resposta.json()['results']['bindings']
        return render_template('writers.html', data = dados)
    else: 
        return render_template('error.html', data = data_iso_formatada)

@app.route('/screenwriters')
def screenwriters():
    sparql_query = """
    PREFIX : <http://rpcw.di.uminho.pt/2024/cinema/>

    select ?screenwriter ?db  where {
    ?screenwriter a :Screenwriter ;
    :birthDate ?db;
    }
    """
    
    resposta = requests.get(graphdb_endpoint, 
                            params = {"query": sparql_query}, 
                            headers = {'Accept': 'application/sparql-results+json'})
    if resposta.status_code == 200 :
        dados = resposta.json()['results']['bindings']
        return render_template('screenwriters.html', data = dados)
    else: 
        return render_template('error.html', data = data_iso_formatada)

@app.route('/composers')
def composers():
    sparql_query = """
    PREFIX : <http://rpcw.di.uminho.pt/2024/cinema/>

    select ?composer ?db  where {
    ?composer a :Composer ;
    :birthDate ?db;
    }
    """
    
    resposta = requests.get(graphdb_endpoint, 
                            params = {"query": sparql_query}, 
                            headers = {'Accept': 'application/sparql-results+json'})
    if resposta.status_code == 200 :
        dados = resposta.json()['results']['bindings']
        return render_template('composers.html', data = dados)
    else: 
        return render_template('error.html', data = data_iso_formatada)

@app.route('/producers')
def producers():
    sparql_query = """
    PREFIX : <http://rpcw.di.uminho.pt/2024/cinema/>

    select ?producer ?db  where {
    ?producer a :Producer ;
    :birthDate ?db;
    }
    """
    
    resposta = requests.get(graphdb_endpoint, 
                            params = {"query": sparql_query}, 
                            headers = {'Accept': 'application/sparql-results+json'})
    if resposta.status_code == 200 :
        dados = resposta.json()['results']['bindings']
        return render_template('producers.html', data = dados)
    else: 
        return render_template('error.html', data = data_iso_formatada)


if __name__ == '__main__':
    app.run(debug=True)