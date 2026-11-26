from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

# Instanciação do ORM fora da fábrica
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa o banco de dados com a instância da aplicação
    db.init_app(app)

    # Registro dos Blueprints (Controllers)
    from app.controllers.auth_controller import auth_bp
    from app.controllers.user_controller import user_bp
    from app.controllers.admin_controller import admin_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(admin_bp)

    return app