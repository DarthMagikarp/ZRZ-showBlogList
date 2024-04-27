# chat conversation
import json
import pymysql
import requests
import http.client
import os
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from itertools import cycle

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=["POST"])
@cross_origin()
def function(self):
    load_dotenv()
    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    DB_DDBB = os.getenv("DB_DDBB")
    #try:
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_DDBB)
    cursor = connection.cursor()

    print("conexión exitosa")

    sql = '''
        select
        titulo, autor, tags, estado, texto, imagen, fecha_publicacion, profesion_autor, id
        from '''+DB_DDBB+'''.blogs
    '''
    cursor.execute(sql)
    resp = cursor.fetchall()
    print(str(resp))

    arrayBlogs=[]
    retorno = {
        "blogs":{}
    }
    for registro in resp:
        item={
            "titulo":registro[0],
            "autor":registro[1],
            "tags":registro[2],
            "estado":registro[3],
            "texto":registro[4],
            "imagen":registro[5],
            "fecha_publicacion":registro[6],
            "profesion_autor":registro[7],
            "id":registro[8]
        }
        arrayBlogs.append(item)
        
    retorno['blogs'] = arrayBlogs
    return retorno

    #except Exception as e:
    #    print('Error: '+ str(e))
    #    retorno = {           
    #        "detalle":"algo falló", 
    #        "validacion":False
    #    }
    #    return retorno

if __name__ == "__main__":
    app.run(debug=True, port=8002, ssl_context='adhoc')