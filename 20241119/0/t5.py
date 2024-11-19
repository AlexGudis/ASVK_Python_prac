class Sender:
    c = False
    @classmethod
    def report(*args):
        if not Sender.c:
            print("Greetings!")
        else:
            print("Get away!")
        Sender.c = True


class Asker:
    @staticmethod
    def askall(lst):
        for el in lst:
            el.report()


check = [Sender(), Sender(), Sender()]
a = Asker()

a.askall(check)

        