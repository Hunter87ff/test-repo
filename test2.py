# const x = 45
# let y = ""
# var z = ""

from typing import Callable


x = {
    "name" : "asd",
    "name" : "something",
    "age" : 4,
    "roles" : [
        3525,456346346
    ],
    "props" : {
        "arg" : "asdasd"
    }
}

f = 36
g = 60

# if (g>f){
#     console.log("g is greater !!")
# }
# else if (){}
# else {}

if g>f:
    print("g is greater !!")
elif f>g:
    print("")
else:
    print("statement !!")

print("g is greater" if g>f else "g is not greater")


async def test(a : int, b:int):
    return a+b

def something(call : Callable, args):
    call(args)


something(lambda x: print(x>5), 7)


class A:
    name : str = "a"
    roles : list[int] = [
        35345,345345
    ]

    def __str__(self):
        return str({"name" : self.name, "roles" : self.roles})

    def __init__(self, name: str) -> None:
        self.name = name
        A.name = name

        


# for (let i=0; i<10; i++){

# }

# arr.forEach((e)=>{

# })
# for (cost x of arr){

# }

# x = [35434,345,345,345]
# for i in range(10):
#     print(i)


arr = [45645,54637,367,56,75,7564753,]

print(56 in arr)



arr = ["hello", "hii", "hahah"]
for _v in arr:
    if _v == "hello":
        print("hello")

arr[8] = "something"