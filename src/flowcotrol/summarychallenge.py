options = ["Learn Python", "Learn Java", "Go swimming", "Have dinner", "Go to bed", "Exit"]
choice = "-"

while choice != "0":
    if choice.isnumeric() and int(choice) in range(len(options)):
        print("You chose {}".format(options[int(choice) - 1]))
    else:
        print("Please choose your option from the list below:")
        for option in options:
            index = options.index(option) + 1
            if index == len(options):
                index = 0
            print("\t{}: {}".format(index, option))

    choice = input()
