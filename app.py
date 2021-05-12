from utils import database

USER_CHOICE = """
ENTER:
- 'a' to add a new book
- 's' to show all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """


# ask for book name and author
def prompt_add_book():
    book_name = input("Enter book name: ").strip().title()
    book_author = input("Enter book author: ").strip().title()

    database.add_book(book_name, book_author)


# show all the books in our list
def show_books():
    books = database.get_all_books()
    for book in books:
        read = "YES" if book["read"] else "NO"
        print(f"{book['name']} by {book['author']}, read: {read}")


# ask for book name and change it to "read" in our list
def prompt_read_book():
    read_book_name = input("Enter the name of the book you just finished reading: ").strip().title()

    database.mark_book_as_read(read_book_name)


# ask for book name and remove book from list
def prompt_delete_book():
    book_name_removal = input("Enter the name of the book that would like to remove: ").strip().title()

    database.delete_book(book_name_removal)


choices = {
    "a": prompt_add_book,
    "s": show_books,
    "r": prompt_read_book,
    "d": prompt_delete_book
}


def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != "q":
        if user_input in choices:
            selected_choice = choices[user_input]
            selected_choice()
        else:
            print("ERROR unknown command. Please try again.")

        user_input = input(USER_CHOICE)


menu()
