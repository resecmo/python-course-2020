class Library:
    def __init__(self, name, books=[]):
        self.name = name
        self.books = books
        self.books_by_author = {}
        for book in books:
            if book.author in self.books_by_author:
                self.books_by_author[book.author].append(book)
            else:
                self.books_by_author[book.author] = [book]

    def add_book(self, book):
        self.books.append(book)
        if book.author in self.books_by_author:
            self.books_by_author[book.author] += [book]
        else:
            self.books_by_author[book.author] = [book]

    def search_by_author(self, author):
        if author not in self.books_by_author:
            return None
        return self.books_by_author[author]

    def tell_info(self, book_title):
        for book in self.books:
            if book.title == book_title:
                return f"Title: {book.title}\nAuthor: {book.author}\nPublication date: {book.publication_date}\nISBN: {book.ISBN}\n"
        return f"No such book in {self.name}!\n"

    def delete_book(self, book):
        if book not in self.books:
            raise ValueError(f"No such book in {self.name}!\n")
        self.books.remove(book)
        self.books_by_author[book.author].remove(book)
        if len(self.books_by_author[book.author]) == 0:
            del self.books_by_author[book.author]


"""Далее надо найти и удалить все книги Толстого из 
библиотеки. Проверить, что в библиотеке в самом деле не осталось книг Толстого"""


class Book:
    def __init__(self, title, author, publication_date=None, ISBN=None):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.ISBN = ISBN


def test_library():
    library = Library("Lenin library", [Book("War and Peace", "L. Tolstoy", ISBN=4823991238419),
                                        Book("Anna Karenina", "L. Tolstoy", ISBN=4987293759244)])
    book1 = Book("kniga", "afftar")
    book2 = Book("Algebra Course", "E. Vinberg", publication_date="Februember 1960", ISBN=4823)
    library.add_book(book1)
    library.add_book(book2)

    by_tolstoy = library.search_by_author("L. Tolstoy")
    for book in by_tolstoy:
        print(library.tell_info(book.title))
    while len(by_tolstoy) > 0:
        library.delete_book(by_tolstoy[0])
    for book in library.books:
        print(library.tell_info(book.title))


if __name__ == '__main__':
    test_library()
