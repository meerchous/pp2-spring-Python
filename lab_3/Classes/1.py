class Account():
    def __init__(self):
        self.s = ""

    def get_string(self):
       self.s = input()
       
    def print_string(self):
        print(self.s.upper())

x = Account()
x.get_string()
x.print_string()
