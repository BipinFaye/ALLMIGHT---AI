# for i in range (1, 10):
#     print("hello world")


# i = 1                 
# while (i < 9):
#     print("hello world")
#     i += 1




# num = int(input("enter the number : "))
# for i in range (1, 11):
#     print(f"{num} X {i} = {num*i}")
#     i += 1
    



# l = ["rahul", "harsh", "samir", "harry", "hira"]
# for name in l:
#     if (name.startswith("r")):
#         print(f"hello {name}")



# num = int(input("enter the number : "))
# i = 1
# while (i <= 10):
#     print(num*i)
#     i += 1




# num = int(input("enter the number : "))
# for i in range(2,num):
#     if (num % i == 0):
#         print("number is not prime")
#     break

# else:
#     print("number is prime")





# num = int(input("enter the number : "))
# i = 1
# sum = 0
# while (i <= num):
#     sum += i
#     i += 1
# print(sum)




# num = 6
# fact = 1
# for i in range(1, num+1):
#     fact = fact * i
# print(f"the factorial of  {num} is {fact}")




'''   *
     ***
    *****
   *******
  *********  '''


# n = 5
# for i in range (1, n+1):
#     print(" "*(n-i), end = "")
#     print("*"*(2*i-1), end = "")
#     print("")


"""
*   
* *   
* * *   
* * * *   
* * * * *   
"""   



# n = 5
# for i in range (1, n+1):
#     print("* "*(i), end = "  ")
#     print()



"""
*****
*   *
*   *
*   *
*****

"""


# n = int(input("enter the number : "))
# for i in range(1, n+1):
#     if (i == 1 or i == n):
#         print("*"*(n), end = "")
#     else:
#         print("*", end = "")
#         print(" "*(n-2), end = "")
#         print("*", end = "")
#     print("")




""" print table backwards """

# n = int(input("enter number : "))
# for i in range (10, 0, -1):
#     print(i*n)


# n = int(input("enter number : "))
# for i in range (1, 11):
#     print(n*(11-i))



def sum (n):
    if (n==1):
        return 1
    return (n-1)+n

print(sum(4))
