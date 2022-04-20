class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

    def main():
        p1 = Person("john")
        p1.say_hi()


if __name__ == '__main__':
    Person.main()
