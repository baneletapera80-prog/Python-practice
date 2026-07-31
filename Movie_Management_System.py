movie = []

def add_movie():
    title = input("Enter movie title: ")
    director = input("Enter movie director: ")
    release_year = input("Enter movie release year: ")
    genre = input("Enter movie genre: ")
    movie.append({"title": title, "director": director, "release_year": release_year, "genre": genre})
    print("Movie added successfully.")

def view_movies():
    if not movie:
        print("No movies found.")
        return
    print("\nMovie List:")
    for index, m in enumerate(movie, start=1):
        print(f"{index}. {m['title']} (Director: {m['director']}, Year: {m['release_year']}, Genre: {m['genre']})")

def update_movie():
    if not movie:
        print("No movies to update.")
        return
    view_movies()
    index = input("Enter the number of the movie to update: ")
    if not index.isdigit() or int(index) < 1 or int(index) > len(movie):
        print("Invalid selection.")
        return
    index = int(index) - 1
    title = input("Enter new title: ")
    director = input("Enter new director: ")
    release_year = input("Enter new release year: ")
    genre = input("Enter new genre: ")
    movie[index] = {"title": title, "director": director, "release_year": release_year, "genre": genre}
    print("Movie updated successfully.")

def delete_movie():
    if not movie:
        print("No movies to delete.")
        return
    view_movies()
    index = input("Enter the number of the movie to delete: ")
    if not index.isdigit() or int(index) < 1 or int(index) > len(movie):
        print("Invalid selection.")
        return
    index = int(index) - 1
    movie.pop(index)
    print("Movie deleted successfully.")

def search_movie():
    query = input("Enter movie title or director to search: ")
    found = [m for m in movie if query.lower() in m['title'].lower() or query.lower() in m['director'].lower()]
    if not found:
        print("No matching movies found.")
        return
    print("\nSearch Results:")
    for index, m in enumerate(found, start=1):
        print(f"{index}. {m['title']} (Director: {m['director']}, Year: {m['release_year']}, Genre: {m['genre']})")

def main():
    while True:
        print("\nMovie Management System")
        print("1. Add Movie")
        print("2. View Movies")
        print("3. Update Movie")
        print("4. Delete Movie")
        print("5. Search Movie")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_movie()
        elif choice == '2':
            view_movies()
        elif choice == '3':
            update_movie()
        elif choice == '4':
            delete_movie()
        elif choice == '5':
            search_movie()
        elif choice == '6':
            print("Enjoy your day!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()