known_users = ["Alice", "Emma", "Georgie", "Harry", "Fred", "Bob", "Claire", "Dan", "Jason", "Miriam", "Luke", "Darth", "Dwight", "Creed"]
print(len(known_users))

while True:
    print("Hi, my name is T!")
    name = input("What's your name?: ").strip().capitalize()

    if name in known_users:
        print("Welcome {}!".format(name))
        remove = input("Would you like to be removed from the system? (y/n): ").strip().lower()
        if remove == 'y':
            known_users.remove(name)
            print("You have been bounced")

    else:
        print("Name not found")
        add = input("Would you like to be added? (y/n): ").strip().lower()
        if add == 'y':
            known_users.append(name)
            print("Your name has been added {}!".format(name))
        elif add == 'n':
            print("Have a nice day")
