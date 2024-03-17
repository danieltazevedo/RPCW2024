import requests
import json

# Define the DBpedia SPARQL endpoint
sparql_endpoint = "http://dbpedia.org/sparql"

# Define the SPARQL query
sparql_query = """
PREFIX dbo: <http://dbpedia.org/ontology/>

SELECT DISTINCT ?filme ?titulo ?resumo ?duracao 
WHERE {
    ?filme a dbo:Film ;
        rdfs:label ?titulo;
        dbo:abstract ?resumo;
        dbp:runtime ?duracao.
    filter(lang(?titulo)='en' && lang(?resumo)='en') .        
}
"""

# Define the headers
headers = {
    "Accept": "application/sparql-results+json"
}

# Define the parameters
params = {
    "query": sparql_query,
    "format": "json"
}

# Send the SPARQL query using requests
response = requests.get(sparql_endpoint, params=params, headers=headers)


# Check if the request was successful
if response.status_code == 200:
    results = response.json()
    # Print the results
    filmes = []
    for result in results["results"]["bindings"]:
        filme = {}
        filme["uri"] = result["filme"]["value"]
        filme["titulo"] = result["titulo"]["value"]
        filme["resumo"] = result["resumo"]["value"]
        filme["duracao"] = result["duracao"]["value"]
        filmes.append(filme)
    file = open("filmes.json",'w')
    json.dump(filmes,file)
    file.close()        
        
else:
    print("Error:", response.status_code)
    print(response.text)
