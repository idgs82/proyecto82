from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger

db = SQLAlchemy()
migrate = Migrate()

swagger = Swagger (template={
    "swagger": "2.0",
    "info": {
        "title": "Api 82",
        "version": "1.0.0",
        "description": "Documentación de usuarios"
    }
})