from flask import Flask, render_template, request, redirect, url_for
import repositorio

app = Flask(__name__)

@app.route("/")
def home():
    dicionario = repositorio.retornarPersonagens()
    return render_template("index.html", dados = dicionario)

@app.route("/personagem/<int:id>", methods=['GET', 'POST'])
def editar_personagem(id):

    if request.method == "POST":
        # quer dizer que o usuário está mandando dados para o servidor
        if "excluir" in request.form:
            repositorio.removerPersonagem(id)
            return redirect(url_for('home'))
        elif "salvar" in request.form:
            personagem = {}
            personagem['nome'] = request.form["nome"]
            personagem['raca'] = request.form["raca"]
            personagem['casa'] = request.form["casa"]
            personagem['altura'] = request.form["altura"]
            personagem['nascimento'] = request.form["nascimento"]
            personagem['imagem'] = request.form["imagem"]

            if id in repositorio.retornarPersonagens().keys():
                repositorio.atualizarPersonagem(id, personagem)

            return redirect(url_for('home'))
    else:
        # retorna os dados de um personagem na página de cadastro
        personagem = repositorio.retornarPersonagem(id)
        personagem['id'] = id
        return render_template("cadastro.html", **personagem)

@app.route("/personagem", methods=['GET', 'POST'])
def criar_personagem():
    if request.method == "POST":
        personagem = {}
        personagem['nome'] = request.form["nome"]
        personagem['raca'] = request.form["raca"]
        personagem['casa'] = request.form["casa"]
        personagem['altura'] = request.form["altura"]
        personagem['nascimento'] = request.form["nascimento"]
        personagem['imagem'] = request.form["imagem"]
        repositorio.criarPersonagem(**personagem)
        return redirect(url_for('home'))
    else:
        return render_template('cadastro.html', id = repositorio.gerarId())

app.run(debug = True)