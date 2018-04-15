''' Poll Game v1.0 By Andrew Ault
4/12/18
'''
names = {}
while True:
    username = input(str("Please type your name: "))
    if username == "quit":
        break
    if len(username) < 1:
        print("Type quit if you would like to move on!")
    if len(username) > 1:
        userinput = input("What month were you born in? Type the number only: ")
        try:
            userinput = int(userinput)
            names[username] = userinput
        except:
            print("Only the number no letters!")
        continue
if len(names) > 0:
    print("The average month from your inputs is: " + sum(names.values()) / len(names))
else:
    pass