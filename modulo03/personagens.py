from flask import Flask, render_template

dicionario = {
    1: {
        "nome": "Harry Potter",
        "raça": "Humano",
        "casa": "Grifinória",
        "altura": 1.80,
        "nascimento": "31/07/1980",
        "imagem": "https://upload.wikimedia.org/wikipedia/commons/9/97/Harry_Potter.jpg"
    },
    2: {
        "nome": "Ron Weasley",
        "raça": "Humano",
        "casa": "Grifinória",
        "altura": 1.80,
        "nascimento": "01/03/1980",
        "imagem": "https://upload.wikimedia.org/wikipedia/en/5/5e/Ron_Weasley_poster.jpg"
    },
    3: {
        "nome": "Hermione Granger",
        "raça": "Humano",
        "casa": "Grifinória",
        "altura": 1.65,
        "nascimento": "19/09/1979",
        "imagem": "https://upload.wikimedia.org/wikipedia/en/d/d3/Hermione_Granger_poster.jpg"
    },
    4: {
        "nome": "Draco Malfoy",
        "raça": "Humano",
        "casa": "Sonserina",
        "altura": 1.80,
        "nascimento": "05/06/1980",
        "imagem": "https://upload.wikimedia.org/wikipedia/commons/a/ac/Drago_Malefoy.jpg"
    }
}

def retornaPersonagem(personagem):
    textoRetorno = f"<h1>{personagem['nome']}</h1><p>É {personagem['raça']} e sua casa é a {personagem['casa']}</p>"
    return textoRetorno

app = Flask(__name__)
#@app.route("/")
#def teste():
    #return retornaPersonagem(dicionario[1])

#@app.route("/personagem/<int:personagemId>")
#def mostraPersonagem(personagemId):
    #return render_template('personagem.html', **dicionario[personagemId])

@app.route("/personagem/<int:personagemId>")
def mostraPersonagemBoot(personagemId):
    return render_template('personagem_boot.html', **dicionario[personagemId])

@app.route("/")
def mostraPersonagens():
    return render_template('personagens.html', personagens = dicionario)
app.run(debug = True)