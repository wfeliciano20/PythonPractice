MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


def add_movie():
    title = input('Enter the movie title: ')
    director = input('Enter the movie director: ')
    year = input('Enter the movie release year: ')

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


def list_movies():
    for movie in movies:
        print_movie(movie)


def print_movie(movie):
    print('Title: ' + movie['title'])
    print('Director: ' + movie['director'])
    print('Release Year: ' + movie['year'])


def find_movie():
    searched_movie = input('What movie do you want?')
    found = False
    for movie in movies:
        if movie['title'] == searched_movie:
            return movie
            found = True
    if not found:
        return 'That movie is not in your collection'


def menu():
    selection = input(MENU_PROMPT)
    print(selection)
    while selection != 'q':
        if selection == 'a':
            add_movie()
        elif selection == 'l':
            list_movies()
        elif selection == 'f':
            result = find_movie()
            if isinstance(result, dict):
                print_movie(result)
            else:
                print(result)
        else:
            print('Enter a valid option.')

        selection = input(MENU_PROMPT)


menu()
