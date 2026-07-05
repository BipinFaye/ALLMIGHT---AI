# class complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def shownumber(self):
#         print(self.real,"i +",self.img,"j")

#     def __add__(self, num2):
#         newreal = self.real + num2.real
#         newimg = self.img + num2.img
#         return complex(newreal, newimg)
    
#     def showline(self):
#         print("____________")
         


# num1 = complex(5, 9)
# num1.shownumber()

# num2 = complex(4, 2)
# num2.shownumber()

# num3 = num1+num2
# num3.showline()
# num3.shownumber()


# #to find circle area and perimeter

# class circle:
#     def __init__(self,radius):
#         self.radius = radius

#     def calcarea(self):
#         print((22/7)* self.radius**2)
    
#     def perimeter(self):
#         print(2 * (22/7) * self.radius)
        
# c1 = circle(21)
# c1.calcarea()
# c1.perimeter()


# class employee:
#     def __init__(self,role, department, salary):
#         self.role = role
#         self.department = department
#         self.salary = salary


#     def showDetails(self):
#         print("role = ", self.role, "\ndepartment = ", self.department, "\nsalary = ", self.salary)
    
# class engineer(employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super(). __init__("engineer", "machines", "55,000")
    

# eng1 = engineer("pravin", 29)
# eng1.showDetails()



class order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self,other):
        if(self.price > other.price):
            print("order 1 is imp")
        else:
            print("order 2 is imp")

ordr1 = order("chips", 50)
ordr2 = order("suger", 40)

ordr2 > ordr1


