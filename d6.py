import random
print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
        """)

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra ').split()

word_generated = random.choice(words)
print(word_generated)

display = []
for word in word_generated:
    display += "_"

game_over = False
lives = 6
while not game_over:

    guess = input("Guess a letter: ").lower()
    i=0

    if guess in display:
        print("You have already guessed that letter")

    for x in word_generated:
        if x == guess:
            display[i] = guess
        i+=1

    print(f"{' '.join(display)}")
    print(HANGMANPICS[lives])
    if guess not in word_generated:
        lives -=1
        print(f"{guess} is not in the word")
        if lives == 0:
            print("You loose!")
            print(f"The correct word was {word_generated}")
            game_over = True

    if '_' not in display:
        game_over = True
        print("You win!")
