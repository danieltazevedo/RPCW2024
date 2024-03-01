1. A partir do dataset criar uma ontologia no Protégé;
2. Escrever script em Python para povoar a ontologia;
3. Carregar a ontologia no GraphDB;
4. Especificar as seguintes queries:
	Quais as cidades de um determinado distrito?
	Distribuição de cidades por distrito?
	Quantas cidades se podem atingir a partir do Porto?
	Quais as cidades com população acima de um determinado valor?

Abordagem:

Foram criadas 2 clases: Cidade, Ligação.

Ficheiros:

[mapa.json]([mapa.json]) -> Dataset

[mapa.ttl](mapa.ttl) -> ontogia com classes, object proprities e data proprities

[gera_mapaTTL.py](gera_mapaTTL.py) -> Script para povoar a ontologia

[mapa_povoado.ttl](map_povoado.ttl) -> ontologia povoada (output da script)

1. Quais as cidades de um determinado distrito?
	
	PREFIX : <http://rpcw.di.uminho.pt/2024/mapa/>
	SELECT ?cidades WHERE { 
	    ?cidade :distrito "Lisboa" .
	    ?cidade :nome ?cidades
	}  

2. Distribuição de cidades por distrito?

	PREFIX : <http://rpcw.di.uminho.pt/2024/mapa/>
	SELECT ?distrito (COUNT(distinct ?cidade) as ?n) WHERE { 
	    ?cidade :distrito ?distrito .
	} group by ?distrito

3. Quantas cidades se podem atingir a partir do Porto?

	PREFIX : <http://rpcw.di.uminho.pt/2024/mapa/>
	SELECT (count(distinct ?cidades) as ?n) WHERE {
	    ?cidades_porto :distrito "Porto" .
	    ?ligacao :origemLigacao ?cidades_porto .
	    ?ligacao :destinoLigacao ?dest .
	    ?dest :nome ?cidades
	}

4. Quais as cidades com população acima de um determinado valor?

	PREFIX : <http://rpcw.di.uminho.pt/2024/mapa/>
	SELECT ?cidades ?populacao WHERE {
	    ?cidade :populacao ?populacao
	    filter (?populacao > 500000) .
	    ?cidade :nome ?cidades . 
	}

