import xml.etree.ElementTree as ET

tree = ET.parse("royal.xml")
root = tree.getroot()


ttl = f"""
@prefix : <http://rpcw.di.uminho.pt/2024/familia/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@base <http://rpcw.di.uminho.pt/2024/familia/> .

<http://rpcw.di.uminho.pt/2024/familia> rdf:type owl:Ontology .

#################################################################
#    Object Properties
#################################################################

###  http://rpcw.di.uminho.pt/2024/familia/temMae
:temMae rdf:type owl:ObjectProperty ;
        rdfs:domain :Pessoa ;
        rdfs:range :Pessoa .


###  http://rpcw.di.uminho.pt/2024/familia/temPai
:temPai rdf:type owl:ObjectProperty ;
        rdfs:domain :Pessoa ;
        rdfs:range :Pessoa .


#################################################################
#    Data properties
#################################################################

###  http://rpcw.di.uminho.pt/2024/familia#dataMorte
:dataMorte rdf:type owl:DatatypeProperty .


###  http://rpcw.di.uminho.pt/2024/familia#dataNas
:dataNas rdf:type owl:DatatypeProperty .


###  http://rpcw.di.uminho.pt/2024/familia#localEnterro
:localEnterro rdf:type owl:DatatypeProperty .


###  http://rpcw.di.uminho.pt/2024/familia#localMorte
:localMorte rdf:type owl:DatatypeProperty .


###  http://rpcw.di.uminho.pt/2024/familia#localNas
:localNas rdf:type owl:DatatypeProperty .


###  http://rpcw.di.uminho.pt/2024/familia#sexo
:sexo rdf:type owl:DatatypeProperty .


###  http://rpcw.di.uminho.pt/2024/familia#titulo
:titulo rdf:type owl:DatatypeProperty .


###  http://rpcw.di.uminho.pt/2024/familia/nome
:nome rdf:type owl:DatatypeProperty .


#################################################################
#    Classes
#################################################################

###  http://rpcw.di.uminho.pt/2024/familia/Pessoa
:Pessoa rdf:type owl:Class .


#################################################################
#    Individuals
#################################################################
"""

for person in root.findall('person'):
    
    title = person.find('titl')
    if title is not None:
        title = title.text
    else:
        title = ""
        
    sex = person.find('sex')
    if sex is not None:
        sex = sex.text
    else: 
        sex = ""
        
    birthdate = person.find('birthdate')
    if birthdate is not None:
        birthdate = birthdate.text 
    else:
        birthdate = ""
    
    deathdate = person.find('deathdate')
    if deathdate is not None:
        deathdate = deathdate.text 
    else:
        deathdate = ""
        
    deathplace = person.find('deathplace')
    if deathplace is not None:
        deathplace = deathplace.text
    else:
        deathplace = ""
        
    burialplace = person.find('burialplace')
    if burialplace is not None:
        burialplace = burialplace.text
    else:
        burialplace = ""

    parent = person.findall('parent')
    relacoes = ""
    if len(parent) == 2:
        relacoes = f""":temMae :{parent[1].get('ref')} ;
    :temPai :{parent[0].get('ref')} ;"""
    
    elif len(parent) == 1:
        relacoes = f"""
        :temPai :{parent[0].get('ref')} ;
        """
        

        
    pessoa = f"""
###  http://rpcw.di.uminho.pt/2024/familia#{person.find('id').text}
:{person.find('id').text} rdf:type owl:NamedIndividual ,
             :Pessoa ;
    {relacoes}
    :dataMorte "{deathdate}" ;
    :dataNas "{birthdate}" ;
    :localEnterro "{burialplace}" ;
    :localMorte "{deathplace}" ;
    :localNas "Kensington,Palace,London,England" ;
    :sexo "{sex}" ;
    :titulo "{title}" ;
    :nome "{person.find('name').text}" .
    """    
    ttl += pessoa

    
ttl += "###  Generated by the OWL API (version 4.5.26.2023-07-17T20:34:13Z) https://github.com/owlcs/owlap"

output = open("familia_real_povoada.ttl", "w")
output.write(ttl)
