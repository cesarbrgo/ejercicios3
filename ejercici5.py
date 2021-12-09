# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    frase = 'Practica els problemes de List comprehensions per a ser més Pythonic!'
    vocals = [x for x in frase if not x in 'aeiou']
    print(vocals)


if __name__ == '__main__':
    main()
# See PyCharm help at httpsmain.py://www.jetbrains.com/help/pycharm/
