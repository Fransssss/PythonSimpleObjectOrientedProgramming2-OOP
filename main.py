from animal import Dog  # call the class

print("\n== Dog Database ==")
print("1. Input data of a dog")
print("2. Display the name of the dog")
print("3. Display the height of the dog")
print("4. Display the weight of the dog")
print("5. Display the life expectancy of the dog")
print("6. Display the personality/ies of the dog")
print("7. Display the full information of the dog")
choice = input("choice: ")

dog = Dog("NoName", 0, 0, 0, "NoPersonality")  # default value of dog object
data_has_changed = False                       # make sure user has chosen option no 1 and updated new data
invalid_subject = False                        # make sure whether input is valid or not
invalid_measure = 0

while choice != 'E' and choice != 'e':
    if choice == '1':
        print("\n[ Input data of a dog ]")
        name = ""
        name = input("Input name: ")
        try:                                          # make sure user input is string
            if int(name):
                print("\n[ Invalid name - string only ]")
                print("[ Update failed ]")
                name = "NoName"
                invalid_subject = True
        except ValueError:
            if name[0].islower():
                name = name.capitalize()               # capitalize dog's name

        if not invalid_subject:                        # make sure name is valid for user to continue update value
            height = 0
            try:                                       # just in case user input not digit input
                print("Input height: ", end="")        # end= - means the prompt and input is put in one line / no new line
                height = int(input())
            except ValueError:
                print("\n[ Invalid input - digit only ]\n")

            weight = 0
            try:
                print("Input weight: ", end="")
                weight = int(input())
            except ValueError:
                print("\n[ Invalid input - digit only ]\n")
                invalid_measure += 1

            life_expectancy = 0
            try:
                print("Input life expectancy: ", end="")
                life_expectancy = int(input())
            except ValueError:
                print("\n[ Invalid input - digit only ]\n")
                invalid_measure += 1

            personalities = ""
            personalities = input("Input personality/ies: ")
            if invalid_measure == 0:                    # if only all user inputs are valid then update data
                dog = Dog(name, height, weight, life_expectancy, personalities)
                data_has_changed = True
                print("\n[ Data updated ]")
            else:
                print("\n[ Update failed ]")

    elif choice == '2':
        print("\n[ Display the name of the dog ]\n")
        print(dog.name)
        print("--------")
        print(dog.the_name())

    elif choice == '3':
        print("\n[ Display the height of the dog ]\n")
        print(dog.height)
        print("--------")
        print(dog.the_height())

    elif choice == '4':
        print("\n[ Display the weight of the dog ]\n")
        print(dog.weight)
        print("--------")
        print(dog.the_weight())

    elif choice == '5':
        print("\n[ Display the life expectancy of the dog ]\n")
        print(dog.life_expectancy)
        print("--------")
        print(dog.the_life_expectancy())

    elif choice == '6':
        print("\n[ Display the personality/ies of the dog ]\n")
        if dog.personalities[0].islower():
            dog.personalities = dog.personalities.capitalize()     # capitalize for the sake of output
        print(dog.personalities)
        if dog.personalities[0].isupper():
            dog.personalities = dog.personalities.lower()          # make lower case again for full information
        print("--------")
        print(dog.the_personalities())

    elif choice == '7':
        print("\n[ Information of the dog ]")
        print("------------------------------")
        if data_has_changed:
            print(dog.the_dog_information())
        else:
            print("No update: ", dog.name, " - ", dog.height, " - ", dog.weight, " - ",
                  dog.life_expectancy,
                  " - ", dog.personalities)

    else:
        print("\n[ Invalid choice ]")

    print("\n== Dog Database ==")
    print("1. Input data of a dog")
    print("2. Display the name of the dog")
    print("3. Display the height of the dog")
    print("4. Display the weight of the dog")
    print("5. Display the life expectancy of the dog")
    print("6. Display the personality/ies of the dog")
    print("7. Display the full information of the dog")
    choice = input("choice: ")

if choice == 'e' or choice == 'E':
    print("\n== Exit Program ==")