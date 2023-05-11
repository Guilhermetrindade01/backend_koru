from flask import Flask, jsonify, request, redirect, url_for
import repositorio

app = Flask(__name__)

# Rota para retornar todos os personagens
@app.route("/personagens", methods=['GET'])
def get_personagens():
    lista_personagens = repositorio.retornarPersonagens()
    return jsonify(lista_personagens)

# Rota para retornar um único personagem
@app.route("/personagem/<int:id>", methods=['GET'])
def get_personagem(id):
    personagem = repositorio.retornarPersonagem(id)
    if personagem:
        return jsonify(personagem)
    else:
        return jsonify({"message": "Personagem não encontrado!"}), 404

# Rota para cadastrar um personagem    
@app.route("/personagem", methods=['POST'])
def post_personagem():
    personagem = request.json
    id_personagem = repositorio.criarPersonagem(**personagem)
    personagem["id"] = id_personagem
    return jsonify(personagem), 201

# Rota para alterar um personagem
@app.route("/personagem/<int:id>", methods=['PUT'])
def put_personagem(id):
    personagem = repositorio.retornarPersonagem(id)
    if personagem:
        dados_atualizados = request.json
        dados_atualizados["id"] = id
        repositorio.atualizarPersonagem(**dados_atualizados)
        return (jsonify(dados_atualizados))
    else:
        return jsonify({"message": "Personagem não encontrado!"}), 404

# Rota para deletar um personagem    
@app.route("/personagem/<int:id>", methods=['DELETE'])
def delete_personagem(id):
    personagem = repositorio.retornarPersonagem(id)
    if personagem:
        repositorio.removerPersonagem(id) 
        return jsonify({"message": "Personagem deletado com sucesso!"})
    else:
        return jsonify({"message": "Personagem não encontrado!"}), 404

app.run(debug = True)