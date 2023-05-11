from flask import Flask, render_template, request, redirect, url_for
import repositorio

app = Flask(__name__)

@app.route("/")
def home():
    lista_personagens = repositorio.retornarPersonagens()
    return render_template("index.html", dados = lista_personagens)

# Rota para atualizar, excluir e salvar um novo personagem
@app.route("/personagem/<int:id>", methods=['GET', 'POST'])
def editar_personagem(id):

    if request.method == "POST":
        # Quer dizer que o usuário está mandando dados para o servidor
        if "excluir" in request.form:
            repositorio.removerPersonagem(id)
            return redirect(url_for('home'))
        elif "salvar" in request.form:
            id = request.form["id"]
            nome = request.form["nome"]
            raca = request.form["raca"]
            casa = request.form["casa"]
            altura = request.form["altura"]
            nascimento = request.form["nascimento"]
            imagem = request.form["imagem"]

            dados_retornados = repositorio.retornarPersonagem(id)
            if dados_retornados:
                repositorio.atualizarPersonagem(id = id, nome = nome, raca = raca, casa = casa, altura = altura, nascimento = nascimento, imagem = imagem)
            else:
                repositorio.criarPersonagem(nome = nome, raca = raca, casa = casa, altura = altura, nascimento = nascimento, imagem = imagem)

            return redirect(url_for('home'))
    else:
        # retorna os dados de um personagem na página de cadastro (método GET - botão adicionar)
        id, nome, raca, casa, altura, nascimento, imagem = repositorio.retornarPersonagem(id)
        return render_template("cadastro.html", id = id, nome = nome, raca = raca, casa = casa, altura = altura, nascimento = nascimento, imagem = imagem)

app.run(debug = True)