from rdflib import Graph, Namespace, URIRef, Literal, RDF , OWL
from urllib.parse import quote
import pprint
import json
import re

def normalize_iri(iri):
    iri = re.sub(r"[\＃\“\”\£\²\♪\−\—\‘\.\,\;\-\–\+\…\¿\#\=\¹\³\$\%\*\¡\×\@\-\°\:\’\!\?\~\&\'\<\>\"\{\}\[\]\(\)\|\\\^\`\/\n\s ]", '', iri)
    return iri

cinema = Namespace("http://rpcw.di.uminho.pt/2024/cinema/")

g = Graph()
g.parse('cinema.ttl')

file = open("../Dataset/filmes.json","r")
data = json.load(file)

genres = []
countries = []
actors = []
directors = []
writers = []
screenwriters = []
composers = []
producers = []

for film in data:
  if film['title'] != [] :
    title = normalize_iri(film['title'][0])
    uri_film = URIRef(f"{cinema}{title}")
    
    g.add((uri_film, RDF.type, OWL.NamedIndividual))
    g.add((uri_film, RDF.type, cinema.Film))
    g.add((uri_film, cinema.title, Literal(title)))
    
    #gender
    for genre in film["gender"]:
          genre = normalize_iri(genre)
          genre_uri = URIRef(f"{cinema}{genre}")
          if genre_uri not in genres:
              genres.append(genre_uri)
              g.add((genre_uri, RDF.type, OWL.NamedIndividual))
              g.add((genre_uri, RDF.type, cinema.Genre))
              g.add((genre_uri, cinema.name, Literal(genre)))
          g.add((uri_film, cinema.hasGenre, genre_uri))
          
    #duration
    duration = film["duration"]
    if duration != []:
      g.add((uri_film, cinema.duration, Literal(duration)))
    
    #country
    for country in film['country']:
      country = normalize_iri(country.split("/")[-1])
      country_uri = URIRef(f"{cinema}{country}")
      if country_uri not in countries:
          countries.append(country_uri)
          g.add((country_uri, RDF.type, OWL.NamedIndividual))
          g.add((country_uri, RDF.type, cinema.Country))
          g.add((country_uri, cinema.name, Literal(country)))
      g.add((uri_film, cinema.hasCountry, country_uri))
    
    #release
    release = film["release"]
    if release != []:
      g.add((uri_film, cinema.date, Literal(release)))
      
    #actors
    actors_film = film["actors"]
    for actor in actors_film:
      name = normalize_iri(actors_film[actor]["name"])
      birth = actors_film[actor]["birth"]
      uri_actor = URIRef(f"{cinema}{name}")
      if uri_actor not in actors:
        g.add((uri_actor, RDF.type, OWL.NamedIndividual))
        g.add((uri_actor, RDF.type, cinema.Actor))
        g.add((uri_actor, cinema.name, Literal(name)))
        g.add((uri_actor, cinema.birthDate, Literal(birth)))
        actors.append(uri_actor)   
      g.add((uri_film, cinema.hasActor, uri_actor))

    #directors
    directors_film = film["directors"]
    for director in directors_film:
      name = normalize_iri(directors_film[director]["name"])
      birth = directors_film[director]["birth"]
      uri_director = URIRef(f"{cinema}{name}")
      if uri_director not in directors:
          g.add((uri_director, RDF.type, OWL.NamedIndividual))
          g.add((uri_director, RDF.type, cinema.Director))
          g.add((uri_director, cinema.name, Literal(name)))
          g.add((uri_director, cinema.birthDate, Literal(birth)))
          directors.append(uri_director)
      g.add((uri_film, cinema.hasDirector, uri_director))
    
    #writers
    writers_film = film["writers"]
    for writer in writers_film:
      name = normalize_iri(writers_film[writer]["name"])
      birth = writers_film[writer]["birth"]
      uri_writer = URIRef(f"{cinema}{name}")
      if uri_writer not in writers:
          g.add((uri_writer, RDF.type, OWL.NamedIndividual))
          g.add((uri_writer, RDF.type, cinema.Writer))
          g.add((uri_writer, cinema.name, Literal(name)))
          g.add((uri_writer, cinema.birthDate, Literal(birth)))
          writers.append(uri_writer)
      g.add((uri_film, cinema.hasWriter, uri_writer))
    
    #screenwriters
    screenwriters_film = film["screenwriters"]
    for screenwriter in screenwriters_film:
      name = normalize_iri(screenwriters_film[screenwriter]["name"])
      birth = screenwriters_film[screenwriter]["birth"]
      uri_screenwriter = URIRef(f"{cinema}{name}")
      if uri_screenwriter not in screenwriters:
          g.add((uri_screenwriter, RDF.type, OWL.NamedIndividual))
          g.add((uri_screenwriter, RDF.type, cinema.Screenwriter))
          g.add((uri_screenwriter, cinema.name, Literal(name)))
          g.add((uri_screenwriter, cinema.birthDate, Literal(birth)))
          screenwriters.append(uri_screenwriter)
      g.add((uri_film, cinema.hasScreenwriter, uri_screenwriter))
    
    #composers
    composers_film = film["composers"]
    for composer in composers_film:
      name = normalize_iri(composers_film[composer]["name"])
      uri_composer = URIRef(f"{cinema}{name}")
      if uri_composer not in composers:
          g.add((uri_composer, RDF.type, OWL.NamedIndividual))
          g.add((uri_composer, RDF.type, cinema.Composer))
          g.add((uri_composer, cinema.name, Literal(name)))
          g.add((uri_composer, cinema.birthDate, Literal(birth)))
          composers.append(uri_composer)
      g.add((uri_film, cinema.hasComposer, uri_composer))
          
    #producers
    producers_film = film["producers"]
    for producer in producers_film:
      name = normalize_iri(producers_film[producer]["name"])
      birth = producers_film[producer]["birth"]
      uri_producer = URIRef(f"{cinema}{name}")
      if uri_producer not in producers:
          g.add((uri_producer, RDF.type, OWL.NamedIndividual))
          g.add((uri_producer, RDF.type, cinema.Producer))
          g.add((uri_producer, cinema.name, Literal(name)))
          g.add((uri_producer, cinema.birthDate, Literal(birth)))
          producers.append(uri_producer)
      g.add((uri_film, cinema.hasProducer, uri_producer))
          
print(len(g))
output = open('cinema_pg50311.ttl', 'wb')
output.write(g.serialize().encode('utf-8'))    


for smt in g:
  pprint.pprint(smt)
  
