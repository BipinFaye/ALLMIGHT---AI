# class programmer():
#         company = "mocrosoft"
#         def __init__(self,name, lang, salary):
#             self.name = name
#             self.lang = lang
#             self.salary = salary
#             print("here is the info of the programers ")

#         def get_info (self):
#             print(f"name = {self.name},\nused language = {self.lang},\nsallary is = {self.salary}" )

# employee1 =programmer("harry", "python", "12,000")

# employee1.get_info()

# e2 = programmer("harish", "java", "50,000")
# e2.get_info()
# e3 = programmer ("anshul shende", "HTML and CSS", "25k")
# e3.get_info()

#---------------------------------------------------------------------------------------------------------------------------------------------



# class calculator():
#     def __init__(self,value):
#         self.value = value


#     def square (self):
#         print(f"the square of the number is : {self.value**2}")

#     def cube (self):
#         print(f"the cube of the number is : {self.value*self.value*self.value}")

#     def square_root(self):
#         print(f"the square root of the number is : {self.value**1/2}")

#     @staticmethod
#     def greet():
#         print("hello user")

# number  = calculator(float(input("enter the number : ")))
# number.greet()
# number.square()

#------------------------------------------------------------------------------------------------------------------------------------------------------------


# from random import randint

# class train():
#    def __init__(self, name, fro, to):
#       self.name = name
#       self.fro = fro
#       self.to = to


#    def booking(self):
#       print(f"hello {self.name}")
      
#       print(f"your seat is booked in train number : {randint(1234, 5655)}\nand the seat nuber is : {randint(1234455, 2344500)}")

#    def status(self):
#       print(F"your train from {self.fro} to {self.to} is running on time")

#    def fare(self):
#       print(f"the price for ticket from {self.fro} to {self.to} will be {randint(100, 500)}")
      
      
# p1 = train("harry", "rampur","nagpur")
# p1.booking()
# p1.status()
# p1.fare()


#------------------------------------------------------------------------------------------------------------------------------------------------------


# class calc():
#     def __init__(slf,val1,val2):
#         slf.val1 = val1
#         slf.val2 = val2
#     def add(slf):
#         print(slf.val1 + slf.val2)

# v1 = calc(5,6)
# v1.add()