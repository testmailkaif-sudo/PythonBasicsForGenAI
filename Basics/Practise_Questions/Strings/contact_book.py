'''Build a simple contact book with these functions:

add_contact(book, name, phone) → adds contact, name stored in title case
search_contact(book, name) → searches case-insensitively, prints contact or "Not found"
show_all(book) → prints all contacts sorted alphabetically'''
book = {}
def add_contact(book, name, phone):
    """Adds a contact with the name stored in Title Case."""
    book[name.title()] = phone


def search_contact(book, name):
    """Searches for a contact case‑insensitively and prints the result."""
    name = name.lower()
    for stored_name, phone in book.items():
        if stored_name.lower() == name:
            print(f"{stored_name}: {phone}")
            return
    print("Not found")


def show_all(book):
    """Prints all contacts sorted alphabetically by name."""
    for name in sorted(book):
        print(f"{name}: {book[name]}")
add_contact(book, "kaif","798148")
search_contact(book, "kaif1")
show_all(book)