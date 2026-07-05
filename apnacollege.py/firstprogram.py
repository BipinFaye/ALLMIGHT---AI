
"""print("welcome to rohit cycle store")
print("please enter the purchased brand , quantity and price of the product ")
input("please enter the brand name :")  
quantity =  int(input("enter the quantity : "))
price = int(input("enter tne price : "))
print("your total your hero cycle is :", quantity*price) 
print("thank you for visiting our cycle store")"""


#two numbers and their sum
"""number1 = int(input("num1 :"))
number2 = int(input("num2 :"))
print("sum = ", number1 + number2)"""


#program for finding area of the square
"""side1 = float(input("length of side 1 : "))
side2 = float(input("length of side 2 : "))
print("area of square:", side1*side2)"""


#input 2 floating point numbers and print their average
"""first = float(input("num 1 : "))
second = float(input("num 2 : "))
print("average =", (first+second)/2)"""


#input 2 numbers print true if a is greater than or equal to b if no print false
"""a = int(input("num 1 : "))
b = int(input("num 2 : "))
print(a>=b)"""


#wap to input users name and print it's length
"""str=input("enter name : ")
print(len(str))"""


#wap to find the occerence of "o" in a string
"""str=("come to school")
print(str.count("o"))"""


#wap for a school grading system
"""marks = int(input("enter obtained marks -->"))
if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "c"
elif(marks >= 60 and marks < 70):
    grade = "D"
else:
    grade = "fail"
print("grade of the student is :", grade)"""  


#wap to find the number is odd or even
"""number = int(input("enter the number --> "))
if(number % 2 == 0):
    print ("the number is an even number")
else:
    print("the number is an odd number")"""


#wap to find the gratest number from the input 3 numbers
"""num1 = int(input("enter number 1 -->"))
num2 = int(input("enter number 2 -->"))
num3 = int(input("enter number 3 -->"))
if(num1 > num2 and num1 > num3):
    print(num1)
elif(num2 > num3):
        print(num2)
else:
    print(num3)"""


#wap to check weather the number is a multiple of 7

"""b = int(input("enter the number --> "))
if (b % 7 == 0):
    print("it is the multiple of seven")
else:
    print("it is not the multiple of seven")"""


#wap to ask the user to enter names of their three favourite movies and store them into a list
"""movies = []
movie1 = input ("movie 1 --> ")
movie2 = input ("movie 2 --> ")
movie3 = input ("movie 3 --> ")
movies.append (movie1)
movies.append (movie2)
movies.append (movie3)
print (movies)"""



#wap to search for a palindrome
"""list1 = [1, 2, 5]
list2 = [1, 2, 3]
copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list1 == list1):
    print("palindrome")
else:
    print("not a palindrome")"""


#wap to count A
"""grade = ("C", "D", "A", "A", "B","B", "A")
print(grade.count("A"))"""


#wap to sort in ascending order 
"""list1 = ["C", "D", "A", "A", "B","B", "A",]
list.sort(list1)
print(list1)"""


"""dict1 = {
    "cat" : "a small animal" ,
    "table" : ("a piece of furniture" ,"list of facts and figures")
    }
print(dict1)"""


"""subjects = {
    "python" ,"python" ,"python" ,"java" ,"java" ,"c" ,"javascript" ,"java" ,"c++"
    }
print(len(subjects))"""


"""marks = {}

a = int(input("enter physics marks :"))
marks.update({"physics" : a})

b = int(input("enter chemistry marks :"))
marks.update({"chemistry" : b})

c = int(input("enter biology marks"))
marks.update({"biology" : c})
print(marks)"""


#wap for writing 9.0 and 9 as a seperate value in the set
"""values = {
("float" , 9.0),
("int" , 9)
}
print(values)"""

"""i = 100
while (i >= 1) :
    print(i)
    i -= 1 """

"""i = 3
while i <= 30 :
    print(i)
    i += 3 """

"""n = int(input("enter the number for table : "))
i = 1
while i <= 10 :
    print(n *i)
    i += 1"""

"""num1 = int(input("enter first no :"))
num2 = int(input("enter second no :"))
if num1>num2:
    print("the greater number is :", (num1))
else:
    print(num2)"""

"""dictionary = {
    "table" : ["a piece of furniture", "list of facts & figures"]
    "cat" : "a small animal"
}
print (dictionary)"""


"""subjects = {
    "python", "c", "python", "java", "python","java","c","c"
}
print(subjects)"""

#wap to enter marks of 3 subjects from the user and store them in 
# the  dictionary . start with an empty set & add one by one . use subject as key & marks as value

"""marks = {}
v = int(input("enter phy marks :" ))
marks.update({"phy" : v })
v = int(input("enter marathi marks :"))
marks.update({"marathi" : v})
v = int(input("enter chem marks :"))
marks.update({"chem" : v})
print(marks)
"""

nums = (1,4,9,16,25,36,49,64,81,100)
x = 9
i = 0
while i < len(nums):
    if (nums[i] == x):
        print("found at idx", i)
        i += 1


