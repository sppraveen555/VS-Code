name = input("What is your name? ")
print("Hello,", name)

mood = input("How are you feeling today? ")
if mood == "good":
    print("That's great!")
elif mood == "bad":
    print("Hope you feel better soon.")
else:
    print("Thanks for sharing.")

print("Goodbye,", name)