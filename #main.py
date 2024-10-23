#main.py

class Book:
    # Constructor for the Book class
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre
        self.read = False  # Defaults to False when the book is created.
        self.purchase_count = 0  # Tracks how many times the book has been purchased.

    # Returns a string description of the book's details.
    def description(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, Genre: {self.genre}"

    # Marks the book as read and prints a confirmation.
    def mark_as_read(self):
        self.read = True
        print(f'You have marked "{self.title}" as read!')

class EbookReader:
    # Constructor for EbookReader class to manage catalog and library
    def __init__(self):
        self.catalog = []  # List of all available books
        self.library = []  # List of books purchased by the user

    # Adds a book to the catalog.
    def add_to_catalog(self, book):
        self.catalog.append(book)

    # Displays all books in the catalog with purchase counts.
    def view_catalog(self):
        for i, book in enumerate(self.catalog, start=1):
            print(f"{i}. {book.description()} - Purchased {book.purchase_count} times")

    # Displays all available genres in the catalog
    def display_genres(self):
        genres = {book.genre for book in self.catalog}  # Uses a set to avoid duplicates
        print("Available genres:", ", ".join(genres))

    # Filters and displays books by the selected genre
    def filter_by_genre(self, genre):
        filtered_books = [book for book in self.catalog if book.genre == genre]
        if filtered_books:
            for book in filtered_books:
                print(book.description())
        else:
            print(f"No books found for the genre: {genre}")

    # Allows users to buy a book from the catalog
    def buy_book(self, book_number):
        if 0 < book_number <= len(self.catalog):  # Ensures the input is valid
            book = self.catalog[book_number - 1]  # Adjusts for zero-based index
            if book not in self.library:  # Checks if the book is already purchased
                self.library.append(book)
                book.purchase_count += 1  # Increments purchase count
                print(f'You have purchased "{book.title}"!')
            else:
                print(f'You already own "{book.title}".')

    # Displays all books in the user's library and their read status
    def view_library(self):
        for i, book in enumerate(self.library, start=1):
            print(f"{i}. {book.description()}, Read: {'Yes' if book.read else 'No'}")

    # Marks a book in the library as read
    def read_book(self, book_number):
        if 0 < book_number <= len(self.library):  # Ensures valid input
            book = self.library[book_number - 1]
            if not book.read:  # Only marks the book as read if it hasn't been read
                book.mark_as_read()

    # Displays the top 3 most purchased books
    def top_purchased_books(self):
        top_books = sorted(self.catalog, key=lambda b: b.purchase_count, reverse=True)[:3]
        for book in top_books:
            print(f"{book.title} - Purchased {book.purchase_count} times")

    # Performs a linear search for books by the specified author
    def search_by_author(self, author_name):
        found_books = [book for book in self.catalog if book.author.lower() == author_name.lower()]
        if found_books:
            print(f"Books by {author_name}:")
            for book in found_books:
                print(book.description())
        else:
            print(f"No books found by {author_name}.")

    # Performs a binary search for a book by title after sorting the catalog by title
    def search_by_title(self, title):
        sorted_books = sorted(self.catalog, key=lambda b: b.title)  # Sorts books by title
        low, high = 0, len(sorted_books) - 1
        while low <= high:
            mid = (low + high) // 2
            if sorted_books[mid].title.lower() == title.lower():
                print(f"Book found: {sorted_books[mid].description()}")
                return
            elif sorted_books[mid].title.lower() < title.lower():
                low = mid + 1
            else:
                high = mid - 1
        print(f"No book found with the title: {title}")

    # Saves the list of purchased books to a file
    def save_purchases(self, file_name):
        with open(file_name, "w") as file:
            for book in self.library:
                file.write(f"{book.title},{book.author},{book.pages},{book.genre}\n")
        print("Purchases saved!")

    # Loads the list of purchased books from a file
    def load_purchases(self, file_name):
        try:
            with open(file_name, "r") as file:
                for line in file:
                    title, author, pages, genre = line.strip().split(',')
                    book = Book(title, author, int(pages), genre)
                    self.library.append(book)  # Adds the books back to the library
            print("Purchases loaded!")
        except FileNotFoundError:
            print("No saved purchases found.")

def main():
    reader = EbookReader()

    # Adds books to the catalog
    reader.add_to_catalog(Book("Moby Dick", "Herman Melville", 635, "Adventure"))
    reader.add_to_catalog(Book("Sherlock Holmes", "Arthur Conan Doyle", 307, "Mystery"))
    reader.add_to_catalog(Book("Dracula", "Bram Stoker", 418, "Horror"))
    reader.add_to_catalog(Book("Pride and Prejudice", "Jane Austen", 279, "Romance"))

    # Main menu loop
    while True:
        print("\n1. View Catalog\n2. Buy a Book\n3. View Library\n4. Read a Book\n5. Search by Author")
        print("6. Search by Title\n7. Display Genres\n8. Filter by Genre\n9. Top Purchased Books\n10. Save Purchases\n11. Load Purchases\n12. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            reader.view_catalog()
        elif choice == '2':
            reader.view_catalog()
            try:
                book_number = int(input("Enter the number of the book you want to purchase: "))
                reader.buy_book(book_number)
            except ValueError:
                print("Invalid input. Enter a number.")
        elif choice == '3':
            reader.view_library()
        elif choice == '4':
            reader.view_library()
            try:
                book_number = int(input("Enter the number of the book you want to read: "))
                reader.read_book(book_number)
            except ValueError:
                print("Invalid input. Enter a number.")
        elif choice == '5':
            author = input("Enter the author's name: ")
            reader.search_by_author(author)
        elif choice == '6':
            title = input("Enter the title of the book: ")
            reader.search_by_title(title)
        elif choice == '7':
            reader.display_genres()
        elif choice == '8':
            genre = input("Enter the genre: ")
            reader.filter_by_genre(genre)
        elif choice == '9':
            reader.top_purchased_books()
        elif choice == '10':
            file_name = input("Enter the file name to save purchases: ")
            reader.save_purchases(file_name)
        elif choice == '11':
            file_name = input("Enter the file name to load purchases: ")
            reader.load_purchases(file_name)
        elif choice == '12':
            break

# calls the main function to execute the program.
main()
