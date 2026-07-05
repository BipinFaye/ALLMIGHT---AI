# def greet ():
#     name = input("what your name : ")
#     print("welcome", name)
    
# greet()




# def big_number():
#     a = int(input("enternthe  number "))
#     b = int(input("enternthe  number "))
#     c = int(input("enternthe  number "))
#     if(a>=b and a>=c):
#         print(a,"is the biggest nymber")

#     elif (b>=a and b>=c):
#         print(b, "is the biggest number")

#     elif(c>=a and c>=b):
#         print(c, "is the biggest number")

#     else:
#         ("there are same numbers present ")


# big_number()




# def temp():
#     n = int(input("enter the temp in farenheit : " ))
#     print("the temperature is ",(5*(n-32)/9), "celcius")
    

# temp()


"""sum of n natural numbers """
# def sum(n):
#     if (n==1):
#          return 1
#     return sum(n-1)+n

# print(sum(4))





# n = int(input("enter the number : "))
# def pattern(n):
#     if (n==0):
#      return
#     print("*"*n)
#     pattern(n-1)

# pattern(n)


# def convert(inch):
#     return inch*2.4
# n = float(input("enter the distance in inches : "))

# print(f"the distance is CMs will be :",{convert(n)},"CMs")
    
# convert()




# n = float(input("enter the distance in inches : "))
# def convert ():
#     return n*2.54

# print("the distance in CMS will be", convert(),"CMs")




def multiply():
    n = int(input("number : "))
    for i in range (1, 11):
       print(f"{n} X {i} = {n*i}")

multiply()