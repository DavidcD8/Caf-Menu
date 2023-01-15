coffee = ["Café Latte", "Caffe Americano", "Espresso", "Cappuccino", "Macchiato"]

choice = int(input("Enter Choice: "))

try:
    if choice == 1:
        print(coffee[0])
    elif choice == 2:
        print(coffee[1])
    elif choice == 3:
        print(coffee[2])
    elif choice == 4:
        print(coffee[3])
    elif choice == 5:
        print(coffee[4])
    else:
        print(coffee[6])
except:
    print("Invalid number")
finally:
    print("Have a good day")
