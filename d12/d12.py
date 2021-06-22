import logo
from data import data
import sys
import random

length_list = len(data)
logo.print_logo()

def get_followers():
    global j
    j +=1
    bio = data[j]
    followers = bio['follower_count']

def load_data(i):
    bio = data[i]
    name = bio['name']
    description = bio['description']
    country = bio['country']
    print(f"{name}, a {description}, from {country}")

def check_answer(a, b):
    bio_a = data[a]
    bio_b = data[b]
    followers_a = bio_a['follower_count']
    followers_b = bio_b['follower_count']
    print(followers_a, followers_b)
    if followers_a > followers_b:
        i = i
        return 'a'
    else:
        i = j
        return 'b'

i = random.randint(0, length_list-1)
def game():
    global i
    global j
    j = random.randint(0, length_list-1)
    print("Compare A: ")
    print(load_data(i))
    logo.print_vs()
    print("Against B: ", load_data(j))
    choice = input("Who has more followers? 'A' or 'B'").lower()
    if choice == check_answer(i, j):
        print("cool")
        game()
    else:
        print("You lost! Better luck next time")
        sys.exit()
game()
