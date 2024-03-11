Abordagem:

Criação de uma página web responsável por exibir os dados da ontologia da tabela periódica.

Ficheiros:

[app.py]([app.py]) -> Código python responsável por iniciar o servidor Flask, sendo responsável por fazer pedidos de dados, via HTTP, ao GraphDB.

[index.html](index.html) -> Página inicial, onde é possivel navegar para as páginas de elementos e grupos.

[elementos.html](elementos.html) -> Página onde são listados os elemento de tabela periódica assim como as suas informações (numero atómico, simbolo, grupo)

[elemento.html](elemento.html) -> Página que demostra a informação de um único elementos,

[grupos.html](grupos.html) -> Página onde são listados os diversos grupos da tabela periódica.

[grupo.html](grupo.html) -> Página que demostra todos os elementos pertencentes a um determinado grupo.

[error.html](error.html) -> Página de erro demostrada quando não é possivel realizar a comunicação com o GraphDB.
