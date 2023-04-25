class Soda:
    def __init__(self, ing=None):
        self.ing = ing

    def show_my_drink(self):

        if self.ing:
            print('Добавка ' + self.ing)
        else:
            print('обычная газировка')

drink1 = Soda()
drink2 = Soda('cherry')
drink1.show_my_drink()
drink2.show_my_drink()








