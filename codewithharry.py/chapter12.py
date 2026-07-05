# try:
#     with open ("fight.txt") as f:
#        print(f.read())
# except Exception as e:
#     print(e)

# try:
#     with open ("fileio.txt") as f:
#         print(f.read())
# except Exception as e:
#     print(e)

# try:
#     with open ("flf.txt") as f :
#         print(f.read())

# except Exception as e:
#     print(e)



# global keyword( it basically changes the global keyword with the new entered value)
# a = 89
# def func():
#     global a
#     a = 3
#     print (a)


# func()
# print(a)



# l = [1,2,3,4,5,6,7,8,9]
# for i, item in enumerate (l):
#     if(i == 3 or i == 5 or i == 7):
#         print(item)  

# for index, item in enumerate (l):
#     print(f"the number at index {index} is {item}")

   


# n = 5
# list = [n*i for i in range (1, 11)]
# print(list)




# try:
#     a = int(input("enter a number "))
#     b = int(input("enter a number "))
#     print(a/b)
# except ZeroDivisionError as e:
#     print("infinite")
    



# n = int(input("enter a number :"))
# padhe = [n*i for i in range (1, 11)]
# with open ("padhe.txt" , "a") as f:
#     f.write(f" {str(padhe)}")
