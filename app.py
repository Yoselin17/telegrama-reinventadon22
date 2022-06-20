import os
from flask import Flask, jsonyfy, request
from models import db, User, Capitulo, Personaje, FavoritoCapitulo, FavoritoPersonaje
from flask_migrate import flask_Migrate
from flask_cors import CORS
from flask_sqlalchemy import SQLALchemy


BASEDIR = os.path.abspath(os.path.dirname(__file__)) carpeta raiz
app = Flask(__name__)


app.config ['SQLALCHEMY_DATABASE_URI'] = ' sqlite:///'+ os.path.join(BASEDIR, 'test.db')
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = flask_Migrate

db.init_app(app)
CORS(app)
Migrate(app, db)






@app.route('user', methods= ['POST'])
def user():
    user = User()
    user.user_correo = request.json.get("user_correo")
    user.user_contraseña = request.jason.get("user_contraseña")

    db.session.add(user)
    db.session.commit()

    return jsonify(user.serialize()), 200


@app.route('/users', methods= ['GET'])
def all_users():
    users = User.query.all()
    users = list(map(lambda user: user.serialize(), users))
    print(users)
    return jsonify(users), 200    


@app.route('users/<int:id>', methods= ['DELETE'])
def erase_user(id):
    #user = User()
    #filter(lambda x: id == "id")
    #print(user)
    return "Hello wordl"