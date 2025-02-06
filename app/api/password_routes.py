from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Password

password_routes = Blueprint("passwords", __name__)


@password_routes.route("/")
@login_required
def passwords():
    passwords = Password.query.all()
    return {"passwords": [password.to_dict() for password in passwords]}


@password_routes.route("/<int:id>")
@login_required
def password(id):
    password = Password.query.get(id)
    return password.to_dict()
