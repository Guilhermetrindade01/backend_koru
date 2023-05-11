import sqlite3
import os

# Obtem o diretório atual do arquivo
caminho = os.path.dirname(os.path.realpath(__file__))

# Conectando o caminho do arquivo do banco de dados a partir do diretório atual
caminho_bd = os.path.join(caminho, 'harry_potter_personagens.db')

# Conectar com o banco de dados 
conexao = sqlite3.connect(caminho_bd)

# Deletando informação do banco de dados
cursor = conexao.cursor()
sql_delete = "DELETE FROM personagens WHERE id_personagem = ?"
cursor.execute(sql_delete, (4, ))
conexao.commit()
sql_select_unico = "SELECT * FROM personagens WHERE id_personagem = ?"
cursor.execute(sql_select_unico, (4, ))
print(cursor.fetchone())