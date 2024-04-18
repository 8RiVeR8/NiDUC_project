from operand import Operand


class Multiplier:
    from operand import Operand

    # klasa odpowiedzialna za mnozenie

    def __init__(self):
        self.number_x = Operand()
        self.number_y = Operand()
        self.result = Operand()
        self.modulo = Operand()

    def binary_multiply(self, number_x, number_y):
        # Wywołanie metody do dodawania
        bin_x = number_x
        bin_y = number_y

        # Inicjalizacja listy iloczynów częściowych
        partial_products = []

        for i, bitX in enumerate(bin_x[::-1]):
            partial_product = ""
            carry = 0

            for j, bitY in enumerate(bin_y[::-1]):
                # print(int(bitX), int(bitY))
                product = int(bitX) * int(bitY) + carry
                # print(str(product % 2))
                partial_product += str(product % 2)
                carry = product // 2

            #partial_product += str(carry)
            partial_product = partial_product[::-1]
            partial_product += "0" * i
            # partial_product = partial_product[::-1]
            partial_products.append(partial_product)

        # for partial_product in partial_products:
        #     print(partial_product, "partial product binarny -> ", int(partial_product, 2))

        # result = sum(int(partial, 2) for partial in partial_products)

        # print(result, "Wynik niby")

        return partial_products

    def get_error(self, partial_products):
        # Znajdź najdłuższy wiersz
        max_length = max(len(row) for row in partial_products)

        for i in range(max_length):
            print(i, end="")
        print(" <- numery kolumn")

        # Wyświetlenie tablicy dwuwymiarowej
        for partial_product in partial_products:
            print(partial_product)


        # WAŻNE jeśli nie chcę brać pod uwagę różnych długości ciągu !!!!
        # Sprawdzić jak działą to na bramkach logicznych!
        # for j in range(len(partial_products[0])):  # Iteracja po kolumnach
        #     for i in range(len(partial_products)):  # Iteracja po wierszach
        #         print(partial_products[i][j])
        #     print("----------------------")

        print("Wybierz numer kolumny: ")
        column_number = int(input())

        # Sprawdzenie czy wybrana kolumna nie jest pusta
        if column_number < max_length:
            # Iteracja po wierszach
            for i in range(len(partial_products)):
                # Sprawdź czy kolumna ma wystarczającą długość
                if column_number < len(partial_products[i]):
                    print(partial_products[i][column_number], "<-", i)
                else:
                    print("Puste")

            print("Wybierz numer bitu do zanegowania: ")
            bit_error = int(input())

            # Zanegowanie bitu pod warunkiem, że nie jest pusty
            if bit_error < len(partial_products):
                if partial_products[bit_error][column_number] != "":
                    # Konwersja ciągu znaków na listę
                    temp_list = list(partial_products[bit_error])
                    # Zanegowanie bitu
                    if temp_list[column_number] == "0":
                        temp_list[column_number] = "1"
                    elif temp_list[column_number] == "1":
                        temp_list[column_number] = "0"
                    # Konwersja listy z powrotem na ciąg znaków
                    partial_products[bit_error] = "".join(temp_list)
                    print(f"Zanegowano bit w kolumnie {column_number} i wierszu {bit_error}.")
                else:
                    print("Wybrany bit jest pusty.")
            else:
                print("Nieprawidłowy numer bitu.")
        else:
            print("Nieprawidłowy numer kolumny.")

        print("----------------------")
        return partial_products


    # def get_error(self, partial_products):
    #     # print("Oto iloczyny częściowe:")
    #
    #     # Znajdź najdłuższy wiersz
    #     max_length = max(len(row) for row in partial_products)
    #
    #     # # Iteracja po kolumnach
    #     # for j in range(max_length):
    #     #     # Iteracja po wierszach
    #     #     for i in range(len(partial_products)):
    #     #         # Sprawdź czy kolumna ma wystarczającą długość
    #     #         if j < len(partial_products[i]):
    #     #             print(partial_products[i][j])
    #     #         else:
    #     #             print("Puste")
    #     #     print("----------------------")
    #
    #     for i in range(max_length):
    #         print(i, end="")
    #     print(" <- numery kolumn")
    #     for partial_product in partial_products:
    #         print(partial_product)
    #
    #     print("Wybierz numer kolumny: ")
    #     column_number = int(input())
    #
    #     # # Iteracja po wierszach
    #     # for i in range(len(partial_products)):
    #     #     # Sprawdź czy kolumna ma wystarczającą długość
    #     #     if column_number < len(partial_products[i]):
    #     #         print(partial_products[i][column_number], "<-", i)
    #     #     else:
    #     #         print("Puste")
    #     # print("----------------------")
    #     #
    #     # print("Wybierz numer bitu do zanegowania: ")
    #     # bit_error = int(input())
    #
    #     if column_number < max_length:
    #         # Iteracja po wierszach
    #         for i in range(len(partial_products)):
    #             # Sprawdź czy kolumna ma wystarczającą długość
    #             if column_number < len(partial_products[i]):
    #                 print(partial_products[i][column_number], "<-", i)
    #             else:
    #                 print("Puste")
    #
    #         print("Wybierz numer bitu do zanegowania: ")
    #         bit_error = int(input())
    #
    #         # Zanegowanie bitu pod warunkiem, że nie jest pusty
    #         if bit_error < len(partial_products):
    #             if partial_products[bit_error][column_number] != "":
    #                 # Zanegowanie bitu
    #                 if partial_products[bit_error][column_number] == "0":
    #                     partial_products[bit_error][column_number] = "1"
    #                 elif partial_products[bit_error][column_number] == "1":
    #                     partial_products[bit_error][column_number] = "0"
    #                 print(f"Zanegowano bit w kolumnie {column_number} i wierszu {bit_error}.")
    #             else:
    #                 print("Wybrany bit jest pusty.")
    #         else:
    #             print("Nieprawidłowy numer bitu.")
    #     else:
    #         print("Nieprawidłowy numer kolumny.")
    #
    #     print("----------------------")
    #     return partial_products

    def carry_check(self, number_a, number_b):
        # Sprawdzanie przeniesienia
        pass

    def overflow_check(self, number_a, number_b):
        # Sprawdzanie przepełnienia
        pass

    def get_result(self):
        # Zwracanie wyniku
        pass
