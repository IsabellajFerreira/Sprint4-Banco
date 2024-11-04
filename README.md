## VOM+HIVE - Aplicação CRUD para Produtos em MongoDB

O projeto oferece uma interface gráfica desenvolvida em Python com Tkinter para realizar operações de CRUD (Create, Read, Update, Delete) em uma base de dados MongoDB. 
 
## Pré-requisitos
Antes de iniciar a execução do aplicativo, é necessário instalar algumas dependências e configurar o ambiente.

1. Instalar o Python 3.x

2. Instalar as Bibliotecas Necessárias
Para este projeto, as bibliotecas que devem ser instaladas são:

pymongo: Conecta o Python ao MongoDB.
tkinter: Usada para a interface gráfica.

Instalar

## pip install pymongo tk

3. Executando o Aplicativo

## python VOM+HIVE.py


## Funcionalidades do Aplicativo

1. Criar Produto
Campos Disponíveis
ID (numérico)
Nome do Produto (texto)
Público-Alvo (texto)
Diferencial (texto)
Preço (numérico)
Canal de Vendas (texto)
Categoria (texto)
Descrição (texto)
Estoque (numérico)
Avaliação (numérico)
Data de Lançamento (YYYY-MM-DD)

## Como Usar
Preencha os campos com as informações do produto.
Clique no botão "Criar Produto".
Se o produto for criado com sucesso, uma mensagem de confirmação será exibida.

# --> Exemplo
ID: 1
Nome do Produto: Smart TV
Público-Alvo: Adultos
Diferencial: 4K e HDR
Preço: 2999.99
Canal de Vendas: Loja Física e Online
Categoria: Eletrônicos
Descrição: TV 50 polegadas com resolução 4K.
Estoque: 30
Avaliação: 4.5
Data de Lançamento: 2023-05-10

2. Consultar Produto
Como Usar
Insira o ID ou o Nome do Produto que deseja consultar.
Clique no botão "Consultar Produto".
Se o produto for encontrado, seus detalhes serão exibidos em uma janela.

Exemplo:
ID: 1
Nome do Produto: Smart TV

3. Atualizar Produto

ID do Produto (para identificar o item)
Atributo que deseja atualizar (ex: preço, estoque)
Novo Valor para o atributo

Como Usar
Insira o ID do produto, o nome do atributo IGUAL ESTÁ NO JSON a ser atualizado e o novo valor.
Clique em "Atualizar Produto".
Uma mensagem confirmará se a atualização foi bem-sucedida ou se o produto não foi encontrado.

## Atributos que devem ser mencionados
id_produto
nome
publico_alvo
diferencial
preco
canal_vendas
categoria
descricao
estoque
avaliacao
data_lancamento 


Exemplo
ID: 1
Atributo: preco
Novo Valor: 2599.99

4. Deletar Produto
Como Usar
Insira o ID do produto que deseja deletar.
Clique em "Deletar Produto".
O aplicativo confirmará se o produto foi removido.

Exemplo
ID: 1


5. Exportar Dataset
A função Exportar Dataset cria um arquivo JSON com todos os dados armazenados nas coleções do banco de dados MongoDB. 

--> Como Usar
Clique em "Exportar Dataset".
O aplicativo criará um arquivo dados_exportados.json na pasta do projeto, contendo todas as coleções e documentos do banco de dados.

