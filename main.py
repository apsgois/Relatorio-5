from db.biblioteca import BibliotecaDAO
from helper1.WriteAJson import writeAJson


pessoa = BibliotecaDAO()
#Ler todos os documentos da collection.
#res = pessoa.read_livro()

#Alterar o preço de um livro.
#res = pessoa.update_preco_livro("63129fc530a1ae8c5c160c7f", 1000)

#Adicionar um livro.
#res = pessoa.create_livro("O Senhor dos Anéis", "J.R.R. Tolkien", 2001, 150)

#Deletar um livro.
#res = pessoa.delete_livro("O Senhor dos Anéis")

#Crie um index crescente por ano de lançamento.
res = pessoa.read_livro()

writeAJson(res,"pessoa")