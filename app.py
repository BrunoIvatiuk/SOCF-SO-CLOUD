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
            ],
            'PID':os.getpid(),
            'Memoria_Utilizada':(psutil.virtual_memory().used // 1024 ** 2),
            'Uso_CPU':psutil.cpu_percent(percpu=True),
            'SO':platform.platform()
        }
    ])