class invalidTypeError(Exception):
      
    def __init__(self, name, email):

        self.message = {
                        "wrong fields": [
                                {
                                    "nome": f"{type(name).__name__}"
                                },
                                {
                                    "email": f"{type(email).__name__}"
                                }
                            ]
                        }

        super().__init__(self.message)
