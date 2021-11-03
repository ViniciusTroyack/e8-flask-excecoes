from flask import Flask, request, jsonify
import json
from app import utils
from app.models import User
from app.exceptions import invalidTypeError
from http import HTTPStatus

app = Flask(__name__)

@app.get('/users')
def list_users():

    utils.database_exist()
    utils.is_empty()

    with open("./app/database/database.json", "r") as json_file:
        data = json.load(json_file)
        

    return data, HTTPStatus.OK

@app.post('/users')
def post_user():    
    utils.database_exist()
    utils.is_empty()

    data_request = request.get_json()

    if User.verify_valid_typs(**data_request):
        error_message = User.verify_valid_typs(**data_request)
        return error_message, HTTPStatus.BAD_REQUEST
        

    new_user = User(**data_request)
    new_user_jason = new_user.toJson()


    if utils.verify_email_exist(new_user_jason['email']):
        return {"error": "User already exists."}, HTTPStatus.CONFLICT

        
    with open("./app/database/database.json", "r") as json_file:
        new_data = json.load(json_file)
        new_data['data'].append(new_user_jason)

        with open("./app/database/database.json", 'w') as json_file:
            json.dump(new_data, json_file, indent=4)
    
    
    return new_user_jason, HTTPStatus.CREATED
    
   