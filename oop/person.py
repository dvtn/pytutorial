class Person:
    """
    人 类型
    """
    people = []

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Person.people.append(self)

    def say(self, word):
        print(f"{self.name}在说:{word}")

    @classmethod
    def show(cls):
        for name in cls.people:
            print(name)

    @staticmethod
    def do_something(self):
        print("Performing some testing...")

    def __str__(self):
        return '['+self.name+','+str(self.age)+','+self.gender+']'


def main():
    p = Person("风清扬", 80, '男')
    print(p.name)
    print(p.age)
    print(p.gender)
    p.say("您好")
    print("-" * 50)
    p1 = Person('独孤求败', 100, '男')
    print(p1.name)
    print(p1.age)
    print(p1.gender)
    p1.say("我武功很好")

    Person.show()




if __name__ == '__main__':
    main()
