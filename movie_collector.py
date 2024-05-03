# where to store data              - movies are stored in a list
# what information details a movie - title; year; director; genre
# how to store movie info          - dictionary, where the title is the key (?)
# show the user menu               - get users input; run a loop and get input
#                                    again at the end

movie_list = []

MENU_PROMPT = """
Enter following commands:
'a' - add a movie to the list
'l' - show all movies in the list
'f' - find a movie by it's property
'q' - quit program
: """

movie_list.append({
    "title": "Transformers",
    "year": "2001",
    "director": "Rolf",
    "genre": "horror"
})
movie_list.append({
    "title": "Power Rangers",
    "year": "2010",
    "director": "Bob",
    "genre": "happy"
})
movie_list.append({
    "title": "Cars",
    "year": "1998",
    "director": "Anne",
    "genre": "motocycles"
})


def add_movie():
    print("Enter the following information about the movie:")
    title = input("title: ")
    year = input("year: ")
    director = input("director: ")
    genre = input("genre: ")
    movie_list.append({
        "title": title.title(),
        "year": year,
        "director": director.title(),
        "genre": genre.title()
    })


def list_movies():
    for movie in movie_list:
        print("--------------------")
        print_movie(movie)
        print("--------------------")


def print_movie(movie):
    title = '"' + movie['title'] + '"'
    print(title)
    print(f"\tYear: {movie['year']}")
    print(f"\tDirector: {movie['director']}")
    print(f"\tGenre: {movie['genre']}")


def find_movies():
    find_by = input("What property? ('title', 'year', 'director', 'genre'): ")
    if find_by not in movie_list[0]:
        print("unknown movie property, try again")
        return
    looking_for = input(f"What {find_by} are you searching for?: ")

    found_movies = find_by_attribute(
            movie_list,
            looking_for.lower(),
            lambda x: x[find_by].lower()
    )

    if len(found_movies) == 0:
        print("No movies meet these criteria")
    else:
        for movie in found_movies:
            print_movie(movie)


def find_by_attribute(items, expected, finder):
    found = []

    for i in items:
        if expected == finder(i):
            found.append(i)

    return found


user_options = {
        "a": add_movie,
        "l": list_movies,
        "f": find_movies
}


def menu():
    user_option = input(MENU_PROMPT)
    while user_option != 'q':
        if user_option in user_options:
            selected_function = user_options[user_option]
            selected_function()
        else:
            print("invalid command, try again")
        user_option = input(": ")


menu()
