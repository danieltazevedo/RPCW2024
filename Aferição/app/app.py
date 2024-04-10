from flask import Flask, render_template, url_for, request
from datetime import datetime
import requests

app = Flask(__name__)

# data do sistema no formato ISO
data_hora_atual = datetime.now()
data_iso_formatada = data_hora_atual.strftime('%Y-%m-%dT%H:%M:%S')

# GraphDB endpoint
graphdb_endpoint = "http://localhost:7200/repositories/Alunos"

@app.route('/api/alunos')
def alunos():
  if "curso" in request.args:
    sparql_query = f"""
PREFIX : <http://rpcw.di.uminho.pt/2024/avaliacao/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?nome WHERE {{
  ?aluno rdf:type :Aluno .
  ?aluno :nome ?nome.
  ?aluno :hasCurso ?curso .
  ?curso :cursoNome "{request.args["curso"]}" .
}} ORDER BY ?nome
    """
  elif "groupBy" in request.args:
    if request.args["groupBy"] == "curso":
      sparql_query = """
PREFIX : <http://rpcw.di.uminho.pt/2024/avaliacao/>

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT ?curso (COUNT(?aluno) AS ?numAlunos)
WHERE {
  ?aluno rdf:type :Aluno .
  ?aluno :hasCurso ?curso .
  ?curso rdf:type :Curso .
}
GROUP BY ?curso
ORDER BY ?curso
      """
    elif request.args["groupBy"] == "projeto":
      sparql_query = """
PREFIX : <http://rpcw.di.uminho.pt/2024/avaliacao/>

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT ?notaProjeto (COUNT(?aluno) AS ?numAlunos)
WHERE {
  ?aluno rdf:type :Aluno .
  ?aluno :hasProject ?projeto .
  ?projeto rdf:type :Projeto .
  ?projeto :notaProjeto ?notaProjeto .
}
GROUP BY ?notaProjeto
ORDER BY ?notaProjeto
      """
    elif request.args["groupBy"] == "recurso":
      sparql_query = """
PREFIX : <http://rpcw.di.uminho.pt/2024/avaliacao/>

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT ?aluno ?nome ?curso ?notaExame
WHERE {
  ?aluno rdf:type :Aluno .
  ?aluno :nome ?nome .
  ?aluno :hasCurso ?curso .
 
  
  ?exame rdf:type :Exame .
  ?aluno :hasExame ?exame .
  ?exame :exameTipo "recurso" .
  ?exame :exameNota ?notaExame .
}
ORDER BY ?nome
      """
  else:
    sparql_query = """ 
PREFIX : <http://rpcw.di.uminho.pt/2024/avaliacao/>

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT ?idAluno ?nome ?curso 
WHERE {
  ?aluno rdf:type :Aluno .
  ?aluno :alunoId ?idAluno .
  ?aluno :nome ?nome .
  ?aluno :hasCurso ?curso .

}
GROUP BY ?idAluno ?nome ?curso
ORDER BY (?nome)
    """
    
  resposta = requests.get(graphdb_endpoint, 
                          params = {"query": sparql_query}, 
                          headers = {'Accept': 'application/sparql-results+json'})
  if resposta.status_code == 200 :
      dados = resposta.json()['results']['bindings']
      return dados
  else:
      return "ERROR"
    

@app.route('/api/alunos/<string:id>')
def aluno(id):
  sparql_query = f""" 
PREFIX : <http://rpcw.di.uminho.pt/2024/avaliacao/>

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT *
WHERE {{
  ?aluno rdf:type :Aluno .
  ?aluno :alunoId "{id}" .
  ?aluno :nome ?nome .
  ?aluno :hasCurso ?curso .
  ?aluno :hasTPC ?tpc .
  ?tpc :tpcNota ?tpcNota .
  ?aluno :hasProject ?projeto .
  ?aluno :hasExame ?exame.
  ?exame :exameTipo ?tipo .
  ?exame :exameNota ?notaExame .  
  
}}
    """
    
  resposta = requests.get(graphdb_endpoint, 
                          params = {"query": sparql_query}, 
                          headers = {'Accept': 'application/sparql-results+json'})
  if resposta.status_code == 200 :
      dados = resposta.json()['results']['bindings']
      return dados
  else:
      return "ERROR"
  


@app.route('/api/alunos/tpc')
def tpc():
    sparql_query = """ 
PREFIX : <http://rpcw.di.uminho.pt/2024/avaliacao/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>


SELECT ?idAluno ?nome ?curso (COUNT(?tpc) AS ?numTPC)
WHERE {
  ?aluno rdf:type :Aluno ;
         :alunoId ?idAluno ;
         :nome ?nome ;
         :hasCurso ?curso ;
         :hasTPC ?tpc .
}
GROUP BY ?idAluno ?nome ?curso
ORDER BY ?nome
    """
    
    resposta = requests.get(graphdb_endpoint, 
                            params = {"query": sparql_query}, 
                            headers = {'Accept': 'application/sparql-results+json'})
    if resposta.status_code == 200 :
        dados = resposta.json()['results']['bindings']
        return dados
    else:
        return "ERROR"
    
@app.route('/api/alunos/avaliados')
def avaliados():
    sparql_query = """ 
PREFIX : <http://rpcw.di.uminho.pt/2024/avaliacao/>

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT ?aluno ?nome ?curso ?projeto (SUM(?tpcNota) AS ?totalTPC) ?nExame
WHERE {
  ?aluno rdf:type :Aluno .
  ?aluno :nome ?nome .
  ?aluno :hasCurso ?curso .
  ?aluno :hasProject ?projeto .
  ?aluno :hasTPC ?tpc .
  ?tpc :tpcNota ?tpcNota .
  ?aluno :hasExame ?exame.
  ?exame :exameNota ?notaExame .  
  
} group by ?aluno ?nome ?curso ?projeto ?nExame
order by ?nome


    """
    
    resposta = requests.get(graphdb_endpoint, 
                            params = {"query": sparql_query}, 
                            headers = {'Accept': 'application/sparql-results+json'})
    if resposta.status_code == 200 :
      dados = resposta.json()['results']['bindings']
      
      for dado in dados:
        notasExames = []
        projeto = 0
        tpc = 0.0
        
        for key, value in dado.items():
          if key == "projeto":
            projeto = int(value)
          if key == "totalTPC":
            tpc = float(value)
          if key == "notaExame":
            notasExames.append(float(value))
        
        notamax= max(notasExames)
        if projeto < 10:
          dado["notaFinal"] = "R"
        else:
          dado["notaFinal"] = tpc + 0.4 * projeto + 0.4 * notamax              
              
      return dados
    else:
      return "ERROR"


if __name__ == '__main__':
    app.run(debug=True)
