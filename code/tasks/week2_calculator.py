# Week 2: Challenge Activity

class Calculator:
    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4
    QUIT = 5

    def __init__(self):
        pass

    def add(self):
        a = self.__try_integer(input('add this: '))
        b = self.__try_integer(input(' to this: '))
        print(f'{a} + {b} = {a + b}')
    
    def sub(self):
        a = self.__try_integer(input('sub this: '))
        b = self.__try_integer(input(' to this: ')) 
        print(f'{a} - {b} = {a - b}')
    
    def mul(self):
        a = self.__try_integer(input('mul this: '))
        b = self.__try_integer(input(' to this: ')) 
        print(f'{a} * {b} = {a * b}')
    
    def div(self):
        a = self.__try_integer(input('div this: '))
        b = self.__try_integer(input(' to this: ')) 
        print(f'{a} / {b} = {a / b}')

    def __try_integer(self, s: str) -> int:
        try:
            return int(s)
        except ValueError:
            print(f'\n** ❌ "{s}" is not a valid number **')

    def __print_initial_screen(self):
        s = '''
            Welcome to your calculator
            your options are:

            1. ➕ Addition
            2. ➖ Subtraction
            3. ✖  Multiplication
            4. ➗ Division
            5. 🚪 Quit
        '''
        print(s)

    def main(self):
        while True:
            self.__print_initial_screen()
            selection = self.__try_integer(input('Choose your option: '))
            match selection:
                case self.QUIT:
                    print('Bye!')
                    return # Exit while loop
                case self.ADD:
                    self.add()
                case self.SUB:
                    self.sub()
                case self.MUL:
                    self.mul()
                case self.DIV:
                    self.div()
                case _: # No matches
                    print(f'\n** No valid option selected **')
                    
class UnhandledError(Exception):
    pass

if __name__ == '__main__':
    try:
        Calculator().main()
    except KeyboardInterrupt:
        # CTRL + C
        print('\nBye!')
    except UnhandledError as error:
        print(f'Something went wrong! {error}')