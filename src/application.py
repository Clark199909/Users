from flask import request, jsonify
from flask_bcrypt import Bcrypt
from src import app
from src.resources.user_resource import UserResource


@app.route("/api/users/register", methods=["POST"])
def register():
    data = request.json
    bcrypt = Bcrypt()

    encrypted_password = bcrypt.generate_password_hash(data['password'])
    username = data['username']
    email = data['email']
    phone = data['phone']

    if UserResource.search_user_by_username(username) is not None:
        return generate_response("User name already exists!", 400)

    if UserResource.search_user_by_email(email) is not None:
        return generate_response("Email already exists!", 400)

    if UserResource.search_user_by_phone(phone) is not None:
        return generate_response("Phone already exists!", 400)

    UserResource.save_user(username, email, phone, encrypted_password)

    return generate_response("Successfully registered!", 200)


def generate_response(msg, status_code):
    response = jsonify(msg)
    response.status_code = status_code
    return response


@app.route("/api/users/login", methods=["POST"])
def login():
    data = request.json
    bcrypt = Bcrypt()

    email = data['email']
    password = data['password']
    if UserResource.search_user_by_email(email) is None:
        return generate_response("User does not exist!", 400)

    encrypted_password = UserResource.get_password(email)
    if not bcrypt.check_password_hash(encrypted_password, password):
        return generate_response("Password is incorrect!", 400)

    return generate_response("Login successfully!", 200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5015)
