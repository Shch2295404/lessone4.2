class Author():
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality


class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info_book(self):
        print(self.title, self.author.name, self.author.nationality)


author = Author('George R. R. Martin', 'American')
book = Book('Игра Престолов', author)
book.get_info_book()

print(author.name, author.nationality, book.title)
# George R. R. Martin American Игра Престолов
