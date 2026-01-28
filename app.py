from flask import Flask
from controllers.HomeController import blueprint_home

def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint_home,url_prefix='/api/v1')
    @app.route('/')
    def home():
        return {'msj': 'hola mundo jsjsjx2'}

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=  True, 
            host= '0.0.0.0')