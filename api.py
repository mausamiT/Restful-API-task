from games_data import *
# importing libraries
from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
#from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
#tryig git

@app.route('/')
def msg():
    return '<h1>hello</h1>'

@app.route('/games', methods=['GET'])
def showall():
    return jsonify({'Games': Game.get_all_games()})

@app.route('/newgame', methods=['POST'])
def insert():
    request_data = request.get_json()  # getting data from client
    games_data.add_game(request_data["title"], request_data["platform"],request_data["score"],
                    request_data["genre"],request_data["editors_choice"])
    response = Response("Game added", 201, mimetype='application/json')
    return response

@app.route('/games/<title>/<platform>/<score>', methods=['PUT'])
def update_gamedet(title,platform):
  
    request_data = request.get_json()
    games_data.update_game(request_data['title'], request_data['platform'],request_data['score'])
    response = Response("Game score Updated", status=200, mimetype='application/json')
    return response

# route to delete game using the DELETE method
@app.route('/games/<title>/<platform>', methods=['DELETE'])
def remove_game(title,platform):
    '''Function to delete game from the database'''
    games_data.delete_game(title,platform)
    response = Response("Game Deleted", status=200, mimetype='application/json')
    return response
if __name__ == "__main__":
    app.run(port=1234, debug=False)
