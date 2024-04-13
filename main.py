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
        print("Wynik dodawania:", self.adder.get_result())
        print("Wynik dodawania modulo:", self.adder.get_result_modulo())


    def multiply(self):
        self.multiply.run()

    def auto_tests(self):
        self.auto_tests.run()

    def main(self):
        while True:
            self.print_menu()
            choice = input("Wybierz opcję: ")
            if choice == "1":
                self.add_number()
            elif choice == "2":
                self.multiply()
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
