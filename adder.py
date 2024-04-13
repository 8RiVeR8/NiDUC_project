from operand import Operand


# klasa odpowiedzialna za dodawanie

class Add:
    def __init__(self):
        self.number_x = Operand()
        self.number_y = Operand()
        self.modulo = Operand()
        self.result = Operand()

    def get_result(self):
        # Wywołanie metody do dodawania
        result = self.binary_addition(self.number_x._char_list, self.number_y._char_list)
        return result

    def get_result_modulo(self):
        # Wywołanie metody do dodawania
        result_modulo = self.modulo_binary_addition(self.number_x._char_list, self.number_y._char_list, self.modulo._modulo_number)
        return result_modulo

    def binary_addition(self, number_x, number_y):
        # Dodawanie w systemie binarnym
        max_length = max(len(number_x), len(number_y))

        bin_x = ''.join(number_x).zfill(max_length)
        bin_y = ''.join(number_y).zfill(max_length)

        carry = 0
        wynik = ''

        for i in range(max_length - 1, -1, -1):
            suma = int(bin_x[i]) + int(bin_y[i]) + carry
            carry = self.carry_check(bin_x, bin_y, i, carry)
            wynik = str(suma % 2) + wynik

        if carry:
            wynik = '1' + wynik

        return wynik

    def carry_check(self, number_x, number_y, position, c):
        if int(number_x[position]) + int(number_y[position]) + c >= 2:
            carry = 1
        else:
            carry = 0
        return carry
        pass

    def modulo_binary_addition(self, number_x, number_y, modulo_value):
        max_length = max(len(number_x), len(number_y))

        bin_x = ''.join(number_x).zfill(max_length)
        bin_y = ''.join(number_y).zfill(max_length)
        carry = 0
        wynik = ''

        dec_x = int(bin_x, 2)
        dec_y = int(bin_y, 2)

        dec_x = dec_x % modulo_value
        dec_y = dec_y % modulo_value

        bin_x_modulo = bin(dec_x)[2:].zfill(max_length)
        bin_y_modulo = bin(dec_y)[2:].zfill(max_length)

        for i in range(max_length - 1, -1, -1):
            suma = int(bin_x_modulo[i]) + int(bin_y_modulo[i]) + carry
            carry = self.carry_check(bin_x_modulo, bin_y_modulo, i, carry)
            wynik = str(suma % 2) + wynik

        if carry:
            wynik = '1' + wynik

        return wynik

    def overflow_check(self, number_a, number_b):
        # Sprawdzanie przepełnienia
        pass


