from datetime import datetime

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

# Função que gera um novo id
def gerarId():
    id = len(personagens) + 1
    return id

# Função para criar um personagem no dicionário
def criarPersonagem(nome, raca, casa, altura, nascimento, imagem):
    personagens[gerarId()] = {"nome": nome, "raca": raca, "casa": casa, "altura": altura, "nascimento": nascimento, "imagem": imagem}

# Retorna um dicionário com todos os personagens
def retornarPersonagens():
    for id, personagem in personagens.items():
        personagem["nascimento"] = tratar_iso_para_dmy(personagem["nascimento"])
    return personagens

# Retorna um único personagem
def retornarPersonagem(id:int):
    if id in personagens.keys():
        personagens[id]["nascimento"] = tratar_dmy_para_iso(personagens[id]["nascimento"])
        return personagens[id]
    else:
        return {}

# Atualiza os dados de um personagem
def atualizarPersonagem(id:int, dadosPersonagem:dict):
    dadosPersonagem['nascimento'] = tratar_iso_para_dmy(dadosPersonagem['nascimento'])
    personagens[id] = dadosPersonagem

# Remove um personagem
def removerPersonagem(id:int):
    del personagens[id]

# Testes das funções
# print(retornarPersonagens())

# criarPersonagem("Amanda", "Humano", "Grifinória", 1.68, "03/01/1989", "")

# print(retornarPersonagem(5))

# atualizarPersonagem(5, {'nome': 'Amanda Pardinho', 'raca': 'Humano', 'casa': 'Grifinória', 'altura': 1.68, 'nascimento': '03/01/1989', 'imagem': ''})

# print(retornarPersonagem(5))
# removerPersonagem(5)
# print(retornarPersonagem(5))