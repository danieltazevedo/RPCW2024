import requests
import json

# Define the DBpedia SPARQL endpoint
sparql_endpoint = "http://dbpedia.org/sparql"

f = open("filmes.json")
filmes = json.load(f)
f.close()

# Define the headers
headers = {
    "Accept": "application/sparql-results+json"
}

for filme in filmes:
    ##########################################################################################
    ##atores##
    ##########################################################################################

    sparql_query_atores = f"""
    SELECT DISTINCT ?ator ?nome ?biografia WHERE {{
            <{filme['uri']}> dbo:starring ?ator .
            optional{{ ?ator rdfs:label ?nome . 
                       filter(lang(?nome)='en') .}}
            optional {{?ator dbo:abstract ?biografia .
                       filter(lang(?biografia)='en') . }}
        }}
    """
    print("Filme:", filme['uri'])
    params = {
        "query": sparql_query_atores,
        "format": "json"
    }

    # Send the SPARQL query using requests
    response = requests.get(sparql_endpoint, params=params, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        results = response.json()
        # Print the results
        filme['atores'] = []

        for result in results["results"]["bindings"]:
            ator = {}
            ator["uri"] = result["ator"]["value"]
            if 'nome' in result.keys():
                ator["nome"] = result["nome"]["value"]
            if 'biografia' in result.keys():
                ator["biografia"] = result["biografia"]["value"]
            filme['atores'].append(ator)

    ##########################################################################################
    ##Realizadores##
    ##########################################################################################

    sparql_query_realizadores = f"""
    SELECT DISTINCT ?realizador ?nome ?biografia WHERE {{
            <{filme['uri']}> dbo:director ?realizador .
            optional{{ ?realizador rdfs:label ?nome . 
                       filter(lang(?nome)='en') .}}
            optional {{?realizador dbo:abstract ?biografia .
                       filter(lang(?biografia)='en') . }}
        }}
    """

    params = {
        "query": sparql_query_realizadores,
        "format": "json"
    }

    # Send the SPARQL query using requests
    response = requests.get(sparql_endpoint, params=params, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        results = response.json()
        # Print the results
        filme['realizadores'] = []
        for result in results["results"]["bindings"]:
            realizador = {}
            realizador["uri"] = result["realizador"]["value"]
            if 'nome' in result.keys():
                realizador["nome"] = result["nome"]["value"]
            if 'biografia' in result.keys():
                realizador["biografia"] = result["biografia"]["value"]
            filme['realizadores'].append(realizador)

    ##########################################################################################
    ##Escritores##
    ##########################################################################################

    sparql_query_escritores = f"""
    SELECT DISTINCT ?escritor ?nome ?biografia WHERE {{
            <{filme['uri']}> dbo:writer ?escritor .
            optional{{ ?escritor rdfs:label ?nome . 
                       filter(lang(?nome)='en') .}}
            optional {{?escritor dbo:abstract ?biografia .
                       filter(lang(?biografia)='en') . }}
        }}
    """

    params = {
        "query": sparql_query_escritores,
        "format": "json"
    }

    # Send the SPARQL query using requests
    response = requests.get(sparql_endpoint, params=params, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        results = response.json()
        # Print the results
        filme['escritores'] = []
        for result in results["results"]["bindings"]:
            escritor = {}
            escritor["uri"] = result["escritor"]["value"]
            if 'nome' in result.keys():
                escritor["nome"] = result["nome"]["value"]
            if 'biografia' in result.keys():
                escritor["biografia"] = result["biografia"]["value"]
            filme['escritores'].append(escritor)

    ##########################################################################################
    ##Musicos##
    ##########################################################################################

    sparql_query_musicos = f"""
    SELECT DISTINCT ?musico ?nome ?biografia WHERE {{
            <{filme['uri']}> dbp:music ?musico .
           optional{{ ?musico rdfs:label ?nome . 
                       filter(lang(?nome)='en') .}}
            optional {{?musico dbo:abstract ?biografia .
                       filter(lang(?biografia)='en') . }}
        }}
    """

    params = {
        "query": sparql_query_musicos,
        "format": "json"
    }

    # Send the SPARQL query using requests
    response = requests.get(sparql_endpoint, params=params, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        results = response.json()
        # Print the results
        filme['musicos'] = []
        for result in results["results"]["bindings"]:
            musico = {}
            musico["uri"] = result["musico"]["value"]
            if 'nome' in result.keys():
                musico["nome"] = result["nome"]["value"]
            if 'biografia' in result.keys():
                musico["biografia"] = result["biografia"]["value"]
            filme['musicos'].append(musico)

    else:
        print("Error:", response.status_code)
        print(response.text)

file = open("cinema.json", 'w')
json.dump(filmes, file)
file.close()
