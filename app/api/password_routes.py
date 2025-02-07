from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Password
from ..models import db
from ..forms.password_form import PasswordForm

password_routes = Blueprint("passwords", __name__)


@password_routes.route("/")
@login_required
def user_passwords(user_id):
    passwords = Password.query.filter_by(user_id=user_id).all()
    return {"passwords": [password.to_dict() for password in passwords]}


@password_routes.route("/<int:id>")
@login_required
def password(id):
    password = Password.query.get(id)
    return password.to_dict()


@password_routes.route("/<int:user_id>/new", methods=["POST"])
@login_required
def create_password(user_id):
    form = PasswordForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    # print(business)
    # if not business:
    #     return {"error": "Business not found"}
    # query reviews by user id, if there are any, throw err msg saying user can't post more than once

    # Create a new password using the form data
    if form.validate():
        new_password = Password(
            website=form.website.data,
            emailUser=form.emailUser.data,
            user_id=current_user.id,
            password=form.password.data,
            name=form.name.data,
        )

        # Add and commit the new review to the database
        db.session.add(new_password)
        db.session.commit()

        return {"review": new_password.to_dict()}

    # If form validation fails, return errors
    return {"errors": form.errors}
