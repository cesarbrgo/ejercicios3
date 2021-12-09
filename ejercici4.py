# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    frase = 'Practica els problemes de List comprehensions per a ser més Pythonic!'
    espais=[x for x in frase if x in ' ']
    print('els espais son:')
    print(len(espais))

if __name__ == '__main__':
    main()
# See PyCharm help at httpsmain.py://www.jetbrains.com/help/pycharm/
