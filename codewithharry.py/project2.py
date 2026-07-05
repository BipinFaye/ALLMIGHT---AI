from random import randint
n = randint(1, 100)
a = -1
guesses = 1
while(a != n):
    a = int(input("Guess the number : "))
    if (a > n):
        print("lower number please")

    elif (a < n):
        print("Higher number please")
        guesses += 1

print(f"congratulation you have guessed the number {n} in {guesses} guesses")