
"""def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")


if __name__ == '__main__':
    main()"""
#Salida
"""
Traceback (most recent call last):
  File "c:/Users/Elizabeth/Documents/LAUNCH X/ProgramasPython/EJERCICIOS/KATA_10/config.py", line 10, in <module>
    main()
  File "c:/Users/Elizabeth/Documents/LAUNCH X/ProgramasPython/EJERCICIOS/KATA_10/config.py", line 4, in main
    configuration = open('config.txt')
PermissionError: [Errno 13] Permission denied: 'config.txt'

"""

def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except PermissionError:
        print("Found config.txt but it haven't permission, couldn't read it")

if __name__ == '__main__':
    main()

