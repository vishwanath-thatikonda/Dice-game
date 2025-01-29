import random
import time

def players():
    players = input("Enter no of players : ")
    print()
    while not players.isdigit():
        print("Please Enter a Valid number!, Atleast 1 player should play this game")
        players = input("Enter no of players : ")
        print()

    names = []
    y = int(players)
    while y > 0:
        name = input("Enter You're name: ")
        names.append(name)
        y -= 1
    return names


def dice_game():
    names = players()
    x = len(names)
    
    for j in range(len(names)):
        print(f"Player {names[j]} Chance:")
        n = input("Enter No of Times You Want to play: ")
        while not n.isdigit():
            print("Please Enter a Valid number!")
            n = input("Enter No of Times You Want to play: ")
        print("Generating results....................")
        start = time.sleep(1)
        
        

        
        result = []
        for i in range(int(n)):
            random_num = random.randint(1,6)
            result.append(random_num)
        print(f"Player {names[j]} Game outcome result is : {result}")
        print()

dice_game()




      

            

            

    