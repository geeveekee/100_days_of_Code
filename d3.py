print("""
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
        """)
print("Welcome to Treasure Island. Your mission is to find the treasure.")
path1 = input("You're at a crossoroad. Where do you want to go? Left or Right?")
if(path1 == "right"):
    print("Game over")
else:
    path2 = input("You are now at a river. Do you wish to travel upstream or downstream? (Type up or down)")
    if(path2 == "up"):
        print("Game over")
    else:
        path3 = input("There are now 2 doors, one red and blue. Which one do you open?")
        if(path3 == "red"):
            print("Game over")
        else:
            print("Yay! You have found the treasure!")
