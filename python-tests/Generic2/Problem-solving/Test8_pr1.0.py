#using while condition
i = 10
while i <=15:
    print(i)
    i = i + 1
print("done")

#using while to create a guess game
secret_number = 9
guesscount = 0
guesslimit = 3
while guesscount < guesslimit:
    guess = int(input('Guess:'))
    guesscount += 1
    if guess == secret_number:
        print("you won!")
        break
    else:
        print("sorry try again")
else:
    print("you execeeded tries,you failed")





