Abordagem:

Criação de um dataset (JSON) com informações de filmes (titulo, resumo, duração, atores, realizadores, escritores, musicos). Primeiramente foi criada ao ficheiro [dbpedia_filmes.py]([dbpedia_filmes.py]), onde é  criado o ficheiro  [filmes.json]([filmes.json])  que contém informação sobre o filme(URI, titulo, resumo, duração). Posteriormente o ficheiro [dbpedia_cinema.py]([dbpedia_cinema.py]) que lê a informação do ficheiro json anterior, e para cada filme adiciona os atores, realizadores, escritores e os musicos, criando um novo ficheiro json [cinema.json]([cinema.json]).

Ficheiros:

[filmes.json]([filmes.json]) -> Ficheiro json que contém a informação básica de um filme, (URI, titulo, resumo, duração).

[cinema.json](cinema.json) ->  Ficheiro json que contém toda a informação de um filme, (URI, titulo, resumo, duração, atores, realizadores, escritores e os musicos). Cada um dos atores, realizadores, escritores e os musicos possui o seu URI, nome e biografia.

[dbpedia_filmes.py](dbpedia_filmes.py) -> Script python responsável por por criar o ficheiro filmes.json. Realiazando pedidos HTTP ao dbpedia.
        Querie:

PREFIX dbo: <http://dbpedia.org/ontology/>

SELECT DISTINCT ?filme ?titulo ?resumo ?duracao 
WHERE {
    ?filme a dbo:Film ;
        rdfs:label ?titulo;
        dbo:abstract ?resumo;
        dbp:runtime ?duracao.
    filter(lang(?titulo)='en' && lang(?resumo)='en') .        
}


[dbpedia_cinema.py](dbpedia_cinema.py) -> Script python responsável por por criar o ficheiro cinema.json. Realiazando pedidos HTTP ao dbpedia.

        Querie para os atores:

SELECT DISTINCT ?ator ?nome ?biografia WHERE {{
            <{filme['uri']}> dbo:starring ?ator .
            optional{{ ?ator rdfs:label ?nome . 
                       filter(lang(?nome)='en') .}}
            optional {{?ator dbo:abstract ?biografia .
                       filter(lang(?biografia)='en') . }}
        }}


        Querie para os realizadores:

SELECT DISTINCT ?realizador ?nome ?biografia WHERE {{
            <{filme['uri']}> dbo:director ?realizador .
            optional{{ ?realizador rdfs:label ?nome . 
                       filter(lang(?nome)='en') .}}
            optional {{?realizador dbo:abstract ?biografia .
                       filter(lang(?biografia)='en') . }}
        }}


        Querie para os escritores:

SELECT DISTINCT ?escritor ?nome ?biografia WHERE {{
            <{filme['uri']}> dbo:writer ?escritor .
            optional{{ ?escritor rdfs:label ?nome . 
                       filter(lang(?nome)='en') .}}
            optional {{?escritor dbo:abstract ?biografia .
                       filter(lang(?biografia)='en') . }}
        }}


        Querie para os musicos:

SELECT DISTINCT ?musico ?nome ?biografia WHERE {{
            <{filme['uri']}> dbp:music ?musico .
           optional{{ ?musico rdfs:label ?nome . 
                       filter(lang(?nome)='en') .}}
            optional {{?musico dbo:abstract ?biografia .
                       filter(lang(?biografia)='en') . }}
        }}
