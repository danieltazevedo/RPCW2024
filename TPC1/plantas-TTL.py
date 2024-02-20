import json

f = open("plantas.json")
bd = json.load(f)
f.close

ttl = ""


for planta in bd:
    registo = f"""
    ###  http://www.rpcw.di.uminho.pt/2024/plantas#{planta['Local'].replace(" ","_").replace('"',"")}_{planta['Código de rua']}
    <http://www.rpcw.di.uminho.pt/2024/plantas#{planta['Local'].replace(" ","_").replace('"',"")}_{planta['Código de rua']}> rdf:type owl:NamedIndividual ,
                                                                        :Morada;
                                                                :codigo_rua "{planta["Código de rua"]}"^^xsd:int;
                                                                :rua "{planta["Rua"]}"^^xsd:string;
                                                                :local "{planta["Local"]}"^^xsd:string ;
                                                                :freguesia "{planta["Freguesia"]}"^^xsd:string;

    
    ###  http://www.rpcw.di.uminho.pt/2024/plantas#{planta['Id']}
    <http://www.rpcw.di.uminho.pt/2024/plantas#{planta['Id']}> rdf:type owl:NamedIndividual ,
                                                                        :Planta;
                                                                :numero_registo "{planta["Número de Registo"]}"^^xsd:int;
                                                                :especie "{planta["Espécie"]}"^^xsd:string;
                                                                :nome_cientifico "{planta["Nome Científico"]}"^^xsd:string;
                                                                :origem "{planta["Origem"]}"^^xsd:string;
                                                                :data_plantacao "{planta["Data de Plantação"]}"^^xsd:dateTime;
                                                                estado "{planta['Estado']}"^^xsd:string;
                                                                :caldeira "{planta["Caldeira"]}"^^xsd:boolean;
                                                                :tutor "{planta["Tutor"]}"^^xsd:boolean;
                                                                :implantacao "{planta["Implantação"]}"^^xsd:string;
                                                                :gestor "{planta["Gestor"]}"^^xsd:string;
                                                                :data_atualizacao "{planta["Data de actualização"]}"^^xsd:dateTime;
                                                                :numero_intervencao "{planta["Número de intervenções"]}"^^xsd:int.                                                                                                                         
    
    
    
    
    
    
    """
    ttl += registo

output = open("plantas_output.ttl", "w")
output.write(ttl)