with open("100_days_of_Code/d25/names.txt") as f:
    content = f.readlines()


f = open("100_days_of_Code\d25\letterDraft.txt", "r")
draft = f.read()

for name in content:
    name = name.strip()
    new_letter = draft.replace("name", name)
    print(new_letter)

    with open(f"100_days_of_Code\d25\mails\{name}_invite.txt", "w") as file:
        file.write(new_letter)
 
