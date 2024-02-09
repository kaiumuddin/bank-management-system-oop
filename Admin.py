
class Admin:
    def __init__(self, name, email, password) -> None:
        self.id = None
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self) -> str:
        cls = self.__class__.__name__
        return f'{cls}:: id:{self.id}, name:{self.name}, email:{self.email}'