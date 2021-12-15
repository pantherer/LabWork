import random
num = int(input("enter any num"))
rand = print(random.randrange(1,9))
if num != rand:
    print("sorry ! try again")
if num == rand:
    print("congratulation you have successfully guessed")

