import os
import json

DATABASE_DIRECTORY = os.environ.get('DATABASE_DIRECTORY')

def is_empty():
    if os.path.getsize(f'{DATABASE_DIRECTORY}/database.json') == 0:
        new_database = {'data': []}
        with open("./app/database/database.json", "w") as json_file:
            json.dump(new_database, json_file, indent=4)


def database_exist():
    if not os.path.isdir(DATABASE_DIRECTORY):
        os.mkdir(DATABASE_DIRECTORY)

    if not 'database.json' in os.listdir(DATABASE_DIRECTORY):
        with open(f"{DATABASE_DIRECTORY}/database.json", "a"):
            ...


def verify_email_exist(email):
    with open("./app/database/database.json", "r") as json_file:
            user_list = json.load(json_file)
    
            email_list = [user['email'] for user in user_list['data']]
            
    return email in email_list 

print('ok')