
import random


def play_game():
    n = int(input("Enter how many time you need to play: "))
    while n > 0:
        x = []
        lst = [1,2,3,4,5,6]


        user_lst = []
        
        for i in range(5):
            user_choice = random.choice(lst)
            user_lst.append(user_choice)
            
        print(f"You're dice outputs are: {user_lst}")

        

        x.append(sum(user_lst))
        

        n -= 1


    return x

# play = int(input("Enter how many time you need to play: "))
# for i in range(play + 1):
#     x = play_game()

            

            

    