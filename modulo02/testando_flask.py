from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloWorld():
    return "<h2>Hello world!</h2>"

@app.route("/teste")
def testeRota():
    return "Esta é outra página!<br><b>Funcionou!!!</b>"

app.run(debug=True)