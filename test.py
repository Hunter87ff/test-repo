


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




class Human:
    eye_count = 2
    leg_count = 2
    hand_count = 2
    name = "human"

    def __init__(self, name: str):
        self.name = name

    def speak(self, message: str):
        print(f"{self.name} : {message}")

    @staticmethod
    def kick(name : str):
        print(f"{name} kicked")


Human.kick("Ayush")
h1 = Human("priyojeet")
h2 = Human("Ayush")
h1.speak("Hello")
h2.speak("Hi")