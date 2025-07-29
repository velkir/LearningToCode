import json


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'{self.title} by {self.author}.'

    def __eq__(self, other):
        return self.author == other.author and self.title == other.title

    def __hash__(self):
        return hash((self.author, self.title))

    def _serialize(self):
        return {"title": self.title, "author": self.author}


class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self, book: Book):
        if book not in self.book_list:
            self.book_list.append(book)
            return f"{book.title} by {book.author} has been added to the library."
        else:
            return f"{book.title} by {book.author} is already in the library."

    def delete_book(self, title, author):
        book_deleted = False
        for book in self.book_list:
            if hash((author, title)) == hash(book):
                self.book_list.remove(book)
                book_deleted = True
                break
        if book_deleted:
            return f"{title} by {author} has been deleted from the library."
        else:
            return f"{title} by {author} hasn't been deleted from the library. Please double check the author and the title."

    def find_book(self, title, author):
        for book in self.book_list:
            if hash((author, title)) == hash(book):
                return f'{title} by {author} has been found in the library.'
        return f'{title} by {author} hasn\'t been found in the library.'

    def save_library_to_json(self, json_path="library.json"):
        serialized_library = self._serialize()
        json_str = json.dumps(serialized_library)
        try:
            with open(json_path, "w") as f:
                f.write(json_str)
                return f'A library was successfully saved to {json_path} file.'
        except FileNotFoundError:
            return "Please provide a correct json path to save a file."

    def load_library_from_json(self, json_path="library.json"):
        try:
            with open(json_path, "r") as f:
                s = json.load(f)
                self.book_list = self._deserialize(s)
                return f'A library was successfully loaded from {json_path} file.'
        except FileNotFoundError:
            return "Please provide a correct json path to load library."

    def _serialize(self):
        try:
            return [book._serialize() for book in self.book_list]
        except ValueError:
            return 'Couldn\'t serialize a library.'

    def _deserialize(self, s):
        try:
            return [Book(book["title"], book["author"]) for book in list(s)]
        except ValueError:
            return 'Couldn\'t deserialize a string to a library.'

    def __str__(self):
        return "Library:\n"+"\n".join([f"{idx+1}."+str(book) for idx, book in enumerate(self.book_list)])

library = Library()
book1 = Book(title="Catch me if you can",
             author="Frank Abagnale")
book2 = Book(title="Naruto",
             author="Masashi Kishimoto")
book3 = Book(title="Atomic Habits",
             author="James Clear")

print(library.add_book(book1))
print(library.add_book(book2))
print(library.add_book(book3))
print(str(library))
library.save_library_to_json()
# library.delete_book("Naruto", "Masashi Kishimoto")
# library.load_library_from_json()
# print(str(library))
