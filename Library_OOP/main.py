class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'{self.title} by {self.author}.'

class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self, book: Book):
        if book not in self.book_list:
            self.book_list.append(book)
            print(f"{book.title} by {book.author} has been added from the library.")
        else:
            print("The book is already in the library.")

    def delete_book(self, title, author):
        book_deleted = False
        for book in self.book_list:
            if book.title == title and book.author == author:
                self.book_list.remove(book)
                book_deleted = True
                break
        if book_deleted:
            print(f"{title} by {author} has been deleted from the library.")
        else:
            print(f"{title} by {author} hasn't been deleted from the library. Please double check the author and the title.")

    def __str__(self):
        books_str = "Library:\n"
        for idx, book in enumerate(self.book_list):
            books_str += f"{idx+1}."+book.__str__()+"\n"
        return books_str

library = Library()
book1 = Book(title="Catch me if you can",
             author="Frank Abagnale")
book2 = Book(title="Naruto",
             author="Masashi Kishimoto")
book3 = Book(title="Atomic Habits",
             author="James Clear")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
print(library.__str__())
library.delete_book("Naruto", "Masashi Kishimoto")
print(library.__str__())