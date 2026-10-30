import random 

movies = [
    {
        "Title":"Pokemon",
        "Genre":"Action/Adventure,Fantasy",
        "Rating":"10.0",
        "Mood":"Exciting",
        "Overview":"Pokémon anime spans Ash Ketchum's 25-year quest and the newer generation led by Liko and Roy."
    },
    {
        "Title":"The Lion King",
        "Genre":"Adventure",
        "Rating":8.7,
        "Mood":"Exciting"
    },
    {
        "title": "Finding Nemo",
        "genre": "Animation",
        "rating": 8.2,
        "mood": "Happy",
        "overview": "A loving father goes on an amazing adventure to find his lost son."
    },
    {
        "title": "Harry Potter",
        "genre": "Fantasy",
        "rating": 7.6,
        "mood": "Exciting",
        "overview": "A young wizard discovers friendship, magic and the power of courage."
    },
    {
        "title": "Paddington",
        "genre": "Comedy",
        "rating": 7.3,
        "mood": "Happy",
        "overview": "A friendly bear finds a new family and brings joy and laughter."
    },
    {
        "title": "Toy Story",
        "genre": "Animation",
        "rating": 8.3,
        "mood": "Happy",
        "overview": "Toys come alive in a funny adventure about friendship and teamwork."
    },
    {
        "title": "Jurassic Park",
        "genre": "Adventure",
        "rating": 8.2,
        "mood": "Exciting",
        "overview": "Scientists visit a dinosaur park where a dangerous adventure begins."
    },
    {
        "title": "Coco",
        "genre": "Fantasy",
        "rating": 8.4,
        "mood": "Emotional",
        "overview": "A boy discovers family secrets through music, love and memories."
    }
]

def analyse_sentiment(overview):

    positive_words = [
        "wonderful", "funny", "friendship", "brave", "amazing",
        "loving", "love", "courage", "joy", "laughter",
        "happy", "great", "friendly", "teamwork"
    ]

    negative_words = [
        "danger", "dangerous", "sad", "fear", "lost",
        "problem", "evil", "terrible", "death"
    ]

    text = overview.lower()

    positive_count = 0
    negative_count = 0

    for word in positive_words:
        if word in text:
            positive_count += 1

    for word in negative_words:
        if word in text:
            negative_count += 1

    if positive_count > negative_count:
        return "Positive 😊"
    elif negative_count > positive_count:
        return "Negative 😟"
    else:
        return "Neutral 😐"
def display_movie(movie):

    print("\n------------------------------")
    print("       MOVIE RECOMMENDATION")
    print("------------------------------")

    print("Title:", movie["title"])
    print("Genre:", movie["genre"])
    print("IMDb Rating:", movie["rating"], "/ 10")
    print("Mood:", movie["mood"])
    print("Overview:", movie["overview"])

    sentiment = analyse_sentiment(movie["overview"])
    print("Overview Sentiment:", sentiment)

    print("------------------------------")


def random_recommendation():

    movie = random.choice(movies)
    print("\nHere is a random movie for you!")
    display_movie(movie)


def recommend_by_genre():

    print("\nAvailable genres:")
    print("Animation, Adventure, Fantasy, Comedy")

    genre = input("Enter your favourite genre: ").strip().lower()

    matching_movies = []

    for movie in movies:
        if movie["genre"].lower() == genre:
            matching_movies.append(movie)

    if matching_movies:
        print("\nMovies matching your genre:")
        for movie in matching_movies:
            display_movie(movie)
    else:
        print("Sorry, no movies found for that genre.")


def recommend_by_mood():

    print("\nAvailable moods:")
    print("Happy, Exciting, Emotional")

    mood = input("How do you feel today? ").strip().lower()

    matching_movies = []

    for movie in movies:
        if movie["mood"].lower() == mood:
            matching_movies.append(movie)

    if matching_movies:
        print("\nMovies matching your mood:")
        for movie in matching_movies:
            display_movie(movie)
    else:
        print("Sorry, no movies found for that mood.")

def recommend_by_rating():

    try:
        minimum_rating = float(
            input("Enter the minimum IMDb rating (0 to 10): ")
        )

        if minimum_rating < 0 or minimum_rating > 10:
            print("Please enter a rating between 0 and 10.")
            return

        matching_movies = []

        for movie in movies:
            if movie["rating"] >= minimum_rating:
                matching_movies.append(movie)

        if matching_movies:
            print("\nMovies with your chosen rating:")
            for movie in matching_movies:
                display_movie(movie)
        else:
            print("No movies found with that rating.")

    except ValueError:
        print("Please enter a valid number.")

def main():

    print("==============================")
    print(" AI MOVIE RECOMMENDATION SYSTEM")
    print("==============================")

    while True:

        print("\nWhat would you like to do?")
        print("1. Get a random movie")
        print("2. Choose movies by genre")
        print("3. Choose movies by mood")
        print("4. Choose movies by IMDb rating")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            random_recommendation()

        elif choice == "2":
            recommend_by_genre()

        elif choice == "3":
            recommend_by_mood()

        elif choice == "4":
            recommend_by_rating()

        elif choice == "5":
            print("\nThank you for using the Movie Recommendation System!")
            print("Enjoy watching your next movie! 🎬")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()