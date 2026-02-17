from flask import Flask
from controllers.HomeController import blueprint_home
from extensions import db,migrate, swagger
from config import Config
from models.user import User
from controllers.userController import user_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)


    db.init_app(app)
    migrate.init_app(app,db)
    swagger.init_app(app)



    app.register_blueprint(user_bp,url_prefix='/api/auth')



    app.register_blueprint(blueprint_home,url_prefix='/api/v1')
    @app.route('/')
    def home():
        return {'msj': 'hola mundo jsjsjx2'}

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=  True, 
            host= '0.0.0.0')