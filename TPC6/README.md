Abordagem:

1. Carregar o dataset no endpoint: 'http://epl.di.uminho.pt:7200', no repositório:
http://epl.di.uminho.pt:7200/repositories/cinema2024
2. Construir queries SPARQL para responder às perguntas:
	- Quantos filmes existem no repositório?
	- Qual a distribuição de filmes por ano de lançamento?
	- Qual a distribuição de filmes por género?
	- Em que filmes participou o ator "Burt Reynolds"?
	- Produz uma lista de realizadores com o seu nome e número de filmes que realizou.
	- Qual o título dos livros que aparecem associados aos filmes?
	
3. Usar flask para gerar uma interface web ao repositório de filmes 

Diretorias:

APP - Diretoria que contém toda a aplicação web que gerar a interface web ao repositório de filmes 

Dataset - Contém a script python para obter todos os filmes e informações do dbpedia que são guardados na ficheiro .json

Ontologia - Contém no no ficheiro cinema.ttl a base da ontoligia que irá ser povoada, gera_cinemaTTL.py script python responsável por povoar a ontologia, cinema_pg50311.ttl ontologia final povoada.

Ficheiro queries.txt contém as queries responsável por responder a cada uma das query propostas.
