# Mike Pendleton
# Follow the assignment instructions to code an app that
# will tell a user their birthstone.

#print("#Chapter 3.13 INfinite Loops")



while True:
    user_input = input("Enter your Birthmonth. ie '1' >")
    month = int(user_input)
    #print("Birth Month", user_input)
    #break
    if user_input == "1":
        print("Your birthstone is Garnet")
        print("." * 30)
        break
    elif user_input == "2":
        print("Your birthstone is Amethyst")
        print("." * 30)
        break
    elif user_input == "3":
        print("Your birthstone is bloodstone")
        print("." * 30)
        break
    elif user_input == "4":
        print("Your birthstone is Diamond")
        print("." * 30)
        break
    elif user_input == "5":
        print("Your birthstone is Emerald")
        print("." * 30)
        break
    elif user_input == "6":
        print("Your birthstone is Pearl")
        print("." * 30)
        break
    elif user_input == "7":
        print("Your birthstone is Ruby")
        print("." * 30)
        break
    elif user_input == "8":
        print("Your birthstone is Peridot")
        print("." * 30)
        break
    elif user_input == "9":
        print("Your birthstone is Sapphire")
        print("." * 30)
        break
    elif user_input == "10":
        print("Your birthstone is Opal")
        print("." * 30)
        break
    elif user_input == "11":
        print("Your birthstone is Citrine")
        print("." * 30)
        break
    elif user_input == "12":
        print("Your birthstone is Zircon")
        print("." * 30)
        break
    else:
        print("Try month value again!")
        break

