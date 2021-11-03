import json
from app.exceptions import invalidTypeError

class User():

    def __init__(self, nome, email) -> None:
        self.nome = nome.title()
        self.email = email.lower()
        self.id = self.create_id()
      

    def create_id(self):
        with open("./app/database/database.json", "r") as json_file:
            user_list = json.load(json_file)
        try:
            id = [user['id'] for user in user_list['data']]
            return max(id) + 1
        except:
            return 0

    
    def toJson(self):
        return {"nome": self.nome, "email": self.email, "id": self.id}

    
    @staticmethod
    def verify_valid_typs(nome, email):
        try:
            if type(nome) != str or type(email) != str:
                raise invalidTypeError(nome, email)

            return False

        except invalidTypeError as err:
            return err.message
            