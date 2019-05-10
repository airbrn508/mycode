#!/usr/bin/python3

class Dog:
    def __init__(self, name, age):
        self.n = name
        self.a = age
        return

    def __str__(self):
        return 'Name: ' + self.n + ' Age: ' + str(self.a)

    def aged(self, yearsolder):
        self.a = self.a + yearsolder
        return


class JackRussell(Dog):
    def __init__(self, name, age, isWirehair, isHunter):
        Dog.__init__(self, name, age)
        self.wh = isWirehair
        self.h = isHunter
        return

    def __str__(self):
        retStr = Dog.__str__(self)
        retStr += ' Wirehaired: ' + str(self.wh) + ' Trained to hunter: ' + str(self.h)
        return retStr


def main():
    muttley = Dog("Fido", 3)
    print(muttley)

    muttley.aged(1)
    print(muttley)

    eddie = JackRussell('Eddie', 4, False, True)
    print(eddie)

    eddie.aged(3)
    print(eddie)
    return


if __name__ == '__main__':
    main()

