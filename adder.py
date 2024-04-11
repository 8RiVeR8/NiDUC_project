from operand import Operand


# klasa odpowiedzialna za dodawanie

class Add:
    def __init__(self):
        self.number_a = Operand()
        self.number_b = Operand()
        self.result = Operand()

    def add(self, number_a, number_b):
        # Wywołanie metody do dodawania
        self.binary_addition(number_a, number_b)

    def binary_addition(self, number_a, number_b):
        # Dodawanie w systemie binarnym
        self.carry_check(number_a, number_b)
        self.overflow_check(number_a, number_b)

    def carry_check(self, number_a, number_b):
        # Sprawdzanie przeniesienia
        pass

    def overflow_check(self, number_a, number_b):
        # Sprawdzanie przepełnienia
        pass

    def get_result(self):
        # Zwracanie wyniku
        pass
