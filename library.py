class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append({"name": book, "issued": False})
        print("Book added successfully.")

    def remove_book(self, book):
        for item in self.books:
            if item["name"] == book:
                self.books.remove(item)
                print("Book removed successfully.")
                return

        print("Book not found.")

    def issue_book(self, book):
        for item in self.books:
            if item["name"] == book:
                if not item["issued"]:
                    item["issued"] = True
                    print("Book issued successfully.")
                else:
                    print("Book is already issued.")
                return

        print("Book not found.")

    def return_book(self, book):
        for item in self.books:
            if item["name"] == book:
                if item["issued"]:
                    item["issued"] = False
                    print("Book returned successfully.")
                else:
                    print("Book was not issued.")
                return

        print("Book not found.")

    def display_books(self):
        print("\nLibrary Books:")
        for item in self.books:
            status = "Issued" if item["issued"] else "Available"
            print(item["name"], "-", status)


# Create library object
library = Library()

# Add books
library.add_book("Python Programming")
library.add_book("Data Science")
library.add_book("Machine Learning")

# Display books
library.display_books()

# Issue a book
library.issue_book("Python Programming")

# Display books
library.display_books()

# Return the book
library.return_book("Python Programming")

# Display books
library.display_books()

# Remove a book
library.remove_book("Data Science")

# Display final books
library.display_books()