class inp_outp_str:
    def __init__(self):
        self.s = " "
        self.get_string()
        self.print_in_upper()
    def get_string(self):
        self.s = input()
    def print_in_upper(self):
        print(self.s.upper())
if __name__ == '__main__':
    inp_outp_str()
