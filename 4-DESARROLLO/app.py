from flask import Flask,session, jsonify,request,render_template,redirect,url_for
import json
from flask_mysqldb import MySQL

app=Flask(__name__)
@app.route("/")
def root():
    return "SERVICIO NACIONAL DE APRENDIZAJE ****"
@app.route("/N")
def Nivel():
    msgito="Hola Papa"
    kk1="Teleinormatica"
    
    b=[1,4,5,6]
    return render_template("prueba.html",N=2)
if __name__ == '__main__':
    app.run(port=5000, debug=True)
