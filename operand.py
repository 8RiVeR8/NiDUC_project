
#klasa modelowa dla operandu przechowuje listy znaków i reszty
class Operand:
    def __init__(self):
        _char_list = []
        _rest_list = []
        _fault_char_list = []
        _fault_rest_list = []

    def get_char_list(self):
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