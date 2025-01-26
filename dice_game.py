import random
def play_game(n):
    while n > 0:
        x = []
        lst = [1,2,3,4,5,6]


        user_lst = []
        
        for i in range(5):
            user_choice = random.choice(lst)
            user_lst.append(user_choice)

        

        x.append(sum(user_lst))
        

        n -= 1


    return x

x = play_game(3)
print(x)

            

            

    