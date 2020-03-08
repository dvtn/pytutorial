import datetime


class Person:
    def __init__(self, name, gender, birthday, email):
        self.name = name,
        self.gender = gender
        self.birthday = birthday
        self.email = email

    @property
    def age(self):
        return datetime.datetime.now().year - self.birthday.year


class Publisher:
    def __init__(self, name, address, email, telephone):
        self.name = name,
        self.address = address,
        self.email = email,
        self.telephone = telephone


class Editor(Person):
    def __init__(self, name, gender, birthday, email, publisher, qq):
        Person.__init__(self, name, gender, birthday, email)
        self.publisher = publisher
        self.qq = qq


class Author(Person):
    def __init__(self, name, gender, birthday, email, expertise):
        Person.__init__(self, name, gender, birthday, email)
        self.expertise = expertise

    def __str__(self):
        return f"[{self.name}, {self.email}, {self.expertise}]"


class Book:
    def __init__(self, title, isbn, author, editor, price, publisher):
        self.title = title
        self.isbn = isbn
        self.author = author
        self.editor = editor
        self.price = price
        self.publisher = publisher

    def __str__(self):
        return self.title

    def __add__(self, other):
        return self.price + other.price


def main():
    publisher = Publisher('人民邮电出版社', '北京市海淀区', 'people.publisher@china.cn', '010-83597766')
    author = Author('独孤求败', '男', datetime.date(1984, 8, 12), 'duguqiubai@wuxia.cn', '写作')
    editor = Editor('风清扬', '男', datetime.date(1988, 9, 11), 'fengqinyang@wuxia.cn', '人民教育出版社', '88888888')

    book = Book('论中华武术的崛起', 'BJYD0000120200305001', author, editor, 99.9, publisher)

    print(book.author.age)


if __name__ == '__main__':
    main()
