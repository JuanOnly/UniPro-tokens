# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 10:42:10 2021

@author: Jota
"""


from flask import Flask
import os
from flask import request
from jose import jwt

app = Flask(__name__)
os.environ["JWT_SECRET_KEY"]="Jwt@Tokens*"
JWT_SECRET_KEY = "Jwt@Tokens*"

@app.route("/")
def hello_world():
    return "<p>Hello, World Tokens!</p>"


@app.route("/crear-token")
def crear():
    nombre = request.args.get("nombre")
    id_persona = request.args.get("id")
    id_rol = request.args.get("id_rol")
    try:
        secret_key = "Jwt@Tokens*"
        token = jwt.encode({'nombre': nombre, 'id': id_persona, 'rol': id_rol}, secret_key, algorithm='HS256')
        return token
    except Exception as e:
        return ""

@app.route("/validar-token")
def validar():
    token = request.args.get("token")
    rol = request.args.get("rol")
    try:
        secret_key = "Jwt@Tokens*"
        token = jwt.decode(token, secret_key, algorithms=['HS256'])
        print(token)
        if token["rol"] == rol:
            return "OK"
        else:
            return "KO"
    except Exception as e:
        return "KO"


@app.route("/verificar-token")
def verificar():
    token = request.args.get("token")
    try:
        secret_key = "Jwt@Tokens*"
        token = jwt.decode(token, secret_key, algorithms=['HS256'])
        return "OK"
    except Exception as e:
        return "KO"

if __name__ == '__main__':
    app.run(host="localhost", port=5001)