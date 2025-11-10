from flask import Flask
import json, psutil, os, platform

print()


print()

APP = Flask(__name__)

@APP.get("/info")
def info():
    return json.dumps([
        {
            'integrantes':[
                'Artur Moretti Zimmermann',
                'Bruno Navarro Ivatiuk'
            ]
        }
    ])

@APP.get("/metricas")
def metricas():
    return json.dumps([
        {
            'integrantes':[
                'Artur Moretti Zimmermann',
                'Bruno Navarro Ivatiuk'
            ]
        }
    ])