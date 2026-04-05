
class User:
    name: str = "hello"
    
    def __init__(
            self, 
            name: str, 
            email: str, 
            password: str
        ):
        self.name = name
        self.email = email
        self.password = password
    
    def hash(self):
        return self.password[::-1]
    
    @staticmethod 
    def do_something():
        print("Doing something")
        User.name = "something else"

    @classmethod
    def hello(cls):
        print("Hello from class method")
        cls.name = "hello"

u0 = User(
    name="John Doe",
    email="example@test.in",
    password="password123"
)

