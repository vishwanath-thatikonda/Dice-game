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
    
    for i in range(y):
        name = input(f"Enter player{i+1} name: ")
        names.append(name)
        
    return names


def dice_game():
    names = players()
    x = len(names)
    
    for j in range(len(names)):
        print('-'*50)
        print(f"{names[j].upper()} Chance:")
        n = input("Enter No of Times You Want to play: ")
        while not n.isdigit():
            print("Please Enter a Valid number!")
            n = input("Enter No of Times You Want to play: ")
        print(f"Rolling Dice {n} times and Generating Results...")
        start = time.sleep(1)
        
        

        
        result = []
        for i in range(int(n)):
            random_num = random.randint(1,6)
            result.append(random_num)
        print(f"{names[j].upper()} Game outcome result is : {result}")
        print()

dice_game()




      

            

            

    
