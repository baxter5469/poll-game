''' Poll Game v1.5 By Andrew Ault
4/12/18
'''
import json
names = {}
while True:
    username = input(str("Please type your name: ")).lower()
    if username.lower() in names:
        print("Name already in the list, Try again.")
        continue
    if username == "quit":
        break
    if len(username) < 1:
        print("Type quit if you would like to move on!")
    if len(username) > 1:
        userinput = input("What month were you born in? Type the number only: ")
        try:
            userinput = int(userinput)
            names[username] = userinput
            with open('file.txt', 'w') as file:
                file.write(json.dumps(names))
        except:
            print("Only the number no letters!")
if len(names) > 0:
    print("The average month from your inputs is: " + str(sum(names.values()) / len(names)))
else:
    pass