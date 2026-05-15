from textblob import TextBlob

print("Welcome to Sentiment Analyzer!")

name = input("Enter your name: ")

if name == "":
    name = "User"

print("Hello,", name)

history = []

while True:
    text = input("\nType a sentence (or type 'history' / 'exit'): ")

    
    if text.lower() == "exit":
        print("Goodbye,", name)
        break

    
    elif text.lower() == "history":
        if len(history) == 0:
            print("No history available.")
        else:
            print("\nConversation History:")
            for item in history:
                print(item)
        continue

    
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        sentiment = "Positive 😊"
    elif polarity < 0:
        sentiment = "Negative 😔"
    else:
        sentiment = "Neutral 😐"

    
    history.append(f"{text} --> {sentiment}")

    # Print result
    print("Sentiment:", sentiment)