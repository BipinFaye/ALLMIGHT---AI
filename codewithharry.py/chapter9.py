
# f  =  open("file.txt")
# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# line3 = f.readline()
# print(line3)

# f.close()



# with open ("poem.txt", "r") as f:
#     doc = f.read("poem.txt")
#     if ("twinkle" in doc):
#         print("its present")
    
#     else:
#         print("not present")




# with open("poem.txt") as f:
#     content = f.read()
#     if("twinkle" in content):
#         print("yes")

#     else:
#         ("not")





# import random

# def game ():
#     print("your playing a game .... ")
#     score = random.randint(1, 50)
#     with open("hi_score.txt", "r") as f:
#         hiscore = f.read()
#         if (hiscore != ""):
#             hiscore = int(hiscore)     

#         else:
#             hiscore = 0
            
#     print(f"your score is : {score}")   
#     if (score>hiscore):
#         with open ("hi_score.txt", "w") as f:
#             f.write(str(score))

#     return score
            

# game()





# def printtable(n):
#     table = ""
#     for i in range (1 , 11):
#         table += (f"{n} x {i} = {n*i}\n")


#     with open (f"tables/table_{n}.txt", "w")as f:
#         f.write(table)


# for i in range (2 , 21):
#     printtable(i)





words = ["donkey", "hot", "cold"]
replacement = "######"

with open("file.txt", "r") as f:
    content = f.read() 

for word in words:
    content = content.replace(word, replacement)

with open("file.txt", "w") as f:
    f.write(content)
