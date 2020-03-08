import datetime


class Employee:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def say(self, word):
        print(f'{self.name}在说：{word}')

    def __str__(self):
        return '[' + self.name + ',' + str(self.birthday) + ']'

    @property
    def age(self):
        return datetime.date.today().year - self.birthday.year


def main():
    e = Employee("李世民", datetime.date(1990, 3, 3))
    print(e.birthday)
    print(e)
    e.say('Hello')
    print(f'{e.name}的年龄是:{e.age}岁')


if __name__ == '__main__':
    main()
