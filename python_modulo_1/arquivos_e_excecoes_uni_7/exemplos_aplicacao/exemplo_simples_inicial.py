""" 
Manipulando arquivos
"""
with open("dados.txt", "w") as arquivo:
    arquivo.write("Counter-Strike é melhor do que Valorant.")
    arquivo.write("O correto é 'bolacha'.")

""" 
Vamos analisar passo a passo o que esse código faz:

1. with open("dados.txt", "w") as arquivo:: Aqui, estamos usando a palavra-chave reservada with, uma construção em Python que garante que o arquivo seja fechado corretamente após o seu uso. 
Estamos abrindo o arquivo chamado "dados.txt" em modo de escrita ("w"), que permite escrever no arquivo. Se o arquivo não existir, ele será criado. A variável arquivo é associada ao arquivo aberto. 
Veja que usamos esse with de um jeito bem parecido com o if/elif/else, for ou while.

    1.arquivo.write("Counter-Strike é melhor do que Valorant."): Nesta linha, estamos chamando o método write() na variável arquivo. Isso permite escrever o conteúdo especificado entre parênteses no arquivo aberto. 
    No caso, estamos escrevendo a string "Counter-Strike é melhor do que Valorant." no arquivo.

    2.arquivo.write("O correto é 'bolacha'."):  Na próxima linha, chamamos novamente o método write() para adicionar mais uma frase ao arquivo. Aqui, estamos escrevendo a frase "O correto é 'bolacha'.".

    3.O bloco with é encerrado e, automaticamente, o arquivo é fechado. Isso é importante para garantir que os recursos do sistema operacional associados ao arquivo sejam liberados corretamente, 
    e que não apareça algum tipo de mensagem dizendo que você não poderia modificar o seu arquivo porque ele estaria em uso.
"""

""" 
Agora, e se quisermos ler o conteúdo de um arquivo? Teste isto:
"""
with open("dados.txt", "r") as arquivo:

    linhas = arquivo.readlines()

    print(linhas)
    
""" 
Vamos analisar este código:

1. with open("dados.txt", "r") as arquivo::Aqui, voltamos a usar a palavra-chave with para abrir o arquivo. A diferença em relação ao exemplo anterior é a de que estamos usando o modo de leitura ("r"). 
Isso permite que possamos ler (ao invés de escrever) o conteúdo do arquivo. A variável arquivo é associada ao arquivo aberto.

    1. linhas = arquivo.readlines():  Nesta linha, estamos chamando o método readlines() na variável arquivo. Esse método lê todas as linhas do arquivo e retorna uma lista de strings, onde cada elemento 
    da lista representa uma linha do arquivo. Essa lista é atribuída à variável linhas.

    2. print(linhas): Por fim, estamos utilizando a função print() para exibir o conteúdo da lista linhas, ou seja, todas as linhas do arquivo.

O resultado disso será ["Counter-Strike é melhor do que Valorant.O correto é 'bolacha'."]
    3. O bloco with é encerrado e, automaticamente, o arquivo é fechado. Isso garante que os recursos do sistema operacional (como memória e processador) 
    associados ao arquivo sejam liberados corretamente.
"""