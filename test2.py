

# if (condition){
#     //statement
# }
# else if(condition){
#     //statement
# }
# else{
#     //statement
# }



# int z = 7;
# if (z==5)printf("z is 5");
# else if( z==7 ) printf("z is 7");
# else printf("z is not 5 or 7");


# x = 7
# if x == 5:
#     print("x is 5")
# elif x == 7:
#     print("x is 7")
# else:
#     print("x is not 5 or 7")


# int i= 0;
# for (i; i<10; i++){
#     printf("%d",i);
# }


# int arr[] = {0,1,2,3,4,5,6,7,8,9};
# arr = [0,1,2,3,4,5,6,7,8,9, "hello"]
# arr.append(554)
# print(arr)

# arr = [0,1,2,3,4,5,6,7,8,9]
# for i in arr:
#     print(i, end=",")

# while (condition){
#     //statement
#     //++, --
# }

# i = 0
# while i < 10:
#     print(f"hello {i}")
#     i += 1



def method_name(a):
    _type = str(type(a))

    if 'function' in _type:
        a()


    

def method_2():
    print("hello world")

args = [
    6,
    [83,34,654,567],
    method_2
]



method_name(args[0])
method_name(args[1])
method_name(args[2])

# output: