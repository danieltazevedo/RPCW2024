import json

f = open("aval-alunos.json")
bd = json.load(f)
f.close

ttl = f"""
@prefix : <http://rpcw.di.uminho.pt/2024/avaliacao/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@base <http://rpcw.di.uminho.pt/2024/avaliacao/> .

<http://rpcw.di.uminho.pt/2024/avaliacao> rdf:type owl:Ontology .

#################################################################
#    Object Properties
#################################################################

###  http://rpcw.di.uminho.pt/2024/avaliacao/hasCurso
:hasCurso rdf:type owl:ObjectProperty ;
          rdfs:domain :Aluno ;
          rdfs:range :Curso .


###  http://rpcw.di.uminho.pt/2024/avaliacao/hasExame
:hasExame rdf:type owl:ObjectProperty ;
          rdfs:domain :Aluno ;
          rdfs:range :Exame .


###  http://rpcw.di.uminho.pt/2024/avaliacao/hasProject
:hasProject rdf:type owl:ObjectProperty ;
            rdfs:domain :Aluno ;
            rdfs:range :Projeto .


###  http://rpcw.di.uminho.pt/2024/avaliacao/hasTPC
:hasTPC rdf:type owl:ObjectProperty ;
        rdfs:domain :Aluno ;
        rdfs:range :TPC .


#################################################################
#    Data properties
#################################################################

###  http://rpcw.di.uminho.pt/2024/avaliacao#exameTipo
:exameTipo rdf:type owl:DatatypeProperty ;
           rdfs:domain :Exame ;
           rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/avaliacao/alunoId
:alunoId rdf:type owl:DatatypeProperty ;
         rdfs:domain :Aluno ;
         rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/avaliacao/cursoNome
:cursoNome rdf:type owl:DatatypeProperty ;
           rdfs:domain :Curso ;
           rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/avaliacao/exameNota
:exameNota rdf:type owl:DatatypeProperty ;
           rdfs:domain :Exame ;
           rdfs:range xsd:int .


###  http://rpcw.di.uminho.pt/2024/avaliacao/nome
:nome rdf:type owl:DatatypeProperty ;
      rdfs:domain :Aluno ;
      rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/avaliacao/notaProjeto
:notaProjeto rdf:type owl:DatatypeProperty ;
             rdfs:domain :Projeto ;
             rdfs:range xsd:int .


###  http://rpcw.di.uminho.pt/2024/avaliacao/tpcNota
:tpcNota rdf:type owl:DatatypeProperty ;
         rdfs:domain :TPC ;
         rdfs:range xsd:float .


#################################################################
#    Classes
#################################################################

###  http://rpcw.di.uminho.pt/2024/avaliacao/Aluno
:Aluno rdf:type owl:Class .


###  http://rpcw.di.uminho.pt/2024/avaliacao/Curso
:Curso rdf:type owl:Class .


###  http://rpcw.di.uminho.pt/2024/avaliacao/Exame
:Exame rdf:type owl:Class .


###  http://rpcw.di.uminho.pt/2024/avaliacao/Projeto
:Projeto rdf:type owl:Class .


###  http://rpcw.di.uminho.pt/2024/avaliacao/TPC
:TPC rdf:type owl:Class .


#################################################################
#    Individuals
#################################################################
"""
cursos = []

for aluno in bd['alunos']:
    tpcs = [f":{aluno['idAluno']}_{tpc['tp']}" for tpc in aluno['tpc']]
    tpc_string = ',\n\t\t\t\t'.join(tpcs)
    
    hasExame_parts = []

    if 'recurso' in aluno['exames']:
        hasExame_parts.append(f":{aluno['idAluno']}_recurso")
        recurso = f"""
###  http://rpcw.di.uminho.pt/2024/avaliacao/{aluno['idAluno']}_recurso
:{aluno['idAluno']}_recurso rdf:type owl:NamedIndividual ,
                         :Exame ;
                :exameTipo "recurso" ;
                :exameNota {aluno['exames']['recurso']} .
        """
        ttl += recurso
        

    if 'especial' in aluno['exames']:
        hasExame_parts.append(f":{aluno['idAluno']}_especial")
        especial = f"""
###  http://rpcw.di.uminho.pt/2024/avaliacao/{aluno['idAluno']}_especial
:{aluno['idAluno']}_especial rdf:type owl:NamedIndividual ,
                          :Exame ;
                 :exameTipo "especial" ;
                 :exameNota {aluno['exames']['especial']} .
        """
        ttl += especial
        

    if 'normal' in aluno['exames']:
        hasExame_parts.append(f":{aluno['idAluno']}_normal")
        normal = f"""
###  http://rpcw.di.uminho.pt/2024/avaliacao/{aluno['idAluno']}_normal
:{aluno['idAluno']}_normal rdf:type owl:NamedIndividual ,
                        :Exame ;
               :exameTipo "normal" ;
               :exameNota {aluno['exames']['normal']} .
        """
        ttl += normal
        

    hasExame_string = ",\n\t\t\t\t".join(hasExame_parts)
    
    proj = f"""
###  http://rpcw.di.uminho.pt/2024/avaliacao/{aluno['idAluno']}_proj
:{aluno['idAluno']}_proj rdf:type owl:NamedIndividual ,
                      :Projeto ;
             :notaProjeto {aluno['projeto']} .
    """    
    ttl += proj
    
    registo = f""" 
###  http://rpcw.di.uminho.pt/2024/avaliacao#{aluno['idAluno']}
:{aluno['idAluno']} rdf:type owl:NamedIndividual ,
                 :Aluno ;
        :hasCurso :{aluno['curso']} ;
        :hasExame {hasExame_string} ;
        :hasProject :{aluno['idAluno']+'_proj'} ;
        :hasTPC {tpc_string};
        :alunoId  "{aluno['idAluno']}";
        :nome "{aluno['nome']}".
    """
    ttl += registo
    
    if aluno['curso'] not in cursos:
        cursos.append(aluno['curso'])
        curso = f"""
###  http://rpcw.di.uminho.pt/2024/avaliacao#{aluno['curso']}
:{aluno['curso']} rdf:type owl:NamedIndividual ,
              :Curso ;
     :cursoNome "{aluno['curso']}" .
    """
        ttl+= curso
        
    
    for tpc in aluno['tpc']:
        tpc_s = f"""
###  http://rpcw.di.uminho.pt/2024/avaliacao/{aluno['idAluno']}_{tpc['tp']}
:{aluno['idAluno']}_{tpc['tp']} rdf:type owl:NamedIndividual ,
                      :TPC ;
             :tpcNota {tpc['nota']} .      
        """
        ttl+= tpc_s 

    
ttl += f"""###  Generated by the OWL API (version 4.5.26.2023-07-17T20:34:13Z) https://github.com/owlcs/owlapi"""

output = open("avaliacao_povoada.ttl", "w")
output.write(ttl)
