from os import system

print("""
                                          88                
                                    ,d    ""                          
                                    88                                
,adPPYYba, 88       88  ,adPPYba, MM88MMM 88  ,adPPYba,  8b,dPPYba,   
""     `Y8 88       88 a8"     ""   88    88 a8"     "8a 88P'   `"8a  
,adPPPPP88 88       88 8b           88    88 8b       d8 88       88  
88,    ,88 "8a,   ,a88 "8a,   ,aa   88,   88 "8a,   ,a8" 88       88  
`"8bbdP"Y8  `"YbbdP'Y8  `"Ybbd8"'   "Y888 88  `"YbbdP"'  88       88  

        """)

clear = lambda: system('clear')
print("Welcome to the secret auction program.")
bidders = {}
auction = True
while auction:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid
    max_bid = 0;
    for ppl in bidders:
        if bidders[ppl] > max_bid:
            max_bid = bidders[ppl]



    flag = input("Are there any other bidders? Type 'yes' or 'no'")

    max_bidder_name = list(bidders.keys())[list(bidders.values()).index(max_bid)]
    if flag == 'no':
        auction = False
    clear()

print(f"The max bid is ${max_bid}, bid by {max_bidder_name}")
