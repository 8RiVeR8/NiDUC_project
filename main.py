from adder import Add
from autoTests import AutoTests
from multiplier import Multiplier
from operand import Operand


class Main:
    def __init__(self):
        self.adder = Add()
        self.multiply = Multiplier()
        self.auto_tests = AutoTests()

    def print_menu(self):
        print("1. Dodawanie")
        print("2. Mnożenie")
        print("3. Testy")
        print("4. Wyjdź z programu")

    def add_number(self):
        operand_x = Operand()
        operand_x.get_bin_number("X")

        operand_y = Operand()
        operand_y.get_bin_number("Y")

        operand_modulo = Operand()
        operand_modulo.get_modulo_number()

        self.adder.number_x = operand_x
        self.adder.number_y = operand_y
        self.adder.modulo = operand_modulo

        result = self.adder.get_result()
        result_after_modulo = self.adder.result_after_modulo(result)
        second_result_after_modulo = self.adder.result_after_modulo_second(self.adder.get_result_modulo())
        print("Wynik dodawania X i Y:", result)
        print("Wynik dodawania modulo |X|A + |Y|A:", self.adder.get_result_modulo())
        print("Wynik dodawania modulo |X + Y|A:", result_after_modulo)
        print("Wynik dodawania ||X|A + |Y|A|: ", second_result_after_modulo)
        self.adder.error_check(result_after_modulo, second_result_after_modulo)


    def multiply_number(self):
        operand_x = Operand()
        bin_x = operand_x.get_bin_number("X")

        operand_y = Operand()
        bin_y = operand_y.get_bin_number("Y")

        self.multiply.number_x = bin_x
        self.multiply.number_y = bin_y

        print("Iloczyny częściowe: ")
        for partial_product in self.multiply.binary_multiply(bin_x, bin_y):
            print(partial_product, "<-")

    def auto_tests(self):
        self.auto_tests.run()

    def main(self):
        while True:
            self.print_menu()
            choice = input("Wybierz opcję: ")
            if choice == "1":
                self.add_number()
            elif choice == "2":
                self.multiply_number()
            elif choice == "3":
                self.auto_tests()
            elif choice == "4":
                print("Wyjście z programu")
                break
            else:
                print("Niepoprawny wybór. Spróbuj ponownie.")


if __name__ == "__main__":
    program = Main()
    program.main()
