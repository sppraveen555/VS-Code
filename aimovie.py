import pandas as pd
from textblob import TextBlob

# Load movie data
df = pd.read_csv("imdb_top_1000.csv")

# Get user details
name = input("Enter your name: ")
mood = input("How do you feel today? ")
genre = input("Enter your favourite genre: ")
rating = float(input("Enter minimum IMDb rating: "))

# Analyze user mood
mood_score = TextBlob(mood).sentiment.polarity

# Filter by genre and rating
movies = df[
    (df["Genre"].str.contains(genre, case=False, na=False)) &
    (df["IMDB_Rating"] >= rating)
]

# Check movie sentiment and recommend
recommendations = []

for _, movie in movies.iterrows():
    overview = str(movie["Overview"])
    movie_score = TextBlob(overview).sentiment.polarity

    # Match mood
    if mood_score >= 0 and movie_score >= 0:
        recommendations.append(movie["Series_Title"])
    elif mood_score < 0 and movie_score < 0:
        recommendations.append(movie["Series_Title"])

    if len(recommendations) == 5:
        break

# Show results
print(f"\nMovie recommendations for {name}:")

if recommendations:
    for i, movie in enumerate(recommendations, 1):
        print(f"{i}. {movie}")
else:
    print("No suitable movies found.")