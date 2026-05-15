import random


destinations = {
    "beach": ["Bali", "Maldives", "Goa"],
    "mountain": ["Himalayas", "Swiss Alps", "Rocky Mountains"],
    "city": ["Paris", "Tokyo", "New York"]
}


jokes = [
    "Why do travelers always feel warm? Because of hot spots!",
    "Why did the computer go on vacation? It needed a break!",
    "Why don't programmers like nature? Too many bugs!"
]

print("Welcome to TravelBot!")

name = input("What is your name? ")
print("Hello,", name)

while True:
    print("\nChoose an option:")
    print("1. Recommendation")
    print("2. Packing Tips")
    print("3. Joke")
    print("4. Exit")

    choice = input("Enter your choice: ").lower()

    
    if choice == "1" or choice == "recommendation":
        place = input("Do you like beach, mountain, or city? ").lower()

        if place in destinations:
            print("You can visit:", random.choice(destinations[place]))
        else:
            print("Sorry, I don't have suggestions for that.")

    
    elif choice == "2" or choice == "packing tips":
        days = input("How many days is your trip? ")

        print("\nPacking Tips:")
        print("- Pack comfortable clothes")
        print("- Carry chargers")
        print("- Take important documents")
        print("- Check the weather")

    
    elif choice == "3" or choice == "joke":
        print(random.choice(jokes))

    
    elif choice == "4" or choice == "exit":
        print("Goodbye! Safe travels,", name)
        break

    else:
        print("Invalid choice. Please try again.")