# C:/Users/Щетинин Д Б/Documents/GitHub/lessone4.2/main10.py
# В этом фрагменте кода определены два класса: Author и Book.
# Класс Author имеет метод __init__, который принимает в качестве параметров имя и национальность
# и присваивает их переменным экземпляра self.name и self.nationality, соответственно.
# Класс Book также имеет метод __init__, который принимает в качестве параметров title и author
# и присваивает их переменным экземпляра self.title и self.author, соответственно.
# Класс Book также имеет метод get_info_book, который выводит название, имя и национальность книги.
# В фрагменте кода создается экземпляр класса Author с именем 'George R. R. Martin'
# и национальностью 'American'. Затем создается экземпляр класса Book с названием 'Игра Престолов'
# и ранее созданным экземпляром Author в качестве автора.
# На экземпляре Book вызывается метод get_info_book, который выводит название, имя и национальность книги.
# Наконец, имя и национальность автора и название книги выводятся отдельно.
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
