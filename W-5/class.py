# Base class
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        print(f"Reading '{self.title}' by {self.author}...")

    def get_summary(self):
        return f"'{self.title}' is written by {self.author} and has {self.pages} pages."


# Subclass with inheritance and encapsulation
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)  # Inherit from Book
        self.__file_size = file_size  # Encapsulated attribute

    def read(self):
        print(f"Opening the eBook '{self.title}' on your device...")

    def get_file_size(self):
        return f"The file size is {self.__file_size}MB"

    def download(self):
        print(f"Downloading '{self.title}'...")


# Testing the classes
physical_book = Book("The Alchemist", "Paulo Coelho", 208)
ebook = EBook("Digital Fortress", "Dan Brown", 384, 2.5)

physical_book.read()
print(physical_book.get_summary())

print()

ebook.read()
print(ebook.get_summary())
print(ebook.get_file_size())
ebook.download()