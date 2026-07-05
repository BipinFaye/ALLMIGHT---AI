# class student:
#     def __init__(self,name,age,speciality):
#         self.name = name
#         self.age = age
#         self.speciality = speciality
#         print ("adding new students in the database")


# s1 = student("karan",19,"math")
# print(s1.name, s1.age,s1.speciality )

# s2 = student("harsh",21,"bio")
# print(s2.name,s2.age, s2.speciality)





# class cars:
#     def __init__(self,brand,year):
#         self.brand = brand
#         self.year = year
#         print("heres the car")

# c1 = cars ("BMW",2014)
# print(cars.brand,cars.year) 




# class student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def get_avg(self):
#      sum = 0
#      for val in self.marks:
#          sum += val
#      print("hello",self.name,"your average score is --", sum/3)

# s1 = student("harsh",[78,85,74])

# s1.get_avg()





# class cars:
#    def __init__(self,name,weight):
#       self.name = name
#       self.weight = weight
#    def get_weight(self):
#     sum = 0
#     for val in self.weight:
#       sum += val
#     print ("hello your cars avg weight is -- ",sum/len(self.weight))
         
# c1 = cars("bmw, audi, GTR",[15,16,97])
# c1.get_weight()






# class height_wise:
#   def __init__(self,name,height):
#     self.name = name
#     self.height = height
#   def get_height(self):
#     sum = 0
#     for val in self.height:
#       sum += val
#     print("the avg height of ",self.name ,"is", sum/3)
# p1 = height_wise("harsh", [6.1,6.2,6.8])
# p1.get_height()
      




# class account:
#     def __init__(self,balance,account_no):
#         self.balance = balance
#         self.account_no = account_no
        
#     def debit(self):
#         ammount = int(input("enter the ammount to debit "))
#         self.balance -= ammount
#         print("your account is debited by -- ", ammount,"your remaining balance is -- ",self.return_balance())
            
#     def credit(self):
#         ammount = int(input("enter the ammount to credit "))
#         self.balance += ammount
#         print("your account is credited by -- ", ammount,"your remaining balance is -- ",self.return_balance())
    
#     def return_balance(self):
#         return self.balance

# p1 = account(5000,123456)
# p1.credit()
# p1.debit()
# p1.credit()
# p1.debit()





#chachu ki jameen

#basic code for super() method

# class chachu:
#     def __init__(self,jaydat,**kwargs):
#         super().__init__(**kwargs)
#         self.jaydat = jaydat

# class father:
#     def __init__(self,height,**kwargs):
#         super().__init__(**kwargs)
#         self.height = height
        

# class mother:
#     def __init__(self,skin,**kwargs):
#         super().__init__(**kwargs)
#         self.skin = skin
       
# class child(father,mother,chachu):
#     def __init__(self,name,height,skin,jaydat):
#         self.name = name
#         super().__init__(height=height,skin=skin,jaydat=jaydat)
        

# c1 = child("harry",5,"fair","9_ekr")
# print("name" , c1.name,"\nheight", c1.height, "\nskin", c1.skin,"\nyour_jaydat : ",c1.jaydat)

 