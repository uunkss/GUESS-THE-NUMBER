import random
again = "yes"
while again == "yes":
    secret_number = random.randrange(1, 129)
    guess = 0
    score = 0
    while guess != secret_number:
        guess = (int)(input("Guess a number 1 to 128: "))
        if guess < secret_number:
            if guess < 1:
                print ("The number is invalid!")
            print("Too low.")
            score = score + 1
        elif guess > secret_number:
            if guess > 128:
                print ("The number is invalid!")
            print("Too high.")
            score = score + 1
        else:
            print("Correct!")
            score = score + 1
            print("Total guess time : " + str(score))
    print("Play again?")
    again = input("if yes type 'yes' if no type anything: >> ")
