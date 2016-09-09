# encoding: utf-8
from flask import Flask, render_template, jsonify, request, json
import socket
from ast import literal_eval


app = Flask(__name__)


@app.route("/")  # ao digitar '/' renderizar a função hello()
def hello():
    # renderizar o arquivo "index.html" localizado na pasta "templates"
    avisos = [[1, 'Site Inalgurado'], [2, 'Estamos em teste'], [3, 'Fique ligado nas novidades']]
    return render_template("index.html", avisos=avisos)


@app.route("/mensagem/")  # ao digitar '/mensagem' renderizar a função mensagem()
def mensagem():
    # retornar mensagens como objeto em JSON
    mensagens = []

    try:
        open('mensagens.txt', 'rb')
    except:
        open('mensagens.txt', 'w+')

    try:
        with open('mensagens.txt', 'rb') as tmpFile:
            for msg in tmpFile.readlines():
                mensagens.append(literal_eval(msg))
    except:
        mensagens = []
    return jsonify(mensagens=mensagens)


@app.route("/mensagem/", methods=["POST"])  # ao digitar '/mensagem' renderizar a função mensagem()
def mensagem_post():
    print (request.form)
    try:
        open('mensagens.txt', 'a')
    except:
        open('mensagens.txt', 'w+')

    with open('mensagens.txt', 'a') as tmpFile:
        mensagem = '\n{"user":"'+ request.form.get('user', '')+'","mensagem":"'+request.form.get('mensagem', '') +'"}'
        tmpFile.write(mensagem)

    return 'TRUE'


if __name__ == "__main__":
    # O código começará a partir desse ponto
    meu_ip = socket.gethostbyname(socket.gethostname())  # descobre meu IP local
    app.run(host=meu_ip, debug=True)  # inicia o servidor
