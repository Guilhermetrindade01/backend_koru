import sqlite3
import os

# Obtem o diretório atual do arquivo
caminho = os.path.dirname(os.path.realpath(__file__))

# Conectando o caminho do arquivo do banco de dados a partir do diretório atual
caminho_bd = os.path.join(caminho, 'harry_potter_personagens.db')

# Conectar com o banco de dados 
conexao = sqlite3.connect(caminho_bd)

# Seleção de item do banco de dados
print("Personagem de código 2")
cursor = conexao.cursor()
sql_select_unico = "SELECT * FROM personagens WHERE id_personagem = ?"
cursor.execute(sql_select_unico, (2, )) # Há necessidade dessa vírgula após o número do id para que o python reconheça a tupla
id, nome, raca, casa, altura, nascimento, imagem = cursor.fetchone()
    # Tupla => estrutura imutável do python em que cada dado está separado por vírgulas
# print(cursor.fetchone()) # Fetchone => método usado quando se tem um SELECT que retorna apenas uma linha
    # Substituição que o python pode fazer desmontando a tupla quando damos o mesmo número de variáveis
print(f"{id} ---- {nome}")

# sql_select_varios = "SELECT * FROM personagens"
# cursor.execute(sql_select_varios)
# print(cursor.fetchall())