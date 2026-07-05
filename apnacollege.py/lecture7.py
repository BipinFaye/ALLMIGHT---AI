# f = open("demo.txt","a")
# f.write("\n i am an editor")
# f.close()

#wap to reaplace any data in the file

# def replace():
#     with open("practice.txt","r") as f:
#             data = f.read()

#     new_data = data.replace("python", "c++")
#     print(new_data)

#     with open ("practice.txt","w") as f:
#         f.write(new_data)

# replace()

# wap to find any word in a file

# def findtheword():
    
#     with open ("practice.txt", "r") as f:
#         data = f.read()
#         word = ("learning")
#         if (word in data ):
#             print("found")
#         else:
#             print("not found")

# findtheword()


# to find in which the error is


# def check_line():
#     word = ("learning")
#     data = True
#     line_no = 1
#     with open ("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if (word in data):
#                 print(line_no)
#                 return
#             line_no += 1

#     return -1

# check_line()


# with open ("practice.txt","r") as f: 
#     data= f.read()
# count = 0
# num = data.split(",")
# for val in num:
#     if(int(val) %2 == 0):
#         count += 1
    
# print(count)