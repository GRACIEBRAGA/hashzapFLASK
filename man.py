# site com os scripts: https://cdnjs.com/
# pip install python-socketio flask-socketio simple-websocket

from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# ufuncionalidade de enviar mensagem
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)

#criar a nossa 1ª página = 1ª rota

@app.route("/")
def homepage():
    return render_template("index.html")

# roda o nosso aplicativo

socketio.run(app, host="152.188.014")

# websocket -> tunel

# install python-socketio / flask-socketio / simple-websocketio
