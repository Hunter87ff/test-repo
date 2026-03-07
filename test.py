from typing import Callable
import time;


students = [
    9,2,1,6, 8
]


start_time = time.time()
print("something")
end_time = time.time()

print("execution time: ", end_time - start_time)

def test_method(name: str):
    print(f"testing method with name: {name}")


test_method("asdasd")


actions = {
    "1" : {
        "name" : "join class",
        "perm" : 1
    },
    "2" : {
        "name" : "kick classmates",
        "perm" : 5
    },
    "3" : {
        "name" : "sleep during classes",
        "perm" : 0
    }
}


def action(func: Callable):

    def validate(id:str, perm:int):
        _action = actions.get(id)
        if _action is None:
            print("invalid action")
            return
        
        if _action.get("perm") > perm: # type: ignore
            print("you dont have permission to do this action")
            return
        
        return func(id, perm)
    
    return validate

        
        
@action
def kick(id:str, perm:int):
    print("kicking classmates")


@action
def join(id:str, perm:int):
    print("joining class")


@action
def sleep(id:str, perm:int):
    print("sleeping during classes")


print(1/0)

kick("2", 1)
join("1", 1)
sleep("3", 0)
