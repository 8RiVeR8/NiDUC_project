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

    def get_modulo(self):
        return self.modulo._modulo_number

    def error_check(self, result, result_modulo):
        if result == result_modulo:
            print("Nie wykryto błędu")
        else:
            print("Błąd został wykryty")

    #dla |X| + |Y|
    def result_after_modulo_second(self, result):
        result = int(result, 2)
        result = result % self.modulo._modulo_number
        result = bin(result)[2:]
        return result

    # dla X+Y
    def result_after_modulo(self, result):
        result = int(result, 2)
        result = result % self.modulo._modulo_number
        result = bin(result)[2:]
        return result

    def get_error_variable(self):
        print("Czy chcesz wygenerować błąd? -> (t/n): ")
        error = input()
        error_variable = None
        if str.upper(error) == 'T':
            while error_variable not in range(1, 3):
                print("1. Liczba X")
                print("2. Liczba Y")
                print("Podaj dla jakiej liczby chcesz wprowadzić błąd:")
                error_variable = int(input())
                if error_variable not in range(1, 3):
                    print("Podano niewłaściwy numer. Spróbuj ponownie")
        return error_variable

    def get_error_result(self, wynik):
        print("Czy chcesz wygenerować błąd dla wyniku? -> (t/n): ")
        error = input()
        if str.upper(error) == 'T':
            print("Chcesz zmienić całą liczbę (1) czy tylko pojedynczy bit (2)? -> (1/2):  ")
            choice = int(input())
            wynik = self.error_change(wynik, choice)
        return wynik


    def error_change(self, bin, choice):
        if choice == 1:  # Zmiana całej liczby
            print("Podaj nową liczbę binarną:")
            new_bin = input()  # Pobranie nowej liczby
            if len(new_bin) <= len(bin):
                bin = new_bin.zfill(len(bin))  # Dopisanie zer na początku, jeśli nowa liczba jest krótsza
            else:
                print("Nowa liczba jest dłuższa niż oryginalna. Wprowadź liczbę ponownie.")

        elif choice == 2:  # Zmiana pojedynczego bitu
            for i in range(0, len(bin)):
                print(i, end="")
            print(" <- indeksy a pod nimi liczba")
            print(bin)
            print("Podaj pozycję bitu do zmiany (0 - {}):".format(len(bin) - 1))
            position = int(input())
            if 0 <= position < len(bin):  # Sprawdzenie czy pozycja jest prawidłowa
                bin_list = list(bin)  # Konwersja na listę, aby można było zmienić pojedynczy bit
                bin_list[position] = '0' if bin_list[position] == '1' else '1'  # Negacja bitu
                bin = ''.join(bin_list)  # Ponowne połączenie listy w ciąg znaków
            else:
                print("Podano nieprawidłową pozycję bitu.")


        return bin

    def generate_error(self, bin):
        print("Chcesz zmienić całą liczbę (1) czy tylko pojedynczy bit (2)? -> (1/2):  ")
        choice = int(input())
        bin = self.error_change(bin, choice)
        return bin

    def binary_addition(self, number_x, number_y):
        # Dodawanie w systemie binarnym
        max_length = max(len(number_x), len(number_y))

        bin_x = ''.join(number_x).zfill(max_length)
        bin_y = ''.join(number_y).zfill(max_length)

        carry = 0
        wynik = ''
        again = 'T'

        while again == 'T':
            error_variable = self.get_error_variable()
            if error_variable == 1:
                bin_x = self.generate_error(bin_x)
            elif error_variable == 2:
                bin_y = self.generate_error(bin_y)
            print("Czy chcesz wprowadzić błąd ponownie? -> (T/N): ")
            again = input().upper()


        for i in range(max_length - 1, -1, -1):
            suma = int(bin_x[i]) + int(bin_y[i]) + carry
            carry = self.carry_check(bin_x, bin_y, i, carry)
            wynik = str(suma % 2) + wynik

        if carry:
            wynik = '1' + wynik

        wynik = self.get_error_result(wynik)

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


