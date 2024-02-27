import json

f = open("plantas.json")
bd = json.load(f)
f.close

ttl = ttl = f"""
@prefix : <http://rpcw.di.uminho.pt/2024/plantas/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@base <http://rpcw.di.uminho.pt/2024/plantas/> .

<http://rpcw.di.uminho.pt/2024/plantas> rdf:type owl:Ontology .

#################################################################
#    Annotation properties
#################################################################

###  http://purl.org/dc/elements/1.1/creator
<http://purl.org/dc/elements/1.1/creator> rdf:type owl:AnnotationProperty .


#################################################################
#    Object Properties
#################################################################

###  http://www.rpcw.di.uminho.pt/2024/plantas#temMorada
:temMorada rdf:type owl:ObjectProperty ;
          rdfs:domain :Planta ;
          rdfs:range :Morada ;
          <http://purl.org/dc/elements/1.1/creator> "danieltazevedo" .


#################################################################
#    Data properties
#################################################################


<http://www.rpcw.di.uminho.pt/2024/plantas#codigo_rua
:codigoDeRua rdf:type owl:DatatypeProperty ;
             rdfs:domain :Morada ;
             rdfs:range xsd:int ;
             <http://purl.org/dc/elements/1.1/creator> "danieltazevedo" .


<http://www.rpcw.di.uminho.pt/2024/plantas#freguesia
:freguesia rdf:type owl:DatatypeProperty ;
           rdfs:domain :Morada ;
           rdfs:range xsd:string ;
           <http://purl.org/dc/elements/1.1/creator> "danieltazevedo" .


<http://www.rpcw.di.uminho.pt/2024/plantas#local
:local rdf:type owl:DatatypeProperty ;
       rdfs:domain :Morada ;
       rdfs:range xsd:string ;
       <http://purl.org/dc/elements/1.1/creator> "danieltazevedo" .


<http://www.rpcw.di.uminho.pt/2024/plantas#rua
:rua rdf:type owl:DatatypeProperty ;
     rdfs:domain :Morada ;
     rdfs:range xsd:string ;
     <http://purl.org/dc/elements/1.1/creator> "danieltazevedo" .

  


<http://www.rpcw.di.uminho.pt/2024/plantas#id
:id rdf:type owl:DatatypeProperty ;
    rdfs:domain :Planta ;
    rdfs:range xsd:integer ;
    <http://purl.org/dc/elements/1.1/creator> "danieltazevedo" .


<http://www.rpcw.di.uminho.pt/2024/plantas#numero_registo
:numero_registo rdf:type owl:DatatypeProperty ;
                 rdfs:domain :Planta ;
                 rdfs:range xsd:int ;
                 <http://purl.org/dc/elements/1.1/creator> "danieltazevedo" .


<http://www.rpcw.di.uminho.pt/2024/plantas#especie
:especie rdf:type owl:DatatypeProperty ;
                rdfs:domain :Planta ;
                rdfs:range xsd:string ;
                <http://purl.org/dc/elements/1.1/creator> "danieltazevedo" .


<http://www.rpcw.di.uminho.pt/2024/plantas#nome_cientifico
:nome_cientifico rdf:type owl:DatatypeProperty ;
                rdfs:domain :Planta ;
                rdfs:range xsd:string ;
                <http://purl.org/dc/elements/1.1/creator> "danieltazevedo" .


<http://www.rpcw.di.uminho.pt/2024/plantas#origem
:origem rdf:type owl:DatatypeProperty ;
        rdfs:domain :Planta ;
        rdfs:range xsd:string ;
        <http://purl.org/dc/elements/1.1/creator> "danieltazevedo" .


<http://www.rpcw.di.uminho.pt/2024/plantas#data_plantacao
:data_plantacao rdf:type owl:DatatypeProperty ;
                 rdfs:domain :Planta ;
                 rdfs:range xsd:string ;
                 <http://purl.org/dc/elements/1.1/creator> "danieltazevedo" .


<http://www.rpcw.di.uminho.pt/2024/plantas#estado
:estado rdf:type owl:DatatypeProperty ;
        rdfs:domain :Planta ;
        rdfs:range xsd:string ;
        <http://purl.org/dc/elements/1.1/creator> "danieltazevedo" .


<http://www.rpcw.di.uminho.pt/2024/plantas#caldeira
:caldeira rdf:type owl:DatatypeProperty ;
          rdfs:domain :Planta ;
          rdfs:range xsd:string ;
          <http://purl.org/dc/elements/1.1/creator> "danieltazevedo" .


<http://www.rpcw.di.uminho.pt/2024/plantas#tutor
:tutor rdf:type owl:DatatypeProperty ;
       rdfs:domain :Planta ;
       rdfs:range xsd:string ;
       <http://purl.org/dc/elements/1.1/creator> "danieltazevedo" .


<http://www.rpcw.di.uminho.pt/2024/plantas#implantacao
:implantacao rdf:type owl:DatatypeProperty ;
             rdfs:domain :Planta ;
             rdfs:range xsd:string ;
             <http://purl.org/dc/elements/1.1/creator> "danieltazevedo" .


<http://www.rpcw.di.uminho.pt/2024/plantas#gestor
:gestor rdf:type owl:DatatypeProperty ;
        rdfs:domain :Planta ;
        rdfs:range xsd:string ;
        <http://purl.org/dc/elements/1.1/creator> "danieltazevedo" .


<http://www.rpcw.di.uminho.pt/2024/plantas#data_atualizacao
:data_atualizacao rdf:type owl:DatatypeProperty ;
                    rdfs:domain :Planta ;
                    rdfs:range xsd:string ;
                    <http://purl.org/dc/elements/1.1/creator> "danieltazevedo" .


<http://www.rpcw.di.uminho.pt/2024/plantas#numero_intervencao
:numero_intervencao rdf:type owl:DatatypeProperty ;
                      rdfs:domain :Planta ;
                      rdfs:range xsd:int ;
                      <http://purl.org/dc/elements/1.1/creator> "danieltazevedo" .



#################################################################
#    Classes
#################################################################


###  http://www.rpcw.di.uminho.pt/2024/plantas#Morada
:Morada rdf:type owl:Class ;
        <http://purl.org/dc/elements/1.1/creator> "danieltazevedo" .


###  http://www.rpcw.di.uminho.pt/2024/plantas#Planta
:Planta rdf:type owl:Class ;
        <http://purl.org/dc/elements/1.1/creator> "danieltazevedo" .


#################################################################
#    Individuals
#################################################################

"""




for planta in bd:
    registo = f"""
    ###  http://www.rpcw.di.uminho.pt/2024/plantas#{planta['Local'].replace(" ","_").replace('"',"")}_{planta['Código de rua']}
    <http://www.rpcw.di.uminho.pt/2024/plantas#{planta['Local'].replace(" ","_").replace('"',"")}_{planta['Código de rua']}> rdf:type owl:NamedIndividual ,
                                                                        :Morada;
                                                                :codigo_rua "{planta["Código de rua"]}"^^xsd:int ;
                                                                :rua "{planta['Rua'].replace(" ", "_")}^^xsd:string ;
                                                                :local "{planta['Local'].replace(" ", "_")}^^xsd:string ;
                                                                :freguesia "{planta['Freguesia'].replace(" ", "_")}^^xsd:string ;

    
    ###  http://www.rpcw.di.uminho.pt/2024/plantas#{planta['Id']}
    <http://www.rpcw.di.uminho.pt/2024/plantas#{planta['Id']}> rdf:type owl:NamedIndividual ,
                                                                        :Planta;
                                                                :temMorada :"{planta['Código de rua']}"^^xsd:int ;
                                                                :id "{planta['Id']}"^^xsd:int ;
                                                                :numero_registo "{planta["Número de Registo"]}"^^xsd:int ;
                                                                :especie "{planta['Espécie'].replace(" ", "_")}^^xsd:string ;
                                                                :nome_cientifico "{planta['Nome Científico'].replace(" ", "_")}^^xsd:string ;
                                                                :origem "{planta["Origem"]}"^^xsd:string ;
                                                                :data_plantacao "{planta["Data de Plantação"]}"^^xsd:string ;
                                                                :estado "{planta['Estado']}"^^xsd:string ;
                                                                :caldeira "{planta["Caldeira"]}"^^xsd:boolean ;
                                                                :tutor "{planta["Tutor"]}"^^xsd:boolean ;
                                                                :implantacao "{planta['Implantação'].replace(" ", "_")}"^^xsd:string ;
                                                                :gestor "{planta["Gestor"]}"^^xsd:string ;
                                                                :data_atualizacao "{planta["Data de actualização"]}"^^xsd:string ;
                                                                :numero_intervencao "{planta["Número de intervenções"]}"^^xsd:int.                                                                                                                         
    
    
    
    
    
    
    """
    ttl += registo

output = open("plantas_output.ttl", "w")
output.write(ttl)
