# list = [1,2,3,4,5,6,7,8,9]
# def length():
#     print(len(list))

# length()
# n = (int(input("enter the number :")))
# def calc_fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     print(fact)
      
# calc_fact(n)  
# # def plus (a , b):
#     sum = a+b
#     print(sum)

# plus(2 , 3)

# def average(a,b,c):
#     sum = a+b+c
#     avg = sum/3
#     print(avg)
# average(1,2,3)
# average(4,6,12)    
        
# number = [1,4,5,6,8,3,2,9]
# def list(number):
#     for item in number:

#         print(item, end = " " )

# list(number)

# n = (int(input("enter the number : ")))
# def factorial(n):
#     x = 1
#     for i in range(1,n+1):
#         x *= i
#     print(x)

# factorial(n)

#usd to inr converter

# n = (int(input("enter the usd value: ")))
# inr_val =n* 83
# def convert(n):
#    print(n,"USD", inr_val, "INR")
# convert(n)

# n = (int(input("enter the usd value: ")))
# def number(n):
#     if(n%2):
#         print("odd")
#     else:
#         print("even")

# number(n)


"""recursion"""


# def show(n):
#     if (n == 0):
#         return
#     print(n)
#     show(n-1)
# show(5)

#factorial using rec

# def fact(n):
#     if (n==1 or n==0):
#         return 1
#     return fact (n-1)*n
# print(fact(5))

# wap to cslculate the sum of first n natural numbers
# n = (int(input("enter the number : ")))
# def nature(n):
#     if (n==0):
#      return 0
    
#     return nature(n-1) + n
# sum = (nature(n))
# print ("your total is ",sum)


# print element of list using recursion

# list_num = ["apple","mango","banana","watermln"]
# def item_list(list, idx=0):
#     if (idx == len(list_num)):
#         return
    
#     print(list[idx])
#     item_list(list,idx+1)

# item_list(list_num)
