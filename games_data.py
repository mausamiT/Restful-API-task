from app import *
import json
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
#from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345''@localhost/task'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Initializing our database

# the class Game will inherit the db.Model of SQLAlchemy
class Game(db.Model):
    __tablename__ = 'games_data'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    platform = db.Column(db.String(80), nullable=False)
    score = db.Column(db.Float, nullable=False)
    genre = db.Column(db.String(80), nullable=False)
    editors_choice= db.Column(db.String(1), nullable=False)

# this method will convert our output to json


    def json(self):
    	return {'title': self.title,'platform':self.platform,'score': self.score, 'genre': self.genre,'editors_choice' : self.editors_choice}

    def add_game(_title,_platform,_score, _genre, _edchoice):
    
    # creating an instance of game constructor
    	new_game = Game(title=_title,platform = _platform,score=_score, genre = _genre, editors_choice=_edchoice)
    	db.session.add(new_game)  # add new game to database session
    	db.session.commit()  # commit changes to session

    def get_game(_title):
        '''function to get game data using the title'''
        return [Game.json(Game.query.filter_by(title=_title))]

    def get_all_games():
        return [Game.json(game) for game in Game.query.all()]

    def update_game(_title, _platform,_score):
        '''function to update the score of a game using the title and platform'''
        game_to_update = Game.query.filter_by(title=_title,platform=_platform)
        game_to_update.score = _score
        db.session.commit()

    def delete_game(_title,_platform):
        '''function to delete a game from the database using the title and platform'''
        Game.query.filter_by(title=_title,platform=_platform).delete()
        db.session.commit()

