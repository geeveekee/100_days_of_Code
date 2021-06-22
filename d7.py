print("""
  _____                          _____ _       _               
 / ____|                        / ____(_)     | |              
| |     ___  __ _ ___  ___ _ __| |     _ _ __ | |__   ___ _ __ 
| |    / _ \/ _` / __|/ _ \ '__| |    | | '_ \| '_ \ / _ \ '__|
| |___|  __/ (_| \__ \  __/ |  | |____| | |_) | | | |  __/ |   
 \_____\___|\__,_|___/\___|_|   \_____|_| .__/|_| |_|\___|_|   
                                        | |                    
                                        |_|
        """)

run = True
while run:
    mode = input("Type 'encode' to encrypt and 'decode' to decrypt:")
    message = input("Type your message: ")
    shift_no = int(input("Type your shift number"))
    
    if mode == 'encode':
        encoded_msg = ''
        for letter in message:
            letter = (ord(letter) + shift_no)
            letter_s = chr(letter)
            encoded_msg += letter_s
        print(encoded_msg)

    elif mode == 'decode':
        decoded_msg = ''
        for letter in message:
            letter = (ord(letter) - shift_no)
            letter_d = chr(letter)
            decoded_msg +=letter_d
        print(decoded_msg)

    choice = input("Type 'yes' if you want to go again. Otherwise type 'no'")
    if choice == 'no':
        run = False

        
