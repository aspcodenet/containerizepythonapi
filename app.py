from flask import Flask,jsonify
from playerDTO import PlayerDTO
import json
from player.playerRepository import findAll 
app = Flask(__name__)

@app.route("/api/player")
def players():
    return json.dumps([PlayerDTO(x.id,x.name,x.year,x.jersey,x.teamName) for x in findAll() ], default=vars)


@app.route("/")
def hello_world():
    return "Hello, World!"


with app.app_context():
    app.run()