# x = 3.14
# y = [
#     1,
#     "hello",
#     [],
#     {
#         "key": "value"
#     },
#     (),
# ]

# d = {
#     "a": 1,
#     "b": 2,
#     "n" : [1, 2, 3],
#     "c" : {},
#     "g" : ()
# }

# s = {5,7,8,9}

# t = (1, 2, 3, 4)



# int i =0;
# for (i; i<4; i++){
#     if (s[i] != 9){
#         continue;
#     }
#     if(s[i] == 8){
#         print("found 8")
#         break;
#     }
# }



# for i in s:
#     if i != 8:
#         continue

#     if i==8:
#         print("found 8")
#         break


# print(8 not in s)

# arr = [1, 2, 3, 4, 5]
# for i in arr:
#     print(i)



def getSum(a : int, b : int):
    c = a + b
    return c


ar = [1, 2, 3, 4, 5]

# def find_max(arr: list):
#     max_val = arr[0]
#     for i in arr:
#         if i > max_val:
#             max_val = i
#     return max_val

# print(max(ar))
# print(min(ar))

# print(find_max(ar))

users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
]

def find_user(name: str) -> dict:
    for u in users:
        _name: str = u.get("name")
        if _name == name:
            return u
        
        elif u.get("age") > 30:
            return u
        
    return None

u = find_user("Bob")
print(u)






# print(getSum(3, 4))
# print(getSum("fgh", 8))