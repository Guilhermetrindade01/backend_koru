from datetime import datetime
import sqlite3
import os

# Simulação de um banco de dados para o projeto de CRUD

# Dicionário "personagens" é o repositório principal
personagens = {
    1: {
        "nome": "Harry Potter",
        "raca": "Humano",
        "casa": "Grifinória",
        "altura": 1.80,
        "nascimento": "31/07/1980",
        "imagem": "https://upload.wikimedia.org/wikipedia/en/d/d7/Harry_Potter_character_poster.jpg"
    },
    2: {
        "nome": "Ron Weasley",
        "raca": "Humano",
        "casa": "Grifinória",
        "altura": 1.80,
        "nascimento": "01/03/1980",
        "imagem": "https://upload.wikimedia.org/wikipedia/en/5/5e/Ron_Weasley_poster.jpg"
    },
    3: {
        "nome": "Hermione Granger",
        "raca": "Humano",
        "casa": "Grifinória",
        "altura": 1.65,
        "nascimento": "19/09/1979",
        "imagem": "https://upload.wikimedia.org/wikipedia/en/d/d3/Hermione_Granger_poster.jpg"
    },
    4: {
        "nome": "Draco Malfoy",
        "raca": "Humano",
        "casa": "Sonserina",
        "altura": 1.80,
        "nascimento": "05/06/1980",
        "imagem": "https://upload.wikimedia.org/wikipedia/en/1/16/Draco_Mal.JPG"
    }
}

# Tratamento de datas => solução provisória antes de linkar com o banco de dados
def tratar_iso_para_dmy(data:str):
    if "-" in data:
        data = datetime.strptime(data, '%Y-%m-%d')
        return data.strftime('%d/%m/%Y')
    else:
        return data

def tratar_dmy_para_iso(data:str):
    if "/" in data:
        data = datetime.strptime(data, '%d/%m/%Y')
        return data.strftime('%Y-%m-%d')
    else:
        return data
    
# Obtém o diretório atual do arquivo
caminho = os.path.dirname(os.path.realpath(__file__))

# Conectando o caminho do arquivo do banco de dados a partir do diretório atual
caminho_bd = os.path.join(caminho, 'harry_potter_personagens.db')

# Função que gera um novo id
def gerarId():
    conn = sqlite3.connect(caminho_bd)
    cursor = conn.cursor()
    cursor.execute("SELECT seq FROM sqlite_sequence WHERE name = 'personagens'")
    next_id = cursor.fetchone()[0]
    return next_id + 1

# Função para criar um personagem no dicionário
def criarPersonagem(nome, raca, casa, altura, nascimento, imagem):
    try:
        conn = sqlite3.connect(caminho_bd)
        cursor = conn.cursor()
        sql_insert = "INSERT INTO personagens (nome_personagem, raca_personagem, casa_personagem, altura_personagem, nascimento_personagem, imagem_personagem) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(sql_insert, (nome, raca, casa, altura, nascimento, imagem))
        personagem_id = cursor.lastrowid # lastrowid => função que pega o último id inserido após o último insert
        conn.commit()
        conn.close()
        return personagem_id
    except Exception as ex: # Caso aconteça uma exceção, a variável ex é criada => esta variável mostra detalhes do meu erro
        print(ex)
        return 0

# Retorna um dicionário com todos os personagens
def retornarPersonagens():
    try:
        conn = sqlite3.connect(caminho_bd)
        cursor = conn.cursor()
        sql_select = "SELECT * FROM personagens"
        cursor.execute(sql_select)
        personagens = cursor.fetchall() # Retorna uma lista
        return personagens
    except:
        return False

# Retorna um único personagem
def retornarPersonagem(id:int):
    try:
        if id == 0: # O id == 0 mostra que se quer criar um personagem novo
            return gerarId(), "", "", "", "", "", ""
        conn = sqlite3.connect(caminho_bd)
        cursor = conn.cursor()

        sql_select = "SELECT * FROM personagens WHERE id_personagem = ?"
        cursor.execute(sql_select, (id, ))
        id, nome, raca, casa, altura, nascimento, imagem = cursor.fetchone()
        conn.close()
        return id, nome, raca, casa, altura, nascimento, imagem
    except:
        return False

# Atualiza os dados de um personagem
def atualizarPersonagem(id:int, nome, raca, casa, altura, nascimento, imagem):
    # try => tenta executar o pedaço do código contido nele e, caso não consiga, o bloco except é executado
    try:
        conn = sqlite3.connect(caminho_bd)
        cursor = conn.cursor()
        sql_update = "UPDATE personagens SET nome_personagem = ?, raca_personagem = ?, casa_personagem = ?, altura_personagem = ?, nascimento_personagem = ?, imagem_personagem = ? WHERE id_personagem = ?"
        cursor.execute(sql_update, (nome, raca, casa, altura, nascimento, imagem, id))
        conn.commit()
        conn.close()
        return True
    except Exception as ex: # caso aconteça uma exceção, a variável ex é criada => esta variável mostra detalhes do meu erro
        print(ex)
        return False
    
# Remove um personagem
def removerPersonagem(id:int):
    try:
        conn = sqlite3.connect(caminho_bd)
        cursor = conn.cursor()
        sql_delete = "DELETE FROM personagens WHERE id_personagem = ?"
        cursor.execute(sql_delete, (id, ))
        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        print(ex)
        return False

'''
TESTE DAS FUNÇÕES ATUALIZADAS

nome = "Harry Potter"
raca = "Humano"
casa = "Grifinória"
altura = 1.80
nascimento = "31/07/1980"
imagem = "https://upload.wikimedia.org/wikipedia/commons/9/97/Harry_Potter.jpg"

id = criarPersonagem(nome, raca, casa, altura, nascimento, imagem)
print(id)
print(retornarPersonagem(id))

id, nome, raca, casa, altura, nascimento, imagem = retornarPersonagem(id)
atualizarPersonagem(id, "Harry James Potter", raca, casa, altura, nascimento, imagem)
print(retornarPersonagem(id))
id, nome, raca, casa, altura, nascimento, imagem = retornarPersonagem(id) 

print(retornarPersonagens())

removerPersonagem(id) 

print(retornarPersonagens())
'''