import requests
import json

# Define the DBpedia SPARQL endpoint
sparql_endpoint = "http://dbpedia.org/sparql"

# Define the SPARQL query
sparql_query = """
select distinct ?film ?title ?gender ?duration ?country ?book ?release 
?actor ?actor_name ?actor_birth 
?director ?director_name ?director_birth 
?writer ?writer_name ?writer_birth 
?screen_writer ?screen_writer_name ?screen_writer_birth 
?composer ?composer_name ?composer_birthDate 
?producer ?producer_name ?producer_birth 
where {

    ?film rdf:type <http://dbpedia.org/ontology/Film> .

    optional {?film dbp:name ?title.
            FILTER(LANG(?title) = "en")}

    optional {?film dbp:genre ?film_genre.
            ?film_genre rdfs:label ?gender .
            FILTER(LANG(?gender) = "en")}

    optional {?film dbo:runtime ?duration .}

    optional { ?film dbo:country ?country .}

    optional {?film dbp:basedOn ?book_based.
            ?book_based rdfs:label ?book .
            FILTER(LANG(?book) = "en")}

    optional {?film dbo:releaseDate ?release .}

    optional {?film dbo:starring ?actor.
            ?actor rdfs:label ?actor_name .
            ?actor dbo:birthDate ?actor_birth .
            FILTER(LANG(?actor_name) = "en")}

    optional {?film dbo:director ?director.
            ?director rdfs:label ?director_name .
            ?director dbo:birthDate ?director_birth .
            FILTER(LANG(?director_name) = "en")}

    optional {?film dbo:writer ?writer.
            ?writer rdfs:label ?writer_name .
            ?writer dbo:birthDate ?writer_birth .
            FILTER(LANG(?writer_name) = "en")}

    optional {?film dbp:screenplay ?screen_writer.
            ?screen_writer rdfs:label ?screen_writer_name .
            ?screen_writer dbo:birthDate ?screen_writer_birth .
            FILTER(LANG(?screen_writer) = "en")}

    optional {?film dbo:musicComposer ?composer.
            ?composer foaf:name ?composer_name .
            ?composer dbo:birthDate ?composer_birthDate .
            FILTER(LANG(?composer) = "en")}

    optional {?film dbo:producer ?producer.
            ?producer rdfs:label ?producer_name .
            ?producer dbo:birthDate ?producer_birth .
            FILTER(LANG(?producer_name) = "en")}
  } 
"""

offset = 0
exist_films = True
films = {}

# Define the headers
headers = {
    "Accept": "application/sparql-results+json"
}

while exist_films:
        paginacao = sparql_query + f"\nLIMIT 9999\nOFFSET {offset}"
        # Define the parameters
        params = {
                "query": paginacao, 
                "format": "json", 
                "timeout": 200000
        }
      
        # Send the SPARQL query using requests
        response = requests.get(sparql_endpoint, params=params, headers=headers)


        # Check if the request was successful
        if response.status_code == 200 or response.status_code == 206:
                results = response.json()
                for result in results["results"]["bindings"]:
                        URI = result["film"]["value"]
                        if URI not in films:
                                film = {}
                                film["film"] = URI
                                film["title"] = []
                                film["gender"] = []
                                film["duration"] = [] 
                                film["country"] = []
                                film["book"] = []
                                film["release"] = []
                                film["actors"] = {}
                                film["directors"] = {}
                                film["writers"] = {}
                                film["screenwriters"] = {}
                                film["composers"] = {}
                                film["producers"] = {}
                                films[URI] = film
                        film = films[URI]
                        
                        if 'title' in result.keys():
                                title = result["title"]["value"]
                                if title not in film["title"]:
                                        film["title"].append(title)
                        
                        if 'gender' in result.keys():
                                gender = result["gender"]["value"]
                                if gender not in film["gender"]:
                                        film["gender"].append(gender)
                                        
                        if 'duration' in result.keys():
                                film["duration"] = result["duration"]["value"]
                                
                        if 'country' in result.keys():
                                country = result["country"]["value"]
                                if country not in film["country"]:
                                        film["country"].append(country)
                        
                        if 'book' in result.keys():
                                book = result["book"]["value"]
                                if book not in film["book"]:
                                        film["book"].append(book)
                                        
                        if 'release' in result.keys():
                                film["release"] = result["release"]["value"]
                        
                        if 'actor' in result.keys():    
                                actors = film["actors"]
                                actor = result["actor"]["value"]
                                if actor not in actors:
                                        name = ""
                                        birth = ""
                                        if 'actor_name' in result.keys():
                                                name = result["actor_name"]["value"]
                                        if 'actor_birth' in result.keys():
                                                birth = result["actor_birth"]["value"]
                                        actors[actor] = {"name" : name , "birth" : birth}
                                        film["actors"] = actors
                                        
                        if 'director' in result.keys():    
                                directors = film["directors"]
                                director = result["director"]["value"]
                                if director not in directors:
                                        name = ""
                                        birth = ""
                                        if 'director_name' in result.keys():
                                                name = result["director_name"]["value"]
                                        if 'director_birth' in result.keys():
                                                birth = result["director_birth"]["value"]
                                        directors[director] = {"name" : name , "birth" : birth}
                                        film["directors"] = directors
                        
                        
                        if 'writer' in result.keys():    
                                writers = film["writers"]
                                writer = result["writer"]["value"]
                                if writer not in writers:
                                        name = ""
                                        birth = ""
                                        if 'writer_name' in result.keys():
                                                name = result["writer_name"]["value"]
                                        if 'writer_birth' in result.keys():
                                                birth = result["writer_birth"]["value"]
                                        writers[writer] = {"name" : name , "birth" : birth}
                                        film["writers"] = writers

                        if 'screen_writer' in result.keys():    
                                screenwriters = film["screenwriters"]
                                screen_writer = result["screen_writer"]["value"]
                                if screen_writer not in screenwriters:
                                        name = ""
                                        birth = ""
                                        if 'screen_writer_name' in result.keys():
                                                name = result["screen_writer_name"]["value"]
                                        if 'screen_writer_birth' in result.keys():
                                                birth = result["screen_writer_birth"]["value"]
                                        screenwriters[screen_writer] = {"name" : name , "birth" : birth}
                                        film["screenwriters"] = screenwriters
                                        

                        if 'composer' in result.keys():    
                                composers = film["composers"]
                                composer = result["composer"]["value"]
                                if composer not in composers:
                                        name = ""
                                        birth = ""
                                        if 'composer_name' in result.keys():
                                                name = result["composer_name"]["value"]
                                        if 'composer_birthDate' in result.keys():
                                                birth = result["composer_birthDate"]["value"]
                                        composers[writer] = {"name" : name , "birth" : birth}
                                        film["composers"] = composers
                                                                        
                        if 'producer' in result.keys():    
                                producers = film["producers"]
                                producer = result["producer"]["value"]
                                if producer not in producers:
                                        name = ""
                                        birth = ""
                                        if 'producer_name' in result.keys():
                                                name = result["producer_name"]["value"]
                                        if 'producer_birth' in result.keys():
                                                birth = result["producer_birth"]["value"]
                                        producers[writer] = {"name" : name , "birth" : birth}
                                        film["producers"] = producers
                                        
                        films[URI] = film    
                        
                if   len(results["results"]["bindings"]) != 9999:
                        has_more_results = False
                if 'Link' in response.headers:
                        links = response.headers['Link'].split(',')
                        for link in links:
                                if 'next' in link:
                                        sparql_endpoint = link.split('>')[0].strip()[1:] 
                                        exist_films = True
                                        break
                                        

                
        else:
                print("Error:", response.status_code)
                #print(response.text)
                
        offset += 9999
                
file = open("filmes.json",'w')
json.dump(list(films.values()),file)
file.close()