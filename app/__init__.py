from flask import Flask 
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from app.modelo.modelo import db
#from .vistas import 
from flask_jwt_extended import JWTManager
from flask_cors import CORS


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    CORS(app)
    db.init_app(app)
    Migrate(app,db)
    JWTManager(app)
    
    app = Api(app)

    #aqui van las rutas
    #api.add_resouce()

    return app