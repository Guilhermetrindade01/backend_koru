import sqlite3
import os

# Obtem o diretório atual do arquivo
caminho = os.path.dirname(os.path.realpath(__file__))

# Conectando o caminho do arquivo do banco de dados a partir do diretório atual
caminho_bd = os.path.join(caminho, 'harry_potter_personagens.db')

# Conectar com o banco de dados 
conexao = sqlite3.connect(caminho_bd)

# Criação dos dados para manipular no banco de dados
nome = "Harry Potter"
raca = "Humano"
casa = "Grifinória"
altura = "1.80"
nascimento = "31/07/1980"
imagem = "https://upload.wikimedia.org/wikipedia/en/d/d7/Harry_Potter_character_poster.jpg"

# cursor => objeto que será capaz de executar as instruções em SQL (quando se usa o sqlite)

# Inserir dados no banco
    #interrogações => são parâmetros usados para proteger o banco de dados de um ataque chamado sql injection
cursor = conexao.cursor()
sql_insert = "INSERT INTO personagens (nome_personagem, raca_personagem, casa_personagem, altura_personagem, nascimento_personagem, imagem_personagem) VALUES (?, ?, ?, ?, ?, ?)"

cursor.execute(sql_insert, (nome, raca, casa, altura, nascimento, imagem))

personagem_id = cursor.lastrowid
conexao.commit()
print(f"O último código inserido foi: {personagem_id}")