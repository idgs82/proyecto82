from flask import Flask

def create_app():
    app = Flask(__name__)
    @app.route('/')
    def home():
        return {'msj': '********************hola hello world******************'}

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=  True, 
            host= '0.0.0.0')