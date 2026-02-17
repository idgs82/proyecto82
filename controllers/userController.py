from flask import Blueprint,jsonify, request
from services.authService import AuthService
from flasgger import swag_from
user_bp = Blueprint('auth', __name__)


@user_bp.route('/register', methods=['POST'])
@swag_from('../docs/resgister.yml')
def register():
    data = request.get_json();
    try:
        user = AuthService.register(
            data.get('username'),
            data.get('email'),
            data.get('password'))

        return jsonify({
            "msj": "Accion ejecutada fine", 
            "username": user.user,
            "email": user.email,
            "password": user.password}), 201

    except ValueError as e:
        return {'msj': str(e)},400
    