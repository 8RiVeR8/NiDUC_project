
#klasa modelowa dla operandu przechowuje listy znaków i reszty
class Operand:
    def __init__(self):
        self._char_list = []
        self._rest_list = []
        self._fault_char_list = []
        self._fault_rest_list = []
        self._modulo_number = ''


    def get_bin_number(self, name):
        print(f"Podaj liczbę binarną {name}:")
        self._char_list = list(input())

    def get_modulo_number(self):
        while True:
            print("Podaj wartość modulo: ")
            self._modulo_number = int(input())
            if self._modulo_number % 2 == 0:
                print("Podana liczba jest parzysta. Wprowadź liczbę nieparzystą!")
            else:
                break

    def get_char_list(self, sign):
        #print("Podaj liczbę " + sign + ": ")
        #self._char_list.append(list(input()))
        return self._char_list

    def get_rest_list(self):
        return self._rest_list

    def get_fault_char_list(self):
        return self._fault_char_list

    def get_fault_rest_list(self):
        return self._fault_rest_list

    def set_char_list( char_list):
        _char_list = char_list

    def set_rest_list( rest_list):
        _rest_list = rest_list

    def set_fault_char_list( fault_char_list):
        _fault_char_list = fault_char_list

    def set_fault_rest_list( fault_rest_list):
        _fault_rest_list = fault_rest_list