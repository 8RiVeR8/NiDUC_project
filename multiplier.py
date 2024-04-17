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

        result = sum(int(partial, 2) for partial in partial_products)

        print(result, "Wynik niby")

        return partial_products

    def carry_check(self, number_a, number_b):
        # Sprawdzanie przeniesienia
        pass

    def overflow_check(self, number_a, number_b):
        # Sprawdzanie przepełnienia
        pass

    def get_result(self):
        # Zwracanie wyniku
        pass
